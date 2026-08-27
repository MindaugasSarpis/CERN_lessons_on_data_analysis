// Capture a frame sequence of the landing-page particle sphere for an animated
// GIF/WebP. Same harness as render-banner.mjs (headless Chromium + SwiftShader,
// FAKED clock → deterministic 60 fps sim, raw-CDP screenshots, request-time
// bundle rewrites), but steps the clock one output frame at a time and writes
// frames/<comp>/f%04d.png for each requested composition. Render WIDE (2.6:1)
// at 2× so one sim run yields both the landing composition (central 16:9 crop —
// same camera, so identical to a 16:9 render) and a sphere-centered 16:9 crop.
//
//   node render-gif.mjs --from 9 --dur 8 --fps 12.5 --bursts 7,9,11,13,15,17 ...
//   node render-gif.mjs --from 0 --dur 9.6 --intro ...   (materialise sequence)
import { createServer } from 'node:http';
import { readFile, stat, mkdir, writeFile } from 'node:fs/promises';
import { join, extname, normalize, resolve } from 'node:path';
import { chromium } from 'playwright-chromium';

const argv = process.argv.slice(2);
const opt = (n, d) => { const i = argv.indexOf(n); return i > -1 ? argv[i + 1] : d; };
const DIST = resolve(opt('--dist', 'dist'));
const OUT = resolve(opt('--out', 'frames'));
const W = +opt('--w', 1404), H = +opt('--h', 540), DPR = +opt('--dpr', 2);
const FPS = +opt('--fps', 12.5);
const FROM = +opt('--from', 9), DUR = +opt('--dur', 8);
const COMPS = opt('--comps', 'landing,centered').split(',');
const BOOST = +opt('--boost', 1), SIZE = +opt('--size', 1);
const TWINKLE = argv.includes('--twinkle');
const FLARE = +opt('--flare', 1);            // scale of core flash + collision flare (<1 → calmer)
const CALM_DUST = argv.includes('--calm-dust');
const DUST = +opt('--dust', 0);
const LOOP = +opt('--loop-period', 0);       // make both visible fibers' travelling pulses periodic in this many seconds              // ambient sim texture size on the top tier (448=200k, 256=65k, 160=26k) // cap near-camera ambient point size (no big soft discs)
const BURSTS = opt('--bursts', '').split(',').filter(Boolean).map(Number).sort((a, b) => a - b);
const N = Math.round(DUR * FPS);
const STEP = 1000 / FPS;

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
await page.clock.install({ time: new Date('2026-08-27T10:00:00Z') });
await page.clock.pauseAt(new Date('2026-08-27T10:00:01Z'));

