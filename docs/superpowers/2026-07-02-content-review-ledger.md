# Content Review Ledger — Owner Decisions (2026-07-02)

Findings from the full-deck content review that were **deliberately NOT changed**
because they are factual/semantic/owner-level calls. Safe fixes and flow
improvements from the same review were applied directly (see commits of
2026-07-02). Line numbers are pre-edit approximations.

> **Closeout (2026-07-03):** a textbook-grounded content-enrichment pass
> (spec: `specs/2026-07-03-deck-content-enrichment-design.md`) resolved every
> **per-lecture** flag below — each is now marked ✅ RESOLVED or ⏸ DEFERRED
> with a reason. New slides were added where the canonical treatment had gaps;
> cross-lecture forward references were verified against delivery order. The
> full deck passes the zero-overflow QA gate (530 slides). The **Course-wide**
> items remain open owner decisions.

## Course-wide  *(still open — owner decisions)*

- Every lecture cover subtitles the course "Data Analysis and Artificial
  Intelligence" while the repo calls it "Lessons on Data Analysis from CERN" —
  consistent across covers, so presumably intentional; unify only if desired.
- Almost every slide is `hideInToc: true`, so the deck-level TOC is nearly
  empty. Decide whether content slides should appear in the TOC.
- British vs American English is inconsistent *between* files (L03_1_2/L07
  British, L03_1_1/parts of L06 American). Within-file consistency was
  enforced; a deck-wide canonical choice is an owner call.
- 13 of 24 referenced videos are absent from `public/videos/` and rely on the
  remote GitHub-release fallback — fine online, silently broken offline.

## L01 Course Orientation

- ⏸ DEFERRED to FF-2026 Workstream A (2026-07-03): Grading slide is stale
  BS-era content (Quiz 20% + Quiz 20% + Project 60%, both quizzes dated
  "Apr 16th") — the roadmap replaces this with 100 % project grading.
- ⏸ DEFERRED to FF-2026 Workstream A (2026-07-03): Contact-hours stat
  (48 h contact / 212 h self-study) contradicts the FF `.docx`
  (64 contact / 76 self-study).
- ⏸ DEFERRED to FF-2026 Workstream A (2026-07-03): Schedule table dates
  (Feb 19 – Apr 18) are BS-era.
- ✅ RESOLVED (2026-07-03): audit found no dangling forward references;
  added `python`/`python3` platform note to match L05's install check.

## L02 Introduction to CERN

- ✅ RESOLVED (2026-07-03): 5-sigma restated as background-fluctuation
  frequency ("if there were no new particle…"), teasered to L09, and turned
  into an MCQ whose first distractor is the old misreading.
- ✅ RESOLVED (2026-07-03): pipeline reordered — trigger selection now
  precedes event reconstruction; a dedicated "From Collision to Dataset"
  slide walks the 40 MHz → L1 → HLT cascade.
- ✅ RESOLVED (2026-07-03): figures re-verified — 25 member states (Slovenia
  2025), "(as of 2026)" suffixes added; WLCG card now says "hundreds of
  petabytes per year". Still aging by design; re-verify each term.
- ✅ RESOLVED (2026-07-03): local file + slide reference renamed to
  Perseverance; the `fallback` prop pins the old misspelled release-asset
  URL. Owner action still open: re-upload the release asset under the
  correct name, then drop the fallback.

## L03_1_1 Crash Course on Computer Science

- ✅ RESOLVED (2026-07-03): asset renamed to `first_transistor.jpg`
  (reference updated).
- ✅ RESOLVED (2026-07-03): warning card now explains the decimal kB vs
  binary KiB conventions explicitly; table stays decimal and says so.
- ✅ RESOLVED (2026-07-03): Python/NumPy examples labelled as previews
  pointing at the Python crash course.
- ✅ RESOLVED (2026-07-03): CSV/JSON reframed as uncompressed plain-text
  formats inside the Lossless card ("that's why they zip so well").
- ✅ RESOLVED (2026-07-03): "x86/x64 and (typically) ARM" — bi-endian
  simplification acknowledged.

## L03_1_2 File Handling

- ✅ RESOLVED (2026-07-02): camel-case example corrected in the restyle batch.
- ✅ RESOLVED (2026-07-03): advice inverted — scripts use project-root-relative
  paths; absolute paths only for machine-specific config, never shared code.
- ✅ RESOLVED (2026-07-03): attribution note linking HMS RDM added to the
  File Naming Conventions slide; "at most 40–50 characters" phrasing kept
  (upper bound, consistent with HMS guidance).
- ✅ RESOLVED (2026-07-03): second ISO-8601 bullet replaced with the
  *why* (dates sort correctly when placed first).

## L03_2 Command Line

- ✅ RESOLVED (2026-07-03): reworded to "`rm -rf` on the wrong directory" with
  a note that modern rm refuses `/` but `rm -rf ~` has no guard.
- ✅ RESOLVED (2026-07-03): the "Beyond the Basics" card already labels git/
  Markdown/VS Code as upcoming lectures — verified sufficient; no unlabelled
  forward references remain.
- ✅ RESOLVED (2026-07-03): processes slide now carries an "optional
  power-user detour" note.

## L03_3 Markdown

