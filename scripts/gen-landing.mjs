#!/usr/bin/env node
/**
 * gen-landing.mjs — emit a self-contained course-home landing page at
 * <out>/index.html from decks.json. No external assets (GitHub-Pages / CSP
 * safe): all CSS is inlined. Decks are grouped by block; each links to its
 * own deck at `<prefix>/<slug>/`. Block E is marked Optional.
 *
 * Exported as genLanding() for build-all.mjs; also runnable standalone:
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

  const blockSections = [...byBlock.entries()]
    .filter(([, decks]) => decks.length)
    .map(([key, decks]) => {
      const optional = key === 'E';
      const cards = decks.map((d) => `
        <a class="deck${d.optional ? ' opt' : ''}" href="${base}/${d.slug}/">
          <span class="num">${esc(d.slug.split('-')[0])}</span>
          <span class="dt">${esc(d.title)}</span>
          ${d.optional ? '<span class="tag">optional</span>' : ''}
        </a>`).join('');
      return `
      <section class="block">
        <h2>Block ${esc(key)} — ${esc(manifest.blocks[key])}${optional ? ' <span class="tag">drop if short on time</span>' : ''}</h2>
        <div class="grid">${cards}</div>
      </section>`;
    }).join('');

  const html = `<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(manifest.course)}</title>
<style>
  :root { color-scheme: dark; }
  * { box-sizing: border-box; }
  body { margin: 0; font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
         background: #060911; color: #e6edf6; line-height: 1.5;
         background-image: radial-gradient(1200px 600px at 80% -10%, rgba(56,189,248,.10), transparent 60%),
                           radial-gradient(900px 500px at -10% 110%, rgba(129,140,248,.10), transparent 60%); }
  .wrap { max-width: 1080px; margin: 0 auto; padding: clamp(1.5rem, 4vw, 4rem) clamp(1rem, 4vw, 2rem) 5rem; }
  header .who { color: #93a4b8; font-size: .95rem; letter-spacing: .02em; }
  h1 { font-size: clamp(1.7rem, 5vw, 2.8rem); line-height: 1.1; margin: .3rem 0 .2rem;
       background: linear-gradient(100deg, #7dd3fc, #a5b4fc 60%, #e6edf6);
       -webkit-background-clip: text; background-clip: text; color: transparent; font-weight: 800; }
  .sub { color: #93a4b8; margin: 0 0 2.2rem; max-width: 55ch; }
  .block { margin: 2.2rem 0; }
  .block h2 { font-size: 1.05rem; font-weight: 700; color: #cdd9e8; margin: 0 0 .9rem;
              border-left: 3px solid; border-image: linear-gradient(#38bdf8, #818cf8) 1; padding-left: .7rem; }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: .8rem; }
  a.deck { display: flex; align-items: center; gap: .75rem; text-decoration: none; color: inherit;
           background: rgba(18, 26, 40, .72); border: 1px solid rgba(148,163,184,.16); border-radius: 14px;
           padding: .9rem 1rem; transition: transform .15s ease, border-color .15s ease, background .15s ease; }
  a.deck:hover { transform: translateY(-2px); border-color: rgba(125,211,252,.55); background: rgba(24, 34, 52, .9); }
  a.deck.opt { opacity: .82; }
  .deck.soon { opacity: .5; cursor: default; }
  .deck.soon .num { color: #6b7c92; margin-right: .55rem; }
  .num { font-variant-numeric: tabular-nums; font-weight: 800; font-size: 1.15rem;
         min-width: 2ch; color: #7dd3fc; }
  .dt { font-weight: 600; flex: 1; }
  .tag { font-size: .68rem; font-weight: 700; text-transform: uppercase; letter-spacing: .06em;
         color: #fcd34d; background: rgba(252,211,77,.12); border-radius: 999px; padding: .12rem .5rem; }
  .block h2 .tag { color: #93a4b8; background: rgba(148,163,184,.12); font-size: .6rem; vertical-align: middle; }
  footer { margin-top: 3rem; color: #6b7c92; font-size: .85rem; border-top: 1px solid rgba(148,163,184,.12); padding-top: 1.2rem; }
  .seminars { color: #93a4b8; }
</style>
</head><body>
  <div class="wrap">
    <header>
      <div class="who">${esc(manifest.presenter)}</div>
      <h1>${esc(manifest.course)}</h1>
      <p class="sub">A practice-first course: tool-agnostic thinking, reproducible analysis, automation, and efficient work with data and files. Pick a lecture below — each opens on its own so it loads fast, even on a phone.</p>
    </header>
    ${blockSections}
    ${(manifest.upcoming && manifest.upcoming.length) ? `
      <section class="block">
        <h2>Coming soon <span class="tag">in preparation</span></h2>
        <div class="grid">${manifest.upcoming.map((u) => `
          <span class="deck opt soon"><span class="num">${String(u.n).padStart(2, '0')}</span><span class="dt">${esc(u.title)}</span></span>`).join('')}</div>
      </section>` : ''}
    <footer>
      <p class="seminars">Each lecture has a paired hands-on seminar in the workbook. Blocks D–E are the optional tail if the term runs short.</p>
    </footer>
  </div>
</body></html>`;

  await mkdir(outDir, { recursive: true });
  await writeFile(join(outDir, 'index.html'), html, 'utf8');
  await writeFile(join(outDir, '404.html'), gen404(manifest, base), 'utf8');
  return join(outDir, 'index.html');
}

// Root-level 404.html — the only 404 page GitHub Pages honors (per-deck copies
// in subdirectories are ignored). Decks use hash routing, but links shared
// before the switch look like `<base>/<slug>/5`; rewrite those to
// `<base>/<slug>/#/5` so they keep working. Anything else gets a link home.
function gen404(manifest, base) {
  const slugs = manifest.decks.map((d) => d.slug);
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
         background: #060911; color: #e6edf6; }
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
