#!/usr/bin/env node
/**
 * check-slides.mjs — fast full-deck visual QA harness.
 *
 * Renders EVERY slide of a built deck and (a) measures content overflow and
 * (b) optionally screenshots each slide, so the whole deck can be checked for
 * overflow AND reviewed for content/style on each styling iteration.
 *
 * Speed: instead of a full page-reload per slide, each worker loads the deck
 * ONCE and then client-side-navigates (history + popstate) through its shard,
 * settling on `.slidev-page[data-slidev-no=N]` (instant, reliable). N workers
 * run in parallel. ~10-20s for the whole published deck vs ~5min for reload-
 * per-slide.
 *
 * Usage:
 *   1. Build through an entry point that loads the theme (NOT a single
 *      slides/L0X.md — that drops the custom theme):
 *        pnpm exec slidev build lectures/content/best_research_and_data_analysis_practices_from_CERN.md --out .qa-dist
 *   2. node scripts/check-slides.mjs .qa-dist [options]
 *        --shots <dir>      also write <dir>/slide-<NNN>.png for every slide
 *        --workers <n>      parallel browser pages (default 6)
 *        --tolerance <px>   overflow tolerance (default 6)
 *        --only 8,76,...    check only these slide numbers
 *
 * Exit 0 = all slides fit; 1 = at least one overflows (or error).
 * Requires playwright-chromium (already a devDependency).
 */
import { createServer } from 'node:http';
import { readFile, stat, mkdir } from 'node:fs/promises';
import { join, extname, normalize } from 'node:path';
import { chromium } from 'playwright-chromium';

const argv = process.argv.slice(2);
const distDir = argv[0];
if (!distDir || distDir.startsWith('--')) {
  console.error('usage: node scripts/check-slides.mjs <distDir> [--shots <dir>] [--workers n] [--tolerance px] [--only a,b,c]');
  process.exit(2);
}
const opt = (name, def) => { const i = argv.indexOf(name); return i > -1 ? argv[i + 1] : def; };
const TOL = Number(opt('--tolerance', 6));
const WORKERS = Number(opt('--workers', 6));
const SHOTS = opt('--shots', null);
const ONLY = argv.includes('--only') ? opt('--only').split(',').map(Number) : null;

const MIME = {
  '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript',
  '.css': 'text/css', '.json': 'application/json', '.svg': 'image/svg+xml',
  '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.jfif': 'image/jpeg',
  '.webp': 'image/webp', '.avif': 'image/avif', '.gif': 'image/gif',
  '.woff': 'font/woff', '.woff2': 'font/woff2', '.ttf': 'font/ttf',
  '.mp4': 'video/mp4', '.ico': 'image/x-icon',
};

const server = createServer(async (req, res) => {
  try {
    const url = decodeURIComponent(req.url.split('?')[0]);
    let fp = normalize(join(distDir, url));
    if (!fp.startsWith(normalize(distDir))) { res.statusCode = 403; return res.end(); }
    let s = await stat(fp).catch(() => null);
    if (s && s.isDirectory()) { fp = join(fp, 'index.html'); s = await stat(fp).catch(() => null); }
    if (!s) fp = join(distDir, 'index.html'); // SPA fallback
    res.setHeader('Content-Type', MIME[extname(fp)] || 'application/octet-stream');
    res.end(await readFile(fp));
  } catch (e) { res.statusCode = 500; res.end(String(e)); }
});
const port = await new Promise((r) => server.listen(0, '127.0.0.1', () => r(server.address().port)));
const base = `http://127.0.0.1:${port}`;

// Hide decorative backdrops (they intentionally bleed past the frame) and
// pre-click v-click transforms (parked off-frame before reveal), plus all
// transitions (so no outgoing slide lingers), so we measure real CONTENT.
const NEUTRALIZE = `
  *, *::before, *::after { transition: none !important; animation: none !important; }
  .aurora, .vol-light, .cover-bg, .cover-accent, .section-accent { display: none !important; }
  /* Force the fully-revealed end-state: v-click/reveal content is otherwise
     hidden at click-index 0, so screenshots would miss it and overflow would
     be measured pre-reveal. Showing all of it makes screenshots faithful and
     overflow worst-case (fits in every click state → fits, period). */
  .slidev-vclick-hidden, .reveal-left, .reveal-up, .reveal-scale, .reveal-blur {
    transform: none !important; filter: none !important;
    visibility: visible !important; opacity: 1 !important;
  }
  .anim-ex.slidev-vclick-hidden { max-height: none !important; }`;

if (SHOTS) await mkdir(SHOTS, { recursive: true });
const browser = await chromium.launch();

// Video slides never reach networkidle (streaming / remote-release fallback
// fetches), and their downloads starve the per-slide JS chunk loads — one
// video slide can time out an entire worker's shard. Videos contribute
// nothing to overflow measurement, so abort all media requests up front.
async function newQAPage() {
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  await page.route('**/*', (route) =>
    route.request().resourceType() === 'media' || /\.(mp4|webm|mov)(\?|$)/i.test(route.request().url())
      ? route.abort()
      : route.continue());
  return page;
}

