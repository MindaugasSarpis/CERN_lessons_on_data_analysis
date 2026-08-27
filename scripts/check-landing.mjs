#!/usr/bin/env node
/**
 * check-landing.mjs — smoke-test a BUILT landing directory (index.html +
 * assets/). Asserts: title, every released deck link (and that drafts are
 * listed unlinked as "coming soon"), JS boot (js class),
 * scene-or-fallback gating (field-on | static-bg), reveal-on-scroll, the
 * reduced-motion fallback, zero console/page errors, and (with ?qa +
 * preserveDrawingBuffer) that the WebGL scene renders non-blank pixels and
 * that scroll moves the camera (via the ?qa-gated window.__qaCam hook).
 *
 * Usage: node scripts/check-landing.mjs <distDir> [--base <prefix>]
 * Exit 0 = pass; 1 = failures; 2 = usage.
 */
import { createServer } from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import { join, extname, normalize, resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium } from 'playwright-chromium';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const argv = process.argv.slice(2);
const distDir = argv[0];
if (!distDir || distDir.startsWith('--')) {
  console.error('usage: node scripts/check-landing.mjs <distDir> [--base <prefix>]');
  process.exit(2);
}
const opt = (n, d) => { const i = argv.indexOf(n); return i > -1 ? argv[i + 1] : d; };
const PREFIX = opt('--base', '').replace(/\/$/, '');

const manifest = JSON.parse(await readFile(join(ROOT, 'lectures', 'content', 'decks.json'), 'utf8'));

// Every released deck must have exactly one linked row; every draft must be
// listed (title visible) but NOT linked — a draft's deck dir is absent in dist.
async function checkRows(page) {
  for (const d of manifest.decks) {
    const href = `${PREFIX}/${d.slug}/`;
    const links = await page.locator(`a.row[href="${href}"]`).count();
    if (d.draft) {
      ok(links === 0, `draft ${d.slug} not linked`);
      ok(await page.locator(`.row.soon[data-slug="${d.slug}"]`).count() === 1, `draft ${d.slug} listed as coming soon`);
    } else {
      ok(links === 1, `deck link ${href}`);
    }
  }
}

const MIME = {
  '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript',
  '.css': 'text/css', '.json': 'application/json', '.svg': 'image/svg+xml',
  '.png': 'image/png', '.jpg': 'image/jpeg', '.woff': 'font/woff', '.woff2': 'font/woff2',
};
const server = createServer(async (req, res) => {
  try {
    const url = decodeURIComponent(req.url.split('?')[0]);
    let fp = normalize(join(distDir, url));
    if (!fp.startsWith(normalize(distDir))) { res.statusCode = 403; return res.end(); }
    let s = await stat(fp).catch(() => null);
    if (s && s.isDirectory()) { fp = join(fp, 'index.html'); s = await stat(fp).catch(() => null); }
    if (!s) { res.statusCode = 404; return res.end('not found'); }
    res.setHeader('Content-Type', MIME[extname(fp)] || 'application/octet-stream');
    res.end(await readFile(fp));
  } catch (e) { res.statusCode = 500; res.end(String(e)); }
});
const port = await new Promise((r) => server.listen(0, '127.0.0.1', () => r(server.address().port)));
const home = `http://127.0.0.1:${port}/`;

const fails = [];
const ok = (cond, label) => { console.log(`  ${cond ? '✓' : '✗'} ${label}`); if (!cond) fails.push(label); };

// SwiftShader flags: headless Chromium provides software WebGL2 with these.
const browser = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });

async function loadPage({ reducedMotion }) {
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 800 }, reducedMotion });
  const page = await ctx.newPage();
  const errors = [];
  page.on('console', (m) => { if (m.type() === 'error') errors.push(m.text()); });
  page.on('pageerror', (e) => errors.push(String(e)));
  await page.goto(home, { waitUntil: 'load' });
  await page.waitForFunction(() => document.documentElement.classList.contains('js'), null, { timeout: 15000 })
    .catch(() => {});
  return { ctx, page, errors };
}

