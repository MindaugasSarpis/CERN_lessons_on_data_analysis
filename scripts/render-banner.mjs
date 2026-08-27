// Render the landing-page particle sphere to static high-DPI 16:9 PNGs.
// Drives the built landing (ldist/) in headless Chromium (SwiftShader WebGL2)
// with a FAKED clock so the sim runs at a deterministic 60 fps regardless of
// software-render speed (keeps the fps guard from degrading pixel ratio /
// particle count). Screenshots are taken via raw CDP (no in-page rAF needed).
import { createServer } from 'node:http';
import { readFile, stat, mkdir, writeFile } from 'node:fs/promises';
import { join, extname, normalize, resolve } from 'node:path';
import { chromium } from 'playwright-chromium';

const argv = process.argv.slice(2);
const opt = (n, d) => { const i = argv.indexOf(n); return i > -1 ? argv[i + 1] : d; };
const DIST = resolve(opt('--dist', 'dist'));
const OUT = resolve(opt('--out', 'out'));
const W = +opt('--w', 1920), H = +opt('--h', 1080), DPR = +opt('--dpr', 2);
const TIMES = opt('--times', '7,9,12').split(',').map(Number);   // sim seconds to snapshot
const TAG = opt('--tag', 'landing');
const CENTER = argv.includes('--center');
const BOOST = +opt('--boost', 1);      // core point brightness multiplier (>1 → more dots go white)
const SIZE = +opt('--size', 1);        // core point size multiplier
const TWINKLE = argv.includes('--twinkle'); // widen the twinkle amplitude (more contrast between dots)
const BURSTS = opt('--bursts', '').split(',').filter(Boolean).map(Number).sort((a, b) => a - b);
// --bursts t1,t2: at those sim seconds fire the landing's own row-hover fiber burst
// (synthetic pointerenter on a.row) — its arrival ~1.8 s later ripples a flash of
// white dots across the sphere. Time them so ripples are mid-spread at capture.   // also emit a sphere-centered 16:9 crop
await mkdir(OUT, { recursive: true });

const MIME = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.png': 'image/png', '.woff2': 'font/woff2', '.svg': 'image/svg+xml' };
const server = createServer(async (req, res) => {
  try {
    let fp = normalize(join(DIST, decodeURIComponent(req.url.split('?')[0])));
    let s = await stat(fp).catch(() => null);
    if (s?.isDirectory()) { fp = join(fp, 'index.html'); s = await stat(fp).catch(() => null); }
    if (!s) { res.statusCode = 404; return res.end(); }
    res.setHeader('Content-Type', MIME[extname(fp)] || 'application/octet-stream');
    res.end(await readFile(fp));
  } catch (e) { res.statusCode = 500; res.end(String(e)); }
});
const port = await new Promise((r) => server.listen(0, '127.0.0.1', () => r(server.address().port)));

const browser = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
const ctx = await browser.newContext({
  viewport: { width: W, height: H }, deviceScaleFactor: DPR,
  screen: { width: 2560, height: 1440 }, reducedMotion: 'no-preference',
});
const page = await ctx.newPage();
const errors = [];
page.on('console', (m) => { if (m.type() === 'error') errors.push(m.text()); });
page.on('pageerror', (e) => errors.push(String(e)));
await page.clock.install({ time: new Date('2026-08-27T10:00:00Z') });
await page.clock.pauseAt(new Date('2026-08-27T10:00:01Z'));
// Request-time rewrite of the built bundle (no source changes):
//  --no-fiber3: the third fiber's far point (6,-4,-34) lies almost on the view
//    ray at scroll 0, so in a STILL it collapses into a zig-zag inside the sphere.
//  --boost/--size/--twinkle: core shader constants (core.js NODE_VERT).
const REWRITES = [];
if (argv.includes('--no-fiber3')) REWRITES.push([/(new U\(6,-4,-34\)[^}]*baseAlpha:)\.4\}/, '$10}']);
if (BOOST !== 1) REWRITES.push(['vAlpha = (0.65 + 0.35 * tw)', `vAlpha = ${BOOST.toFixed(2)} * (0.65 + 0.35 * tw)`]);
if (SIZE !== 1) REWRITES.push(['float size = mix(34.0, 54.0,', `float size = ${SIZE.toFixed(2)} * mix(34.0, 54.0,`]);
if (TWINKLE) REWRITES.push(['float tw = 0.75 + 0.25 * sin(', 'float tw = 0.55 + 0.45 * sin(']);
if (REWRITES.length) {
  await page.route('**/assets/landing.js', async (route) => {
    let body = await readFile(join(DIST, 'assets', 'landing.js'), 'utf8');
    for (const [from, to] of REWRITES) {
      const next = body.replace(from, to);
      if (next === body) console.warn(`  ! rewrite not applied: ${from}`);
      body = next;
    }
    await route.fulfill({ body, contentType: 'text/javascript' });
  });
}
await page.goto(`http://127.0.0.1:${port}/?qa`, { waitUntil: 'load' });
await page.addStyleTag({ content: `
  #field { opacity: 1 !important; transition: none !important; }
  .grain { display: none !important; }
  .js .line { animation: none !important; transform: none !important; }
  .scroll-hint, .corner { display: none !important; }
  html.clean .wrap { visibility: hidden !important; }
` });
await page.evaluate(() => document.fonts.ready);
const cls = await page.evaluate(() => [...document.documentElement.classList]);
console.log('html classes:', cls.join(' '));
if (!cls.includes('field-on')) { console.error('WebGL field did not boot'); process.exit(1); }