// Read total slide count once from the "N / M" nav counter.
const probe = await newQAPage();
await probe.goto(`${base}/1`, { waitUntil: 'domcontentloaded' });
await probe.waitForSelector('.slidev-layout', { timeout: 30000 }).catch(() => {});
await probe.waitForTimeout(1000);
const total = await probe.evaluate(() => {
  for (const el of document.querySelectorAll('*')) {
    if (el.children.length) continue;
    const m = (el.textContent || '').trim().match(/^(\d+)\s*\/\s*(\d+)$/);
    if (m) return Number(m[2]);
  }
  const bm = document.body.innerText.match(/\b\d+\s*\/\s*(\d+)\b/);
  return bm ? Number(bm[1]) : null;
});
await probe.close();
if (!total) { console.error('Could not read slide count.'); await browser.close(); server.close(); process.exit(2); }

const slides = ONLY ? ONLY.filter((n) => n >= 1 && n <= total) : Array.from({ length: total }, (_, i) => i + 1);
console.log(`Checking ${slides.length}/${total} slides with ${WORKERS} workers${SHOTS ? `, screenshots → ${SHOTS}` : ''} (tolerance ${TOL}px)...`);

// Split into contiguous shards, one per worker.
const shardSize = Math.ceil(slides.length / WORKERS);
const shards = [];
for (let i = 0; i < slides.length; i += shardSize) shards.push(slides.slice(i, i + shardSize));

const offenders = [];
const skipped = [];
let measured = 0;
const t0 = Date.now();

async function runShard(shard) {
  const page = await newQAPage();
  await page.goto(`${base}/${shard[0]}`, { waitUntil: 'domcontentloaded' });
  await page.waitForSelector('.slidev-layout', { timeout: 30000 }).catch(() => {});
  await page.addStyleTag({ content: NEUTRALIZE });
  // Decks build with `routerMode: hash` (GitHub Pages has no SPA rewrites); a
  // hash build normalizes its URL to `#/1` on load, which is how we detect it.
  // History-mode fallback kept for legacy builds (e.g. the combined entry).
  const hashNav = await page.evaluate(() => location.hash.startsWith('#/'));
  for (const n of shard) {
    await page.evaluate(({ n, hashNav }) => {
      if (hashNav) location.hash = '#/' + n;
      else { history.pushState({}, '', '/' + n); window.dispatchEvent(new PopStateEvent('popstate')); }
    }, { n, hashNav });
    await page.waitForSelector(`.slidev-page[data-slidev-no="${n}"] .slidev-layout`, { timeout: 8000 }).catch(() => {});
    await page.addStyleTag({ content: NEUTRALIZE }); // re-assert after slide swap
    const m = await page.evaluate((n) => {
      const pg = document.querySelector(`.slidev-page[data-slidev-no="${n}"]`);
      const el = pg ? pg.querySelector('.slidev-layout') : document.querySelector('.slidev-layout');
      if (!el) return null;
      const h = el.querySelector('h1, h2');
      return { oy: el.scrollHeight - el.clientHeight, ox: el.scrollWidth - el.clientWidth,
               title: (h ? h.textContent : '').trim().slice(0, 60) };
    }, n);
    if (SHOTS) {
      // Force the revealed end-state for the screenshot. Some theme rules
      // (e.g. `.card-glass.slidev-vclick-hidden{opacity:0!important}`) out-
      // specify a stylesheet override, so set inline styles — inline !important
      // beats any stylesheet !important regardless of specificity.
      await page.evaluate(() => {
        // Also reveal mount-gated content wrappers (section/cover fade in on a
        // setTimeout after mount; a fast screenshot would otherwise catch them
        // at opacity 0 → blank slide).
        for (const el of document.querySelectorAll('.slidev-vclick-hidden, .reveal-left, .reveal-up, .reveal-scale, .reveal-blur, .section-body, .cover-content')) {
          el.style.setProperty('opacity', '1', 'important');
          el.style.setProperty('visibility', 'visible', 'important');
          el.style.setProperty('transform', 'none', 'important');
          el.style.setProperty('filter', 'none', 'important');
        }
      });
      await page.screenshot({ path: join(SHOTS, `slide-${String(n).padStart(3, '0')}.png`) });
    }
    // Note: for .anim-card slides (L06 / video deck) the neutralized state
    // shows a large heading AND fully-expanded examples at once — taller than
    // ever renders live — so those may be *over*-reported. That can only inflate
    // the offender list, never hide real overflow.
    if (!m) { skipped.push(n); continue; } // slide never settled — do NOT count as "fits"
    measured++;
    if (m.oy > TOL || m.ox > TOL) {
      offenders.push({ n, ...m });
      console.log(`  ✗ slide ${n}: overflow y=${m.oy}px x=${m.ox}px  — "${m.title}"`);
    }
  }
  await page.close();
}

await Promise.all(shards.map(runShard));
await browser.close();
server.close();

offenders.sort((a, b) => a.n - b.n);
skipped.sort((a, b) => a - b);
const secs = ((Date.now() - t0) / 1000).toFixed(1);
console.log(`\nMeasured ${measured}/${slides.length} slides in ${secs}s.`);
if (skipped.length) {
  // A slide that never rendered was NOT verified — never report it as "fits".
  console.log(`⚠️  ${skipped.length} slide(s) failed to render and were NOT checked: ${skipped.join(', ')}`);
}
if (offenders.length) {
  console.log(`❌ ${offenders.length} slide(s) overflow the frame (tolerance ${TOL}px).`);
  console.log('   Offending slides: ' + offenders.map((o) => o.n).join(', '));
}
if (offenders.length === 0 && skipped.length === 0) {
  console.log(`✅ No overflow: all ${slides.length} slides fit the frame.`);
  process.exit(0);
}
process.exit(1);
