#!/usr/bin/env node
// Timing report: estimate delivery minutes for every lecture deck and check
// every seminar brief against the 2-hour session slot (16 weeks, 2h lecture
// + 2h seminar per week).
//
// The model is a heuristic — it exists so the course stays *measurably*
// balanced, the same way `pnpm qa` keeps slides measurably non-overflowing.
// Model and target band are documented in
// docs/superpowers/specs/2026-07-06-course-timing-rebalance-design.md
//
// Usage:
//   node scripts/timing-report.mjs            # report all weeks
//   node scripts/timing-report.mjs --check    # exit 1 if any week is UNDER
//   node scripts/timing-report.mjs --json     # machine-readable output
//
// Lecture model (minutes; the code is scripts/timing-model.mjs):
//   structural slide (cover/intro/quote/section/statement/fact/center-bkg,
//   or no prose)                                            0.5
//   light content slide (≤40 prose words — figure/visual)   0.9 + words/120
//   normal content slide                                    1.3 + words/120
//   <MCQ>            (+3 each: think, vote, discuss)        +3.0
//   {monaco-run}     (+1.5 each: run, tweak, explain)       +1.5
//   <VideoPlayer>    (+1.5 each: clip plays out)            +1.5
//   ```mermaid       (+0.5 each: diagram walked through)    +0.5
//   self-check       (the section slide `# Check **Yourself**` and every
//   slide after it: quizzes for after the lecture)          0
//   for the curious  (the section slide `# For the **Curious**` and every
//   slide after it: the inner workings, shown only if time
//   is left; lecturer, 21 Oct 2026)                         0
//
// Target band: a 2h slot minus break/admin gives ~110 teaching minutes.
// The course prefers slightly too much over too little, so a deck should
// ESTIMATE in [105, 145]; < 105 is UNDER (must fix), > 145 is HEAVY
// (trim or mark a backup section).
//
// A week that is mostly hands-on can move time from the lecture to the
// seminar: `"split": {"lecture": 60, "seminar": 180}` on its deck in
// decks.json (Lecture 05, Oct 2026). The deck's band is then scaled to its
// minutes (60 → 53–73) and its seminar must declare at least `seminar`.

import { readFile, readdir } from 'node:fs/promises';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { estimateDeck } from './timing-model.mjs';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const CONTENT = join(ROOT, 'lectures', 'content');
const SLIDES_DIR = join(CONTENT, 'slides');
const SEMINARS_DIR = join(ROOT, 'lectures', 'workbook', 'docs', 'seminars');

const BAND = { min: 105, max: 145 };
const SEMINAR_MIN = 120;

const args = process.argv.slice(2);
const CHECK = args.includes('--check');
const AS_JSON = args.includes('--json');

const SLOT = 120;

function bandOf(split) {
  if (!split) return BAND;
  return { min: Math.round((BAND.min * split.lecture) / SLOT), max: Math.round((BAND.max * split.lecture) / SLOT) };
}

function bandFlag(minutes, band = BAND) {
  if (minutes < band.min) return 'UNDER';
  if (minutes > band.max) return 'HEAVY';
  return 'ok';
}

// Seminar number → the minutes its week gives it (default SEMINAR_MIN).
const seminarMinutes = new Map();

async function reportLectures() {
  // Drive from the deck manifest, not the directory: a slide file that was
  // removed from decks.json (topic dropped) must not keep gating the course.
  const manifest = JSON.parse(await readFile(join(CONTENT, 'decks.json'), 'utf8'));
  const files = manifest.decks.flatMap((d) => d.srcs);
  const onDisk = (await readdir(SLIDES_DIR)).filter((f) => /^\d\d_.*\.md$/.test(f));
  const stray = onDisk.filter((f) => !files.includes(f));
  if (stray.length) {
    console.error(`note: slide file(s) not in decks.json, ignored: ${stray.join(', ')}`);
  }
  const rows = [];
  for (const d of manifest.decks) {
    const band = bandOf(d.split);
    if (d.split) seminarMinutes.set(d.seminar ?? Number(d.slug.slice(0, 2)), d.split.seminar);
    for (const f of d.srcs) {
      const src = await readFile(join(SLIDES_DIR, f), 'utf8');
      const est = estimateDeck(src);
      rows.push({ file: f, ...est, band, flag: bandFlag(est.minutes, band) });
    }
  }
  return rows;
}

async function reportSeminars() {
  const files = (await readdir(SEMINARS_DIR)).filter((f) => /^seminar_\d\d\.md$/.test(f)).sort();
  const rows = [];
  for (const f of files) {
    const src = await readFile(join(SEMINARS_DIR, f), 'utf8');
    // The length is an HTML comment near the top (`<!-- ~120 min ... -->`), kept
    // out of the rendered page since 18 Oct 2026; the older bold form still counts.
    const declared = Number((src.match(/<!--\s*~(\d+)\s*min/) || src.match(/\*\*~(\d+)\s*min\*\*/) || [])[1] || 0);
    const tasksSection = (src.split(/^## Tasks\s*$/m)[1] || '').split(/^## /m)[0];
    const stretchSection = (src.split(/^## Stretch goals\s*$/m)[1] || '').split(/^## /m)[0];
    const tasks = (tasksSection.match(/^\d+\.\s/gm) || []).length;
    const stretch = (stretchSection.match(/^-\s/gm) || []).length;
    const slot = seminarMinutes.get(Number(f.match(/\d+/)[0])) ?? SEMINAR_MIN;
    rows.push({
      file: f,
      declared,
      slot,
      tasks,
      stretch,
      flag: declared < slot ? 'UNDER' : 'ok',
    });
  }
  return rows;
}

const lectures = await reportLectures();
const seminars = await reportSeminars();

if (AS_JSON) {
  console.log(JSON.stringify({ band: BAND, lectures, seminars }, null, 2));
} else {
  console.log(`Lectures — estimated delivery minutes (target band ${BAND.min}–${BAND.max} for a 2h slot)\n`);
  console.log('  deck                                    slides  words   mcq mon vid  est   flag');
  for (const r of lectures) {
    const name = r.file.replace(/\.md$/, '').padEnd(40);
    console.log(
      `  ${name}${String(r.slides).padStart(4)}${String(r.words).padStart(8)}${String(r.mcq).padStart(6)}${String(r.monaco).padStart(4)}${String(r.video).padStart(4)}${String(r.minutes).padStart(6)}   ${r.flag === 'ok' ? '' : r.flag}${r.band === BAND ? '' : ` (band ${r.band.min}–${r.band.max})`}`,
    );
  }
  const total = lectures.reduce((a, r) => a + r.minutes, 0);
  console.log(`\n  total ≈ ${total} min across ${lectures.length} lectures (slot budget ${lectures.length * 120} min)\n`);

  console.log(`Seminars — declared duration (slot = ${SEMINAR_MIN} min)\n`);
  console.log('  brief          declared  tasks  stretch  flag');
  for (const r of seminars) {
    console.log(
      `  ${r.file.replace(/\.md$/, '').padEnd(16)}${String(r.declared).padStart(5)}${String(r.tasks).padStart(8)}${String(r.stretch).padStart(8)}   ${r.flag === 'ok' ? '' : r.flag}${r.slot === SEMINAR_MIN ? '' : ` (slot ${r.slot})`}`,
    );
  }
}

const under = [...lectures, ...seminars].filter((r) => r.flag === 'UNDER');
if (CHECK && under.length > 0) {
  console.error(`\n${under.length} week(s) UNDER the band: ${under.map((r) => r.file).join(', ')}`);
  process.exit(1);
}
