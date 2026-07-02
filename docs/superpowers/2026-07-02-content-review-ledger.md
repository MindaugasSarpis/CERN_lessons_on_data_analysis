# Content Review Ledger — Owner Decisions (2026-07-02)

Findings from the full-deck content review that were **deliberately NOT changed**
because they are factual/semantic/owner-level calls. Safe fixes and flow
improvements from the same review were applied directly (see commits of
2026-07-02). Line numbers are pre-edit approximations.

## Course-wide

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

- Triple-quoted strings taught as "multi-line comments" (they're string
  literals/docstrings) — common simplification.
- "All platforms offer free tiers" — dubious for Udemy/Codecademy.
- 13.6 TeV attributed to ATLAS as a dict key (it's the collider's Run-3
  energy; will also age).

## L06 Concepts of Data Analysis

- Clinical-trial "cautionary tale" reads as a real event but is unsourced —
  cite or label as hypothetical.
- FAIR quote slide is verbatim GO FAIR text without attribution.
- 23andMe example — company went bankrupt in 2025, database sold; could become
  a teaching point.
- Facebook iframe embed: network + third-party dependency, bypasses the
  VideoPlayer convention.
- SMART expanded with "actionable" (standard is "Achievable").
- "Invenio" listed as a metadata schema (it's a repository platform).
- "dissertation-grade dataset" — CERN Open Data terminology is
  "research-grade"/"derived".
- Overfitting MCQ distractor "depends on the test set performance" is arguably
  also correct.
- "Cleaning is 60–80 % of the work" — folklore figure stated as fact.

## L07 Data Visualisation

- 12 `disabled: true` draft slides remain in the file (legend what's-wrong
  series, bar-chart series, colorblind, histogram images) — delete or
  re-enable deliberately. One (colorblind) has a caption/image mismatch.
- 1976 Bundestag pie example: verify "four parties…supermajority" against
  Wilke's figure (likely three groups, slim majority).
- Okabe-Ito caption on the rainbow-fix figure: verify the figure isn't a
  continuous (viridis-like) fix.
- Perceptual-hierarchy attribution to Cleveland & McGill folds in later
  extensions.

## L08 Version Control

- Word-processor "no synchronous editing, no change history" claim is stale
  (Google Docs/Word Online have both).
- "`reset --hard` cannot be undone" — committed states recoverable via reflog.
- Merge-conflict examples use Python-flavoured code one lecture before Python.
- Verify L03_3's exercise file is named `about_me.md` (referenced here).

## L09 Probability & Statistics

- "Connecting to Data Fitting" teases L10, which is not in the published deck
  — forward reference dangles for students this term.
- Motivation slide mentions statistical significance; hypothesis testing is
  explicitly deferred.
- "The normal distribution is the pattern of patterns" quote has no
  attribution.
- Frontmatter `mermaid: true` with no Mermaid content (harmless).
