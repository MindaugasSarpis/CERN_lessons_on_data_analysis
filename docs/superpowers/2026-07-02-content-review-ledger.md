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

- `first_transisor.jpg` misspelled asset name on disk.
- "1 KB = 1,024 bytes" vs the table's "~1,000 bytes" — KB/KiB convention mix.
- Python/NumPy examples appear before Python is taught (delivery order) —
  possibly intentional teasers.
- CSV/JSON listed under "Lossless compression" conflates uncompressed formats
  with lossless compression.
- ARM listed as little-endian (technically bi-endian; fine as simplification).

## L03_1_2 File Handling

- `FileName.xxx` labelled "Camel case" is strictly PascalCase.
- "Use **absolute** paths for scripts and configs" is contested advice —
  relative-from-project-root is the usual reproducibility recommendation.
- File-naming section closely tracks Harvard HMS RDM guidance — consider an
  attribution line; verify the "40–50 characters" figure against the workbook.
- ISO-8601 date bullet appears verbatim on two consecutive slides.

## L03_2 Command Line

- "`rm -rf /` deletes your entire system" — modern GNU rm refuses without
  `--no-preserve-root`.
- README/Markdown/version-control forward references precede those lectures.
- "Working with Processes" (nohup, Start-Job) may exceed first-contact scope.

## L03_3 Markdown

- Rendered Markdown-logo image pulls from Wikimedia at lecture time (network
  dependency) and is nearly invisible black-on-dark; consider a local light
  asset.

## L03_4 VS Code

- "(Dark+ is the default)" — stale; default is "Dark Modern" since v1.78.
- "Jupyter notebook support built-in" for the Python extension — verify.
- "We'll use this in the next lecture" (Markdown) breaks if term order shifts.
- Practice slide assumes bash (`mkdir -p`, `touch`) — fails in PowerShell.
- `python` vs `python3` command consistency with L05.
- "install via apt/dnf" needs Microsoft's repo first; "100+ languages" holds
  only with extensions.

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
