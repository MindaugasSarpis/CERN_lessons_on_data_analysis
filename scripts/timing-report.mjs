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
// Lecture model (minutes):
//   structural slide (cover/intro/quote/section/statement/fact/center-bkg,
//   or no prose)                                            0.5
//   light content slide (≤40 prose words — figure/visual)   0.9 + words/120
//   normal content slide                                    1.3 + words/120
//   <MCQ>            (+3 each: think, vote, discuss)        +3.0
//   {monaco-run}     (+1.5 each: run, tweak, explain)       +1.5
//   <VideoPlayer>    (+1.5 each: clip plays out)            +1.5
//   ```mermaid       (+0.5 each: diagram walked through)    +0.5
//
// Target band: a 2h slot minus break/admin gives ~110 teaching minutes.
// The course prefers slightly too much over too little, so a deck should
// ESTIMATE in [105, 145]; < 105 is UNDER (must fix), > 145 is HEAVY
// (trim or mark a backup section).

import { readFile, readdir } from 'node:fs/promises';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const CONTENT = join(ROOT, 'lectures', 'content');
const SLIDES_DIR = join(CONTENT, 'slides');
const SEMINARS_DIR = join(ROOT, 'lectures', 'workbook', 'docs', 'seminars');

const BAND = { min: 105, max: 145 };
const SEMINAR_MIN = 120;

const STRUCTURAL_LAYOUTS = new Set([
  'cover', 'intro', 'quote', 'section', 'statement', 'fact', 'center-bkg', 'end',
]);

const args = process.argv.slice(2);
const CHECK = args.includes('--check');
const AS_JSON = args.includes('--json');

/** Split a Slidev markdown file into slides ({ frontmatter, content }). */
function splitSlides(src) {
  const lines = src.split('\n');
  // Segment the file at `---` lines that sit outside fenced code blocks.
  const segments = [];
  let cur = [];
  let inFence = false;
  for (const line of lines) {
    if (/^(```|~~~)/.test(line.trim())) inFence = !inFence;
    if (!inFence && line.trim() === '---') {
      segments.push(cur);
      cur = [];
    } else {
      cur.push(line);
    }
  }
  segments.push(cur);

  // A segment is YAML frontmatter when every non-blank line is a mapping
  // entry, list item, comment, or indented continuation.
  const isYaml = (seg) => {
    const meaningful = seg.filter((l) => l.trim() !== '');
    if (meaningful.length === 0) return false;
    return meaningful.every(
      (l) => /^[A-Za-z_][\w-]*\s*:/.test(l) || /^\s+\S/.test(l) || /^\s*(-\s|#)/.test(l),
    );
  };

  // Walk segments: YAML segment -> frontmatter of the *next* segment.
  const slides = [];
  let i = 0;
  // Leading empty segment before the first `---` (file starts with headmatter).
  if (segments.length > 0 && segments[0].every((l) => l.trim() === '')) i = 1;
  while (i < segments.length) {
    const seg = segments[i];
    if (isYaml(seg) && i + 1 < segments.length) {
      slides.push({ frontmatter: seg.join('\n'), content: segments[i + 1].join('\n') });
      i += 2;
    } else {
      slides.push({ frontmatter: '', content: seg.join('\n') });
      i += 1;
    }
  }
  return slides;
}

function countWords(text) {
  // Strip HTML tags and markdown syntax noise; keep prose and code tokens
  // (code on a slide is talked through, so it costs time too).
  const cleaned = text
    .replace(/<[^>]+>/g, ' ')
    .replace(/[#*_`|>\-=[\]():{}]/g, ' ');
  return cleaned.split(/\s+/).filter((w) => /\w/.test(w)).length;
}

function estimateDeck(src) {
  const slides = splitSlides(src);
  let minutes = 0;
  const counts = { slides: slides.length, structural: 0, content: 0, words: 0, mcq: 0, monaco: 0, video: 0, mermaid: 0 };
  for (const s of slides) {
    const layout = (s.frontmatter.match(/^layout\s*:\s*(\S+)/m) || [])[1];
    const words = countWords(s.content);
    counts.words += words;
    const structural = STRUCTURAL_LAYOUTS.has(layout) || words < 8;
    if (structural) {
      counts.structural += 1;
      minutes += 0.5;
    } else {
      counts.content += 1;
      minutes += (words <= 40 ? 0.9 : 1.3) + words / 120;
    }
    const mcq = (s.content.match(/<MCQ/g) || []).length;
    const monaco = (s.content.match(/\{monaco-run\}/g) || []).length;
    const video = (s.content.match(/<VideoPlayer/g) || []).length;
    const mermaid = (s.content.match(/```mermaid/g) || []).length;
    counts.mcq += mcq;
    counts.monaco += monaco;
    counts.video += video;
    counts.mermaid += mermaid;
    minutes += mcq * 3 + monaco * 1.5 + video * 1.5 + mermaid * 0.5;
  }
  return { minutes: Math.round(minutes), ...counts };
}

function bandFlag(minutes) {
  if (minutes < BAND.min) return 'UNDER';
  if (minutes > BAND.max) return 'HEAVY';
  return 'ok';
}

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
  for (const f of files) {
    const src = await readFile(join(SLIDES_DIR, f), 'utf8');
    const est = estimateDeck(src);
    rows.push({ file: f, ...est, flag: bandFlag(est.minutes) });
  }
  return rows;
}

async function reportSeminars() {
  const files = (await readdir(SEMINARS_DIR)).filter((f) => /^seminar_\d\d\.md$/.test(f)).sort();
  const rows = [];
  for (const f of files) {
    const src = await readFile(join(SEMINARS_DIR, f), 'utf8');
    const declared = Number((src.match(/\*\*~(\d+)\s*min\*\*/) || [])[1] || 0);
    const tasksSection = (src.split(/^## Tasks\s*$/m)[1] || '').split(/^## /m)[0];
    const stretchSection = (src.split(/^## Stretch goals\s*$/m)[1] || '').split(/^## /m)[0];
    const tasks = (tasksSection.match(/^\d+\.\s/gm) || []).length;
    const stretch = (stretchSection.match(/^-\s/gm) || []).length;
    rows.push({
      file: f,
      declared,
      tasks,
      stretch,
      flag: declared < SEMINAR_MIN ? 'UNDER' : 'ok',
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
      `  ${name}${String(r.slides).padStart(4)}${String(r.words).padStart(8)}${String(r.mcq).padStart(6)}${String(r.monaco).padStart(4)}${String(r.video).padStart(4)}${String(r.minutes).padStart(6)}   ${r.flag === 'ok' ? '' : r.flag}`,
    );
  }
  const total = lectures.reduce((a, r) => a + r.minutes, 0);
  console.log(`\n  total ≈ ${total} min across ${lectures.length} lectures (slot budget ${lectures.length * 120} min)\n`);

  console.log(`Seminars — declared duration (slot = ${SEMINAR_MIN} min)\n`);
  console.log('  brief          declared  tasks  stretch  flag');
  for (const r of seminars) {
    console.log(
      `  ${r.file.replace(/\.md$/, '').padEnd(16)}${String(r.declared).padStart(5)}${String(r.tasks).padStart(8)}${String(r.stretch).padStart(8)}   ${r.flag === 'ok' ? '' : r.flag}`,
    );
  }
}

const under = [...lectures, ...seminars].filter((r) => r.flag === 'UNDER');
if (CHECK && under.length > 0) {
  console.error(`\n${under.length} week(s) UNDER the band: ${under.map((r) => r.file).join(', ')}`);
  process.exit(1);
}
