# WebGL Landing Page (Active Theory style) — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the card-grid course landing with an activetheory.net-style page: fixed full-screen GPU particle field (Three.js, ping-pong FBO sim, cursor wake) behind a huge-type hero and a scrolling typographic lecture list — still generated from `decks.json`, fully usable without JS.

**Architecture:** New `landing/` source dir (JS + GLSL + CSS + fonts) built by Vite to fixed-name assets; `scripts/gen-landing.mjs` keeps rendering ALL content server-side from the manifest and links the prebuilt assets (progressive enhancement). A new `scripts/build-landing.mjs` (vite build → copy assets → genLanding) is called by `build-all.mjs` and by `qa-all.mjs`, which gains a landing smoke test via new `scripts/check-landing.mjs`.

**Tech Stack:** Three.js (WebGL2, half/full-float FBOs), Vite, @fontsource/space-grotesk, playwright-chromium (existing) for QA.

**Spec:** `docs/superpowers/specs/2026-07-05-webgl-landing-design.md` — read it first.

## Global Constraints

- No external network requests from the page (GitHub Pages / CSP safe): fonts self-hosted, all assets relative (`./assets/...`), works under any `--base` prefix.
- Page fully readable/navigable with JS disabled; canvas and animations are additive.
- Palette: base `#050507`, text `#f2f5f9`, dimmed `#8b97a6`, single accent `#7dd3fc`. No other hues.
- Content parity: every deck of `decks.json` in block order linked to `<base>/<slug>/`, `optional` tags, Block E header tag "drop if short on time", `upcoming[]` section, presenter, course title, seminar footer note.
- `gen404()` redirect script behavior unchanged (palette-only retouch).
- `prefers-reduced-motion` or no usable WebGL2 → no canvas boot, static gradient, instant reveals.
- Repo has no unit-test framework; verification = exact commands below + `scripts/check-landing.mjs` (the landing's test). Run them and check output as written.
- All commands run from the repo root.

## File Map

- Create: `landing/vite.config.mjs`, `landing/src/main.js`, `landing/src/sim.js`, `landing/src/shaders/noise.glsl.js`, `landing/src/shaders/passes.glsl.js`, `landing/src/style.css`
- Create: `scripts/build-landing.mjs`, `scripts/check-landing.mjs`
- Modify: `scripts/gen-landing.mjs` (HTML/CSS rewrite; keep `genLanding` signature + `gen404` script), `scripts/build-all.mjs` (call buildLanding), `scripts/qa-all.mjs` (landing step), `package.json`, `.gitignore`, `CLAUDE.md`
- Fonts come from the `@fontsource/space-grotesk` package (no vendored files; the spec's `landing/fonts/` is realized via the package + Vite asset copying).

---

### Task 1: Dependencies + landing source skeleton that builds

**Files:**
- Modify: `package.json`, `.gitignore`
- Create: `landing/vite.config.mjs`, `landing/src/main.js` (gating stub, no scene yet), `landing/src/style.css` (minimal palette only)

**Interfaces (Produces):**
- `pnpm build:landing:assets` → emits `landing/dist-assets/assets/landing.js`, `assets/landing.css`, `assets/*.woff2` (fixed names, no hashes).
- `landing/src/main.js` contract used by Tasks 3–5: adds `js` class to `<html>` immediately; then adds exactly one of `field-on` (scene booted) or `static-bg` (fallback).

- [ ] **Step 1: Install dependencies**

```bash
pnpm add -D three vite @fontsource/space-grotesk
```

Expected: lockfile updated; `node_modules/three`, `node_modules/vite`, `node_modules/@fontsource/space-grotesk/400.css` exist.

- [ ] **Step 2: Ignore the Vite scratch output**

Append to `.gitignore`:

```
landing/dist-assets/
```

- [ ] **Step 3: Create `landing/vite.config.mjs`**

```js
import { defineConfig } from 'vite';
import { fileURLToPath } from 'node:url';
import { dirname, resolve } from 'node:path';

const here = dirname(fileURLToPath(import.meta.url));

// Builds the landing enhancement bundle to FIXED filenames (no hashes) so
// gen-landing.mjs can reference them statically. base './' keeps every URL
// relative → works under any GitHub Pages --base prefix.
export default defineConfig({
  root: here,
  base: './',
  build: {
    outDir: resolve(here, 'dist-assets'),
    emptyOutDir: true,
    target: 'es2019',
    rollupOptions: {
      input: { landing: resolve(here, 'src/main.js') },
      output: {
        entryFileNames: 'assets/[name].js',
        chunkFileNames: 'assets/[name].js',
        assetFileNames: 'assets/[name][extname]',
      },
    },
  },
});
```

- [ ] **Step 4: Create `landing/src/style.css` (minimal — full sheet lands in Task 4)**

```css
:root { color-scheme: dark; }
html { background: #050507; color: #f2f5f9; }
body { margin: 0; font-family: 'Space Grotesk', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif; }
```

- [ ] **Step 5: Create `landing/src/main.js` (gating stub — real scene in Task 5)**

```js
import '@fontsource/space-grotesk/400.css';
import '@fontsource/space-grotesk/500.css';
import '@fontsource/space-grotesk/700.css';
import './style.css';

const html = document.documentElement;
html.classList.add('js');

const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

function webgl2Ok() {
  try {
    const gl = document.createElement('canvas').getContext('webgl2');
    return !!gl && (gl.getExtension('EXT_color_buffer_float') !== null
      || gl.getExtension('EXT_color_buffer_half_float') !== null);
  } catch { return false; }
}

if (reduced || !webgl2Ok()) {
  html.classList.add('static-bg');
} else {
  // Task 5 replaces this stub with the particle scene boot.
  html.classList.add('field-on');
}
```

- [ ] **Step 6: Add build script to `package.json`**

In `"scripts"`, add (build:landing itself arrives in Task 2):

```json
"build:landing:assets": "vite build --config landing/vite.config.mjs",
```

- [ ] **Step 7: Build and verify fixed names**

```bash
pnpm build:landing:assets && ls landing/dist-assets/assets/
```

Expected: `landing.js`, `landing.css`, and several `space-grotesk-*.woff2` files — **no hash suffixes** in `landing.js` / `landing.css`.

- [ ] **Step 8: Commit**

```bash
git add package.json pnpm-lock.yaml .gitignore landing/
git commit -m "feat(landing): vite + three skeleton for WebGL landing bundle"
```

---

### Task 2: gen-landing HTML rewrite + build-landing + build-all integration

**Files:**
- Modify: `scripts/gen-landing.mjs` (full rewrite of `genLanding`'s HTML; keep export signature and `gen404` script logic)
- Create: `scripts/build-landing.mjs`
- Modify: `scripts/build-all.mjs:50` (swap `genLanding` call for `buildLanding`), `package.json`

**Interfaces:**
- Consumes: Task 1's fixed asset names (`./assets/landing.css`, `./assets/landing.js`).
- Produces: `buildLanding(outDir, prefix)` from `scripts/build-landing.mjs` — builds Vite assets, copies them to `<outDir>/assets/`, then calls `genLanding(manifest, outDir, prefix)`. Standalone: `node scripts/build-landing.mjs [--out dist] [--base <prefix>]`.
- Produces HTML hooks that Tasks 3–5 rely on (exact selectors): `<canvas id="field">`, `main.wrap`, `header.hero` with `h1.title > span.line-wrap > span.line`, `p.kicker`, `p.sub`, `.scroll-hint`, `section.block` + `h2.block-head`, `ol.rows`, `a.row` (deck links, with `span.num`, `span.rt`, `span.arrow`, optional `span.tag`), `span.row.soon` (upcoming), `.reveal` class + inline `--i` custom property on every row `<li>`, `footer.foot`.

- [ ] **Step 1: Rewrite `genLanding` HTML in `scripts/gen-landing.mjs`**

Replace the whole `genLanding` function body (keep `esc`, keep `gen404` for now — Step 2 retouches its colors). New body:

```js
export async function genLanding(manifest, outDir, prefix = '') {
  const base = prefix.replace(/\/$/, '');
  const byBlock = new Map(Object.keys(manifest.blocks).map((k) => [k, []]));
  for (const d of manifest.decks) (byBlock.get(d.block) || byBlock.set(d.block, []).get(d.block)).push(d);

  // Split the course title into ~equal lines for the staggered hero reveal.
  const words = manifest.course.split(' ');
  const per = Math.ceil(words.length / 3);
  const lines = [];
  for (let i = 0; i < words.length; i += per) lines.push(words.slice(i, i + per).join(' '));

  const titleHtml = lines.map((l, i) =>
    `<span class="line-wrap"><span class="line" style="--i:${i}">${esc(l)}</span></span>`).join('\n        ');

  let rowIdx = 0;
  const row = (d) => `
          <li class="reveal" style="--i:${rowIdx++ % 8}">
            <a class="row${d.optional ? ' opt' : ''}" href="${base}/${d.slug}/">
              <span class="num">${esc(d.slug.split('-')[0])}</span>
              <span class="rt">${esc(d.title)}</span>
              ${d.optional ? '<span class="tag">optional</span>' : ''}
              <span class="arrow" aria-hidden="true">&#8594;</span>
            </a>
          </li>`;

  const blockSections = [...byBlock.entries()]
    .filter(([, decks]) => decks.length)
    .map(([key, decks]) => {
      rowIdx = 0;
      return `
      <section class="block">
        <h2 class="block-head reveal" style="--i:0">
          <span class="block-key">Block ${esc(key)}</span>
          <span class="block-name">${esc(manifest.blocks[key])}</span>
          ${key === 'E' ? '<span class="tag">drop if short on time</span>' : ''}
        </h2>
        <ol class="rows">${decks.map(row).join('')}
        </ol>
      </section>`;
    }).join('');

  const upcoming = (manifest.upcoming && manifest.upcoming.length) ? (() => {
    rowIdx = 0;
    return `
      <section class="block">
        <h2 class="block-head reveal" style="--i:0">
          <span class="block-key">Coming soon</span>
          <span class="tag">in preparation</span>
        </h2>
        <ol class="rows">${manifest.upcoming.map((u) => `
          <li class="reveal" style="--i:${rowIdx++ % 8}">
            <span class="row soon">
              <span class="num">${String(u.n).padStart(2, '0')}</span>
              <span class="rt">${esc(u.title)}</span>
            </span>
          </li>`).join('')}
        </ol>
      </section>`;
  })() : '';

  const html = `<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(manifest.course)}</title>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Ccircle cx='8' cy='8' r='5' fill='%237dd3fc'/%3E%3C/svg%3E">
<style>
  /* Critical: correct first paint before landing.css arrives. */
  :root { color-scheme: dark; }
  html { background: #050507; color: #f2f5f9; }
  body { margin: 0; font-family: 'Space Grotesk', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif; }
</style>
<link rel="stylesheet" href="./assets/landing.css">
</head><body>
  <canvas id="field" aria-hidden="true"></canvas>
  <div class="grain" aria-hidden="true"></div>
  <main class="wrap">
    <header class="hero">
      <p class="kicker">${esc(manifest.presenter)}</p>
      <h1 class="title">
        ${titleHtml}
      </h1>
      <p class="sub">A practice-first course: tool-agnostic thinking, reproducible analysis, automation, and efficient work with data and files. Each lecture opens on its own so it loads fast, even on a phone.</p>
      <div class="scroll-hint" aria-hidden="true"><span class="shline"></span><span class="shlabel">Scroll</span></div>
    </header>
    ${blockSections}
    ${upcoming}
    <footer class="foot">
      <p>Each lecture has a paired hands-on seminar in the workbook. Blocks D&ndash;E are the optional tail if the term runs short.</p>
    </footer>
  </main>
  <script type="module" src="./assets/landing.js"></script>
</body></html>`;

  await mkdir(outDir, { recursive: true });
  await writeFile(join(outDir, 'index.html'), html, 'utf8');
  await writeFile(join(outDir, '404.html'), gen404(manifest, base), 'utf8');
  return join(outDir, 'index.html');
}
```

- [ ] **Step 2: Retouch `gen404` palette only**

In `gen404`'s `<style>`, change `background: #060911; color: #e6edf6;` to `background: #050507; color: #f2f5f9;`. Do not touch the `<script>` block.

- [ ] **Step 3: Create `scripts/build-landing.mjs`**

```js
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
  await cp(join(ROOT, 'landing', 'dist-assets', 'assets'), join(outDir, 'assets'), { recursive: true });
  return genLanding(JSON.parse(await readFile(join(ROOT, 'lectures', 'content', 'decks.json'), 'utf8')), outDir, prefix);
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const argv = process.argv.slice(2);
  const opt = (n, d) => { const i = argv.indexOf(n); return i > -1 ? argv[i + 1] : d; };
  const p = await buildLanding(resolve(ROOT, opt('--out', 'dist')), opt('--base', ''));
  console.log(`Landing → ${p}`);
}
```

- [ ] **Step 4: Wire into `scripts/build-all.mjs`**

Replace the import of `genLanding` with `import { buildLanding } from './build-landing.mjs';` and replace line 50:

```js
if (!FLAT) await buildLanding(OUT, PREFIX);
```

Update the comment above it: the landing (assets + index.html) is still written FIRST so a static server pointed at OUT stays valid during rebuilds.

- [ ] **Step 5: Add `build:landing` script to `package.json`**

```json
"build:landing": "node scripts/build-landing.mjs",
```

- [ ] **Step 6: Verify standalone landing build**

```bash
node scripts/build-landing.mjs --out /tmp/claude-1001/-home-mindaugas-wsl-CERN-lessons-on-data-analysis/56713095-ae9e-4ea8-b610-ee3e03e4d384/scratchpad/land-t2
grep -c 'class="row' /tmp/claude-1001/-home-mindaugas-wsl-CERN-lessons-on-data-analysis/56713095-ae9e-4ea8-b610-ee3e03e4d384/scratchpad/land-t2/index.html
grep -o 'href="/16-machine-learning/"' /tmp/claude-1001/-home-mindaugas-wsl-CERN-lessons-on-data-analysis/56713095-ae9e-4ea8-b610-ee3e03e4d384/scratchpad/land-t2/index.html
ls /tmp/claude-1001/-home-mindaugas-wsl-CERN-lessons-on-data-analysis/56713095-ae9e-4ea8-b610-ee3e03e4d384/scratchpad/land-t2/assets/ | head
```

Expected: row count = 16 (decks; `upcoming` is empty today); the href match prints; assets dir lists `landing.js`, `landing.css`, woff2 files. Also verify prefix handling:

```bash
node scripts/build-landing.mjs --out /tmp/claude-1001/-home-mindaugas-wsl-CERN-lessons-on-data-analysis/56713095-ae9e-4ea8-b610-ee3e03e4d384/scratchpad/land-t2b --base /CERN_lessons_on_data_analysis
grep -c 'href="/CERN_lessons_on_data_analysis/01-orientation/"' /tmp/claude-1001/-home-mindaugas-wsl-CERN-lessons-on-data-analysis/56713095-ae9e-4ea8-b610-ee3e03e4d384/scratchpad/land-t2b/index.html
```

Expected: 1.

- [ ] **Step 7: Commit**

```bash
git add scripts/gen-landing.mjs scripts/build-landing.mjs scripts/build-all.mjs package.json
git commit -m "feat(landing): manifest-driven AT-style HTML + build-landing pipeline step"
```

---

### Task 3: check-landing smoke test + qa-all wiring

**Files:**
- Create: `scripts/check-landing.mjs`
- Modify: `scripts/qa-all.mjs` (landing step after deck loop)

**Interfaces:**
- Consumes: Task 2's built landing dir (`index.html` + `assets/`), Task 1's `js`/`field-on`/`static-bg` classes, Task 2's selectors (`a.row[href]`, `li.reveal`).
- Produces: `node scripts/check-landing.mjs <distDir> [--base <prefix>]` — exit 0 pass / 1 fail / 2 usage. Tasks 4–6 re-run it after each change.
- Note on reveal semantics (Task 4 implements them; asserted here): rows are visible by default; with `.js` and no reduced-motion, `.reveal` is hidden until JS adds `.in`; with reduced motion, CSS forces `.reveal` visible.

- [ ] **Step 1: Create `scripts/check-landing.mjs`**

```js
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

console.log('— pass 1: default (scene expected where WebGL2 available) —');
{
  const { ctx, page, errors } = await loadPage({ reducedMotion: 'no-preference' });
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
      return c && c.width > 0 && c.height > 0;
    }), 'canvas has non-zero backing size');
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
  await ctx.close();
}

console.log('— pass 2: prefers-reduced-motion (static fallback expected) —');
{
  const { ctx, page, errors } = await loadPage({ reducedMotion: 'reduce' });
  const cls = await page.evaluate(() => [...document.documentElement.classList]);
  ok(cls.includes('static-bg'), `static-bg present (got: ${cls.join(' ')})`);
  ok(!cls.includes('field-on'), 'field-on absent');
  ok(await page.evaluate(() => {
    const rows = document.querySelectorAll('li.reveal');
    return [...rows].every((r) => getComputedStyle(r).opacity === '1');
  }), 'all rows immediately visible under reduced motion');
  ok(errors.length === 0, `no console/page errors${errors.length ? ` — got: ${errors.join(' | ').slice(0, 300)}` : ''}`);
  await ctx.close();
}

await browser.close();
server.close();
if (fails.length) { console.error(`\n❌ landing check: ${fails.length} failure(s).`); process.exit(1); }
console.log('\n✅ landing check passed.');
```

- [ ] **Step 2: Run it against the Task 2 build (expect PASS with the stub)**

```bash
node scripts/build-landing.mjs --out /tmp/claude-1001/-home-mindaugas-wsl-CERN-lessons-on-data-analysis/56713095-ae9e-4ea8-b610-ee3e03e4d384/scratchpad/land-t3
node scripts/check-landing.mjs /tmp/claude-1001/-home-mindaugas-wsl-CERN-lessons-on-data-analysis/56713095-ae9e-4ea8-b610-ee3e03e4d384/scratchpad/land-t3
```

Expected: pass 1 — title/links/footer ✓, boot gate resolves (either value; the stub sets `field-on` but leaves the canvas backing size at default 300×150, so the canvas-size assertion may print ✗). Pass 2 — static-bg ✓. **If the only failure is `canvas has non-zero backing size`, that is the expected RED for Task 5** (the stub never sizes the canvas); note it and continue. `last row revealed` must PASS because Task 4 hasn't hidden rows yet (`opacity` computes to `1` without reveal CSS) — it guards regressions from Task 4 onward.

- [ ] **Step 3: Wire into `scripts/qa-all.mjs`**

After the deck loop (after line 45, before the summary print), add:

```js
// 3) Landing smoke test (decks build --flat-base with no landing, so build one).
const LAND = join(QA_DIST, '__landing__');
process.stdout.write('\n▶ landing smoke test …\n');
const lb = spawnSync('node', [join(ROOT, 'scripts', 'build-landing.mjs'), '--out', LAND], { cwd: ROOT, stdio: 'inherit' });
const lc = lb.status === 0
  ? spawnSync('node', [join(ROOT, 'scripts', 'check-landing.mjs'), LAND], { cwd: ROOT, stdio: 'inherit' })
  : lb;
if (lc.status !== 0) { bad++; summary.push('✗ landing'); } else summary.push('✓ landing');
```

And generalize the failure line so the count isn't deck-specific:

```js
if (bad) { console.error(`\n❌ ${bad} QA target(s) failed.`); process.exit(1); }
console.log(`\n✅ All ${decks.length} deck(s) + landing pass QA.`);
```

- [ ] **Step 4: Commit**

```bash
git add scripts/check-landing.mjs scripts/qa-all.mjs
git commit -m "test(landing): smoke check (links, boot gate, reveals, fallback) wired into qa"
```

---

### Task 4: Full stylesheet (typography, rows, hero, grain) + reveal observer

**Files:**
- Modify: `landing/src/style.css` (full sheet replaces the Task 1 stub), `landing/src/main.js` (add reveal IntersectionObserver)

**Interfaces:**
- Consumes: Task 2's HTML hooks (`.hero`, `.title .line-wrap/.line`, `.kicker`, `.sub`, `.scroll-hint`, `.block-head`, `ol.rows`, `a.row`, `.row.soon`, `li.reveal[--i]`, `.grain`, `#field`, `.foot`).
- Produces: reveal contract asserted by Task 3 — no JS: rows visible; `.js` + motion OK: `li.reveal` hidden until `.in`; reduced motion: forced visible. Also `.static-bg` gradient backdrop used by Task 5's fallback path, and `#field` fade-in driven by the `field-on` class.

- [ ] **Step 1: Replace `landing/src/style.css` with the full sheet**

```css
:root {
  color-scheme: dark;
  --bg: #050507;
  --fg: #f2f5f9;
  --dim: #8b97a6;
  --accent: #7dd3fc;
  --hair: rgba(139, 151, 166, 0.18);
  --ease: cubic-bezier(0.16, 1, 0.3, 1);
}
* { box-sizing: border-box; }
html { background: var(--bg); color: var(--fg); scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: 'Space Grotesk', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
  line-height: 1.5;
  /* Ambient gradient is ALWAYS present: it is the no-JS/static backdrop, and
     the additive particle canvas draws over it. */
  background:
    radial-gradient(1100px 700px at 78% -8%, rgba(125, 211, 252, 0.07), transparent 62%),
    radial-gradient(900px 600px at -12% 108%, rgba(125, 211, 252, 0.05), transparent 60%),
    var(--bg);
}
.static-bg body { background-attachment: fixed; }

/* Layers: canvas 0 → content 1 → grain 10. */
#field {
  position: fixed; inset: 0; width: 100%; height: 100%;
  z-index: 0; pointer-events: none;
  opacity: 0; transition: opacity 1.2s ease;
}
.field-on #field { opacity: 1; }
.static-bg #field { display: none; }
.grain {
  position: fixed; inset: 0; z-index: 10; pointer-events: none; opacity: 0.05;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='240' height='240'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}

.wrap {
  position: relative; z-index: 1;
  max-width: 1200px; margin: 0 auto;
  padding: 0 clamp(1.25rem, 5vw, 4rem) 6rem;
}

/* ---------- hero ---------- */
.hero {
  min-height: 100svh;
  display: flex; flex-direction: column; justify-content: center;
  padding: clamp(2rem, 6vh, 5rem) 0 3rem;
  position: relative;
}
.kicker, .sub, .shlabel, .block-head, .tag, .foot {
  text-transform: uppercase; letter-spacing: 0.12em;
}
.kicker { font-size: 0.78rem; color: var(--accent); margin: 0 0 1.6rem; font-weight: 500; }
.title {
  margin: 0; font-weight: 700; text-transform: uppercase;
  font-size: clamp(2.6rem, 7.5vw, 6.6rem);
  line-height: 0.98; letter-spacing: -0.02em;
}
.line-wrap { display: block; overflow: hidden; }
.line { display: block; }
.js .line {
  transform: translateY(112%);
  animation: line-in 0.9s var(--ease) forwards;
  animation-delay: calc(0.15s + var(--i) * 0.11s);
}
@keyframes line-in { to { transform: translateY(0); } }
.sub {
  color: var(--dim); font-size: 0.82rem; letter-spacing: 0.1em;
  max-width: 56ch; margin: 2rem 0 0; line-height: 1.9;
}
.scroll-hint {
  position: absolute; bottom: 2.2rem; left: 0;
  display: flex; align-items: center; gap: 0.8rem; color: var(--dim);
}
.shline { display: block; width: 1px; height: 56px; background: var(--dim); transform-origin: top; }
.js .shline { animation: sh 2.4s var(--ease) infinite; }
@keyframes sh { 0% { transform: scaleY(0); } 45% { transform: scaleY(1); transform-origin: top; }
  55% { transform: scaleY(1); transform-origin: bottom; } 100% { transform: scaleY(0); transform-origin: bottom; } }
.shlabel { font-size: 0.65rem; }

/* ---------- blocks & rows ---------- */
.block { margin: clamp(3.5rem, 9vh, 6.5rem) 0 0; }
.block-head {
  display: flex; align-items: baseline; gap: 1.1rem; flex-wrap: wrap;
  font-size: 0.78rem; font-weight: 500; color: var(--dim);
  margin: 0 0 0.4rem; padding-bottom: 0.9rem;
}
.block-key { color: var(--accent); }
.rows { list-style: none; margin: 0; padding: 0; }
.rows li { border-top: 1px solid var(--hair); }
.rows li:last-child { border-bottom: 1px solid var(--hair); }
.row {
  display: grid; grid-template-columns: 3.2ch 1fr auto auto;
  align-items: baseline; gap: clamp(0.8rem, 2.5vw, 1.6rem);
  padding: clamp(0.95rem, 2.2vh, 1.35rem) 0.2rem;
  text-decoration: none; color: inherit;
}
.num { font-variant-numeric: tabular-nums; color: var(--dim); font-size: 0.95rem; transition: color 0.35s var(--ease); }
.rt {
  font-size: clamp(1.35rem, 2.6vw, 2.15rem); font-weight: 500; line-height: 1.15;
  color: var(--fg); opacity: 0.86;
  transition: opacity 0.35s var(--ease), transform 0.35s var(--ease), color 0.35s var(--ease);
}
.arrow {
  font-size: clamp(1.1rem, 2vw, 1.6rem); color: var(--accent);
  opacity: 0; transform: translateX(-14px);
  transition: opacity 0.35s var(--ease), transform 0.35s var(--ease);
}
a.row:hover .rt, a.row:focus-visible .rt { opacity: 1; transform: translateX(6px); }
a.row:hover .num, a.row:focus-visible .num { color: var(--accent); }
a.row:hover .arrow, a.row:focus-visible .arrow { opacity: 1; transform: translateX(0); }
a.row.opt .rt { opacity: 0.62; }
.row.soon { cursor: default; }
.row.soon .rt, .row.soon .num { opacity: 0.35; }
.tag {
  font-size: 0.6rem; font-weight: 700; color: var(--dim);
  border: 1px solid var(--hair); border-radius: 999px; padding: 0.18rem 0.6rem;
  align-self: center; white-space: nowrap;
}

/* ---------- scroll reveal ---------- */
/* Visible by default (no-JS). JS opts elements into the hidden pre-state. */
.js .reveal { opacity: 0; transform: translateY(26px); }
.js .reveal.in {
  opacity: 1; transform: none;
  transition: opacity 0.8s var(--ease), transform 0.8s var(--ease);
  transition-delay: calc(var(--i) * 60ms);
}

/* ---------- footer ---------- */
.foot { margin-top: 5rem; border-top: 1px solid var(--hair); padding-top: 1.4rem; }
.foot p { color: var(--dim); font-size: 0.68rem; letter-spacing: 0.1em; line-height: 1.9; max-width: 72ch; }

/* ---------- reduced motion ---------- */
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  .js .line { transform: none; animation: none; }
  .js .shline { animation: none; }
  .js .reveal { opacity: 1 !important; transform: none !important; transition: none !important; }
  .row, .rt, .num, .arrow { transition: none !important; }
}
```

- [ ] **Step 2: Add the reveal observer to `landing/src/main.js`**

After the gating block, append:

```js
// Scroll reveal — .reveal elements are hidden by CSS only under .js; observer
// flips them to .in as they enter. Under reduced motion CSS forces visibility,
// but add .in anyway so state stays consistent.
const revealEls = document.querySelectorAll('.reveal');
if (reduced || !('IntersectionObserver' in window)) {
  revealEls.forEach((el) => el.classList.add('in'));
} else {
  const io = new IntersectionObserver((entries) => {
    for (const e of entries) if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
  revealEls.forEach((el) => io.observe(el));
}
```

- [ ] **Step 3: Rebuild + re-run the smoke check**

```bash
node scripts/build-landing.mjs --out /tmp/claude-1001/-home-mindaugas-wsl-CERN-lessons-on-data-analysis/56713095-ae9e-4ea8-b610-ee3e03e4d384/scratchpad/land-t4
node scripts/check-landing.mjs /tmp/claude-1001/-home-mindaugas-wsl-CERN-lessons-on-data-analysis/56713095-ae9e-4ea8-b610-ee3e03e4d384/scratchpad/land-t4
```

Expected: `last row revealed after scroll` ✓ (now exercising the real observer), `all rows immediately visible under reduced motion` ✓. The stub's canvas-size ✗ may remain — it disappears in Task 5.

- [ ] **Step 4: Visual spot-check (screenshot, not just build)**

```bash
node -e "
import('playwright-chromium').then(async ({ chromium }) => {
  const { createServer } = await import('node:http');
  const { readFile } = await import('node:fs/promises');
  const { join, extname } = await import('node:path');
  const dir = '/tmp/claude-1001/-home-mindaugas-wsl-CERN-lessons-on-data-analysis/56713095-ae9e-4ea8-b610-ee3e03e4d384/scratchpad/land-t4';
  const mime = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.woff2': 'font/woff2' };
  const srv = createServer(async (req, res) => {
    let p = req.url.split('?')[0]; if (p.endsWith('/')) p += 'index.html';
    try { res.setHeader('Content-Type', mime[extname(p)] || 'application/octet-stream'); res.end(await readFile(join(dir, p))); }
    catch { res.statusCode = 404; res.end(); }
  });
  await new Promise((r) => srv.listen(4173, r));
  const b = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
  const pg = await b.newPage({ viewport: { width: 1440, height: 900 } });
  await pg.goto('http://127.0.0.1:4173/', { waitUntil: 'load' });
  await pg.waitForTimeout(2500);
  await pg.screenshot({ path: '/tmp/claude-1001/-home-mindaugas-wsl-CERN-lessons-on-data-analysis/56713095-ae9e-4ea8-b610-ee3e03e4d384/scratchpad/land-t4-hero.png' });
  await pg.evaluate(() => window.scrollTo(0, 1400)); await pg.waitForTimeout(1500);
  await pg.screenshot({ path: '/tmp/claude-1001/-home-mindaugas-wsl-CERN-lessons-on-data-analysis/56713095-ae9e-4ea8-b610-ee3e03e4d384/scratchpad/land-t4-rows.png' });
  await b.close(); srv.close();
});"
```

Read both PNGs. Check: hero title huge/uppercase in Space Grotesk (three staggered lines), cyan kicker, scroll hint bottom-left; rows page shows hairline-separated large-type rows with dimmed numbers. Fix anything visually broken before committing.

- [ ] **Step 5: Commit**

```bash
git add landing/src/style.css landing/src/main.js
git commit -m "feat(landing): AT-style type system, rows, grain, staggered reveals"
```

---

### Task 5: GPU particle scene (FBO ping-pong sim + additive sprites)

**Files:**
- Create: `landing/src/shaders/noise.glsl.js`, `landing/src/shaders/passes.glsl.js`, `landing/src/sim.js`
- Modify: `landing/src/main.js` (boot the real scene instead of the stub class)

**Interfaces:**
- Consumes: `#field` canvas, `field-on`/`static-bg` CSS contract from Task 4.
- Produces: `createField(canvas) → null | { onPointer(clientX, clientY), onImpulse(clientX, clientY), onScroll(scrollY), setPaused(hidden) }` — Task 6 wires events to these. Returns `null` if renderer/extension setup fails (caller falls back to `static-bg`). All pointer/impulse shader plumbing is COMPLETE here (uniforms idle at neutral values); Task 6 only feeds them.

- [ ] **Step 1: Create `landing/src/shaders/noise.glsl.js`** (standard ashima/webgl-noise 3D simplex, MIT)

```js
// Ashima Arts / Stefan Gustavson 3D simplex noise (MIT), verbatim.
export const NOISE = /* glsl */ `
vec3 mod289(vec3 x){return x - floor(x * (1.0/289.0)) * 289.0;}
vec4 mod289(vec4 x){return x - floor(x * (1.0/289.0)) * 289.0;}
vec4 permute(vec4 x){return mod289(((x*34.0)+1.0)*x);}
vec4 taylorInvSqrt(vec4 r){return 1.79284291400159 - 0.85373472095314 * r;}
float snoise(vec3 v){
  const vec2 C = vec2(1.0/6.0, 1.0/3.0);
  const vec4 D = vec4(0.0, 0.5, 1.0, 2.0);
  vec3 i = floor(v + dot(v, C.yyy));
  vec3 x0 = v - i + dot(i, C.xxx);
  vec3 g = step(x0.yzx, x0.xyz);
  vec3 l = 1.0 - g;
  vec3 i1 = min(g.xyz, l.zxy);
  vec3 i2 = max(g.xyz, l.zxy);
  vec3 x1 = x0 - i1 + C.xxx;
  vec3 x2 = x0 - i2 + C.yyy;
  vec3 x3 = x0 - D.yyy;
  i = mod289(i);
  vec4 p = permute(permute(permute(
      i.z + vec4(0.0, i1.z, i2.z, 1.0))
    + i.y + vec4(0.0, i1.y, i2.y, 1.0))
    + i.x + vec4(0.0, i1.x, i2.x, 1.0));
  float n_ = 0.142857142857;
  vec3 ns = n_ * D.wyz - D.xzx;
  vec4 j = p - 49.0 * floor(p * ns.z * ns.z);
  vec4 x_ = floor(j * ns.z);
  vec4 y_ = floor(j - 7.0 * x_);
  vec4 x = x_ * ns.x + ns.yyyy;
  vec4 y = y_ * ns.x + ns.yyyy;
  vec4 h = 1.0 - abs(x) - abs(y);
  vec4 b0 = vec4(x.xy, y.xy);
  vec4 b1 = vec4(x.zw, y.zw);
  vec4 s0 = floor(b0)*2.0 + 1.0;
  vec4 s1 = floor(b1)*2.0 + 1.0;
  vec4 sh = -step(h, vec4(0.0));
  vec4 a0 = b0.xzyw + s0.xzyw*sh.xxyy;
  vec4 a1 = b1.xzyw + s1.xzyw*sh.zzww;
  vec3 p0 = vec3(a0.xy, h.x);
  vec3 p1 = vec3(a0.zw, h.y);
  vec3 p2 = vec3(a1.xy, h.z);
  vec3 p3 = vec3(a1.zw, h.w);
  vec4 norm = taylorInvSqrt(vec4(dot(p0,p0), dot(p1,p1), dot(p2,p2), dot(p3,p3)));
  p0 *= norm.x; p1 *= norm.y; p2 *= norm.z; p3 *= norm.w;
  vec4 m = max(0.6 - vec4(dot(x0,x0), dot(x1,x1), dot(x2,x2), dot(x3,x3)), 0.0);
  m = m * m;
  return 42.0 * dot(m*m, vec4(dot(p0,x0), dot(p1,x1), dot(p2,x2), dot(p3,x3)));
}`;
```

- [ ] **Step 2: Create `landing/src/shaders/passes.glsl.js`**

Three.js (WebGL2) prepends compatibility defines, so GLSL1 style (`texture2D`, `varying`, `gl_FragColor`) is correct in ShaderMaterial.

```js
import { NOISE } from './noise.glsl.js';

// Fullscreen-quad vertex shader shared by all sim passes.
export const SIM_VERT = /* glsl */ `
varying vec2 vUv;
void main() { vUv = uv; gl_Position = vec4(position, 1.0); }`;

// Seeds a render target from a DataTexture (initial positions).
export const COPY_FRAG = /* glsl */ `
uniform sampler2D uSrc;
varying vec2 vUv;
void main() { gl_FragColor = texture2D(uSrc, vUv); }`;

// Velocity update: ambient curl drift + cursor wake + hover impulse + damping.
export const VEL_FRAG = /* glsl */ `
uniform sampler2D uPos, uVel;
uniform float uDt, uTime;
uniform vec2 uPointer, uPointerVel;
uniform vec4 uImpulse;   // x,y = world pos; z = strength; w = radius^2
varying vec2 vUv;
${NOISE}
vec2 curl(vec3 p) {
  const float e = 0.35;
  float dy = snoise(p + vec3(0.0, e, 0.0)) - snoise(p - vec3(0.0, e, 0.0));
  float dx = snoise(p + vec3(e, 0.0, 0.0)) - snoise(p - vec3(e, 0.0, 0.0));
  return vec2(dy, -dx) / (2.0 * e);
}
void main() {
  vec4 pos = texture2D(uPos, vUv);
  vec2 v = texture2D(uVel, vUv).xy;
  // ambient drift
  v += curl(vec3(pos.xy * 0.16, pos.z * 0.2 + uTime * 0.05)) * 0.55 * uDt;
  // cursor wake: drag particles along the pointer's velocity, gaussian falloff
  vec2 toP = pos.xy - uPointer;
  v += uPointerVel * exp(-dot(toP, toP) / 2.2) * 0.9 * uDt;
  // hover impulse: radial push, decays JS-side via uImpulse.z
  vec2 toI = pos.xy - uImpulse.xy;
  float di = length(toI) + 1e-4;
  v += (toI / di) * uImpulse.z * exp(-di * di / uImpulse.w) * uDt;
  // frame-rate-independent damping + speed clamp
  v *= exp(-1.6 * uDt);
  float sp = length(v);
  if (sp > 3.0) v *= 3.0 / sp;
  gl_FragColor = vec4(v, 0.0, 1.0);
}`;

// Position update: integrate + toroidal wrap inside uBounds.
export const POS_FRAG = /* glsl */ `
uniform sampler2D uPos, uVel;
uniform float uDt;
uniform vec2 uBounds;
varying vec2 vUv;
void main() {
  vec4 pos = texture2D(uPos, vUv);
  vec2 v = texture2D(uVel, vUv).xy;
  vec2 p = pos.xy + v * uDt;
  p = mod(p + uBounds, 2.0 * uBounds) - uBounds;
  gl_FragColor = vec4(p, pos.zw);
}`;

// Points: position.xy carries the sim-texture ref UV.
export const RENDER_VERT = /* glsl */ `
uniform sampler2D uPos, uVel;
uniform float uSize, uPixelRatio;
varying float vAlpha;
varying vec3 vColor;
void main() {
  vec2 ref = position.xy;
  vec4 pos = texture2D(uPos, ref);
  vec2 vel = texture2D(uVel, ref).xy;
  float seed = pos.w;
  vec4 mv = modelViewMatrix * vec4(pos.xyz, 1.0);
  gl_Position = projectionMatrix * mv;
  gl_PointSize = uSize * uPixelRatio * mix(0.5, 1.6, fract(seed * 7.31)) * (12.0 / -mv.z);
  float sp = clamp(length(vel) * 0.9, 0.0, 1.0);
  vColor = mix(vec3(0.30, 0.55, 0.72), vec3(0.98, 0.99, 1.0), sp);  // dim cyan -> white by speed
  vAlpha = mix(0.25, 0.9, sp) * mix(0.4, 1.0, fract(seed * 3.17));
}`;

export const RENDER_FRAG = /* glsl */ `
varying float vAlpha;
varying vec3 vColor;
void main() {
  float d = length(gl_PointCoord - 0.5);
  float a = smoothstep(0.5, 0.05, d) * vAlpha;
  gl_FragColor = vec4(vColor * a, a);
}`;
```

- [ ] **Step 3: Create `landing/src/sim.js`**

```js
import {
  WebGLRenderer, Scene, PerspectiveCamera, OrthographicCamera, Mesh, Points,
  PlaneGeometry, BufferGeometry, BufferAttribute, ShaderMaterial, DataTexture,
  WebGLRenderTarget, RGBAFormat, FloatType, HalfFloatType, NearestFilter,
  AdditiveBlending, Vector2, Vector4, Clock,
} from 'three';
import { SIM_VERT, COPY_FRAG, VEL_FRAG, POS_FRAG, RENDER_VERT, RENDER_FRAG } from './shaders/passes.glsl.js';

const FOV = 55, CAM_Z = 14, PARALLAX = 0.0012, MAX_DT = 1 / 30;

function pickTexSize(coarse) {
  const cores = navigator.hardwareConcurrency || 4;
  const area = (screen.width || 1280) * (screen.height || 800);
  if (coarse || area < 1e6 || cores <= 4) return 160; // ~25.6k particles
  if (cores <= 8) return 256;                         // ~65.5k
  return 448;                                         // ~200.7k
}

export function createField(canvas) {
  const coarse = matchMedia('(pointer: coarse)').matches;
  let renderer;
  try {
    renderer = new WebGLRenderer({ canvas, alpha: true, antialias: false, powerPreference: 'high-performance' });
  } catch { return null; }
  if (!renderer.capabilities.isWebGL2) { renderer.dispose(); return null; }
  const type = renderer.extensions.has('EXT_color_buffer_float') ? FloatType
    : renderer.extensions.has('EXT_color_buffer_half_float') ? HalfFloatType : null;
  if (!type) { renderer.dispose(); return null; }

  const baseDpr = Math.min(devicePixelRatio || 1, coarse ? 1.5 : 2);
  renderer.setPixelRatio(baseDpr);
  renderer.setClearColor(0x000000, 0); // page gradient shows through

  const size = pickTexSize(coarse);
  const count = size * size;

  // --- camera / world extents ---
  const camera = new PerspectiveCamera(FOV, 1, 0.1, 100);
  camera.position.z = CAM_Z;
  const halfH = Math.tan((FOV / 2) * (Math.PI / 180)) * CAM_Z;
  let halfW = halfH; // set in resize()
  const bounds = new Vector2(1, 1);

  // --- sim targets (ping-pong pos + vel) ---
  const rt = () => new WebGLRenderTarget(size, size, {
    type, format: RGBAFormat, minFilter: NearestFilter, magFilter: NearestFilter,
    depthBuffer: false, stencilBuffer: false,
  });
  let posA = rt(), posB = rt(), velA = rt(), velB = rt();

  // --- initial positions: random in bounds-ish box, z in [-4,4], w = seed ---
  const init = new Float32Array(count * 4);
  for (let i = 0; i < count; i++) {
    init[i * 4 + 0] = (Math.random() * 2 - 1) * halfH * 2.4; // x (re-wrapped by sim)
    init[i * 4 + 1] = (Math.random() * 2 - 1) * halfH * 1.9; // y
    init[i * 4 + 2] = (Math.random() * 2 - 1) * 4;           // z (static parallax depth)
    init[i * 4 + 3] = Math.random();                         // seed
  }
  const initTex = new DataTexture(init, size, size, RGBAFormat, FloatType);
  initTex.needsUpdate = true;

  // --- sim pipeline: fullscreen quad, material swapped per pass ---
  const simScene = new Scene();
  const simCam = new OrthographicCamera(-1, 1, 1, -1, 0, 1);
  const quad = new Mesh(new PlaneGeometry(2, 2));
  simScene.add(quad);
  const copyMat = new ShaderMaterial({ vertexShader: SIM_VERT, fragmentShader: COPY_FRAG, uniforms: { uSrc: { value: initTex } } });
  const velMat = new ShaderMaterial({
    vertexShader: SIM_VERT, fragmentShader: VEL_FRAG,
    uniforms: {
      uPos: { value: null }, uVel: { value: null }, uDt: { value: 0 }, uTime: { value: 0 },
      uPointer: { value: new Vector2(999, 999) }, uPointerVel: { value: new Vector2(0, 0) },
      uImpulse: { value: new Vector4(999, 999, 0, 1.4) },
    },
  });
  const posMat = new ShaderMaterial({
    vertexShader: SIM_VERT, fragmentShader: POS_FRAG,
    uniforms: { uPos: { value: null }, uVel: { value: null }, uDt: { value: 0 }, uBounds: { value: bounds } },
  });
  const pass = (mat, target) => {
    quad.material = mat;
    renderer.setRenderTarget(target);
    renderer.render(simScene, simCam);
    renderer.setRenderTarget(null);
  };

  // --- points: position.xy = ref UV into the sim textures ---
  const refs = new Float32Array(count * 3);
  for (let j = 0; j < size; j++) for (let i = 0; i < size; i++) {
    const k = j * size + i;
    refs[k * 3 + 0] = (i + 0.5) / size;
    refs[k * 3 + 1] = (j + 0.5) / size;
  }
  const geo = new BufferGeometry();
  geo.setAttribute('position', new BufferAttribute(refs, 3));
  const renderMat = new ShaderMaterial({
    vertexShader: RENDER_VERT, fragmentShader: RENDER_FRAG,
    transparent: true, depthWrite: false, depthTest: false, blending: AdditiveBlending,
    uniforms: { uPos: { value: null }, uVel: { value: null }, uSize: { value: 1.5 }, uPixelRatio: { value: baseDpr } },
  });
  const points = new Points(geo, renderMat);
  points.frustumCulled = false;
  const scene = new Scene();
  scene.add(points);

  // --- pointer state (world-space); Task 6 feeds client coords ---
  const ptrClient = new Vector2(-1e4, -1e4);
  const ptrWorld = new Vector2(999, 999);
  const ptrPrev = new Vector2(999, 999);
  const ptrVel = new Vector2(0, 0);
  let hasPointer = false, lastPointerAt = 0;
  let scrollY = window.scrollY || 0;
  const impulse = velMat.uniforms.uImpulse.value;

  const toWorld = (cx, cy, out) => out.set(
    ((cx / innerWidth) * 2 - 1) * halfW,
    -((cy / innerHeight) * 2 - 1) * halfH + camera.position.y,
  );

  function resize() {
    renderer.setSize(innerWidth, innerHeight);
    camera.aspect = innerWidth / innerHeight;
    camera.updateProjectionMatrix();
    halfW = halfH * camera.aspect;
    bounds.set(halfW * 1.3, halfH * 1.9);
  }
  addEventListener('resize', resize, { passive: true });
  resize();

  // seed sim state: positions from initTex, velocities cleared to zero
  pass(copyMat, posA);
  renderer.setRenderTarget(velA);
  renderer.clear(true, false, false);
  renderer.setRenderTarget(null);

  // --- loop (visibility pause + fps guard hooks used by Task 6) ---
  const clock = new Clock();
  let raf = 0, paused = false, elapsed = 0;
  // fps guard: after 4s warmup, avg over ~2s windows; degrade at <40fps, twice max
  let guardStage = 0, winFrames = 0, winTime = 0;

  function frame() {
    raf = requestAnimationFrame(frame);
    const dt = Math.min(clock.getDelta(), MAX_DT);
    elapsed += dt;

    // pointer velocity in world units/s (smoothed); idle if no pointer yet
    if (hasPointer) {
      toWorld(ptrClient.x, ptrClient.y, ptrWorld);
      if (dt > 0) {
        ptrVel.set((ptrWorld.x - ptrPrev.x) / dt, (ptrWorld.y - ptrPrev.y) / dt).clampLength(0, 30);
        velMat.uniforms.uPointerVel.value.lerp(ptrVel, 0.15);
      }
      ptrPrev.copy(ptrWorld);
      velMat.uniforms.uPointer.value.copy(ptrWorld);
    }

    velMat.uniforms.uDt.value = dt;
    velMat.uniforms.uTime.value = elapsed;
    posMat.uniforms.uDt.value = dt;

    velMat.uniforms.uPos.value = posA.texture;
    velMat.uniforms.uVel.value = velA.texture;
    pass(velMat, velB);
    posMat.uniforms.uPos.value = posA.texture;
    posMat.uniforms.uVel.value = velB.texture;
    pass(posMat, posB);
    [posA, posB] = [posB, posA];
    [velA, velB] = [velB, velA];

    impulse.z *= 0.86; // hover impulse decay

    camera.position.y = -scrollY * PARALLAX * halfH;
    renderMat.uniforms.uPos.value = posA.texture;
    renderMat.uniforms.uVel.value = velA.texture;
    renderer.render(scene, camera);

    if (elapsed > 4 && guardStage < 2) {
      winFrames++; winTime += dt;
      if (winTime >= 2) {
        if (winFrames / winTime < 40) {
          if (guardStage === 0) renderMat.uniforms.uPixelRatio.value = baseDpr * 0.7,
            renderer.setPixelRatio(baseDpr * 0.7);
          else geo.setDrawRange(0, Math.floor(count / 2));
          guardStage++;
        }
        winFrames = 0; winTime = 0;
      }
    }
  }
  frame();

  return {
    onPointer(cx, cy) { ptrClient.set(cx, cy); hasPointer = true; lastPointerAt = elapsed; },
    onImpulse(cx, cy) {
      const w = toWorld(cx, cy, new Vector2());
      impulse.set(w.x, w.y, 26, 1.4);
    },
    onScroll(y) { scrollY = y; },
    setPaused(p) {
      if (p === paused) return;
      paused = p;
      if (p) cancelAnimationFrame(raf);
      else { clock.getDelta(); frame(); }
    },
  };
}
```

- [ ] **Step 4: Boot the real scene in `landing/src/main.js`**

Replace the stub `if (reduced || !webgl2Ok()) … else html.classList.add('field-on')` block with:

```js
import { createField } from './sim.js';
```

(top of file, with the other imports) and:

```js
let field = null;
if (reduced || !webgl2Ok()) {
  html.classList.add('static-bg');
} else {
  field = createField(document.getElementById('field'));
  html.classList.add(field ? 'field-on' : 'static-bg');
}
```

(Event wiring is Task 6; the scene already drifts ambiently.)

- [ ] **Step 5: Build, check, screenshot**

```bash
node scripts/build-landing.mjs --out /tmp/claude-1001/-home-mindaugas-wsl-CERN-lessons-on-data-analysis/56713095-ae9e-4ea8-b610-ee3e03e4d384/scratchpad/land-t5
node scripts/check-landing.mjs /tmp/claude-1001/-home-mindaugas-wsl-CERN-lessons-on-data-analysis/56713095-ae9e-4ea8-b610-ee3e03e4d384/scratchpad/land-t5
```

Expected: ALL assertions pass now, including `canvas has non-zero backing size` (the Task 3 RED turns GREEN). Re-run the Task 4 Step 4 screenshot one-liner against `land-t5`; the hero shot must show visible particles (faint cyan-white dust) behind the type. If the canvas is black-empty, debug before proceeding (common causes: ref UV vs texture orientation, additive alpha 0, camera facing wrong z).

- [ ] **Step 6: Verify JS budget**

```bash
gzip -c landing/dist-assets/assets/landing.js | wc -c
```

Expected: ≲ 160000 (spec budget ~150 KB gz; tree-shaken three should land well under).

- [ ] **Step 7: Commit**

```bash
git add landing/src/
git commit -m "feat(landing): GPU particle field — FBO ping-pong sim, additive sprites"
```

---

### Task 6: Interactions — cursor wake, hover impulse, scroll parallax, touch attractor, visibility pause

**Files:**
- Modify: `landing/src/main.js` (event wiring), `landing/src/sim.js` (touch attractor in the loop)

**Interfaces:**
- Consumes: Task 5's `field` API (`onPointer`, `onImpulse`, `onScroll`, `setPaused`) plus direct edits to `sim.js` internals (`coarse`, `lastPointerAt`, `ptrClient` are all in scope inside `frame()`).
- Produces: the finished interactive page; no new interfaces.

- [ ] **Step 1: Wire events in `landing/src/main.js`**

After the `field = createField(...)` boot block, add:

```js
if (field) {
  addEventListener('pointermove', (e) => field.onPointer(e.clientX, e.clientY), { passive: true });
  addEventListener('scroll', () => field.onScroll(window.scrollY), { passive: true });
  document.querySelectorAll('a.row').forEach((a) =>
    a.addEventListener('pointerenter', (e) => field.onImpulse(e.clientX, e.clientY)));
  document.addEventListener('visibilitychange', () => field.setPaused(document.hidden));
}
```

- [ ] **Step 2: Touch attractor in `landing/src/sim.js`**

In the `frame()` function, replace the line `if (hasPointer) {` and its opening with an autonomous-attractor branch. The full replacement for the pointer-velocity block:

```js
    // Touch devices idle >2.5s (or before any pointer event): roam a lissajous
    // attractor so the field feels alive without a cursor. Any real pointer /
    // touch-drag event takes over immediately via onPointer().
    if (coarse && (!hasPointer || elapsed - lastPointerAt > 2.5)) {
      ptrClient.set(
        (0.5 + 0.38 * Math.sin(elapsed * 0.31)) * innerWidth,
        (0.5 + 0.34 * Math.cos(elapsed * 0.21)) * innerHeight,
      );
      hasPointer = true;
    }
    if (hasPointer) {
      toWorld(ptrClient.x, ptrClient.y, ptrWorld);
      if (dt > 0) {
        ptrVel.set((ptrWorld.x - ptrPrev.x) / dt, (ptrWorld.y - ptrPrev.y) / dt).clampLength(0, 30);
        velMat.uniforms.uPointerVel.value.lerp(ptrVel, 0.15);
      }
      ptrPrev.copy(ptrWorld);
      velMat.uniforms.uPointer.value.copy(ptrWorld);
    }
```

(The rest of the block is unchanged from Task 5 — only the attractor branch is new.)

- [ ] **Step 3: Build + full smoke check**

```bash
node scripts/build-landing.mjs --out /tmp/claude-1001/-home-mindaugas-wsl-CERN-lessons-on-data-analysis/56713095-ae9e-4ea8-b610-ee3e03e4d384/scratchpad/land-t6
node scripts/check-landing.mjs /tmp/claude-1001/-home-mindaugas-wsl-CERN-lessons-on-data-analysis/56713095-ae9e-4ea8-b610-ee3e03e4d384/scratchpad/land-t6
```

Expected: all ✓, exit 0.

- [ ] **Step 4: Interaction spot-check (wake visibly follows the mouse)**

```bash
node -e "
import('playwright-chromium').then(async ({ chromium }) => {
  const { createServer } = await import('node:http');
  const { readFile } = await import('node:fs/promises');
  const { join, extname } = await import('node:path');
  const dir = '/tmp/claude-1001/-home-mindaugas-wsl-CERN-lessons-on-data-analysis/56713095-ae9e-4ea8-b610-ee3e03e4d384/scratchpad/land-t6';
  const mime = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.woff2': 'font/woff2' };
  const srv = createServer(async (req, res) => {
    let p = req.url.split('?')[0]; if (p.endsWith('/')) p += 'index.html';
    try { res.setHeader('Content-Type', mime[extname(p)] || 'application/octet-stream'); res.end(await readFile(join(dir, p))); }
    catch { res.statusCode = 404; res.end(); }
  });
  await new Promise((r) => srv.listen(4174, r));
  const b = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
  const pg = await b.newPage({ viewport: { width: 1440, height: 900 } });
  await pg.goto('http://127.0.0.1:4174/', { waitUntil: 'load' });
  await pg.waitForTimeout(2000);
  await pg.screenshot({ path: '/tmp/claude-1001/-home-mindaugas-wsl-CERN-lessons-on-data-analysis/56713095-ae9e-4ea8-b610-ee3e03e4d384/scratchpad/land-t6-before.png' });
  for (let i = 0; i <= 30; i++) { await pg.mouse.move(300 + i * 28, 450 + Math.sin(i / 4) * 160); await pg.waitForTimeout(16); }
  await pg.screenshot({ path: '/tmp/claude-1001/-home-mindaugas-wsl-CERN-lessons-on-data-analysis/56713095-ae9e-4ea8-b610-ee3e03e4d384/scratchpad/land-t6-wake.png' });
  await b.close(); srv.close();
});"
```

Read both PNGs: the `wake` shot must show a visibly brighter/denser particle trail along the mouse path (speed tints particles whiter) versus `before`. If indistinguishable, raise the wake gain (the `0.9` in `VEL_FRAG`'s cursor-wake line) and re-check.

- [ ] **Step 5: Commit**

```bash
git add landing/src/
git commit -m "feat(landing): cursor wake, hover impulses, parallax, touch attractor"
```

---

### Task 7: Full-pipeline verification + docs

**Files:**
- Modify: `CLAUDE.md` (commands + architecture blurbs)
- No code changes expected — this task gates the whole feature.

**Interfaces:** Consumes everything; produces the verified, documented feature.

- [ ] **Step 1: Full production-shaped build**

```bash
pnpm build 2>&1 | tail -20
ls dist/assets/ && head -c 400 dist/index.html
```

Expected: all 16 decks ✓, `Landing → dist/index.html` in output (via build-landing), `dist/assets/` holds `landing.js`/`landing.css`/woff2, index.html starts with the new markup. Deck links in `dist/index.html` are `/<slug>/` (no `--base` given).

- [ ] **Step 2: Landing check against the real dist**

```bash
node scripts/check-landing.mjs dist
```

Expected: exit 0 (deck subdirectories exist here, so this is the fullest-fidelity pass).

- [ ] **Step 3: Full QA gate (decks + landing)**

```bash
pnpm qa 2>&1 | tail -25
```

Expected: `✓ <slug>` for all 16 decks, `✓ landing`, `✅ All 16 deck(s) + landing pass QA.` This is the blocking gate — do not proceed with failures.

- [ ] **Step 4: Mobile-viewport screenshot review**

Re-run the Task 4 Step 4 screenshot one-liner against `dist` with `viewport: { width: 390, height: 844 }` (rename output PNGs `land-t7-mobile-*.png`). Read them: hero type must not clip or wrap awkwardly, rows must remain tappable-height, no horizontal scroll (compare `document.documentElement.scrollWidth === 390` via an added `console.log` if unsure).

- [ ] **Step 5: Update `CLAUDE.md`**

- In **Commands**, after the `pnpm qa:shots` line, add:
  ```bash
  pnpm build:landing          # rebuild only the landing page + its WebGL bundle → dist/
  ```
- In **Build pipeline**, add one bullet:
  ```markdown
  - **`landing/` + `scripts/build-landing.mjs`** — the landing page is an Active Theory-style WebGL page: `landing/` (Three.js particle sim + CSS + fonts) is built by Vite to fixed-name assets; `build-landing.mjs` copies them to `<out>/assets/` and calls `gen-landing.mjs`, which still renders all content (hero, lecture rows) from `decks.json` — the page works fully without JS. `qa-all.mjs` smoke-tests it via `scripts/check-landing.mjs` (links, WebGL boot/fallback gating, reveals, zero console errors).
  ```
- In the `pnpm qa` line of Commands, append: `(includes the landing smoke test)`.

- [ ] **Step 6: Final commit**

```bash
git add CLAUDE.md
git commit -m "docs: landing build + QA docs for the WebGL landing page"
```

- [ ] **Step 7: Deployment note (do NOT push without the user)**

Remind the user: Pages deploys from `bs2026` only — the new landing is not live until `ff2026` is pushed as `ff2026:bs2026` (per project memory). Ask before pushing.

---

## Plan Self-Review (completed)

- **Spec coverage:** palette/typography/hero/rows/grain (§2 → Tasks 2/4), particle sim + wake + impulse + parallax (§2.4 → Tasks 5/6), architecture/fixed-names/relative-base/progressive-enhancement (§3 → Tasks 1/2), tiers/DPR caps/fps guard/touch/reduced-motion/no-WebGL2/visibility pause (§4 → Tasks 5/6), check-landing + qa wiring incl. `.qa-dist/__landing__` (§5 → Task 3), 404 palette-only (§2 out-of-scope → Task 2 Step 2), budget check (§4 → Task 5 Step 6). Deviations from spec, both deliberate: fonts ship via `@fontsource/space-grotesk` instead of a vendored `landing/fonts/` dir (same self-hosted result, less manual vendoring); fps guard degrades pixel-ratio first then draw-range (equivalent render-cost halving without an FBO rebuild).
- **Type consistency:** `createField` API names (`onPointer`/`onImpulse`/`onScroll`/`setPaused`) match between Task 5 (producer) and Task 6 (consumer); `buildLanding(outDir, prefix)` matches between Tasks 2/3; CSS class contract (`js`/`field-on`/`static-bg`/`reveal`/`in`) consistent across Tasks 1–5 and asserted in Task 3.
- **Placeholder scan:** no TBDs; every code step carries full code; commands carry expected output.

