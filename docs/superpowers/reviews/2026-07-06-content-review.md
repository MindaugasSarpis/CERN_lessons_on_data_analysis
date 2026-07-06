# Course Content Review — All 16 Lectures (2026-07-06)

Five parallel reviewers read every lecture source in full plus the paired
seminar briefs, checking factual accuracy (2026 lens), narrative/pacing,
alignment with the four course aims, audience fit, and lecture↔seminar
continuity. This is the synthesis; suggestions only — nothing was changed.

## Cross-cutting themes (highest leverage)

1. **Lecture↔seminar sequencing bugs (fix before term).**
   - Seminar 7 requires `try/except` in `parse_line`, but exceptions are
     taught in Lecture 08. Add a one-slide preview in 07 or soften the task.
   - Seminar 11's stretch goal assigns bootstrapping — never defined in any
     lecture. One slide in 11, or drop the stretch goal.
   - **Seminar 15 assumes batch jobs/schedulers (Slurm/HTCondor, `nohup`,
     WLCG estimation) but Lecture 15 never leaves the single machine** —
     the biggest continuity gap found. Add a grid/cluster/scheduler section
     (the lecture's own motivation slide promises it) or rescope the seminar.
   - Lecture 12's "Try It — Fit the D⁰ Peak" demo pre-solves Seminar 12
     nearly verbatim; vary the demo window or omit the printed answers.

2. **Running-project drift.** CLAUDE.md says the running project is the
   "CMS dimuon dataset"; the actual seminars/workbook use **LHCb D⁰→K⁻π⁺**
   (~1865 MeV). Fix CLAUDE.md, then align lecture examples: 07/08's generic
   strings/CSV demos and 13's Higgs→γγ / dimuon examples should use the real
   dataset's columns and peak so lectures rehearse exactly what seminars do.

3. **Scope contradictions between lectures.**
   - Lecture 11 twice defers "hypothesis testing & p-values beyond this
     course"; Lecture 12's "p-value from chi-squared" slide then teaches
     p-values with significance thresholds. Reconcile (keep the χ²
     computation, drop the threshold table — or soften 11's framing).
   - Lecture 03's #1 objective ("think algorithmically") doesn't match its
     actual content (data representation); retitle or add one real
     algorithmic exercise.
   - Lecture 15's title promises infrastructure; content stops at one box.

4. **Interactivity is thin and uneven.** Most decks carry a single MCQ
   (or none — Lecture 01). Highest-value additions: 07 (`.sort()` vs
   `sorted()`), 08 (except-clause order), 03 (after two's complement),
   10 (Anscombe pitfall), 11 (medical-Bayes surprise; LLN vs CLT),
   09 (swap 2 business MCQs for dimuon-flavored ones), 01 (four-aims check).
   Lecture 02: break the ~25-video run with a discussion prompt mid-reel.

5. **Pacing outliers.** Lecture 09 is ~4–5× the length of its neighbors —
   trim the 12-slide domain-examples block to 4–5 and move the rest to the
   workbook. Lecture 04 has a false ending (closing-quote slide mid-deck
   before 40 more slides) — move the quote to the true end or add an
   explicit "Part 2" transition. Lecture 03's 14-slide binary build-up
   could offer a "know binary? skip ahead" cue.

6. **2026 freshness.** Lecture 14 predates the `uv`/`pyproject.toml` era —
   add both (modern lockfile-based envs strengthen the ♻️ aim); trim
   Snakemake to a pointer. Lecture 16's LLM slide is pre-agent-era — add a
   line on agentic tool use; cite ISLP (Python edition); bridge Random
   Forest → "LLMs are the same loop at scale".

7. **Physics-audience accuracy nits (small but visible to this crowd).**
   - L02 "Key Achievement": Higgs gives mass to fundamental particles;
     most visible mass is QCD binding energy — add the caveat.
   - L06: "default branch is `main`" is only true if configured — add
     `git config --global init.defaultBranch main` to the setup slide.
   - L04: replace/caveat the `ls -l | awk` size-filter example (fragile
     anti-pattern; `find -size` was taught two slides earlier).
   - L09: reword the 23andMe "sold" claim (acquired via bankruptcy, nuance).
   - L10: the D⁰ spectrum figure right after the uncertainty section has no
     error bars — add √N bars or an explicit "raw stage" note.
   - L12: Gaussian/exponential Monaco demos don't print χ²/dof though the
     lecture's Do's demand it; no demo shows the mandated residuals panel.

## Per-lecture verdicts (one line each)

| # | Lecture | Verdict |
|---|---------|---------|
| 01 | Orientation | Solid logistics; zero interactivity; schedule table doesn't map to blocks A–E |
| 02 | Intro to CERN | Strong, accurate; 25-video run needs a mid-point beat; Higgs caveat |
| 03 | How Computers Work | Technically flawless; objective/content mismatch; MCQs bunched late |
| 04 | Command Line | Comprehensive; false mid-deck ending; one fragile `ls|awk` example |
| 05 | Markdown & VS Code | Clean and current; missing LaTeX-math markdown for physicists |
| 06 | Version Control | Strong, modern commands; set `init.defaultBranch`; add Git LFS/`git tag` notes |
| 07 | Python Foundations | Solid; feed it real dataset lines; try/except sequencing vs Seminar 7 |
| 08 | Python for Data | Strong bridge; ValueError guard missing from errors slide; git slide redundant with 06 |
| 09 | Concepts of Data Analysis | Rich but 4–5× too long; trim domains; physics-ify MCQs |
| 10 | Data Visualisation | Excellent; error-bar figure inconsistency; add ♻️ badge |
| 11 | Probability & Statistics | Mathematically careful; zero plotted distributions; bootstrap gap vs Seminar 11 |
| 12 | Data Fitting | Best-integrated; p-value scope clash with 11; demos skip their own χ²/residual rules |
| 13 | NumPy & Pandas | Modern pandas 2.x, correct; swap examples to D⁰→K⁻π⁺; mention Arrow backend |
| 14 | Reproducible Workflows | Accurate but pre-`uv` era; 9 tools is too many — trim Snakemake |
| 15 | Computing Infrastructure | Good hardware content; never delivers clusters/grid its title and seminar need |
| 16 | Machine Learning & AI | Best lecture↔seminar alignment; LLM section needs agent-era update |

## Quick wins (< 30 min each)
CLAUDE.md dataset fix · L06 `init.defaultBranch` line · L04 quote move +
"later in this lecture" wording · L05 LaTeX-math callout · L09 23andMe
reword · L10 ♻️ badge · L12 χ²/dof lines in two demos · L16 ISLP citation ·
videos/manifest.toml `Perseverence`→`Perseverance` typo (also flagged by
`videos.py check` as an UNKNOWN REF/UNUSED MANIFEST pair).

## Bigger restructures (plan a session each)
L09 domain-block trim · L15 cluster/scheduler section (or seminar rescope) ·
L02 video-reel split · L03 objectives/content realignment · L14 uv/pyproject
modernization · example alignment to the real running dataset (07/08/13).
