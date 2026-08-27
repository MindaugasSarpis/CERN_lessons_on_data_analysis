#!/usr/bin/env node
/**
 * release.mjs — staged-release helper: flip the `draft` flags in decks.json.
 *
 *   pnpm release 5      # lectures 01–05 live, 06–16 draft ("coming soon")
 *   pnpm release all    # everything live
 *   pnpm release        # show the current state
 *
 * Edits decks.json line by line (keeps formatting). Then: commit on ff2026, wait
 * for qa.yml, and `git push origin ff2026:bs2026` to deploy.
 */
import { readFile, writeFile } from 'node:fs/promises';
import { join, dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const FILE = join(ROOT, 'lectures', 'content', 'decks.json');
const arg = process.argv[2];

let text = await readFile(FILE, 'utf8');
const manifest = JSON.parse(text);

if (arg !== undefined) {
  const upto = arg === 'all' ? Infinity : Number(arg);
  if (!Number.isFinite(upto) && arg !== 'all') { console.error(`usage: pnpm release <NN|all>`); process.exit(2); }
  const lines = text.split('\n');
  let touched = 0;
  for (let i = 0; i < lines.length; i++) {
    const m = lines[i].match(/"slug":\s*"(\d{2})-[^"]*"/);
    if (!m || !/"draft":\s*(true|false)/.test(lines[i])) continue;
    const n = Number(m[1]);
    const draft = n > upto;
    const next = lines[i].replace(/"draft":\s*(true|false)/, `"draft": ${draft}`);
    if (next !== lines[i]) { lines[i] = next; touched++; }
  }
  text = lines.join('\n');
  await writeFile(FILE, text, 'utf8');
  console.log(`Updated ${touched} deck(s).`);
}

const now = JSON.parse(text);
for (const d of now.decks) console.log(`  ${d.draft ? '○ draft' : '● live '}  ${d.slug}`);
const live = now.decks.filter((d) => !d.draft).length;
console.log(`\n${live}/${now.decks.length} live. Next: commit on ff2026 → wait for qa.yml → git push origin ff2026:bs2026`);