// Each pass is wrapped so a thrown assertion (e.g. locator timeout) records a
// failure instead of aborting the run; the context, browser, and server are
// always closed so a failing run exits 1 with the tidy summary — never via an
// uncaught exception or a leaked Chromium process.
try {
  console.log('— pass 1: default (scene expected where WebGL2 available) —');
  {
    let ctx;
    try {
      const loaded = await loadPage({ reducedMotion: 'no-preference' });
      ctx = loaded.ctx;
      const { page, errors } = loaded;
      ok(await page.title() === manifest.course, 'title matches manifest.course');
      await checkRows(page);
      // textContent, not innerText: Task 4's CSS puts text-transform: uppercase
      // on .kicker/.foot, and Playwright's innerText() is render-aware (it
      // reflects the transformed case) while these assertions care about the
      // authored content, not the presentational casing.
      ok(await page.locator('.hero .kicker').textContent() === manifest.presenter, 'presenter in hero');
      ok((await page.locator('footer.foot').textContent()).includes('seminar'), 'seminar footer note');
      const gated = await page.waitForFunction(() => {
        const c = document.documentElement.classList;
        return (c.contains('field-on') || c.contains('static-bg')) ? (c.contains('field-on') ? 'field-on' : 'static-bg') : false;
      }, null, { timeout: 20000 }).then((h) => h.jsonValue()).catch(() => null);
      ok(gated === 'field-on' || gated === 'static-bg', `boot gate resolved (${gated})`);
      if (gated === 'field-on') {
        ok(await page.evaluate(() => {
          const c = document.getElementById('field');
          return c && c.width >= innerWidth * 0.6 && c.height >= innerHeight * 0.6;
        }), 'canvas backing size covers viewport');
      }
      // Reveal-on-scroll: last row must become visible after scrolling to bottom.
      await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
      const revealed = await page.waitForFunction(() => {
        const rows = document.querySelectorAll('li.reveal');
        const last = rows[rows.length - 1];
        return last && getComputedStyle(last).opacity === '1';
      }, null, { timeout: 10000 }).then(() => true).catch(() => false);
      ok(revealed, 'last row revealed after scroll');
      ok(errors.length === 0, `no console/page errors${errors.length ? ` — got: ${errors.join(' | ').slice(0, 300)}` : ''}`);
    } catch (e) {
      ok(false, `pass aborted: ${e.message}`);
    } finally {
      if (ctx) await ctx.close().catch(() => {});
    }
  }

  console.log('— pass 2: prefers-reduced-motion (static fallback expected) —');
  {
    let ctx;
    try {
      const loaded = await loadPage({ reducedMotion: 'reduce' });
      ctx = loaded.ctx;
      const { page, errors } = loaded;
      const cls = await page.evaluate(() => [...document.documentElement.classList]);
      ok(cls.includes('static-bg'), `static-bg present (got: ${cls.join(' ')})`);
      ok(!cls.includes('field-on'), 'field-on absent');
      ok(await page.evaluate(() => {
        const rows = document.querySelectorAll('li.reveal');
        return [...rows].every((r) => getComputedStyle(r).opacity === '1');
      }), 'all rows immediately visible under reduced motion');
      ok(errors.length === 0, `no console/page errors${errors.length ? ` — got: ${errors.join(' | ').slice(0, 300)}` : ''}`);
    } catch (e) {
      ok(false, `pass aborted: ${e.message}`);
    } finally {
      if (ctx) await ctx.close().catch(() => {});
    }
  }

  console.log('— pass 3: JavaScript disabled (server-rendered contract) —');
  {
    let ctx;
    try {
      // javaScriptEnabled: false disables page <script>s (the `js` class never
      // gets added, reveal rows must be visible from CSS alone) — but
      // Playwright's own page.evaluate()/locator() still work, since they run
      // via CDP Runtime.evaluate rather than in-page script execution.
      ctx = await browser.newContext({ viewport: { width: 1280, height: 800 }, javaScriptEnabled: false });
      const page = await ctx.newPage();
      await page.goto(home, { waitUntil: 'load' });
      const cls = await page.evaluate(() => [...document.documentElement.classList]);
      ok(!cls.includes('js'), `no js class with JavaScript disabled (got: ${cls.join(' ')})`);
      await checkRows(page);
      ok(await page.evaluate(() => {
        const rows = document.querySelectorAll('li.reveal');
        return [...rows].every((r) => getComputedStyle(r).opacity === '1');
      }), 'all rows immediately visible with JavaScript disabled');
      ok(await page.title() === manifest.course, 'title matches manifest.course');
    } catch (e) {
      ok(false, `pass aborted: ${e.message}`);
    } finally {
      if (ctx) await ctx.close().catch(() => {});
    }
  }

  console.log('— pass 4: scene pixels at scroll offsets (?qa) —');
  {
    let ctx;
    try {
      const ctx2 = await browser.newContext({ viewport: { width: 1280, height: 800 }, reducedMotion: 'no-preference' });
      ctx = ctx2;
      const page = await ctx2.newPage();
      const errors = [];
      page.on('console', (m) => { if (m.type() === 'error') errors.push(m.text()); });
      page.on('pageerror', (e) => errors.push(String(e)));
      await page.goto(home + '?qa', { waitUntil: 'load' });
      const gated = await page.waitForFunction(() => {
        const c = document.documentElement.classList;
        return (c.contains('field-on') || c.contains('static-bg')) ? (c.contains('field-on') ? 'field-on' : 'static-bg') : false;
      }, null, { timeout: 20000 }).then((h) => h.jsonValue()).catch(() => null);
      if (gated !== 'field-on') {
        console.log(`  - skipped (no WebGL scene: ${gated})`);
      } else {
        // Downsample the field canvas to 64×40 and return luminance samples.
        // Works because ?qa builds the renderer with preserveDrawingBuffer.
        const sample = () => page.evaluate(() => new Promise((resolveP) => {
          requestAnimationFrame(() => requestAnimationFrame(() => {
            try {
              const src = document.getElementById('field');
              const w = 64, h = 40;
              const c = document.createElement('canvas');
              c.width = w; c.height = h;
              const g = c.getContext('2d', { willReadFrequently: true });
              g.drawImage(src, 0, 0, w, h);
              const d = g.getImageData(0, 0, w, h).data;
              const px = []; let lit = 0;
              for (let i = 0; i < d.length; i += 4) {
                const l = 0.2126 * d[i] + 0.7152 * d[i + 1] + 0.0722 * d[i + 2];
                px.push(l);
                if (l > 8) lit++;
              }
              resolveP({ lit, total: w * h, px });
            } catch (e) {
              resolveP({ error: String(e) });
            }
          }));
        }));
        // Scroll→camera wiring is asserted on the camera transform itself via
        // the ?qa-gated hook (window.__qaCam, a live camera.position ref set
        // in sim.js) — deterministic, unlike pixel diffs, which the ambient
        // particle shimmer drowns out.
        const readCam = () => page.evaluate(() =>
          window.__qaCam ? { x: window.__qaCam.x, y: window.__qaCam.y, z: window.__qaCam.z } : null);
        await page.waitForTimeout(1200); // first frames + reveal settle
        const s0 = await sample();
        const cam0 = await readCam();
        await page.evaluate(() => window.scrollTo(0, innerHeight * 2));
        await page.waitForTimeout(1600); // camera damping settle
        const s1 = await sample();
        const cam1 = await readCam();
        const sampleErr = Object.entries({ s0, s1 }).find(([, s]) => s.error);
        if (sampleErr) {
          ok(false, `canvas sampling failed: ${sampleErr[0]} — ${sampleErr[1].error}`);
        } else {
          ok(s0.lit / s0.total > 0.005, `hero frame lit (${s0.lit}/${s0.total} px)`);
          ok(s1.lit / s1.total > 0.005, `scrolled frame lit (${s1.lit}/${s1.total} px)`);
        }
        ok(cam0 && cam1, 'qa camera hook present');
        if (cam0 && cam1) {
          const camMove = Math.hypot(cam1.x - cam0.x, cam1.y - cam0.y, cam1.z - cam0.z);
          ok(camMove > 5, `scroll moves the camera (Δ ${camMove.toFixed(1)} world units)`);
        }
        ok(errors.length === 0, `no console/page errors${errors.length ? ` — got: ${errors.join(' | ').slice(0, 300)}` : ''}`);
      }
    } catch (e) {
      ok(false, `pass aborted: ${e.message}`);
    } finally {
      if (ctx) await ctx.close().catch(() => {});
    }
  }
} finally {
  await browser.close().catch(() => {});
  server.close();
}
if (fails.length) { console.error(`\n❌ landing check: ${fails.length} failure(s).`); process.exit(1); }
console.log('\n✅ landing check passed.');
