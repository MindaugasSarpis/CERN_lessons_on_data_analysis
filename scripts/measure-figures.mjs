#!/usr/bin/env node
// Measure the box each scripted figure gets on a `class: fill` slide and
// write it to figures/src/sizes.json, so that `pnpm figures` draws every
// figure at the size of its box: the frame and the figure coincide and the
// figure fills the rest of the slide (lecturer, 5 Nov 2026).
//
// Usage:
//   node scripts/build-all.mjs --flat-base --out .qa-dist --only <slug>
//   node scripts/measure-figures.mjs --only <slug>[,<slug>...]
//   then regenerate the figures (pnpm figures, or build.py --only <family>)
//
// A box is measured on the slide canvas (980 px wide), inside the frame's
// padding, and turned into inches at PX_PER_IN: at that scale a 10 pt tick
// label reads about as large as a caption. A small box (a card of a three-
// figure grid) is drawn larger in inches, so its text takes less of it.
// Only SVGs of public/figures/viz_* are measured; other images keep theirs.
// A built deck names them /figures/viz_x.svg?v=<content hash>
// (lectures/content/vite.config.mts): the query is not part of the name.
import { createServer } from 'node:http';
import { readFile, writeFile } from 'node:fs/promises';
import { join, extname, dirname, basename } from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium } from 'playwright-chromium';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const argv = process.argv.slice(2);
const only = argv.includes('--only') ? argv[argv.indexOf('--only') + 1].split(',') : null;
if (!only) { console.error('usage: measure-figures.mjs --only <slug>[,<slug>]'); process.exit(2); }
const OUT = join(ROOT, 'figures', 'src', 'sizes.json');
const PX_PER_IN = 90;
const PX_PER_IN_SMALL = 75;   // boxes narrower than SMALL_W
const SMALL_W = 420;
// Figures whose 3D axes are placed by hand for their own canvas (figures/src/
// beyond.py, advanced.py): resized, they crop their axis labels. They keep their figsize
// and sit centred in their box.
const KEEP_OWN_SIZE = new Set(['viz_beyond_surface', 'viz_beyond_scatter4d', 'viz_advanced_slices']);

const TYPES = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.svg': 'image/svg+xml',
  '.png': 'image/png', '.jpg': 'image/jpeg', '.webp': 'image/webp', '.woff2': 'font/woff2', '.json': 'application/json' };

function serve(dir) {
  const server = createServer(async (req, res) => {
    let p = decodeURIComponent(req.url.split('?')[0]);
    if (p.endsWith('/')) p += 'index.html';
    try {
      const body = await readFile(join(dir, p));
      res.writeHead(200, { 'content-type': TYPES[extname(p)] || 'application/octet-stream' });
      res.end(body);
    } catch {
      res.writeHead(200, { 'content-type': 'text/html' });
      res.end(await readFile(join(dir, 'index.html')));
    }
  }).listen(0);
  return server;
}

let sizes = {};
try { sizes = JSON.parse(await readFile(OUT, 'utf8')); } catch { /* first run */ }

const browser = await chromium.launch();
for (const slug of only) {
  const server = serve(join(ROOT, '.qa-dist', slug));
  const base = `http://localhost:${server.address().port}`;
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  await page.goto(`${base}/#/1`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(1000);
  // the slide count, from the "N / M" counter of the nav bar (as check-slides.mjs)
  const total = await page.evaluate(() => {
    for (const el of document.querySelectorAll('*')) {
      if (el.children.length) continue;
      const m = (el.textContent || '').trim().match(/^(\d+)\s*\/\s*(\d+)$/);
      if (m) return Number(m[2]);
    }
    const bm = document.body.innerText.match(/\b\d+\s*\/\s*(\d+)\b/);
    return bm ? Number(bm[1]) : 0;
  });
  if (!total) { console.error(`${slug}: could not read the slide count`); process.exit(2); }
  let found = 0;
  for (let n = 1; n <= total; n++) {
    await page.goto(`${base}/#/${n}`);
    await page.waitForTimeout(250);
    const boxes = await page.evaluate((n) => {
      const layout = document.querySelector(`.slidev-page-${n} .slidev-layout`);
      if (!layout || !layout.classList.contains('fill')) return [];
      return [...layout.querySelectorAll('img')]
        .filter((img) => /\/figures\/viz_[^/?#]+\.svg(?:[?#]|$)/.test(img.getAttribute('src') || ''))
        .map((img) => {
          const cs = getComputedStyle(img);
          const w = img.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
          const h = img.clientHeight - parseFloat(cs.paddingTop) - parseFloat(cs.paddingBottom);
          return { src: img.getAttribute('src'), w, h };
        });
    }, n);
    for (const b of boxes) {
      const name = basename(b.src.split(/[?#]/)[0], '.svg'); // a build adds ?v=<content hash>
      if (KEEP_OWN_SIZE.has(name)) { delete sizes[name]; continue; }
      const ppi = b.w < SMALL_W ? PX_PER_IN_SMALL : PX_PER_IN;
      sizes[name] = [+(b.w / ppi).toFixed(2), +(b.h / ppi).toFixed(2)];
      console.log(`  slide ${n}: ${name} ${Math.round(b.w)}×${Math.round(b.h)} px → ${sizes[name].join(' × ')} in`);
      found++;
    }
  }
  console.log(`${slug}: ${found} figure box(es)`);
  await page.close();
  server.close();
}
await browser.close();
const sorted = Object.fromEntries(Object.keys(sizes).sort().map((k) => [k, sizes[k]]));
await writeFile(OUT, '{\n' + Object.entries(sorted).map(([k, v]) => ` ${JSON.stringify(k)}: [${v.join(', ')}]`).join(',\n') + '\n}\n');
console.log(`wrote ${OUT}`);
