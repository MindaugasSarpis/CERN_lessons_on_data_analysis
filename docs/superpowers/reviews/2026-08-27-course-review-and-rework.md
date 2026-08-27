# Course review & rework (L01–L16) — 2026-08-27

Eight per-deck reviews (source + every rendered slide) after the "running project"
was retired. Everything technical checked out: every MCQ key, every git/shell/Python
snippet traced, no broken images. What follows is what was **applied** and what was
**deferred** — the deferred items are mostly slide merges and section reorders that
change the deck's shape, so they are yours to steer.

## Applied in this pass

Course-wide
- Slidev upgraded 52.14.2 → 52.19.1 (memory router, opt-in PWA offline precaching,
  monaco `lines`/`lineNumbers` honoured, per-slide `codeCopy`, sub-directory base fixes).
  Two things broke and were fixed: a `$$` block glued to an opening `<div>` in L11
  ("Why Variance?") and a Monaco runner in L12 that grew 12px taller. All 16 decks pass
  `pnpm qa` on the new version.
- MCQ questions now render `code` spans (were literal backticks) — `components/MCQ.vue`.
- One-line `<div class="note-text">…</div>` cannot contain markdown (prints literal
  `*asterisks*`); fixed every instance in L01/L05/L07 with `<em>/<strong>/<code>`.
- Git conflict markers: the `{{'<<<<<<< HEAD'}}` trick renders literally — replaced
  with an HTML `<pre><code>` using entities (L06); CLAUDE.md + memory corrected.
- Task-list bullets: theme CSS drops the square bullet next to checkboxes.

L01 Orientation
- Old "one cumulative project" framing removed from slides 13, 21, 36, the week-5
  MCQ (its key was now false), the cover note; "blocks D–E droppable" → block E only.
- "Two Things You'll Build" + "Your Project — Your Call" moved up to follow
  "Project Details" so the correct model is heard before anything else.
- Ending rebuilt: icebreaker follows the cover, break sits before "Data in Your Life",
  deck now closes Golden Rule → MCQ → What You Need (setup = Seminar 1, folder name
  aligned to `analysis-project`).
- Table row "Events → numbers" now matches the seminar briefs.

L02 Introduction to CERN
- Closing promise fixed (next is *How Computers Work*, not the command line).
- "The dataset you'll use all course" / "running dataset" wording removed; Seminar 2
  tie-in now offers "or a dataset from your own field".
- FCC line reworded (feasibility study reported 2025; Council has not approved).
- **Please verify:** member states set to **24** (Estonia, 2024) — was "25 (as of 2026)".
- Hadrons wording on the detector slide; MCQ-1 vs slide-20 wording no longer contradict.

L03 How Computers Work
- Cover/`title` aligned to "How Computers Work"; quote rewritten to match content.
- "A file is a named sequence of bytes" now stated on the File Formats slide (magic
  numbers, `file`, `hexdump`) — it was an objective + MCQ answer never taught.
- Two's-complement MCQ uses a fresh pattern (1101 → −3); NumPy overflow example uses
  an array (the scalar form warns, contradicting "silently"); bit-depth slide no longer
  claims a file-size effect the mixed JPG/PNG images can't show; stale "Crash Course on
  Python" → Lecture 7; `len(s), len(b)` shows its result.

L04 Command Line & Files
- Objectives + Recap now cover scripting and wildcards (a 6-slide section had no
  objective). Four stale cross-refs fixed ("next slide", "the Command Line lesson",
  "the Computer Science lecture", date-first vs date-last recipe).
- Shown outputs made truthful: header line appears in `cut|sort|uniq` (+ `tail -n +2`
  tip), `uniq -c` printed vertically, `mkdir -p results` in `error_report.sh`, full path
  in the bonus command, useless `cat` removed. xkcd 1459 credited.

L05 Markdown & VS Code
- KaTeX wrapper leak in the Math "syntax" fence fixed (one-line `$$ … $$`).
- Section slide "VS Code: The Workshop" added at the half-way seam.
- Objective no longer promises pandoc/MkDocs; "Free & open-source" → "built on open
  source"; Settings Sync said once; regex date example shows the reorder; line-break
  MCQ distractor no longer a real CommonMark feature; Mac shortcut legend on the
  find/replace line; both Seminar-5 tie-ins reframed (seminar dataset; template for
  your own project).

L06 Version Control
- Conflict-marker slide fixed (see course-wide). Clipped `git remote add` line
  shortened. `git tag` teaser points to this deck's Tags section, not L04.
- Seminar-6 tie-in and notes now match `seminar_06.md` (conflict + undo practice;
  PR/pairing is the stretch). "Your seminar group" removed. Repeated `master` bullet
  dropped. `.gitignore` example trimmed to fit without scrolling. Playground slide
  says what to do; "Looking Ahead" names Lecture 14.

