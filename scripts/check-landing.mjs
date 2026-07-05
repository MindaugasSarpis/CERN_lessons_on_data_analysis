#!/usr/bin/env node
/**
 * check-landing.mjs — smoke-test a BUILT landing directory (index.html +
 * assets/). Asserts: title, every manifest deck link, JS boot (js class),
 * scene-or-fallback gating (field-on | static-bg), reveal-on-scroll, the
 * reduced-motion fallback, and zero console/page errors.
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
      for (const d of manifest.decks) {
        const href = `${PREFIX}/${d.slug}/`;
        ok(await page.locator(`a.row[href="${href}"]`).count() === 1, `deck link ${href}`);
      }
      ok(await page.locator('.hero .kicker').innerText() === manifest.presenter, 'presenter in hero');
      ok((await page.locator('footer.foot').innerText()).includes('seminar'), 'seminar footer note');
      const gated = await page.waitForFunction(() => {
        const c = document.documentElement.classList;
        return (c.contains('field-on') || c.contains('static-bg')) ? (c.contains('field-on') ? 'field-on' : 'static-bg') : false;
      }, null, { timeout: 20000 }).then((h) => h.jsonValue()).catch(() => null);
      ok(gated === 'field-on' || gated === 'static-bg', `boot gate resolved (${gated})`);
      if (gated === 'field-on') {
        ok(await page.evaluate(() => {
          const c = document.getElementById('field');
          return c && c.width >= innerWidth && c.height >= innerHeight;
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
} finally {
  await browser.close().catch(() => {});
  server.close();
}
if (fails.length) { console.error(`\n❌ landing check: ${fails.length} failure(s).`); process.exit(1); }
console.log('\n✅ landing check passed.');
