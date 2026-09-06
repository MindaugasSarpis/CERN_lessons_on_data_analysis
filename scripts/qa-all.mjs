#!/usr/bin/env node
/**
 * qa-all.mjs — build every deck at base '/' into .qa-dist/<slug>, then run the
 * overflow checker on each. Aggregate: non-zero exit if ANY deck overflows or
 * has an unrendered slide. This is the per-deck replacement for the old
 * single-entry `pnpm qa`.
 *
 * Usage: node scripts/qa-all.mjs [--only a,b | --changed-since <ref>] [--shots]
 *   --only a,b            QA only these slugs
 *   --changed-since <ref> QA only the decks whose slide sources changed vs <ref>
 *                         (working tree vs merge-base; see scripts/changed-decks.mjs).
 *                         A change to anything shared — theme, components, scripts,
 *                         public/, decks.json, deps, CI — or an unknown ref widens to
 *                         every deck. Zero affected decks still smoke-tests the landing.
 *                         CI passes the last green `main` commit (or the PR base).
 *   --shots               also write .qa-shots/<slug>/slide-NNN.png for review
 */
import { readFile } from 'node:fs/promises';
import { spawnSync } from 'node:child_process';
import { join, dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { decideFor } from './changed-decks.mjs';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const CONTENT = join(ROOT, 'lectures', 'content');
const QA_DIST = join(ROOT, '.qa-dist');

const argv = process.argv.slice(2);
const opt = (n, d) => { const i = argv.indexOf(n); return i > -1 ? argv[i + 1] : d; };
const ONLY = argv.includes('--only') ? opt('--only') : null;
const SINCE = argv.includes('--changed-since') ? opt('--changed-since') : null;
const SHOTS = argv.includes('--shots');
if (ONLY && SINCE) { console.error('error: pass either --only or --changed-since, not both'); process.exit(2); }

const manifest = JSON.parse(await readFile(join(CONTENT, 'decks.json'), 'utf8'));

// Which slugs to QA: all (default), --only's list, or the decks --changed-since touches.
let only = ONLY ? ONLY.split(',') : null;
if (SINCE) {
  const pick = decideFor(SINCE, ROOT);
  console.log(`▶ --changed-since ${SINCE}: ${pick.all ? 'every deck' : `${pick.slugs.length} deck(s)`} — ${pick.reason}`);
  only = pick.all ? null : pick.slugs;
}
const decks = manifest.decks.filter((d) => !only || only.includes(d.slug));

// 1) Build the selected decks flat (base '/') into .qa-dist/<slug>.
if (decks.length) {
  const buildArgs = ['scripts/build-all.mjs', '--flat-base', '--out', '.qa-dist'];
  if (only) buildArgs.push('--only', only.join(','));
  const build = spawnSync('node', buildArgs, { cwd: ROOT, stdio: 'inherit' });
  if (build.status !== 0) { console.error('❌ build phase failed'); process.exit(1); }
}

// 2) Overflow-check each deck's output dir.
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

// 3) Overview gate (scripts/check-overview.mjs) — once per run, on the first
//    deck under QA that embeds videos (else the first deck): proves the theme +
//    VideoPlayer keep Slidev's all-slides overview cheap on phones.
const hasVideo = async (d) => {
  for (const src of d.srcs) {
    if ((await readFile(join(CONTENT, 'slides', src), 'utf8')).includes('<VideoPlayer')) return true;
  }
  return false;
};
let ovDeck = null;
for (const d of decks) if (await hasVideo(d)) { ovDeck = d; break; }
ovDeck ??= decks[0];
if (ovDeck) {
  process.stdout.write(`\n▶ overview check (${ovDeck.slug}) …\n`);
  const ov = spawnSync('node', [join(ROOT, 'scripts', 'check-overview.mjs'), join(QA_DIST, ovDeck.slug)], { cwd: ROOT, stdio: 'inherit' });
  if (ov.status !== 0) { bad++; summary.push(`✗ overview (${ovDeck.slug})`); } else summary.push(`✓ overview (${ovDeck.slug})`);
}

// 4) Landing smoke test (decks build --flat-base with no landing, so build one).
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
