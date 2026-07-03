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

// Shared global headmatter (mirrors lessons_on_data_analysis_from_CERN.md).
function headmatter(title) {
  return [
    '---',
    'theme: ./theme',
    'background: /figures/background_intro.jpg',
    'class: text-left',
    'colorSchema: dark',
    'transition: fade',
    'addons:',
    '  - slidev-addon-python-runner',
    'mermaid: true',
    'defaults:',
    '  preload: false',
    `title: ${JSON.stringify(title)}`,
    '---',
  ].join('\n');
}

function entryContent(deck) {
  const imports = deck.srcs
    .map((s) => `\n---\nsrc: ./slides/${s}\n---\n`)
    .join('');
  return `${headmatter(deck.title)}\n${imports}`;
}

// Clean out stale generated entries (only deck.*.md — never the hand-authored ones).
for (const f of await readdir(CONTENT)) {
  if (f.startsWith('deck.') && f.endsWith('.md')) await unlink(join(CONTENT, f));
}

for (const deck of manifest.decks) {
  await writeFile(join(CONTENT, `deck.${deck.slug}.md`), entryContent(deck), 'utf8');
}

console.log(`Generated ${manifest.decks.length} entry files (lectures/content/deck.*.md)`);