const REWRITES = [];
if (argv.includes('--no-fiber3')) REWRITES.push([/(new U\(6,-4,-34\)[^}]*baseAlpha:)\.4\}/, '$10}']);
if (BOOST !== 1) REWRITES.push(['vAlpha = (0.65 + 0.35 * tw)', `vAlpha = ${BOOST.toFixed(2)} * (0.65 + 0.35 * tw)`]);
if (SIZE !== 1) REWRITES.push(['float size = mix(34.0, 54.0,', `float size = ${SIZE.toFixed(2)} * mix(34.0, 54.0,`]);
if (TWINKLE) REWRITES.push(['float tw = 0.75 + 0.25 * sin(', 'float tw = 0.55 + 0.45 * sin(']);
if (FLARE !== 1) {
  REWRITES.push(['flash * 2.4', `flash * ${(2.4 * FLARE).toFixed(2)}`]);
  REWRITES.push(['flash * 30.0', `flash * ${(30 * FLARE).toFixed(1)}`]);
  REWRITES.push(['170.0 * flare', `${(170 * FLARE).toFixed(1)} * flare`]);
}
if (LOOP) {  // fiber 0 pulseSpeed .10 (10 s), fiber 1 .06 (16.7 s) → both 1/LOOP
  REWRITES.push(['pulseSpeed:.1,', `pulseSpeed:${(1 / LOOP).toFixed(4)},`]);
  REWRITES.push(['pulseSpeed:.06,', `pulseSpeed:${(1 / LOOP).toFixed(4)},`]);
  // fiber shape noise: replace the linear time drift (rate k) with a circle in
  // noise-space of the same per-loop path length (R = k·LOOP / 2π) → shape is
  // exactly periodic in LOOP seconds while drifting at the same visual speed
  const W = (2 * Math.PI / LOOP).toFixed(5);
  const circ = (k, seedExpr) => {
    const R = (k * LOOP / (2 * Math.PI)).toFixed(3);
    return `${seedExpr} + ${R} * cos(uTime * ${W}), ${R} * sin(uTime * ${W})`;
  };
  REWRITES.push(['vec3(t * uFreq, uTime * 0.12, uSeed)', `vec3(t * uFreq, ${circ(0.12, 'uSeed')})`]);
  REWRITES.push(['vec3(t * uFreq * 0.7, uTime * 0.09, uSeed + 31.7)', `vec3(t * uFreq * 0.7, ${circ(0.09, 'uSeed + 31.7')})`]);
  REWRITES.push(['vec3(t * uFreq * 0.55, uTime * 0.10, uSeed + 77.3)', `vec3(t * uFreq * 0.55, ${circ(0.10, 'uSeed + 77.3')})`]);
}
if (DUST) REWRITES.push(['t<=8?256:448}', `t<=8?256:${DUST}}`]);
if (CALM_DUST) REWRITES.push(['(12.0 / max(-mv.z, 0.1))', 'min(12.0 / max(-mv.z, 0.1), 2.5)']);
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
  .grain, .wrap { display: none !important; }
` });
const cls = await page.evaluate(() => [...document.documentElement.classList]);
if (!cls.includes('field-on')) { console.error('WebGL field did not boot:', cls.join(' ')); process.exit(1); }

// Core centre (css px) from the rig at scroll 0 — see render-banner.mjs.
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
  return (dot(v, right) / (dot(v, f) * Math.tan(fov / 2) * (W / H)) + 1) / 2 * W;
}
const cw = H * 16 / 9;
const CLIPS = {
  landing: { x: (W - cw) / 2, y: 0, w: cw, h: H },
  centered: { x: Math.max(0, Math.min(W - cw, coreScreenX() - cw / 2)), y: 0, w: cw, h: H },
};
for (const c of COMPS) { if (!CLIPS[c]) throw new Error(`unknown comp ${c}`); await mkdir(join(OUT, c), { recursive: true }); }

const cdp = await ctx.newCDPSession(page);
const elapsed = () => page.evaluate(() => window.__qaElapsed());
let simT = 0;
const fireBursts = async () => {
  while (BURSTS.length && BURSTS[0] <= simT) {
    BURSTS.shift();
    await page.evaluate(() => document.querySelector('a.row').dispatchEvent(
      new PointerEvent('pointerenter', { clientX: 60, clientY: 60 })));
  }
};
// advance to FROM in coarse steps (bursts still fire on schedule)
while (simT < FROM - 1e-3) {
  await page.clock.runFor(Math.min(250, Math.max(1, Math.round((FROM - simT) * 1000))));
  simT = await elapsed(); await fireBursts();
}
const t0 = Date.now();
for (let i = 0; i < N; i++) {
  for (const c of COMPS) {
    const k = CLIPS[c];
    const { data } = await cdp.send('Page.captureScreenshot', {
      format: 'png', fromSurface: true, captureBeyondViewport: false,
      clip: { x: k.x, y: k.y, width: k.w, height: k.h, scale: DPR },
    });
    await writeFile(join(OUT, c, `f${String(i).padStart(4, '0')}.png`), Buffer.from(data, 'base64'));
  }
  await page.clock.runFor(STEP);
  simT = await elapsed(); await fireBursts();
  if (i % 10 === 0 || i === N - 1) process.stdout.write(`\r  frame ${i + 1}/${N}  sim ${simT.toFixed(2)}s  wall ${((Date.now() - t0) / 1000).toFixed(0)}s   `);
}
console.log(`\nframes → ${OUT} (${COMPS.join(', ')}), ${N} × ${Math.round(cw * DPR)}×${H * DPR}`);
await browser.close();
server.close();
