#!/usr/bin/env node
/**
 * gen-entries.mjs — generate one Slidev entry file per deck from decks.json.
 *
 * Entries live in lectures/content/ as `deck.<slug>.md`, co-located with the
 * custom theme AND the public/ dir — both are resolved relative to the entry's
 * directory at build time, so the entry MUST sit beside them (a bare
 * slides/L0X.md build drops the theme AND can't resolve /figures/* — see
 * project memory). The `deck.` prefix keeps cleanup from ever touching the
 * hand-authored entries (lessons_…, staging.md). Each entry carries the shared
 * global headmatter copied from the published entry, then imports its lecture
 * source file(s) with `src:` — each lecture already provides its own cover.
 */
import { readFile, writeFile, readdir, unlink } from 'node:fs/promises';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const CONTENT = join(ROOT, 'lectures', 'content');

const manifest = JSON.parse(await readFile(join(CONTENT, 'decks.json'), 'utf8'));

// Shared global headmatter (mirrors the combined entry). The FIRST lecture is
// imported via `src:` inside the headmatter block itself, so the lecture's own
// cover becomes slide 1 — otherwise the headmatter block renders as an empty
// slide 1 and the cover slips to slide 2.
function headmatter(title, firstSrc) {
  return [
    '---',
    'theme: ./theme',
    // Hash router: GitHub Pages has no SPA rewrites, so history-mode slide
    // URLs (/<slug>/5) 404 on reload. Hash routes (/<slug>/#/5) always hit
    // the deck's real index.html.
    'routerMode: hash',
    'background: /figures/background_intro.jpg',
    // NO per-slide keys (class, transition, …) here: because `src:` sits in
    // this same headmatter block, the parser applies EVERY key of this block
    // as a frontmatter override to EVERY slide of the first imported lecture
    // (main entry wins over the slide's own frontmatter). `class: text-left`
    // here silently killed each slide's own `class: text-center/text-size-*`.
    // (`background` stays: harmless — every cover sets the identical value.)
    'colorSchema: dark',
    'addons:',
    '  - slidev-addon-python-runner',
    'mermaid: true',
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

for (const deck of manifest.decks) {
  await writeFile(join(CONTENT, `deck.${deck.slug}.md`), entryContent(deck), 'utf8');
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
