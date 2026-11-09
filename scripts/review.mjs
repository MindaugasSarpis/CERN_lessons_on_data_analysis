#!/usr/bin/env node
/**
 * review.mjs — one command for a deck's review loop.
 *
 *   pnpm review <deck> [--since prev|<dir>|<git-ref>] [--from N --to M]
 *                      [--threshold 0.001] [--workers N] [--tolerance PX] [--out <dir>]
 *
 * <deck> is a number, a slug or a piece of one, as for `pnpm dev`. Steps:
 *   1. build the deck at base '/' into .qa-dist/<slug> (build-all.mjs --flat-base
 *      --only). build-all empties .qa-dist first, also other decks' builds there:
 *      `--out .qa-dist-<name>` builds into a folder of your own instead (but
 *      measure-figures.mjs reads .qa-dist);
 *   2. move the screenshots of the run before to .qa-shots/<slug>/prev/;
 *   3. overflow gate + new screenshots: check-slides.mjs --shots .qa-shots/<slug>;
 *   4. contact sheets, four slides per PNG: contact-sheets.py → .qa-shots/<slug>/sheets/;
 *   5. the deck's timing line (timing-report.mjs --json);
 *   6. with --since: shots-diff.py compares every new screenshot with the older
 *      one: side by side in .qa-shots/<slug>/diff/, and contact sheets of the
 *      changed slides only in .qa-shots/<slug>/changed/sheets/. Older is
 *        prev       the screenshots of the run before (step 2)
 *        <dir>      any folder of slide-NNN.png
 *        <git-ref>  the deck as committed at that ref (HEAD, origin/main, a sha):
 *                   exported with `git archive`, built with this checkout's
 *                   node_modules (Slidev's binary, never pnpm: see shootRef),
 *                   shot once and kept in .qa-shots/<slug>/at-<sha>/
 *   --from N --to M  limit the sheets and the comparison to slides N–M (the
 *                    overflow gate still covers every slide).
 * Then a short summary. Exit 1 if the build fails or a slide overflows or does
 * not render. Python steps need Pillow: $REVIEW_PYTHON, else the `figures` or
 * `outreach_talks` micromamba env, else python3. Heavy (Slidev build +
 * Playwright): on a shared machine run it under the machine's render lock.
 */
import { readFile, readdir, mkdir, mkdtemp, rm, rename, copyFile, symlink, unlink, writeFile } from 'node:fs/promises';
import { existsSync, statSync } from 'node:fs';
import { spawn, spawnSync } from 'node:child_process';
import { join, dirname, resolve, relative } from 'node:path';
import { fileURLToPath } from 'node:url';
import { homedir, tmpdir } from 'node:os';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const CONTENT = join(ROOT, 'lectures', 'content');
const rel = (p) => { const r = relative(ROOT, p); return r.startsWith('..') ? p : r || '.'; };

const argv = process.argv.slice(2);
const has = (n) => argv.includes(n);
const opt = (n, d) => { const i = argv.indexOf(n); return i > -1 && argv[i + 1] && !argv[i + 1].startsWith('--') ? argv[i + 1] : d; };
const sel = argv[0] && !argv[0].startsWith('-') ? argv[0] : null;
const FROM = opt('--from', null);
const TO = opt('--to', null);
const OUT = opt('--out', '.qa-dist');
const RANGE = [...(FROM ? ['--from', FROM] : []), ...(TO ? ['--to', TO] : [])];

const manifest = JSON.parse(await readFile(join(CONTENT, 'decks.json'), 'utf8'));
if (!sel) {
  console.error('usage: pnpm review <deck> [--since prev|<dir>|<git-ref>] [--from N --to M]\n\nDecks:');
  for (const d of manifest.decks) console.error(`  ${d.slug}`);
  process.exit(2);
}
// The same lookup as scripts/dev.mjs: exact slug → number → piece of slug → piece of title.
const bynum = (s) => manifest.decks.find((d) => d.slug.split('-')[0] === s.padStart(2, '0'));
const deck =
  manifest.decks.find((d) => d.slug === sel) ||
  (/^\d{1,2}$/.test(sel) ? bynum(sel) : null) ||
  manifest.decks.find((d) => d.slug.includes(sel.toLowerCase())) ||
  manifest.decks.find((d) => d.title.toLowerCase().includes(sel.toLowerCase()));
if (!deck) { console.error(`No deck matches "${sel}" (decks.json).`); process.exit(2); }
const slug = deck.slug;
const SHOTS = join(ROOT, '.qa-shots', slug);
const PREV = join(SHOTS, 'prev');