L07 Python Foundations
- **Functions gap closed**: new "Peek Ahead — Wrapping the Recipe in a Function"
  runner (Seminar 7 requires `def parse_line`, the deck never showed `def`).
- **Teach-before-use**: Control Flow section moved to directly after "Strings & Lists"
  (loops/ifs were used on ~8 slides before being taught).
- "More Built-in Types" card → **Type Conversion** (`int()`, `float()`, the `N/A`
  trap) — the skill Seminar 7 hinges on and the deck never stated.
- Stale forward refs ("file-handling section shortly", "docstrings soon") → L08;
  junk-line example now actually raises from `float()`; naming slide's MeV/GeV slip fixed.

L08 Python for Data
- **Missing exception pattern added**: "Try It — Skip a Bad Row, Count It"
  (`except (ValueError, IndexError)` with a counter) — the one thing Seminar 8 needs
  and L07 explicitly deferred here.
- Recap + notes de-cumulated. `io.py` → `loaders.py` (stdlib shadowing), `data/processed`
  in the flow line, `with` on the whole-tool script, `--window` removed from commands the
  script didn't accept, dead `min_avg` and wrong "Next up: NumPy" print fixed, Parquet
  ref → L13/L15, generic `meta.json`.

## Structural pass (all implemented in the same day)

The items below were first deferred, then implemented deck-by-deck by editing agents
(each gated on its own overflow check + `pnpm timing:check`). Kept here as the record of
what changed and why.

L01 (62 slides, 117 min)
1. Merge padded runs: Weekly Rhythm into Two Halves (drop 1); Learning Outcomes 1/2+2/2
   into one grid; "A Day in Data" ×4 → 2 grids; domain examples ×5 → 2–3 grids; drop the
   second reflection slide. ≈ −8 slides.
2. Deliverables listed three times (Project Details, Your Call, Finished Product) — keep
   one canonical list.
3. Move the automation MCQ next to the automation before/after pair.

L02 (60 slides, 111 min — 24 are film clips)
1. Trigger cascade told three times (17–19): merge to two and add the per-year
   arithmetic slide 18 promises.
2. Open-data tail (25–27) → one slide under a new "Beyond the Ring" section; SCOAP3 into
   Impact; careers/skills/day/why-you (56–59) → two slides.
3. Drop the "Today's Journey" agenda (duplicates objectives). Consider trimming 2–3
   cosmos clips.

L03 (76 slides, 105 min — bottom of band; don't cut without adding)
1. Re-section: Numbers → Text → new "Files & Formats" (file sizes, endianness, formats,
   bit depth) → Compression. Currently files/ints/floats are discussed under "Text Beyond
   ASCII" before Numbers.
2. Overflow taught three times (58/69/70) — fold 69 into 58. Four float run-up slides → 2.
3. Fill the emptiest pay-offs: SHA-256 one-bit-flip example, carries row on binary
   addition, framing sentence on "A Bit of Foresight". Move "Think Like a CPU" next to
   algorithms.

L04 (74 slides, 124 min)
1. Part 1 → Part 2 seam is six thin slides (45–48): delete Demo Challenge, make Part 2 a
   `layout: section`, delete the generic Pitfalls section slide, upgrade or delete the
   stale mid-deck Key Takeaways.
2. File Naming: four ~30 %-filled HMS slides → two grids; Metadata absorbs Conventions.
3. Power Tools order: move Creating & Editing into Everyday Commands, Processes after
   Getting Help; use box-drawing trees everywhere; three in-lecture exercises + a
   hackathon seminar is a lot — demote "Build a Project Skeleton" to try-at-home.

L05 (66 slides, ~118 min)
1. Move the Markdown practice exercise (needs VS Code preview) into "Your First VS Code
   Project"; move the line-break MCQ into the Markdown half.
2. Cut redundancy: orphan "Documentation & knowledge sharing"; "Why Diagrams-as-Text
   Win" into "Why text beats drawing"; "Editing Superpowers" (all repeated on the cheat
   sheet); stale Markdown Key Takeaways (add Mermaid/README).
3. Per-line Mac shortcuts on the feature slides; hide gitGraph hashes; replace the one-off
   `table { font-size }` with a theme class.

L06 (63 slides, 118 min)
1. Rebuild the four legacy `image-right` remote slides (23/24/26/27) as card slides —
   fixes the h3-bullet type scale, duplicate image, near-empty clone slide.
2. Add section slides for the first 33 slides (Local Git / Remotes / Branches); move the
   Git Data Flow SVG after Cloning (and relabel `--cached` → `--staged`); move the
   filename-chaos MCQ next to Committing; GitLab slide to end of the GitHub section.
