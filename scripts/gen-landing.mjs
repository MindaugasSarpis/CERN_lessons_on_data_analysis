#!/usr/bin/env node
/**
 * gen-landing.mjs — emit the course-home landing page (<out>/index.html +
 * <out>/404.html) from decks.json. References the landing enhancement bundle
 * at `./assets/landing.css` + `./assets/landing.js` (built by
 * build-landing.mjs / build:landing:assets) — it does not build that bundle
 * itself. Decks are grouped by block; each links to its own deck at
 * `<prefix>/<slug>/`. Block E is marked Optional. Decks with `draft: true`
 * render in place as a greyed, unlinked "coming soon" row (staged release
 * during the semester: flip the flag on delivery day and redeploy).
 *
 * Exported as genLanding() for build-landing.mjs; also runnable standalone
 * (assumes ./assets/* already exist next to the output):
 *   node scripts/gen-landing.mjs [--out dist] [--base <prefix>]
 */
import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { join, dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

export async function genLanding(manifest, outDir, prefix = '') {
  const base = prefix.replace(/\/$/, '');
  const byBlock = new Map(Object.keys(manifest.blocks).map((k) => [k, []]));
  for (const d of manifest.decks) (byBlock.get(d.block) || byBlock.set(d.block, []).get(d.block)).push(d);

  // Hero title lines: art-directed via manifest.titleLines when present,
  // else split the course title into ~equal lines.
  let lines = manifest.titleLines;
  if (!Array.isArray(lines) || !lines.length) {
    const words = manifest.course.split(' ');
    const per = Math.ceil(words.length / 3);
    lines = [];
    for (let i = 0; i < words.length; i += per) lines.push(words.slice(i, i + per).join(' '));
  }

  const titleHtml = lines.map((l, i) =>
    `<span class="line-wrap"><span class="line" style="--i:${i}">${esc(l)}</span></span>`).join('\n        ');

  let rowIdx = 0;
  const row = (d) => d.draft ? `
          <li class="reveal" style="--i:${rowIdx++ % 8}">
            <span class="row soon" data-slug="${esc(d.slug)}">
              <span class="num">${esc(d.slug.split('-')[0])}</span>
              <span class="rt">${esc(d.title)}</span>
              <span class="tag">coming soon</span>
            </span>
          </li>` : `
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


  // Social/SEO metadata — emitted only when the canonical site URL is known.
  const descr = 'A practice-first course: tool-agnostic thinking, reproducible analysis, automation, and efficient work with data and files.';
  const siteUrl = manifest.site && manifest.site.url ? manifest.site.url.replace(/\/$/, '') : '';
  const metaTags = siteUrl ? `
<meta name="description" content="${esc(descr)}">
<meta property="og:title" content="${esc(manifest.course)}">
<meta property="og:description" content="${esc(descr)}">
<meta property="og:type" content="website">
<meta property="og:url" content="${esc(siteUrl)}/">
<meta property="og:image" content="${esc(siteUrl)}/assets/og.png">
<meta name="twitter:card" content="summary_large_image">` : '';

  const html = `<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(manifest.course)}</title>${metaTags}
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
      <div class="corner corner-tr" aria-hidden="true">Autumn 2026</div>
      <div class="corner corner-br" aria-hidden="true">${manifest.decks.length} lectures &middot; ${manifest.decks.length} seminars</div>
      <p class="kicker">${esc(manifest.presenter)}</p>
      <h1 class="title">
        ${titleHtml}
      </h1>
      <p class="sub">A practice-first course: tool-agnostic thinking, reproducible analysis, automation, and efficient work with data and files. Each lecture opens on its own so it loads fast.</p>
      <div class="scroll-hint" aria-hidden="true"><span class="shline"></span><span class="shlabel">Scroll</span></div>
    </header>
    ${blockSections}
    <footer class="foot">
      <p>Each lecture has a paired hands-on seminar — briefs, overview and lecture notes are in the <a href="${base}/workbook/">workbook &#8594;</a>. Block E is the optional tail if the term runs short.</p>
    </footer>
  </main>
  <script type="module" src="./assets/landing.js"></script>
</body></html>`;

  await mkdir(outDir, { recursive: true });
  await writeFile(join(outDir, 'index.html'), html, 'utf8');
  await writeFile(join(outDir, '404.html'), gen404(manifest, base), 'utf8');
  return join(outDir, 'index.html');
}

// Root-level 404.html — the only 404 page GitHub Pages honors (per-deck copies
// in subdirectories are ignored). Decks use hash routing, but links shared
// before the switch look like `<base>/<slug>/5`; rewrite those to
// `<base>/<slug>/#/5` so they keep working. Anything else (including a not-
// yet-released draft deck) gets a link home.
function gen404(manifest, base) {
  const slugs = manifest.decks.filter((d) => !d.draft).map((d) => d.slug);
  return `<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page not found — ${esc(manifest.course)}</title>
<script>
(function () {
  var base = ${JSON.stringify(base)};
  var slugs = ${JSON.stringify(slugs)};
  var path = location.pathname;
  if (base && path.indexOf(base) === 0) path = path.slice(base.length);
  var m = path.match(/^\\/([^/]+)\\/?(.*)$/);
  if (m && slugs.indexOf(m[1]) !== -1) {
    var rest = m[2] ? '#/' + m[2] : '';
    location.replace(base + '/' + m[1] + '/' + location.search + rest);
  }
})();
</script>
<style>
  :root { color-scheme: dark; }
  body { margin: 0; min-height: 100vh; display: grid; place-items: center;
         font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
         background: #050507; color: #f2f5f9; }
  a { color: #7dd3fc; }
</style>
</head><body>
  <p>Page not found — <a href="${esc(base)}/">go to the course home</a>.</p>
</body></html>`;
}

// Standalone runner
if (import.meta.url === `file://${process.argv[1]}`) {
  const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
  const argv = process.argv.slice(2);
  const opt = (n, d) => { const i = argv.indexOf(n); return i > -1 ? argv[i + 1] : d; };
  const manifest = JSON.parse(await readFile(join(ROOT, 'lectures', 'content', 'decks.json'), 'utf8'));
  const out = resolve(ROOT, opt('--out', 'dist'));
  const p = await genLanding(manifest, out, opt('--base', ''));
  console.log(`Landing → ${p}`);
}
