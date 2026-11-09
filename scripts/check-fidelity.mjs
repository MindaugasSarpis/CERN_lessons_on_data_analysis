#!/usr/bin/env node
/**
 * check-fidelity.mjs: every figure a deck shows must be vector and crisp.
 *
 * The lecturer, 9 Nov 2026, on the live Lecture 7: "Focus on fidelity,
 * everything has to be vectorized, crisp, good fidelity. The same applies to
 * all of the slides." Slidev scales each slide with a CSS transform, so a
 * bitmap (or a PNG that matplotlib embeds in an SVG for `rasterized=True` or
 * `imshow`) turns grainy on a projector.
 *
 * For each deck of decks.json (or --only a,b), every image its slide files
 * reference (`src="/…"`, `![…](/…)`, a frontmatter `image:` or `background:`) is checked:
 *   - an SVG must not contain an <image> (an embedded or linked bitmap);
 *   - a GIF, PNG, JPG or WebP fails, unless scripts/fidelity-allow.json lists
 *     it with the reason it is a bitmap by nature (a photo, a screenshot, a
 *     picture about pixels).
 * Components draw their own SVG and are not checked here.
 *
 *   node scripts/check-fidelity.mjs [--only slug,slug]     exit 1 on a failure
 */
import { readFileSync, existsSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const CONTENT = join(ROOT, 'lectures', 'content');
const PUBLIC = join(CONTENT, 'public');
const argv = process.argv.slice(2);
const only = argv.includes('--only') ? argv[argv.indexOf('--only') + 1].split(',') : null;

const manifest = JSON.parse(readFileSync(join(CONTENT, 'decks.json'), 'utf8'));
const allowFile = join(ROOT, 'scripts', 'fidelity-allow.json');
const allow = existsSync(allowFile) ? JSON.parse(readFileSync(allowFile, 'utf8')).bitmaps ?? {} : {};

const BITMAP = /\.(gif|png|jpe?g|webp)$/i;
let failures = 0;
for (const deck of manifest.decks.filter((d) => !only || only.includes(d.slug))) {
  const refs = new Set();
  for (const src of deck.srcs) {
    const md = readFileSync(join(CONTENT, 'slides', src), 'utf8');
    for (const m of md.matchAll(/src="(\/[^"#?]+)"/g)) refs.add(m[1]);
    for (const m of md.matchAll(/!\[[^\]]*\]\((\/[^)\s#?]+)/g)) refs.add(m[1]);
    for (const m of md.matchAll(/^(?:image|background):\s*['"]?(\/[^'"\s#?]+)/gm)) refs.add(m[1]);
  }
  const bad = [];
  for (const ref of [...refs].sort()) {
    const file = join(PUBLIC, ref.slice(1));
    if (!existsSync(file)) continue; // a missing file is the build's error, not ours
    const name = ref.slice(1);
    if (ref.endsWith('.svg')) {
      const images = (readFileSync(file, 'utf8').match(/<image\b/g) ?? []).length;
      if (images) bad.push(`${name}: ${images} bitmap(s) inside the SVG (rasterized=True or imshow)`);
    } else if (BITMAP.test(ref) && !allow[name]) {
      bad.push(`${name}: a bitmap; draw it as SVG, or list it in scripts/fidelity-allow.json with the reason it is a bitmap by nature`);
    }
  }
  if (bad.length) {
    failures += bad.length;
    console.log(`✗ ${deck.slug}`);
    for (const b of bad) console.log(`    ${b}`);
  } else {
    console.log(`✓ ${deck.slug}`);
  }
}
if (failures) {
  console.log(`\n${failures} figure(s) not vector. Fidelity rule: CLAUDE.md, Visual QA, hard requirement (5).`);
  process.exit(1);
}