3. The branch→PR→merge loop appears three times (38, 57–59, 60) — keep two. VS Code
   section says "show, don't tell" but has no screenshots — add two.

L07 (55 slides, ~120 min)
1. Opening is seven framing slides before the first `print()` — trim to objectives →
   one landscape slide → install → Try It; consider a CERN-specific "Why Python".
2. "Readable Output" re-teaches f-strings used since slide 11 — retitle "f-strings,
   properly" and add a one-line f-string note on the first use. Move the try/except peek
   into the Tracebacks section.
3. Normalise card-heading levels (`###`/`####`/`#####` mixed on one slide); one MCQ in
   the Style/Notebook stretch; physics examples instead of `customer_info`/`person`.
   Note: the moved Control Flow section now precedes "Strings for Data Wrangling" in the
   TOC — fine pedagogically, but "Data Structures" as a section now holds only one slide
   before it; consider renaming sections.

L08 (57 slides, ~120 min)
1. Delete the legacy "Files & Modules" section (12–14): it pre-teaches open modes,
   CSV/JSON and imports that Data Formats / Modules teach properly later; move the
   JSON/YAML cards into Data Formats; drop the Excel/pandas card ("no pandas yet").
2. Move the "Hands-On / Write Real Python" beat next to the CLI section (it is a closing
   beat placed mid-deck; the git-commit slide refers back to it 19 slides later); unify
   `analyse.py` vs `muon_analysis.py`.
3. Normalise `##` vs `####` card headings (visible type-scale jumps between consecutive
   slides); merge sys.argv+argparse, help()+type hints, module+`__main__` pairs. YAML is
   promised in objectives/recap but has one non-runnable line — add or drop.

## Seminar briefs (out of scope of the deck reviews, but noted)
- `seminar_08.md` still says "Prerequisites: Seminar 7", "scale yesterday's parser",
  "the later Pandas version (Seminar 13)" — cumulative wording. Harmless under
  "consecutive briefs may build on each other", but worth a light pass if you want each
  brief to read as fully standalone.


## Second half (L09–L16) — reviewed and reworked the same way

Per-deck reviews (source + every rendered slide, every snippet executed) followed by an
editing pass. Headlines:

- **L09** 70 → 61 slides, 155 (HEAVY) → 135 min. One step vocabulary (six-step loop);
  coffee example moved to illustrate it; two weak MCQs + five duplicate/ToC slides cut;
  stale "recall Lecture 7" fixed; three new section slides; Store sub-stage added.
- **L10** 94 → 87 slides, 145 → 133 min. Twelve caption/figure mismatches fixed; log/sqrt
  bar charts regenerated as dot plots; penguin scatter coloured by species; anatomy figure
  gets a finding-as-title; six section slides; hands-on code now shows its output.
- **L11** 75 → 68 slides, 134 → 126 min. Six raw-`$…$` slides fixed (single-line divs);
  KaTeX `8.8\%`; Poisson √N counting error added (seminar task 6); sample vs population
  notation; CLT "approximately"; Bayes order; new "Sampling & Estimation" section.
- **L12** 63 → 56 slides, 112 min. `absolute_sigma=True` taught and used everywhere;
  parametric bootstrap now agrees with the covariance error (0.052 vs 0.052); stock
  correlogram images replaced by a scripted covariance/ellipse figure; χ²/dof said once.
- **L13** 57 → 53 slides, 142 → 144 min. Seminar's moves now demonstrated: real
  `read_csv`, duplicates/invalid rows, filter-then-derive with `.copy()`, Parquet
  round-trip; Higgs block → one slide; D⁰ walkthrough with column `M`; three new MCQs.
- **L14** 73 → 67 slides, 110 min. Self-contradictions on the ♻️ message fixed (no
  committing `results/`; direct-deps vs lockfile); Testing gets its own section; FAIR
  compressed; pytest sequence actually runs (`python -m pytest`, `select()` defined, MeV).
- **L15** 68 → 65 slides, 105 → 110 min. Three hot-linked (black) image slides removed;
  objectives/recap now cover parallelism, formats, batch; two seminar-mirroring slides
  added; latency table harmonised with L03; PowerShell/core-count/SSD commands fixed.
- **L16** 65 → 63 slides, 117 min. Three scripted figures added (polynomial dial, ROC,
  k-means); tie-in mirrors the brief; MCQ keys de-patterned; feature slide aligned with
  what the masterclass sample actually contains.

Tooling: `scripts/check-slides.mjs` now waits for a slide's images to load/decode
before measuring and capturing (spurious blank figure frames under parallel workers).

Figure pipeline note: `pnpm figures` runs `python3`; the `fitting` family needs scipy
and `associations` needs seaborn — regenerate those with an env that has them.
