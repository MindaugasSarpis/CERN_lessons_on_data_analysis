#!/usr/bin/env node
/**
 * gen-glossary.mjs — the glossary of each lecture, from one hand-edited table.
 *
 * Source (the lecturer edits these): lectures/content/glossary/NN.md, NN = the
 * deck's number (the slug's prefix), a single Markdown table
 *
 *   | Term | Meaning | First on |
 *   | --- | --- | --- |
 *   | Aspect ratio | The width of the plot area divided by its height. | The Aspect Ratio |
 *
 * the term, one line in the lecture's own words (KaTeX `$…$` allowed, a
 * literal pipe written `\|`), and the title of the slide where the term is
 * first explained: the plain text of its `# ` title, without the `**`
 * markers (a `## ` card heading, without its emoji, for a slide that has no
 * title). Decks without a glossary file are skipped.
 *
 * Outputs:
 *   - lectures/content/glossary.<slug>.md (generated, gitignored): a section
 *     slide `# **Glossary**`, then table slides Term · Meaning · Slide, the
 *     terms in the order of the lecture. gen-entries.mjs appends it to the
 *     deck's entry after all its srcs, so the glossary is the very end of the
 *     deck, after `# Check **Yourself**` (0 min: the timing model reads only
 *     the srcs).
 *   - lectures/workbook/docs/glossary.md (committed): every term A–Z with
 *     "Lecture N, slide M", linking the lecture page.
 *
 * The slide number is found at build time: the deck's srcs are split into
 * slides the way Slidev numbers them (@slidev/parser 53: `---` separators
 * outside code fences and HTML comments, a frontmatter block when the next
 * line is not blank, `hide`/`disabled` slides dropped, cover = 1), and the
 * "First on" title is looked up among their `# ` titles (case, `**`,
 * backticks, emoji and HTML tags ignored), then among all their headings.
 * A title that matches no slide is a warning, not an error: its row shows
 * no number.
 *
 * Runs from gen-entries.mjs (so `pnpm build`, `pnpm qa` and `pnpm dev` keep
 * both outputs fresh), or alone after editing a glossary file:
 *   node scripts/gen-glossary.mjs
 */
