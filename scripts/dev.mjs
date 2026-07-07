#!/usr/bin/env node
/**
 * dev.mjs — dev-serve ONE lecture deck (the everyday authoring loop).
 *
 * Usage:
 *   pnpm dev 6                    # by lecture number
 *   pnpm dev 06-version-control   # by exact slug
 *   pnpm dev version              # by substring match on slug/title
 *   pnpm dev                      # no arg: list all decks
 *
 * Anything after the selector is passed through to `slidev` (e.g.
 * `pnpm dev 6 --port 3031`). Entries are regenerated first so decks.json
 * edits propagate, and the deck is served through its generated
 * deck.<slug>.md entry — never a bare slides/NN_*.md, which would drop the
 * theme and /figures/* (see CLAUDE.md).
 */
import { readFile } from 'node:fs/promises';
import { spawnSync } from 'node:child_process';
import { join, dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const CONTENT = join(ROOT, 'lectures', 'content');

const manifest = JSON.parse(await readFile(join(CONTENT, 'decks.json'), 'utf8'));
const argv = process.argv.slice(2);
const sel = argv[0] && !argv[0].startsWith('-') ? argv[0] : null;
const passthrough = sel ? argv.slice(1) : argv;

function listDecks() {
  console.log('Decks (pnpm dev <number|slug|substring>):\n');
  for (const d of manifest.decks) {
    console.log(`  ${d.slug.padEnd(30)} ${d.title}${d.optional ? '  (optional)' : ''}`);
  }
}

if (!sel) {
  listDecks();
  process.exit(0);
}

// Resolve: exact slug → lecture number → substring of slug/title.
const bynum = (s) => manifest.decks.find((d) => d.slug.split('-')[0] === s.padStart(2, '0'));
const deck =
  manifest.decks.find((d) => d.slug === sel) ||
  (/^\d{1,2}$/.test(sel) ? bynum(sel) : null) ||
  manifest.decks.find((d) => d.slug.includes(sel.toLowerCase())) ||
  manifest.decks.find((d) => d.title.toLowerCase().includes(sel.toLowerCase()));

if (!deck) {
  console.error(`No deck matches "${sel}".\n`);
  listDecks();
  process.exit(1);
}

// Regenerate entries so manifest/title edits propagate before serving.
const gen = spawnSync('node', [join(ROOT, 'scripts', 'gen-entries.mjs')], { stdio: 'inherit' });
if (gen.status !== 0) process.exit(gen.status ?? 1);

const entry = join(CONTENT, `deck.${deck.slug}.md`);
console.log(`\n▶ serving ${deck.slug} — ${deck.title}\n`);
const r = spawnSync('pnpm', ['exec', 'slidev', entry, ...passthrough], {
  cwd: ROOT,
  stdio: 'inherit',
});
process.exit(r.status ?? 0);
