#!/usr/bin/env node
/**
 * check-runners.mjs — run every Python runner block ({monaco-run}) of the
 * built decks, the way the lecturer does: in slide order, on one page, so a
 * block that relies on an earlier one gets the same Pyodide session as live.
 *
 * `pnpm qa` measures runner slides BEFORE anything runs. This is the other
 * half: press ▶ on each block, wait for the output to settle, and check
 *   ✗ the slide still fits the frame with the output box open (it grows to
 *     its 11rem cap, then scrolls inside)
 *   ✗ the code ran without a Python error — unless the slide demonstrates
 *     that error and names it (title "Fix It — NameError", or a comment
 *     `x = "3" + 4   # TypeError`)
 *   ⚠ the block printed nothing and drew no figure (a reader sees no result)
 *   ⚠ the output is taller than its box, so part of it scrolls out of view
 *
 * Not part of `pnpm qa` / CI: Pyodide (~10 MB) and its packages come from the
 * jsDelivr CDN, and the first block of a deck waits for that download. Run it
 * after adding or editing runner blocks.
 *
 * Usage:
 *   node scripts/check-runners.mjs                  # every deck with runners
 *   node scripts/check-runners.mjs --only 03-how-computers-work,06-python-foundations
 *   node scripts/check-runners.mjs --no-build       # reuse .qa-dist/<slug>
 *   node scripts/check-runners.mjs --shots .qa-shots/runners
 *
 * Exit 0 = every block ran and fits; 1 = an error or an overflow.
 */
import { createServer } from 'node:http';
import { readFile, stat, mkdir } from 'node:fs/promises';
import { spawnSync } from 'node:child_process';
import { join, extname, normalize, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium } from 'playwright-chromium';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const CONTENT = join(ROOT, 'lectures', 'content');
const QA_DIST = join(ROOT, '.qa-dist');

const argv = process.argv.slice(2);
const opt = (name, def) => { const i = argv.indexOf(name); return i > -1 ? argv[i + 1] : def; };
const ONLY = argv.includes('--only') ? opt('--only').split(',') : null;
const NO_BUILD = argv.includes('--no-build');
const SHOTS = opt('--shots', null);
const TOL = Number(opt('--tolerance', 6));

// Decks whose sources contain a runner block.
const manifest = JSON.parse(await readFile(join(CONTENT, 'decks.json'), 'utf8'));
const decks = [];
for (const d of manifest.decks) {
  if (ONLY && !ONLY.includes(d.slug)) continue;
  const srcs = await Promise.all(d.srcs.map((s) => readFile(join(CONTENT, 'slides', s), 'utf8')));
  if (srcs.some((s) => /\{monaco-run\}/.test(s))) decks.push(d);
}
if (!decks.length) { console.log('No deck with runner blocks selected.'); process.exit(0); }

if (!NO_BUILD) {
  const r = spawnSync('node', ['scripts/build-all.mjs', '--flat-base', '--out', '.qa-dist',
    '--only', decks.map((d) => d.slug).join(',')], { cwd: ROOT, stdio: 'inherit' });
  if (r.status !== 0) process.exit(r.status || 1);
}

const MIME = {
  '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript',
  '.css': 'text/css', '.json': 'application/json', '.svg': 'image/svg+xml',
  '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp',
  '.woff': 'font/woff', '.woff2': 'font/woff2', '.ttf': 'font/ttf', '.wasm': 'application/wasm',
};

function serve(distDir) {
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
  return new Promise((r) => server.listen(0, '127.0.0.1', () => r(server)));
}

if (SHOTS) await mkdir(SHOTS, { recursive: true });
const browser = await chromium.launch();
const failures = [];
const warnings = [];

