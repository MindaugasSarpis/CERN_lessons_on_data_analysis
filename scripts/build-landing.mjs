#!/usr/bin/env node
/**
 * build-landing.mjs — build the landing enhancement bundle (Vite) and emit the
 * landing page: <out>/assets/* + <out>/index.html + <out>/404.html.
 * Used by build-all.mjs (normal builds) and qa-all.mjs (landing smoke test).
 *
 * Standalone: node scripts/build-landing.mjs [--out dist] [--base <prefix>]
 */
import { readFile, mkdir, cp } from 'node:fs/promises';
import { spawnSync } from 'node:child_process';
import { join, dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { genLanding } from './gen-landing.mjs';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');

export async function buildLanding(outDir, prefix = '') {
  const r = spawnSync('pnpm', ['exec', 'vite', 'build', '--config', join(ROOT, 'landing', 'vite.config.mjs')],
    { cwd: ROOT, stdio: 'inherit' });
  if (r.status !== 0) throw new Error('vite build (landing) failed');
  await mkdir(join(outDir, 'assets'), { recursive: true });
  await cp(join(ROOT, 'landing', 'dist-assets', 'assets'), join(outDir, 'assets'),
    { recursive: true, filter: (src) => !src.endsWith('.woff') });
  return genLanding(JSON.parse(await readFile(join(ROOT, 'lectures', 'content', 'decks.json'), 'utf8')), outDir, prefix);
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const argv = process.argv.slice(2);
  const opt = (n, d) => { const i = argv.indexOf(n); return i > -1 ? argv[i + 1] : d; };
  const p = await buildLanding(resolve(ROOT, opt('--out', 'dist')), opt('--base', ''));
  console.log(`Landing → ${p}`);
}
