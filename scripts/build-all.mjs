#!/usr/bin/env node
/**
 * build-all.mjs — build every deck in decks.json to <out>/<slug>/, then emit
 * the landing page at <out>/index.html.
 *
 * Each deck is an independent Slidev SPA at base `<prefix>/<slug>/`, so a
 * visitor loads only that lecture (the mobile-load fix). `--out` is passed to
 * Slidev as an ABSOLUTE path (Slidev resolves a relative --out against the
 * entry file's dir, which is not what we want).
 *
 * Usage:
 *   node scripts/build-all.mjs [--out dist] [--base <prefix>] [--only a,b]
 *     --out <dir>     output root (default: dist), relative to repo root
 *     --base <prefix> URL prefix; per-deck base is `<prefix>/<slug>/`
 *                     (default '' → '/<slug>/'; Pages uses '/<repo>')
 *     --only a,b      build only these slugs (landing still lists all)
 *   Exit non-zero if any deck build fails.
 */
import { readFile, rm, mkdir, readdir } from 'node:fs/promises';
import { spawnSync } from 'node:child_process';
import { join, dirname, resolve, isAbsolute } from 'node:path';
import { fileURLToPath } from 'node:url';
import { buildLanding } from './build-landing.mjs';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const CONTENT = join(ROOT, 'lectures', 'content');

const argv = process.argv.slice(2);
const opt = (name, def) => { const i = argv.indexOf(name); return i > -1 ? argv[i + 1] : def; };
const OUT = resolve(ROOT, opt('--out', 'dist'));
const PREFIX = opt('--base', '').replace(/\/$/, ''); // no trailing slash
const ONLY = argv.includes('--only') ? new Set(opt('--only').split(',')) : null;
const KEEP_VIDEOS = argv.includes('--keep-videos');
// --flat-base: build every deck at base '/' (each served standalone at root),
// which is what the headless overflow checker needs. No landing page in this mode.
const FLAT = argv.includes('--flat-base');

const manifest = JSON.parse(await readFile(join(CONTENT, 'decks.json'), 'utf8'));

// Always regenerate entries first so manifest edits propagate.
const gen = spawnSync('node', [join(ROOT, 'scripts', 'gen-entries.mjs')], { stdio: 'inherit' });
if (gen.status !== 0) process.exit(gen.status ?? 1);

await rm(OUT, { recursive: true, force: true });
await mkdir(OUT, { recursive: true });

// Build the landing (Vite assets + index.html) FIRST so a static server
// pointed at OUT stays valid during rebuilds — otherwise a mid-build refresh
// shows a bare directory listing. Skipped in flat-base/QA mode.
if (!FLAT) await buildLanding(OUT, PREFIX);

const targets = manifest.decks.filter((d) => !ONLY || ONLY.has(d.slug));
let failed = 0;
for (const deck of targets) {
  const base = FLAT ? '/' : `${PREFIX}/${deck.slug}/`;
  const outDir = join(OUT, deck.slug);
  process.stdout.write(`\n▶ building ${deck.slug} (base ${base}) …\n`);
  const r = spawnSync(
    'pnpm',
    ['exec', 'slidev', 'build', join(CONTENT, `deck.${deck.slug}.md`),
      '--out', outDir, '--base', base],
    { stdio: 'inherit', env: { ...process.env, NODE_OPTIONS: '--max-old-space-size=4096' } },
  );
  if (r.status !== 0) { console.error(`✗ ${deck.slug} FAILED`); failed++; }
  else {
    // Videos are served from the GitHub-release remote fallback (they are
    // gitignored and absent in CI). Slidev copies any LOCAL videos into every
    // deck's public/ — strip them so output stays small and matches production.
    if (!KEEP_VIDEOS) await rm(join(outDir, 'videos'), { recursive: true, force: true });
    console.log(`✓ ${deck.slug}`);
  }
}

if (!FLAT) console.log(`\nLanding page → ${join(OUT, 'index.html')}`);

if (failed) { console.error(`\n❌ ${failed}/${targets.length} deck(s) failed to build.`); process.exit(1); }
console.log(`\n✅ Built ${targets.length} deck(s) → ${OUT}`);
