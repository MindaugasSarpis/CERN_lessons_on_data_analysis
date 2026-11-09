// The lecture timing model: estimated delivery minutes of one lecture file.
// Used by scripts/timing-report.mjs (the report and the `pnpm timing:check`
// gate; its header lists the model and the target band) and by
// scripts/gen-entries.mjs (each deck's presenter countdown, `duration`).

// Title of the section slide that opens a deck's self-check quizzes.
const SELF_CHECK_TITLE = /^#\s+Check\s+\*\*Yourself\*\*\s*$/m;
// Title of the section slide that opens the optional inner workings, after
// the recap and before the quizzes: not part of the delivered lecture.
const CURIOUS_TITLE = /^#\s+For\s+the\s+\*\*Curious\*\*\s*$/m;

const STRUCTURAL_LAYOUTS = new Set([
  'cover', 'intro', 'quote', 'section', 'statement', 'fact', 'center-bkg', 'end',
]);

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

export function estimateDeck(src) {
  const slides = splitSlides(src);
  let minutes = 0;
  const counts = { slides: slides.length, structural: 0, content: 0, words: 0, mcq: 0, monaco: 0, video: 0, mermaid: 0, selfCheck: 0 };
  // A deck may end with a section for the curious (shown only if time is
  // left) and a self-check section (quiz slides for after the lecture).
  // Neither is part of the delivered lecture, so they cost no lecture time.
  let selfCheck = false;
  for (const s of slides) {
    const layout = (s.frontmatter.match(/^layout\s*:\s*(\S+)/m) || [])[1];
    if (layout === 'section' && (SELF_CHECK_TITLE.test(s.content) || CURIOUS_TITLE.test(s.content))) selfCheck = true;
    if (selfCheck) {
      counts.selfCheck += 1;
      counts.mcq += (s.content.match(/<MCQ/g) || []).length;
      continue;
    }
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