for (const deck of decks) {
  if (!(await stat(join(QA_DIST, deck.slug, 'index.html')).catch(() => null))) {
    failures.push(`${deck.slug}: no build in .qa-dist/${deck.slug} (run without --no-build)`);
    continue;
  }
  const server = await serve(join(QA_DIST, deck.slug));
  const base = `http://127.0.0.1:${server.address().port}`;
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  // videos add nothing here and their downloads slow the CDN fetches down
  await page.route('**/*', (route) =>
    route.request().resourceType() === 'media' ? route.abort() : route.continue());
  await page.goto(`${base}/`, { waitUntil: 'domcontentloaded' });
  await page.waitForSelector('.slidev-layout', { timeout: 30000 });
  await page.addStyleTag({ content: '*, *::before, *::after { transition: none !important; animation: none !important; }' });

  // slide count from the "N / M" nav counter (it renders a moment after the slide)
  let total = null;
  for (let t = 0; t < 40 && !total; t++) {
    await page.waitForTimeout(250);
    total = await page.evaluate(() => {
      for (const el of document.querySelectorAll('*')) {
        if (el.children.length) continue;
        const m = (el.textContent || '').trim().match(/^(\d+)\s*\/\s*(\d+)$/);
        if (m) return Number(m[2]);
      }
      const bm = document.body.innerText.match(/\b\d+\s*\/\s*(\d+)\s*$/);
      return bm ? Number(bm[1]) : null;
    });
  }
  if (!total) {
    failures.push(`${deck.slug}: could not read the slide count`);
    await page.close();
    server.close();
    continue;
  }
  console.log(`\n=== ${deck.slug} (${total} slides)`);

  let blocks = 0;
  for (let n = 1; n <= total; n++) {
    await page.evaluate((n) => { location.hash = '#/' + n; }, n);
    const sel = `.slidev-page[data-slidev-no="${n}"]`;
    await page.waitForSelector(`${sel} .slidev-layout`, { timeout: 8000 }).catch(() => {});
    const count = await page.locator(`${sel} .slidev-monaco-container`).count();
    if (!count) continue;

    for (let b = 0; b < count; b++) {
      blocks++;
      const box = page.locator(`${sel} .slidev-monaco-container`).nth(b);
      await box.locator('.monaco-editor .view-line').first().waitFor({ timeout: 15000 }).catch(() => {});
      const run = box.locator('button[title="Run code"]');
      await run.waitFor({ timeout: 15000 });
      await run.click();
      // First block of a deck waits for Pyodide + packages. The output box
      // appears before the code has finished (the addon does not await the
      // run), so wait until the output has not changed for 1.5 s — prints
      // stream in, a figure or a late error is appended after them (60 s max).
      await box.locator('.slidev-runner-output').waitFor({ timeout: 180000 });
      let last = '';
      let stableFor = 0;
      for (let t = 0; t < 60000 && stableFor < 1500; t += 250) {
        await page.waitForTimeout(250);
        const now = await box.evaluate((c) => {
          const o = c.querySelector('.slidev-runner-output');
          return o.innerText + '|' + o.querySelectorAll('canvas').length;
        });
        stableFor = now === last ? stableFor + 250 : 0;
        last = now;
      }
      const r = await box.evaluate((c) => {
        const o = c.querySelector('.slidev-runner-output');
        const slide = c.closest('.slidev-layout');
        const errors = [...o.querySelectorAll('.text-red, .text-red-500')].map((e) => e.innerText).filter((s) => s.trim());
        const text = [...o.querySelectorAll('.output-line')].map((e) => e.innerText).join('\n').trim();
        const figures = o.querySelectorAll('.slidev-python-figures canvas').length;
        const code = [...c.querySelectorAll('.view-line')].map((l) => l.innerText).join('\n');
        const firstLine = code.trim().split('\n')[0].slice(0, 50);
        // everything the slide says, minus what the run printed
        // (text nodes joined with spaces: textContent runs "…NameError" and
        // the next paragraph together, and \b no longer finds the word)
        const parts = [];
        const walk = document.createTreeWalker(slide, NodeFilter.SHOW_TEXT);
        while (walk.nextNode()) {
          if (!walk.currentNode.parentElement.closest('.slidev-runner-output')) parts.push(walk.currentNode.nodeValue);
        }
        const said = parts.join(' ') + '\n' + code;
        return {
          errors, text, figures, firstLine, said,
          oy: slide.scrollHeight - slide.clientHeight,
          scrolls: o.scrollHeight - o.clientHeight > 2,
        };
      });
      if (SHOTS) await page.screenshot({ path: join(SHOTS, `${deck.slug}-slide-${String(n).padStart(3, '0')}-${b + 1}.png`) });

      // A block that demonstrates an error says so: the slide names the error
      // (title "Fix It — NameError", or a comment `x = "3" + 4   # TypeError`).
      // Then that error is the expected result.
      const raised = (r.errors[r.errors.length - 1] || '').match(/^(?:[\w.]+\.)?(\w+(?:Error|Exception|Warning|Interrupt|Exit))\b/)?.[1];
      const expectError = Boolean(raised && new RegExp(`\\b${raised}\\b`).test(r.said));
      const where = `${deck.slug} slide ${n}${count > 1 ? ` block ${b + 1}` : ''} ("${r.firstLine}")`;
      const lines = r.text ? r.text.split('\n').length : 0;
      let status = `  ✓ slide ${n}${count > 1 ? `.${b + 1}` : ''}: ${lines} line(s)${r.figures ? `, ${r.figures} figure(s)` : ''}`;
      if (r.errors.length && !expectError) {
        failures.push(`${where}: Python error — ${r.errors[r.errors.length - 1]}`);
        status = `  ✗ slide ${n}: ${r.errors[r.errors.length - 1]}`;
      }
      if (expectError) status += ` (raises ${raised}, as the slide says)`;
      if (r.oy > TOL) {
        failures.push(`${where}: slide overflows by ${r.oy}px with the output open`);
        status = `  ✗ slide ${n}: overflows by ${r.oy}px after running`;
      }
      if (!lines && !r.figures && !r.errors.length) warnings.push(`${where}: printed nothing`);
      if (r.scrolls) warnings.push(`${where}: output (${lines} lines) is taller than its box and scrolls`);
      console.log(status);
    }
  }
  if (!blocks) console.log('  (no runner block rendered)');
  await page.close();
  server.close();
}

await browser.close();
if (warnings.length) {
  console.log(`\n⚠️  ${warnings.length} to look at:`);
  for (const w of warnings) console.log(`   ${w}`);
}
if (failures.length) {
  console.log(`\n❌ ${failures.length} runner block(s) fail:`);
  for (const f of failures) console.log(`   ${f}`);
  process.exit(1);
}
console.log(`\n✅ Every runner block ran and its slide fits with the output open.`);
