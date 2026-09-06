#!/usr/bin/env node
/**
 * check-overview.mjs — gate the cost of Slidev's quick overview (grid button /
 * `o` key) on a built deck. The overview mounts EVERY slide live, which on a
 * phone was a multi-second freeze for the video-heavy decks. The theme + the
 * VideoPlayer component keep it cheap; this check proves they still do:
 *
 *   1. no <video> element is mounted inside the overview (each video slide
 *      renders a static placeholder there) and opening the overview from a
 *      video slide fires NO media request (the overview copy of the current
 *      slide used to re-download the clip being watched);
 *   2. no card inside the overview has a backdrop-filter (each one forces its
 *      own compositor layer);
 *   3. every overview slide container has `content-visibility: auto`, so only
 *      the on-screen rows are laid out and painted.
 *
 * The overview overlay is matched by Slidev's own utility classes
 * (`.z-modal.overflow-y-auto`) — if a Slidev upgrade renames them, (2)/(3)
 * fail here instead of silently regressing on phones.
 *
 * Usage: node scripts/check-overview.mjs <distDir built with --flat-base>
 * Exit 0 = all assertions hold; 1 = at least one fails (or error).
 */
import { createServer } from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import { join, extname, normalize } from 'node:path';
import { chromium, devices } from 'playwright-chromium';

const distDir = process.argv[2];
if (!distDir || distDir.startsWith('--')) {
  console.error('usage: node scripts/check-overview.mjs <distDir>');
  process.exit(2);
}

const MIME = {
  '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript', '.css': 'text/css',
  '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg', '.webp': 'image/webp', '.gif': 'image/gif', '.woff': 'font/woff',
  '.woff2': 'font/woff2', '.ttf': 'font/ttf', '.mp4': 'video/mp4', '.webm': 'video/webm',
};
const server = createServer(async (req, res) => {
  try {
    const url = decodeURIComponent(req.url.split('?')[0]);
    let fp = normalize(join(distDir, url));
    if (!fp.startsWith(normalize(distDir))) { res.statusCode = 403; return res.end(); }
    let s = await stat(fp).catch(() => null);
    if (s && s.isDirectory()) { fp = join(fp, 'index.html'); s = await stat(fp).catch(() => null); }
    if (!s) fp = join(distDir, 'index.html');
    res.setHeader('Content-Type', MIME[extname(fp)] || 'application/octet-stream');
    res.end(await readFile(fp));
  } catch (e) { res.statusCode = 500; res.end(String(e)); }
});
const port = await new Promise((r) => server.listen(0, '127.0.0.1', () => r(server.address().port)));
const base = `http://127.0.0.1:${port}`;

const OVERLAY = '.z-modal.overflow-y-auto';
const browser = await chromium.launch();
const context = await browser.newContext({ ...devices['iPhone 13'] });
const page = await context.newPage();
const media = [];
await page.route(/\.(mp4|webm)(\?|$)/, (r) => { media.push(r.request().url().split('/').pop()); r.abort(); });

// Overview is "rendered" once every slide wrapper has its layout root mounted
// (slide components are async chunks — the wrapper appears before the content).
const overviewRendered = (sel) => {
  const pages = document.querySelectorAll(`${sel} .slidev-page`);
  return pages.length > 0 && [...pages].every((p) => p.querySelector('.slidev-layout'));
};
const openOverview = async () => {
  const t0 = Date.now();
  await page.keyboard.press('o');
  await page.waitForFunction(overviewRendered, OVERLAY, { timeout: 60000 });
  await page.waitForTimeout(1000);
  return Date.now() - t0;
};

await page.goto(`${base}/#/1`);
await page.waitForSelector('.slidev-page[data-slidev-no="1"] .slidev-layout');
await page.waitForTimeout(1000);

// Pass 1: discover the video slides from the overview itself.
await openOverview();
const videoSlides = await page.evaluate((sel) => [...new Set(
  [...document.querySelectorAll(`${sel} .video-player`)].map((el) => +el.closest('[data-slidev-no]').dataset.slidevNo),
)].sort((a, b) => a - b), OVERLAY);
await page.keyboard.press('Escape');
await page.waitForFunction((sel) => !document.querySelector(sel), OVERLAY);

// Pass 2: sit on a video slide (its own player loads), then open the overview.
const startSlide = videoSlides[0] ?? 1;
if (videoSlides.length) {
  await page.evaluate((n) => { location.hash = `#/${n}`; }, startSlide);
  await page.waitForSelector(`#slide-content .slidev-page[data-slidev-no="${startSlide}"] .video-player`);
  // Let the main player settle (ready, or errored because media is aborted here).
  await page.waitForFunction(
    (n) => !!document.querySelector(`#slide-content .slidev-page[data-slidev-no="${n}"] .video-player`)
      && !document.querySelector(`#slide-content .slidev-page[data-slidev-no="${n}"] .video-status:not(.video-error)`),
    startSlide, { timeout: 15000 },
  ).catch(() => {});
  await page.waitForTimeout(1500);
}
const mediaBefore = media.length;
const openMs = await openOverview();
const r = await page.evaluate((sel) => {
  const ov = document.querySelector(sel);
  const cards = [...ov.querySelectorAll('.card')];
  const containers = [...ov.querySelectorAll('.slidev-slide-container')];
  return {
    slides: ov.querySelectorAll('.slidev-page').length,
    videos: ov.querySelectorAll('video').length,
    placeholders: ov.querySelectorAll('.video-placeholder').length,
    cards: cards.length,
    blurredCards: cards.filter((c) => getComputedStyle(c).backdropFilter !== 'none').length,
    containers: containers.length,
    lazyContainers: containers.filter((c) => getComputedStyle(c).contentVisibility === 'auto').length,
  };
}, OVERLAY);
const mediaAfter = media.slice(mediaBefore);
await browser.close();
server.close();

const checks = [
  [`no <video> mounted in the overview (${r.videos} video, ${r.placeholders} placeholders across ${videoSlides.length} video slides)`, r.videos === 0],
  [`no media request when opening the overview from slide ${startSlide} (${mediaAfter.length}: ${mediaAfter.join(', ') || '-'})`, mediaAfter.length === 0],
  [`no card blur in the overview (${r.blurredCards}/${r.cards} cards blurred)`, r.blurredCards === 0],
  [`overview slide containers are content-visibility:auto (${r.lazyContainers}/${r.containers})`, r.containers > 0 && r.lazyContainers === r.containers],
];
console.log(`overview: ${r.slides} slides rendered in ${openMs} ms (iPhone viewport, unthrottled)`);
let bad = 0;
for (const [label, ok] of checks) { console.log(`${ok ? '✓' : '✗'} ${label}`); if (!ok) bad++; }
if (bad) { console.error(`\n❌ overview check: ${bad} assertion(s) failed (${distDir})`); process.exit(1); }
console.log('✅ overview check passed');
