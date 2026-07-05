#!/usr/bin/env node
/**
 * qa-all.mjs — build every deck at base '/' into .qa-dist/<slug>, then run the
 * overflow checker on each. Aggregate: non-zero exit if ANY deck overflows or
 * has an unrendered slide. This is the per-deck replacement for the old
 * single-entry `pnpm qa`.
 *
 * Usage: node scripts/qa-all.mjs [--only a,b] [--shots]
 *   --only a,b   QA only these slugs
 *   --shots      also write .qa-shots/<slug>/slide-NNN.png for review
 */
import { readFile } from 'node:fs/promises';
import { spawnSync } from 'node:child_process';
import { join, dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const CONTENT = join(ROOT, 'lectures', 'content');
const QA_DIST = join(ROOT, '.qa-dist');

const argv = process.argv.slice(2);
const opt = (n, d) => { const i = argv.indexOf(n); return i > -1 ? argv[i + 1] : d; };
const ONLY = argv.includes('--only') ? opt('--only') : null;
const SHOTS = argv.includes('--shots');

const manifest = JSON.parse(await readFile(join(CONTENT, 'decks.json'), 'utf8'));

// 1) Build all decks flat (base '/') into .qa-dist/<slug>.
const buildArgs = ['scripts/build-all.mjs', '--flat-base', '--out', '.qa-dist'];
if (ONLY) buildArgs.push('--only', ONLY);
const build = spawnSync('node', buildArgs, { cwd: ROOT, stdio: 'inherit' });
if (build.status !== 0) { console.error('❌ build phase failed'); process.exit(1); }

// 2) Overflow-check each deck's output dir.
const decks = manifest.decks.filter((d) => !ONLY || ONLY.split(',').includes(d.slug));
let bad = 0;
const summary = [];
for (const d of decks) {
  const dir = join(QA_DIST, d.slug);
  const checkArgs = [join(ROOT, 'scripts', 'check-slides.mjs'), dir];
  if (SHOTS) checkArgs.push('--shots', join(ROOT, '.qa-shots', d.slug));
  const r = spawnSync('node', checkArgs, { cwd: ROOT, stdio: 'inherit' });
  if (r.status !== 0) { bad++; summary.push(`✗ ${d.slug}`); }
  else summary.push(`✓ ${d.slug}`);
}

// 3) Landing smoke test (decks build --flat-base with no landing, so build one).
const LAND = join(QA_DIST, '__landing__');
process.stdout.write('\n▶ landing smoke test …\n');
const lb = spawnSync('node', [join(ROOT, 'scripts', 'build-landing.mjs'), '--out', LAND], { cwd: ROOT, stdio: 'inherit' });
const lc = lb.status === 0
  ? spawnSync('node', [join(ROOT, 'scripts', 'check-landing.mjs'), LAND], { cwd: ROOT, stdio: 'inherit' })
  : lb;
if (lc.status !== 0) { bad++; summary.push('✗ landing'); } else summary.push('✓ landing');

console.log(`\n=== QA summary ===\n${summary.join('\n')}`);
if (bad) { console.error(`\n❌ ${bad} QA target(s) failed.`); process.exit(1); }
console.log(`\n✅ All ${decks.length} deck(s) + landing pass QA.`);