- ✅ RESOLVED (2026-07-03): local light-recoloured mark created at
  `public/figures/markdown_mark_light.svg` and referenced instead of the
  black-on-dark Wikimedia URL. Also added: reference-style-links note and a
  "Where You'll Meet Markdown Again" closing-loop slide.

## L03_4 VS Code

- ✅ RESOLVED (2026-07-03): "Dark Modern is the default".
- ✅ RESOLVED (2026-07-03): verified against the marketplace — Jupyter is a
  separate companion extension; card reworded.
- ✅ RESOLVED (2026-07-03): "next lecture" → "the Markdown lecture".
- ✅ RESOLVED (2026-07-03): PowerShell equivalents added to the practice
  slide (`mkdir`, `ni`).
- ✅ RESOLVED (2026-07-03): run command now shows `python` with a
  `python3` note, matching L01/L05.
- ✅ RESOLVED (2026-07-03): snap-or-repo wording for Linux install;
  "dozens out of the box — 100+ with extensions".

## L05 Python

- ✅ RESOLVED (2026-07-03): comment card now says it's a string literal that
  *works* like a comment; `#` named as the only true comment; docstring
  cross-reference added.
- ✅ RESOLVED (2026-07-03): platform list rebalanced toward fully-free
  resources (official tutorial, freeCodeCamp, Kaggle Learn); paid platforms
  labelled honestly.
- ✅ RESOLVED (2026-07-03): dict key renamed `collision_energy_TeV` with
  "the LHC's Run-3 energy" comment — ages visibly.

## L06 Concepts of Data Analysis

- ✅ RESOLVED (2026-07-03): cautionary tale replaced with the documented
  Reinhart–Rogoff (2010) spreadsheet-error case (Herndon et al. 2013); the
  four checklist gaps re-mapped to what actually went wrong.
- ✅ RESOLVED (2026-07-03): FAIR quote attributed to GO FAIR / Wilkinson
  et al. (2016).
- ✅ RESOLVED (2026-07-03): 23andMe turned into a teaching point — 2025
  bankruptcy + database sale, "data can outlive the company".
- ✅ RESOLVED (2026-07-03): Facebook iframe replaced with a local link card
  (no third-party embed, works offline).
- ✅ RESOLVED (2026-07-03): SMART "actionable" → "achievable".
- ✅ RESOLVED (2026-07-03): Invenio (a platform) replaced with real schemas
  (Dublin Core, DataCite, schema.org).
- ✅ RESOLVED (2026-07-03): "dissertation-grade" → "research-grade".
- ✅ RESOLVED (2026-07-03): overfitting MCQ reworded so exactly one option is
  defensible (question now asks about training accuracy alone).
- ✅ RESOLVED (2026-07-03): "60–80 % of the work" → "often the biggest time
  sink" (folklore no longer stated as a fact).

## L07 Data Visualisation

- ✅ RESOLVED (2026-07-03): 13 disabled slides triaged — 8 re-enabled as
  active-recall "what's wrong / corrected" pairs (legend series + bar-chart
  series, figures verified on disk); 5 deleted (3 superseded histogram raster
  drafts, the datavizcatalogue iframe, and the redundant colorblind slide
  already covered by the rainbow→Okabe-Ito section).
- ✅ RESOLVED (2026-07-03): Bundestag caption corrected to three groups
  (CDU/CSU 243, SPD 214, FDP 39), SPD–FDP slim majority (per Wilke ch. 10).
- ✅ RESOLVED (2026-07-03): rainbow-fix figure verified — it uses the exact
  Okabe-Ito hexes (#e69f00/#56b4e9/#009e73), a categorical recolour, so the
  caption is correct; no change.
- ✅ RESOLVED (2026-07-03): perceptual-hierarchy slide now credits Cleveland
  & McGill (1984) *and* the Heer & Bostock (2010) replication.

## L08 Version Control

- ✅ RESOLVED (2026-07-03): claim reworded — word processors do track changes
  and co-edit; git's difference is line-level diffs, branching/merging, and
  complete offline history.
- ✅ RESOLVED (2026-07-03): "gone for good" scoped to uncommitted changes;
  reflog escape hatch noted.
- ✅ RESOLVED (2026-07-03): conflict example now uses `about_me.md` prose
  (the Markdown-lecture file) instead of Python.
- ✅ RESOLVED (2026-07-03): verified — L03_3's practice slide creates
  `about_me.md`; references align.

## L09 Probability & Statistics

- ✅ RESOLVED (2026-07-03): "Connecting to Data Fitting" is the published
  deck's finale and actually delivers the fitting content (least squares =
  MLE, χ²); the one forward-looking caption reworded to reference "the rest
  of this section" rather than a future lecture.
- ✅ RESOLVED (2026-07-03): motivation's "statistically significant" bullet
  now flags that the term is made precise later in the lecture.
- ✅ RESOLVED (2026-07-03): "pattern of patterns" reworded as the lecture's
  own aphorism (no false attribution).
- ✅ RESOLVED (2026-07-03): unused `mermaid: true` frontmatter removed.
- Added slides: LLN vs CLT (distinct promises), Standard Deviation vs
  Standard Error (closes L07's forward reference), Correlation ≠ Causation.