/** Run a command; stdio inherited, or stdout captured (and echoed unless quiet). */
function run(cmd, args, { capture = false, quiet = false, cwd = ROOT, env = process.env } = {}) {
  return new Promise((done) => {
    const p = spawn(cmd, args, { cwd, env, stdio: ['inherit', capture ? 'pipe' : 'inherit', 'inherit'] });
    let out = '';
    if (capture) p.stdout.on('data', (b) => { out += b; if (!quiet) process.stdout.write(b); });
    p.on('error', (e) => done({ code: -1, out: String(e) }));
    p.on('close', (code) => done({ code, out }));
  });
}
const step = (s) => console.log(`\n▶ review ${slug}: ${s}`);
const shotsIn = async (dir) => (existsSync(dir) ? (await readdir(dir)).filter((f) => /^slide-\d+\.png$/.test(f)).sort() : []);

function findPython() {
  const cands = [
    process.env.REVIEW_PYTHON,
    join(homedir(), 'micromamba', 'envs', 'figures', 'bin', 'python'),
    join(homedir(), 'micromamba', 'envs', 'outreach_talks', 'bin', 'python'),
    'python3', 'python',
  ].filter(Boolean);
  for (const py of cands) {
    if (py.includes('/') && !existsSync(py)) continue;
    if (spawnSync(py, ['-c', 'import PIL'], { stdio: 'ignore' }).status === 0) return py;
  }
  return null;
}

// --since: decide what to compare with before spending minutes on a build.
let since = null;
if (has('--since')) {
  const v = opt('--since', 'prev');
  const asDir = resolve(process.env.INIT_CWD || process.cwd(), v); // INIT_CWD: where `pnpm review` was typed
  if (v === 'prev' || v === 'last' || asDir === PREV) since = { kind: 'prev', dir: PREV, label: 'the run before' };
  else if (existsSync(asDir) && statSync(asDir).isDirectory()) {
    if (asDir === SHOTS) { console.error(`--since ${v}: that is where the new screenshots go; copy it elsewhere, or use --since prev.`); process.exit(2); }
    since = { kind: 'dir', dir: asDir, label: rel(asDir) };
  } else {
    const r = spawnSync('git', ['rev-parse', '--verify', '--quiet', `${v}^{commit}`], { cwd: ROOT, encoding: 'utf8' });
    if (r.status !== 0) { console.error(`--since ${v}: not "prev", not a folder, not a git ref.`); process.exit(2); }
    const sha = r.stdout.trim();
    since = { kind: 'ref', ref: v, sha, dir: join(SHOTS, `at-${sha.slice(0, 10)}`), label: `${v} (${sha.slice(0, 10)})` };
  }
}

// 1. Build.
step('build');
const build = await run('node', [join(ROOT, 'scripts', 'build-all.mjs'), '--flat-base', '--out', OUT, '--only', slug]);
if (build.code !== 0) { console.error(`\n✗ review ${slug}: the build failed (screenshots left as they were).`); process.exit(1); }

// 2. Keep the screenshots of the run before; start the folder afresh.
const before = await shotsIn(SHOTS);
if (before.length) {
  await rm(PREV, { recursive: true, force: true });
  await mkdir(PREV, { recursive: true });
  for (const f of before) await rename(join(SHOTS, f), join(PREV, f));
} else if (since?.kind === 'prev') {
  since.error = `no screenshots of a run before in ${rel(SHOTS)}/ (run once without --since first)`;
}
for (const d of ['sheets', 'changed', 'diff']) await rm(join(SHOTS, d), { recursive: true, force: true });
await mkdir(SHOTS, { recursive: true });

// 3. Overflow gate + screenshots.
step('overflow check + screenshots');
const pass = [...(opt('--workers') ? ['--workers', opt('--workers')] : []), ...(opt('--tolerance') ? ['--tolerance', opt('--tolerance')] : [])];
const check = await run('node', [join(ROOT, 'scripts', 'check-slides.mjs'), resolve(ROOT, OUT, slug), '--shots', SHOTS, ...pass], { capture: true });
const total = Number((check.out.match(/Checking \d+\/(\d+) slides/) || [])[1] || 0);
const over = (check.out.match(/Offending slides: ([\d, ]+)/) || [])[1];
const unrendered = (check.out.match(/NOT checked: ([\d, ]+)/) || [])[1];
const overflowLine = check.code === 0
  ? `✓ all ${total} slides fit the frame`
  : [over && `✗ overflow on slide(s) ${over.trim()}`, unrendered && `⚠ not rendered: ${unrendered.trim()}`]
    .filter(Boolean).join(' · ') || `✗ check-slides failed (exit ${check.code})`;