const cdp = await ctx.newCDPSession(page);
async function shot(name, clipCss) {
  const c = clipCss || { x: 0, y: 0, w: W, h: H };
  // clip.scale = DPR is what makes CDP return device pixels (else it returns CSS px)
  const params = { format: 'png', fromSurface: true, captureBeyondViewport: false,
    clip: { x: c.x, y: c.y, width: c.w, height: c.h, scale: DPR } };
  const { data } = await cdp.send('Page.captureScreenshot', params);
  const fp = join(OUT, name);
  await writeFile(fp, Buffer.from(data, 'base64'));
  console.log('  wrote', fp);
}

// Analytic screen-x of the core centre (rig at scroll 0, first frame snaps).
function coreScreenX() {
  const D2R = Math.PI / 180, C = [3.2, 1.2, 0];
  const azi = -18 * D2R, el = 2 * D2R, r = 10, aside = 3.5, fov = 55 * D2R;
  const pos = [C[0] + r * Math.cos(el) * Math.sin(azi), C[1] + r * Math.sin(el), C[2] + r * Math.cos(el) * Math.cos(azi)];
  const look = [C[0] - aside, C[1], C[2]];
  const sub = (a, b) => a.map((v, i) => v - b[i]);
  const norm = (a) => { const l = Math.hypot(...a); return a.map((v) => v / l); };
  const cross = (a, b) => [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]];
  const dot = (a, b) => a.reduce((s, v, i) => s + v * b[i], 0);
  const f = norm(sub(look, pos)), right = norm(cross(f, [0, 1, 0])), up = cross(right, f);
  const v = sub(C, pos);
  const x = dot(v, right), y = dot(v, up), z = dot(v, f);
  const ndcX = x / (z * Math.tan(fov / 2) * (W / H)), ndcY = y / (z * Math.tan(fov / 2));
  return { x: (ndcX + 1) / 2 * W, y: (1 - ndcY) / 2 * H };
}

let simT = 0;
const t0 = Date.now();
for (const T of TIMES) {
  while (simT < T) {
    await page.clock.runFor(250);
    simT = await page.evaluate(() => window.__qaElapsed ? window.__qaElapsed() : -1);
    while (BURSTS.length && BURSTS[0] <= simT) {
      BURSTS.shift();
      await page.evaluate(() => document.querySelector('a.row').dispatchEvent(
        new PointerEvent('pointerenter', { clientX: 60, clientY: 60, bubbles: false })));
      console.log(`\n  burst fired @ sim ${simT.toFixed(2)}s`);
    }
    process.stdout.write(`\r  sim ${simT.toFixed(2)}s  (wall ${((Date.now() - t0) / 1000).toFixed(0)}s)   `);
  }
  console.log(`\nsnapshot @ sim ${simT.toFixed(2)}s`);
  const c = coreScreenX();
  console.log(`  core centre ≈ (${c.x.toFixed(0)}, ${c.y.toFixed(0)}) css px of ${W}x${H}`);
  await page.evaluate(() => document.documentElement.classList.add('clean'));
  await shot(`${TAG}-clean-t${T}.png`);
  if (CENTER) {
    const cw = H * 16 / 9, ch = H;
    const x = Math.max(0, Math.min(W - cw, c.x - cw / 2));
    await shot(`${TAG}-centered-t${T}.png`, { x, y: 0, w: cw, h: ch });
  }
  await page.evaluate(() => document.documentElement.classList.remove('clean'));
  if (!CENTER) await shot(`${TAG}-title-t${T}.png`);
}
if (errors.length) console.log('console errors:', errors.join(' | ').slice(0, 500));
await browser.close();
server.close();