import { existsSync } from 'node:fs';
import { readFile, writeFile, readdir, unlink } from 'node:fs/promises';
import { join, dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const CONTENT = join(ROOT, 'lectures', 'content');
const SOURCES = join(CONTENT, 'glossary');
const WORKBOOK_DOCS = join(ROOT, 'lectures', 'workbook', 'docs');
const PAGE = join(WORKBOOK_DOCS, 'glossary.md');

const ROWS_PER_SLIDE = 9;

// ---------- slides as Slidev numbers them ----------

// One line of the HTML-comment state machine of @slidev/parser: is the line
// still inside a comment at its end?
function inCommentAfter(line, inComment) {
  let cursor = 0;
  while (cursor < line.length) {
    if (inComment) {
      const end = line.indexOf('-->', cursor);
      if (end < 0) return true;
      inComment = false;
      cursor = end + 3;
    } else {
      const start = line.indexOf('<!--', cursor);
      if (start < 0) return false;
      const end = line.indexOf('-->', start + 4);
      if (end < 0) return true;
      cursor = end + 3;
    }
  }
  return inComment;
}

// The raw text of each slide of one markdown file (@slidev/parser `parse`).
function splitSlides(markdown) {
  const lines = markdown.split(/\r?\n/);
  const slides = [];
  let start = 0;
  let inComment = false;
  const slice = (end) => {
    if (start === end) return;
    slides.push(lines.slice(start, end).join('\n'));
    start = end + 1;
  };
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trimEnd();
    if (inComment) {
      inComment = inCommentAfter(lines[i], true);
      continue;
    }
    if (line.startsWith('---')) {
      slice(i);
      if (line[3] !== '-' && lines[i + 1]?.trim()) {
        // frontmatter: up to the next bare `---`
        start = i;
        for (i += 1; i < lines.length; i++) if (lines[i].trimEnd() === '---') break;
      }
    } else if (line.trimStart().startsWith('```')) {
      const fence = line.match(/^\s*`+/)[0];
      let j = i + 1;
      while (j < lines.length && !lines[j].startsWith(fence)) j++;
      if (j !== lines.length) i = j;
    } else {
      inComment = inCommentAfter(lines[i], false);
    }
  }
  if (start <= lines.length - 1) slice(lines.length);
  return slides;
}

function frontmatterOf(raw) {
  const m = raw.match(/^---.*\r?\n([\s\S]*?)---/);
  return m ? { fm: m[1], content: raw.slice(m[0].length) } : { fm: '', content: raw };
}

const fmValue = (fm, key) => fm.match(new RegExp(`^${key}[ \\t]*:[ \\t]*(.*?)\\s*$`, 'm'))?.[1];
const truthy = (v) => v != null && !/^(false|null|~|0|''|""|)$/i.test(v);

// The headings of a slide's content, outside code fences and HTML comments.
function headingsOf(content) {
  const found = [];
  let fence = null;
  let inComment = false;
  for (const line of content.split(/\r?\n/)) {
    if (fence) {
      if (line.startsWith(fence)) fence = null;
      continue;
    }
    if (inComment) {
      inComment = inCommentAfter(line, true);
      continue;
    }
    if (line.trimStart().startsWith('```')) {
      fence = line.match(/^\s*`+/)[0];
      continue;
    }
    const h = line.match(/^ {0,3}(#{1,6})[ \t]+(.+?)(?:[ \t]+#+)?[ \t]*$/);
    if (h) found.push({ level: h[1].length, text: h[2] });
    inComment = inCommentAfter(line, false);
  }
  return found;
}

/** Every slide of a deck in Slidev's order: [{ no, title, headings, file }]. */
export async function deckSlides(srcs) {
  const out = [];
  async function load(file, chain) {
    const md = await readFile(file, 'utf8');
    for (const raw of splitSlides(md)) {
      const { fm, content } = frontmatterOf(raw);
      if (truthy(fmValue(fm, 'disabled')) || truthy(fmValue(fm, 'hide'))) continue;
      const src = fmValue(fm, 'src')?.replace(/^(["'])(.*)\1$/, '$2');
      if (src) {
        const path = src.split('#')[0];
        const target = path.startsWith('/') ? join(CONTENT, path.slice(1)) : resolve(dirname(file), path);
        if (!chain.includes(target) && existsSync(target)) await load(target, [...chain, target]);
        continue;
      }
      const headings = headingsOf(content);
      out.push({ no: out.length + 1, title: headings.find((h) => h.level === 1)?.text ?? null, headings, file });
    }
  }
  for (const s of srcs) {
    const file = join(CONTENT, 'slides', s);
    await load(file, [file]);
  }
  return out;
}

// ---------- matching a "First on" title ----------

const EMOJI = /[\p{Extended_Pictographic}\u{FE0F}\u{200D}\u{20E3}]/gu;

/** A title as plain text: no HTML tags, emoji, `**`, `*` or backticks. */
export function plain(s) {
  return String(s)
    .replace(/<[^>]*>/g, '')
    .replace(EMOJI, '')
    .replace(/\\([\\`*_{}[\]()#+\-.!|])/g, '$1')
    .replace(/[*`]/g, '')
    .replace(/[‘’]/g, "'")
    .replace(/[“”]/g, '"')
    .replace(/[–—]/g, '-')
    .replace(/…/g, '...')
    .replace(/\s+/g, ' ')
    .trim();
}
const key = (s) => plain(s).toLowerCase();

function findSlide(slides, title) {
  const k = key(title);
  return (
    slides.find((s) => s.title != null && key(s.title) === k) ??
    slides.find((s) => s.headings.some((h) => key(h.text) === k)) ??
    null
  );
}

// ---------- the source table ----------

// Cells of one table row, split at unescaped pipes; `\|` stays as written
// (both outputs are Markdown tables again).
function cells(line) {
  const body = line.trim().replace(/^\|/, '').replace(/(?<!\\)\|$/, '');
  return body.split(/(?<!\\)\|/).map((c) => c.trim());
}

function parseTable(text, file) {
  const rows = [];
  const lines = text.split(/\r?\n/).filter((l) => l.trim().startsWith('|'));
  for (const [i, line] of lines.entries()) {
    const c = cells(line);
    if (i === 0) continue; // header
    if (c.every((x) => /^:?-{3,}:?$/.test(x))) continue; // | --- |
    if (c.length !== 3 || !c[0]) {
      console.warn(`⚠ ${file}: skipped a row that does not have three cells: ${line.trim()}`);
      continue;
    }
    rows.push({ term: c[0], meaning: c[1], firstOn: c[2] });
  }
  return rows;
}

// ---------- outputs ----------

const deckNumber = (slug) => slug.slice(0, 2);

function chunk(rows) {
  const n = Math.max(1, Math.ceil(rows.length / ROWS_PER_SLIDE));
  const size = Math.ceil(rows.length / n); // balanced: 19 rows → 7 + 7 + 5
  const out = [];
  for (let i = 0; i < rows.length; i += size) out.push(rows.slice(i, i + size));
  return out;
}

function deckSlidesFile(glossaryFile, rows) {
  const tables = chunk(rows).map((part) => [
    '---',
    'hideInToc: true',
    '---',
    '',
    '# Glossary',
    '',
    '<div class="card card-primary card-glass pad-compact table-compact glossary-table">',
    '',
    '| Term | Meaning | Slide |',
    '| --- | --- | --- |',
    // The number links the slide (Slidev turns a digits-only href into <Link>).
    ...part.map((r) => `| ${r.term} | ${r.meaning} | ${r.slide ? `[${r.slide}](${r.slide})` : ''} |`),
    '',
    '</div>',
    '',
    // table-compact keeps cells on one line; the meanings may wrap.
    '<style>',
    '.glossary-table td:nth-child(2) { white-space: normal; }',
    '.glossary-table td:first-child { white-space: nowrap; }',
    '.glossary-table th:last-child, .glossary-table td:last-child { text-align: right; }',
    '</style>',
    '',
  ].join('\n'));
  return [
    '---',
    `# Generated by scripts/gen-glossary.mjs from ${glossaryFile}: edit that file, not this one.`,
    'layout: section',
    'hideInToc: true',
    '---',
    '',
    '# **Glossary**',
    '',
    'The words of this lecture, with the slide where each first appears.',
    '',
    ...tables,
  ].join('\n');
}

// A–Z: by the term's first letter or digit (`.gitignore` under G).
function sortKey(term) {
  const p = plain(term).normalize('NFD').replace(/\p{M}/gu, '').toLowerCase();
  return p.replace(/^[^\p{L}\p{N}]+/u, '') || p;
}
function groupOf(term) {
  const c = sortKey(term)[0] ?? '';
  if (/\p{L}/u.test(c)) return c.toUpperCase();
  return '0–9 and symbols';
}

function workbookPage(entries) {
  const sorted = [...entries].sort(
    (a, b) => sortKey(a.term).localeCompare(sortKey(b.term), 'en') || a.lecture - b.lecture || (a.slide ?? 0) - (b.slide ?? 0),
  );
  const groups = new Map();
  for (const e of sorted) {
    const g = groupOf(e.term);
    if (!groups.has(g)) groups.set(g, []);
    groups.get(g).push(e);
  }
  const order = [...groups.keys()].sort((a, b) => (a.length > 1) - (b.length > 1) || a.localeCompare(b, 'en'));
  const where = (e) => {
    const text = `Lecture ${e.lecture}${e.slide ? `, slide ${e.slide}` : ''}`;
    return existsSync(join(WORKBOOK_DOCS, 'lectures', `lecture_${e.lecture}.md`)) ? `[${text}](lectures/lecture_${e.lecture}.md)` : text;
  };
  const out = [
    '<!-- Generated by scripts/gen-glossary.mjs from lectures/content/glossary/NN.md: edit those files, not this page. pnpm build, pnpm qa and pnpm dev regenerate it. -->',
    '',
    '# Glossary',
    '',
    'The words of the lectures, A–Z, each with the lecture and the slide where it first appears.',
    '',
  ];
  if (!sorted.length) out.push('No lecture has a glossary yet.', '');
  for (const g of order) {
    out.push(`## ${g}`, '', '| Term | Meaning | First on |', '| --- | --- | --- |');
    for (const e of groups.get(g)) out.push(`| ${e.term} | ${e.meaning} | ${where(e)} |`);
    out.push('');
  }
  return out.join('\n');
}

async function writeIfChanged(file, text) {
  const old = existsSync(file) ? await readFile(file, 'utf8') : null;
  if (old !== text) await writeFile(file, text, 'utf8');
}

/**
 * Write every deck's glossary slides and the workbook page.
 * @returns {Promise<Map<string, string>>} slug → the generated file's name
 *   (in lectures/content/), for the decks that have a glossary
 */
export async function genGlossary(manifest) {
  const made = new Map();
  const entries = [];
  const sources = existsSync(SOURCES) ? (await readdir(SOURCES)).filter((f) => /^\d\d\.md$/.test(f)) : [];
  for (const f of sources) {
    if (!manifest.decks.some((d) => deckNumber(d.slug) === f.slice(0, 2)))
      console.warn(`⚠ glossary/${f}: no deck ${f.slice(0, 2)} in decks.json, skipped`);
  }
  for (const deck of manifest.decks) {
    const nn = deckNumber(deck.slug);
    if (!sources.includes(`${nn}.md`)) continue;
    const rel = `glossary/${nn}.md`;
    const rows = parseTable(await readFile(join(SOURCES, `${nn}.md`), 'utf8'), rel);
    if (!rows.length) {
      console.warn(`⚠ ${rel}: no rows, no glossary for ${deck.slug}`);
      continue;
    }
    const slides = await deckSlides(deck.srcs);
    for (const r of rows) {
      const s = findSlide(slides, r.firstOn);
      r.slide = s?.no ?? null;
      if (!s) console.warn(`⚠ ${rel}: "${r.term}": no slide of ${deck.slug} is titled "${r.firstOn}"`);
    }
    // the order of the lecture; a row without a number keeps its place
    let last = 0;
    const ordered = rows
      .map((r, i) => ({ r, i, at: (last = r.slide ?? last) }))
      .sort((a, b) => a.at - b.at || a.i - b.i)
      .map(({ r }) => r);
    const name = `glossary.${deck.slug}.md`;
    await writeIfChanged(join(CONTENT, name), deckSlidesFile(rel, ordered));
    made.set(deck.slug, name);
    for (const r of ordered) entries.push({ ...r, lecture: Number(nn) });
  }
  // stale generated files (a glossary removed, a deck renamed)
  for (const f of await readdir(CONTENT)) {
    if (f.startsWith('glossary.') && f.endsWith('.md') && ![...made.values()].includes(f)) await unlink(join(CONTENT, f));
  }
  await writeIfChanged(PAGE, workbookPage(entries));
  return made;
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const manifest = JSON.parse(await readFile(join(CONTENT, 'decks.json'), 'utf8'));
  const made = await genGlossary(manifest);
  console.log(`Glossary: ${made.size} deck(s) → lectures/content/glossary.<slug>.md + lectures/workbook/docs/glossary.md`);
}