// --since <git-ref>: the committed deck, built from a `git archive` export and
// shot once (kept: a commit does not change).
if (since?.kind === 'ref' && !existsSync(join(since.dir, '.complete'))) {
  step(`the deck at ${since.label}`);
  since.error = await shootRef(since);
}

// 4. Contact sheets.
const py = findPython();
let sheetsLine = '⚠ no Python with Pillow (set $REVIEW_PYTHON): no contact sheets, no comparison';
if (py) {
  step('contact sheets');
  const r = await run(py, [join(ROOT, 'scripts', 'contact-sheets.py'), slug, ...RANGE], { capture: true, quiet: true });
  const n = r.out.split('\n').filter((l) => l.trim().endsWith('.png')).length;
  sheetsLine = r.code === 0 ? `${rel(join(SHOTS, 'sheets'))}/ (${n} sheet${n === 1 ? '' : 's'}${FROM || TO ? `, slides ${FROM ?? 1}–${TO ?? 'end'}` : ''})` : `⚠ contact-sheets.py failed (exit ${r.code})`;
}

// 5. Timing.
let timingLine = '⚠ timing-report.mjs failed';
const t = await run('node', [join(ROOT, 'scripts', 'timing-report.mjs'), '--json'], { capture: true, quiet: true });
try {
  const rep = JSON.parse(t.out);
  const parts = rep.lectures.filter((r) => deck.srcs.includes(r.file)).map((r) =>
    `${r.file.replace(/\.md$/, '')} ≈ ${r.minutes} min (band ${r.band.min}–${r.band.max}) ${r.flag}`);
  const sem = deck.seminar === null ? null : String(deck.seminar ?? Number(slug.slice(0, 2))).padStart(2, '0');
  const s = sem && rep.seminars.find((r) => r.file === `seminar_${sem}.md`);
  if (s) parts.push(`seminar_${sem} declares ${s.declared} min (slot ${s.slot}) ${s.flag}`);
  if (parts.length) timingLine = parts.join(' · ');
} catch { /* keep the warning */ }

// 6. What changed.
let changedLine = null;
let changedSheets = null;
if (since) {
  if (since.error) changedLine = `⚠ ${since.error}`;
  else if (!py) changedLine = '⚠ no Python with Pillow';
  else if (!(await shotsIn(since.dir)).length) changedLine = `⚠ nothing to compare: no screenshots in ${rel(since.dir)}/ (run once without --since first)`;
  else {
    step(`compare with ${since.label}`);
    const threshold = opt('--threshold', '0.001');
    const d = await run(py, [join(ROOT, 'scripts', 'shots-diff.py'), since.dir, SHOTS, '--json', '--threshold', threshold, '--out', join(SHOTS, 'diff'), ...RANGE], { capture: true, quiet: true });
    let res = null;
    try { res = JSON.parse(d.out); } catch { changedLine = `⚠ shots-diff.py failed (exit ${d.code})`; }
    if (res) {
      const pct = (s) => (s >= 0.01 ? `${(s * 100).toFixed(0)} %` : `${(s * 100).toFixed(1)} %`);
      const bits = [
        ...res.changed.map((c) => `${c.slide} (${pct(c.share)})`),
        ...res.added.map((n) => `${n} (new)`),
        ...res.removed.map((n) => `old ${n} (taken out)`),
      ];
      changedLine = bits.length || res.moved.length
        ? `${bits.length} of ${res.compared} vs ${since.label}: ${bits.join(', ') || 'none'}${res.moved.length ? ` · moved ${res.moved_runs}` : ''}`
        : `nothing vs ${since.label} (${res.compared} slides compared)`;
      // Contact sheets of the changed slides only: their new screenshots, copied
      // to .qa-shots/<slug>/changed/ for contact-sheets.py.
      const pick = [...res.changed.map((c) => c.slide), ...res.added];
      if (pick.length) {
        const dir = join(SHOTS, 'changed');
        await mkdir(dir, { recursive: true });
        for (const n of pick) {
          const f = `slide-${String(n).padStart(3, '0')}.png`;
          await copyFile(join(SHOTS, f), join(dir, f));
        }
        const r = await run(py, [join(ROOT, 'scripts', 'contact-sheets.py'), `${slug}/changed`], { capture: true, quiet: true });
        const n = r.out.split('\n').filter((l) => l.trim().endsWith('.png')).length;
        changedSheets = `${rel(join(dir, 'sheets'))}/ (${n}) · side by side: ${rel(join(SHOTS, 'diff'))}/ (${pick.length + res.removed.length})`;
      } else if (res.removed.length) changedSheets = `side by side: ${rel(join(SHOTS, 'diff'))}/ (${res.removed.length})`;
    }
  }
}

