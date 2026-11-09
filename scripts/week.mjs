#!/usr/bin/env node
/**
 * week.mjs — release day in one command.
 *
 *   pnpm week 8              # scripts/release.mjs 8 (lectures 01–08 live, the rest draft) and the
 *                            # "## This week" section of the workbook's home page
 *                            # (lectures/workbook/docs/index.md) for week 8; prints what changed and
 *                            # the next steps (qa, commit, push, verify)
 *   pnpm week 8 --dry-run    # the same, printed only: nothing is written
 *   pnpm week 8 --verify     # after the push: wait for the qa.yml run of HEAD (gh run watch), then
 *                            # expect HTTP 200 from the deck, its lecture page and its seminar page
 *   pnpm week 8 --verify --dry-run   # print the commands and the URLs only
 *
 * Week N is Lecture N, on the 2026 Tuesday below. The section is made from decks.json (the
 * lecture's number and title) and the seminar page's first heading (the deck's `seminar`, else N;
 * week 1 has none). The text after a link is kept when the row already links the same page, so a
 * summary written by hand survives a rerun; a new seminar row takes the page's "Today's question".
 */
import { readFile, writeFile } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { spawnSync } from 'node:child_process';
import { join, dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const CONTENT = join(ROOT, 'lectures', 'content');
const DOCS = join(ROOT, 'lectures', 'workbook', 'docs');
const INDEX = join(DOCS, 'index.md');

// The twelve Tuesdays of 2026, weeks 1–12
// (docs/superpowers/specs/2026-11-09-weeks-8-12-ideas-and-tools-design.md, section 4).
const TUESDAYS = ['8 September', '29 September', '6 October', '13 October', '20 October', '27 October',
  '10 November', '17 November', '1 December', '8 December', '15 December', '22 December'];

const argv = process.argv.slice(2);
const DRY = argv.includes('--dry-run');
const VERIFY = argv.includes('--verify');
const N = Number(argv.find((a) => /^\d+$/.test(a)));
if (!Number.isInteger(N) || N < 1 || N > TUESDAYS.length) {
  console.error(`usage: pnpm week <1–${TUESDAYS.length}> [--dry-run] [--verify]`);
  process.exit(2);
}
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const say = (s = '') => console.log(s);

const manifest = JSON.parse(await readFile(join(CONTENT, 'decks.json'), 'utf8'));
const NN = String(N).padStart(2, '0');
const deck = manifest.decks.find((d) => d.slug.startsWith(`${NN}-`));
if (!deck) { console.error(`decks.json has no deck ${NN}-…`); process.exit(2); }
const semNo = deck.seminar === null ? null : (deck.seminar ?? N);
const SS = semNo === null ? null : String(semNo).padStart(2, '0');
const lecturePage = `lectures/lecture_${N}.md`;
const seminarPage = SS && `seminars/seminar_${SS}.md`;
const site = manifest.site.url.replace(/\/$/, '');
const urls = [
  `${site}/${deck.slug}/`,
  `${site}/workbook/lectures/lecture_${N}/`,
  ...(SS ? [`${site}/workbook/seminars/seminar_${SS}/`] : []),
];

if (VERIFY) process.exit(await verify());

// 1. The release: lectures 01–N live, the rest draft (the rule of scripts/release.mjs).
const plan = manifest.decks
  .map((d) => ({ d, n: Number((d.slug.match(/^(\d{2})-/) || [])[1]) }))
  .filter(({ n }) => Number.isFinite(n))
  .map(({ d, n }) => ({ slug: d.slug, from: Boolean(d.draft), to: n > N }));
const flips = plan.filter((p) => p.from !== p.to);
const state = (draft) => (draft ? 'draft' : 'live');
say(`Week ${N}, ${TUESDAYS[N - 1]}: Lecture ${NN} ${deck.title}${SS ? `, Seminar ${Number(SS)}` : ''}`);
if (DRY) say(`\n(dry run: nothing is written)\nwould run: node scripts/release.mjs ${N}`);
else {
  say(`\n▶ node scripts/release.mjs ${N}`);
  const r = spawnSync('node', [join(ROOT, 'scripts', 'release.mjs'), String(N)], { cwd: ROOT, stdio: 'inherit' });
  if (r.status !== 0) { console.error('✗ release.mjs failed'); process.exit(1); }
}
say(`\ndecks.json: ${flips.length ? flips.map((p) => `${p.slug} ${state(p.from)} → ${state(p.to)}`).join(', ') : 'no draft flag changes'}`);

// 2. "## This week" on the workbook's home page.
if (!existsSync(join(DOCS, lecturePage))) {
  console.error(`✗ ${lecturePage} does not exist in the workbook: write it first (mkdocs --strict fails on a link to a missing page)`);
  process.exit(1);
}
const text = await readFile(INDEX, 'utf8');
const { start, end } = locate(text);
const oldSection = text.slice(start, end);
const kept = keptTexts(oldSection);
const cell = (s) => s.replace(/\|/g, '\\|');
const rows = [`| Lecture | [${cell(`${NN} ${deck.title}`)}](${lecturePage})${kept.get(lecturePage) ?? ''} |`];
if (seminarPage) {
  if (!existsSync(join(DOCS, seminarPage))) say(`⚠ ${seminarPage} does not exist: no seminar row`);
  else {
    const src = await readFile(join(DOCS, seminarPage), 'utf8');
    const heading = (src.match(/^# (.+)$/m) || [])[1]?.replace(/\s*\{[^}]*\}\s*$/, '').trim() || `Seminar ${Number(SS)}`;
    const q = question(src);
    rows.push(`| Seminar | [${cell(heading)}](${seminarPage})${kept.get(seminarPage) ?? (q ? `: ${cell(q)}` : '')} |`);
  }
}
const newSection = [`## This week: ${TUESDAYS[N - 1]}`, '', '| | Page |', '|--|--|', ...rows, '', ''].join('\n');
if (newSection === oldSection) say('index.md: "This week" unchanged');
else {
  say('\nindex.md, "This week":');
  const o = oldSection.trimEnd().split('\n');
  const n = newSection.trimEnd().split('\n');
  for (const l of o) if (!n.includes(l)) say(`  - ${l}`);
  for (const l of n) if (!o.includes(l)) say(`  + ${l}`);
  if (!DRY) await writeFile(INDEX, text.slice(0, start) + newSection + text.slice(end), 'utf8');
}
if (!kept.has(lecturePage)) say('  (the lecture row has no summary: write one after its link by hand if you like; a rerun keeps it)');

// 3. What next.
say(`
Next:
  pnpm qa --only ${deck.slug}
  pnpm timing:check
  git add lectures/content/decks.json lectures/workbook/docs/index.md
  git commit -m "Week ${N}: Lecture ${N}${SS ? ` and Seminar ${Number(SS)}` : ''} released"
  ${'git push origin main'.padEnd(24)}# qa.yml gates, builds and deploys (~8 min)
  ${`pnpm week ${N} --verify`.padEnd(24)}# waits for that run, then expects 200 from the pages
A draft mid-rework on main that fails a gate stops every deploy: then ship from a
worktree of origin/main (CLAUDE.md, Deployment).`);

/** Start and end of the "## This week:" section (up to the next "## "), or where it goes. */
function locate(t) {
  const s = t.search(/^## This week:/m);
  if (s === -1) {
    const h = t.search(/^## /m);
    return h === -1 ? { start: t.length, end: t.length } : { start: h, end: h };
  }
  const next = t.slice(s + 1).search(/^## /m);
  return { start: s, end: next === -1 ? t.length : s + 1 + next };
}

/** {page → the text after its link} of the rows in the current section. */
function keptTexts(section) {
  const out = new Map();
  for (const line of section.split('\n')) {
    const m = line.match(/^\|\s*(?:Lecture|Seminar)\s*\|\s*\[[^\]]*\]\(([^)#\s]+)[^)]*\)(.*?)\s*\|\s*$/);
    if (m) out.set(m[1], m[2]);
  }
  return out;
}

/** The seminar page's "**Today's question:** …" paragraph, on one line. */
function question(src) {
  const m = src.match(/^\*\*Today[’']s question:\*\*\s*([\s\S]*?)(?:\n\s*\n|$)/m);
  return m ? m[1].replace(/\s+/g, ' ').trim() : null;
}

/** After the push: the qa.yml run of HEAD green, then 200 from every page. */
async function verify() {
  const sha = spawnSync('git', ['rev-parse', 'HEAD'], { cwd: ROOT, encoding: 'utf8' }).stdout.trim();
  const short = sha.slice(0, 7);
  const list = ['run', 'list', '--workflow', 'qa.yml', '--commit', sha,
    '--json', 'databaseId,status,conclusion,event,headBranch,url', '--limit', '20'];
  if (DRY) {
    say(`--verify, dry run: would
  1. find the qa.yml run of HEAD (${short}) on main:
       gh ${list.join(' ')}
  2. wait for it to end, green:
       gh run watch <run id> --exit-status --interval 15
  3. expect HTTP 200 from (each tried up to 6 times, 20 s apart):
${urls.map((u) => `       ${u}`).join('\n')}`);
    return 0;
  }
  const branches = spawnSync('git', ['branch', '-r', '--contains', sha], { cwd: ROOT, encoding: 'utf8' }).stdout;
  if (!/\borigin\/main\b/.test(branches)) say(`⚠ HEAD ${short} is not on origin/main (only a push to main deploys)`);
  let run = null;
  for (let i = 0; i < 24 && !run; i++) {
    const r = spawnSync('gh', list, { cwd: ROOT, encoding: 'utf8' });
    if (r.status !== 0) { console.error(`✗ gh run list failed:\n${r.stderr}`); return 1; }
    run = JSON.parse(r.stdout || '[]').find((x) => x.headBranch === 'main' && x.event !== 'pull_request') || null;
    if (!run) { if (i === 0) say(`waiting for the qa.yml run of ${short} on main …`); await sleep(10_000); }
  }
  if (!run) { console.error(`✗ no qa.yml run of ${short} on main after 4 min: was it pushed to main?`); return 1; }
  say(`▶ ${run.url}`);
  const w = spawnSync('gh', ['run', 'watch', String(run.databaseId), '--exit-status', '--interval', '15'], { cwd: ROOT, stdio: 'inherit' });
  if (w.status !== 0) { console.error('✗ the qa.yml run is not green: nothing was deployed (the previous site stays up)'); return 1; }
  say('\nPages:');
  let ok = true;
  for (const url of urls) {
    let code = 0;
    for (let i = 0; i < 6; i++) {
      // ?v=<sha> asks the Pages CDN for a fresh copy
      const r = spawnSync('curl', ['-sS', '-o', '/dev/null', '-w', '%{http_code}', '--max-time', '30', `${url}?v=${short}`], { encoding: 'utf8' });
      code = Number(r.stdout.trim()) || 0;
      if (code === 200) break;
      if (i < 5) await sleep(20_000);
    }
    say(`  ${code === 200 ? '✓' : '✗'} ${code} ${url}`);
    if (code !== 200) ok = false;
  }
  if (!ok) { console.error('\n✗ not every page answers 200: not deployed yet'); return 1; }
  say(`\n✓ deployed: week ${N} (${TUESDAYS[N - 1]}), Lecture ${NN} ${deck.title}, is live`);
  return 0;
}
