#!/usr/bin/env node
/**
 * gen-entries.mjs — generate one Slidev entry file per deck from decks.json.
 *
 * Entries live in lectures/content/ as `deck.<slug>.md`, co-located with the
 * custom theme AND the public/ dir — both are resolved relative to the entry's
 * directory at build time, so the entry MUST sit beside them (a bare
 * slides/L0X.md build drops the theme AND can't resolve /figures/* — see
 * project memory). The `deck.` prefix keeps cleanup from ever touching the
 * hand-authored entries (lessons_…, staging.md). Each entry carries ALL the
 * deck-level config (theme, router, colour scheme, addons, title) — this is the
 * ONLY place it lives — then imports its lecture source file(s) with `src:`.
 * A lecture file's cover frontmatter is just `layout: cover` + `title:` (+ a
 * `python:` block on runner decks, which the addon reads from slide 1 = that
 * cover); any deck-level key written there is dead once the file is imported
 * (Slidev takes config from the entry's headmatter alone).
 */
import { readFile, writeFile, readdir, unlink } from 'node:fs/promises';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const CONTENT = join(ROOT, 'lectures', 'content');

const manifest = JSON.parse(await readFile(join(CONTENT, 'decks.json'), 'utf8'));

// Deck-level headmatter. The FIRST lecture is imported via `src:` inside the
// headmatter block itself, so the lecture's own cover becomes slide 1 —
// otherwise the headmatter block renders as an empty slide 1 and the cover
// slips to slide 2.
function headmatter(title, firstSrc) {
  return [
    '---',
    'theme: ./theme',
    // Hash router: GitHub Pages has no SPA rewrites, so history-mode slide
    // URLs (/<slug>/5) 404 on reload. Hash routes (/<slug>/#/5) always hit
    // the deck's real index.html.
    'routerMode: hash',
    // NO per-slide keys (class, transition, background, …) here: because
    // `src:` sits in this same headmatter block, the parser applies EVERY key
    // of this block as a frontmatter override to EVERY slide of the first
    // imported lecture (main entry wins over the slide's own frontmatter).
    // `class: text-left` here silently killed each slide's own
    // `class: text-center/text-size-*`. The cover's background is the
    // cover layout's default (theme/layouts/cover.vue), so nothing to set.
    // No `mermaid:` key either — it is not a Slidev config option; mermaid
    // fences render natively.
    'colorSchema: dark',
    'addons:',
    '  - slidev-addon-python-runner',
    // No `defaults: preload: false` here (the combined 500-slide authoring
    // deck needs it; these per-deck builds don't): it stops Slidev from
    // pre-rendering prev/next (and, after 3s, all) slides, so every FIRST
    // visit to a slide fetched its JS+CSS chunk at click time — a visible
    // flicker on each first slide switch. Videos stay lazy either way
    // (VideoPlayer sets preload="none" and only sets src once active).
    `title: ${JSON.stringify(title)}`,
    `src: ./slides/${firstSrc}`,
    '---',
  ].join('\n');
}

function entryContent(deck) {
  const [first, ...rest] = deck.srcs;
  const more = rest
    .map((s) => `\n---\nsrc: ./slides/${s}\n---\n`)
    .join('');
  return `${headmatter(deck.title, first)}\n${more}`;
}

// Clean out stale generated entries (only deck.*.md — never the hand-authored ones).
for (const f of await readdir(CONTENT)) {
  if (f.startsWith('deck.') && f.endsWith('.md')) await unlink(join(CONTENT, f));
}

// The cover's own `title:` is overridden by the entry's in the deck build, but
// it is what the combined authoring deck's TOC shows — warn when it drifts
// from the manifest (the deployed title) instead of letting the two diverge.
async function coverTitle(src) {
  const text = await readFile(join(CONTENT, 'slides', src), 'utf8');
  const fm = text.match(/^---\r?\n([\s\S]*?)\r?\n---/)?.[1] ?? '';
  const raw = fm.match(/^title:[ \t]*(.*)$/m)?.[1]?.trim();
  return raw == null ? null : raw.replace(/^(["'])(.*)\1$/, '$2');
}

for (const deck of manifest.decks) {
  await writeFile(join(CONTENT, `deck.${deck.slug}.md`), entryContent(deck), 'utf8');
  const t = await coverTitle(deck.srcs[0]);
  if (t !== deck.title)
    console.warn(`⚠ ${deck.srcs[0]}: cover title ${t === null ? 'missing' : JSON.stringify(t)} ≠ decks.json ${JSON.stringify(deck.title)}`);
}

// Emit a lightweight lecture index consumed by the in-deck nav overlay
// (global-top.vue fetches `<base>/lectures.json`). Copied into every
// deck's build via public/, so each deck can link back home and to its siblings.
// Generated + gitignored.
const lectureIndex = manifest.decks.map((d, i) => ({
  n: i + 1,
  slug: d.slug,
  title: d.title,
  block: d.block,
  optional: !!d.optional,
  draft: !!d.draft,
}));
await writeFile(
  join(CONTENT, 'public', 'lectures.json'),
  JSON.stringify({ blocks: manifest.blocks, decks: lectureIndex }),
  'utf8',
);

console.log(`Generated ${manifest.decks.length} entry files (lectures/content/deck.*.md) + public/lectures.json`);