// Summary.
const pad = (s) => s.padEnd(9);
console.log(`\n━━ review ${slug} ━━`);
console.log(`${pad('overflow')}${overflowLine}`);
console.log(`${pad('timing')}${timingLine}`);
if (changedLine) console.log(`${pad('changed')}${changedLine}`);
console.log(`${pad('sheets')}${sheetsLine}`);
if (changedSheets) console.log(`${pad('')}changed only: ${changedSheets}`);
console.log(`${pad('')}screenshots ${rel(SHOTS)}/slide-NNN.png${before.length ? `; the run before in ${rel(PREV)}/` : ''}`);
process.exit(check.code === 0 ? 0 : 1);

/**
 * Build and screenshot the deck as committed at since.sha, into since.dir.
 * Returns an error message, or null.
 */
async function shootRef({ sha, ref, dir }) {
  const tmp = await mkdtemp(join(tmpdir(), `review-${slug}-`));
  try {
    const paths = ['lectures/content', 'lectures/workbook/docs/seminars', 'scripts', 'package.json']
      .filter((p) => spawnSync('git', ['cat-file', '-e', `${sha}:${p}`], { cwd: ROOT }).status === 0);
    const exported = await new Promise((done) => {
      const tar = spawn('tar', ['-x', '-C', tmp], { stdio: ['pipe', 'inherit', 'inherit'] });
      const ga = spawn('git', ['archive', '--format=tar', sha, '--', ...paths], { cwd: ROOT, stdio: ['ignore', 'pipe', 'inherit'] });
      ga.stdout.pipe(tar.stdin);
      // Wait for both: tar can close before git's exit is reported.
      const exit = (p) => new Promise((r) => { p.on('error', () => r(-1)); p.on('close', r); });
      Promise.all([exit(ga), exit(tar)]).then(([g, t]) => done(g === 0 && t === 0));
    });
    if (!exported) return `git archive of ${ref} failed`;
    const old = JSON.parse(await readFile(join(tmp, 'lectures', 'content', 'decks.json'), 'utf8'));
    if (!old.decks.some((d) => d.slug === slug)) return `${ref} has no deck ${slug} in decks.json (compare with a folder instead: --since <dir>)`;
    // The checkout's node_modules, linked read-only. Never run pnpm in the
    // export (its build-all.mjs calls `pnpm exec`): pnpm would find a project
    // without its lockfile and "install" through the link into the checkout's
    // own node_modules. So: the export's gen-entries.mjs, then Slidev's binary.
    await symlink(join(ROOT, 'node_modules'), join(tmp, 'node_modules'), 'dir');
    const gen = await run('node', [join(tmp, 'scripts', 'gen-entries.mjs')], { cwd: tmp, capture: true, quiet: true });
    if (gen.code !== 0) return `gen-entries.mjs fails at ${ref}`;
    const b = await run(join(ROOT, 'node_modules', '.bin', 'slidev'),
      ['build', join(tmp, 'lectures', 'content', `deck.${slug}.md`), '--out', join(tmp, '.qa-dist', slug), '--base', '/'],
      { cwd: tmp, capture: true, quiet: true, env: { ...process.env, NODE_OPTIONS: '--max-old-space-size=4096' } });
    if (b.code !== 0) return `the deck at ${ref} does not build`;
    await rm(dir, { recursive: true, force: true });
    // Its overflow does not matter here, only the screenshots.
    await run('node', [join(ROOT, 'scripts', 'check-slides.mjs'), join(tmp, '.qa-dist', slug), '--shots', dir], { capture: true, quiet: true });
    if (!(await shotsIn(dir)).length) return `no screenshots of the deck at ${ref}`;
    await writeFile(join(dir, '.complete'), `${sha}\n`);
    // Keep the three newest commits' screenshots of this deck, drop older ones.
    const kept = (await readdir(SHOTS)).filter((f) => /^at-[0-9a-f]+$/.test(f))
      .map((f) => ({ f, t: statSync(join(SHOTS, f)).mtimeMs })).sort((a, b) => b.t - a.t);
    for (const { f } of kept.slice(3)) await rm(join(SHOTS, f), { recursive: true, force: true });
    return null;
  } finally {
    await unlink(join(tmp, 'node_modules')).catch(() => {}); // the link only, before the folder goes
    await rm(tmp, { recursive: true, force: true });
  }
}
