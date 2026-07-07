# Course Timing Rebalance — Design

**Date:** 2026-07-06
**Status:** approved for implementation (autonomous session; user asked to "work on timing — 16 weeks, 2h lectures, 2h seminars, content about even, better more than less") — Implemented 2026-07-07; gates green (`pnpm timing:check`, `pnpm qa`: 16 decks + landing, zero overflow).

## Problem

The course runs **16 weeks × (2h lecture + 2h seminar)**, but the material was
written against an older ~90-minute format:

- Every seminar brief declares **~90 min** while the slot is 120 min.
- Workbook lecture pages say "Duration: 90–120 minutes".
- Lecture decks are wildly uneven: estimated delivery ranges from **~27 min
  (L01) to ~186 min (L09)**. Total estimated lecture material is ~1419 min
  against a 1920-min slot budget — the course under-fills 2h slots overall.

The user's constraint: content per week should be **about even**, and it is
**better to have slightly too much than too little**.

## Timing model (the yardstick)

`scripts/timing-report.mjs` (run as `pnpm timing`) estimates delivery minutes
per deck from the markdown source:

| element | minutes |
|---|---|
| structural slide (cover/intro/quote/section/statement/fact/center-bkg, or <8 prose words) | 0.5 |
| light content slide (≤40 prose words — figure/visual) | 0.9 + words/120 |
| normal content slide | 1.3 + words/120 |
| `<MCQ>` (think, vote, discuss) | +3.0 |
| `{monaco-run}` (run, tweak, explain) | +1.5 |
| `<VideoPlayer>` (clip plays out) | +1.5 |
| ` ```mermaid ` (diagram walked through) | +0.5 |

**Target band: 105–145 estimated minutes** per lecture. Rationale: a 2h slot
minus a ~10-min break and admin gives ~110 teaching minutes; the band centres
slightly above that because over-full is preferred, and the model is ±10%.
`UNDER` (< 105) must be fixed; `HEAVY` (> 145) is trimmed or rebalanced.
Seminar briefs must declare **~120 min**. `pnpm timing:check` exits non-zero
if any week is UNDER — same spirit as the `pnpm qa` overflow gate.

The model is a heuristic. Its job is not to be exact but to be a *consistent
yardstick* so "about even" is measurable and stays measurable.

## Baseline (2026-07-06)

```
01_Orientation                 27  UNDER      09_Concepts_of_Data_Analysis  186  HEAVY
02_Introduction_to_CERN        81  UNDER      10_Data_Visualisation         145  ok
03_How_Computers_Work         101  UNDER      11_Probability_and_Statistics 134  ok
04_Command_Line_and_Files      90  UNDER      12_Data_Fitting                92  UNDER
05_Markdown_and_VS_Code        57  UNDER      13_NumPy_and_Pandas           142  ok
06_Version_Control             67  UNDER      14_Reproducible_Workflows      75  UNDER
07_Python_Foundations          57  UNDER      15_Computing_Infrastructure    74  UNDER
08_Python_for_Data             43  UNDER      16_Machine_Learning_and_AI     48  UNDER
```

All 16 seminars: declared 90 min (UNDER).

## Final (2026-07-07)

```
01_Orientation                 119  ok        09_Concepts_of_Data_Analysis  155  HEAVY (accepted)
02_Introduction_to_CERN        111  ok        10_Data_Visualisation         145  ok
03_How_Computers_Work          105  ok        11_Probability_and_Statistics 134  ok
04_Command_Line_and_Files      124  ok        12_Data_Fitting                114  ok
05_Markdown_and_VS_Code        117  ok        13_NumPy_and_Pandas           142  ok
06_Version_Control             118  ok        14_Reproducible_Workflows      117  ok
07_Python_Foundations          118  ok        15_Computing_Infrastructure    105  ok
08_Python_for_Data             117  ok        16_Machine_Learning_and_AI     118  ok
```

All 16 seminars: 120 declared, ≥5 tasks, ≥3 stretch. Total ≈1959/1920 (deck) min.

## Approaches considered

1. **Report only** — build the yardstick, change no content. Rejected: does
   not satisfy "content is about even".
2. **Rebalance + targeted expansion** *(chosen)* — move L09's overweight
   sections into the thin decks they thematically belong to, expand the rest
   with new material aligned with the four aims, retime all seminars to 2h.
   No week is cut; nothing is deleted.
3. **Restructure the syllabus** (merge/split/reorder weeks). Rejected: decks,
   workbook and seminars are 1:1 with weeks; disruption without need.

## Design

### 1. Rebalance L09 (186 → ~155)

L09 "Concepts of Data Analysis" carries material that belongs to other weeks.
Move (adapt transitions, keep slide content):

- **Domain examples block** (Biomedicine, Environmental, Astronomy, Particle
  Physics, Finance, common threads, reflection) → **L01** ("Data in Your
  Life" is exactly this theme).
- **Documentation & knowledge sharing** → **L05** (Markdown/VS Code is the
  documentation lecture).
- **Languages of data + Proprietary tools vs programming languages** →
  **L07** (they complete the "why Python" landscape argument).
- **DataOps & automation + Testing your analysis** → **L14** (Reproducible
  Workflows & Automation), and the **FAIR principles section including the
  CERN Open Data worked example** → **L14** (FAIR is the reproducibility
  lecture's natural capstone; L09 keeps forward pointers).

Executed 2026-07-07: L09 lands at ~155 — still above the 145 advisory line,
which is accepted: the `timing:check` gate fails only UNDER weeks, L09 is the
conceptual heart of the course, and its 7 MCQs give the instructor ~20 min of
pacing slack. Everything else lands inside the band.

### 2. Expand thin decks (order = biggest gap first)

Every expansion follows existing authoring conventions (card system, one
emoji-bold heading style, MCQ component, `{monaco-run} {autorun:false}`,
section dividers) and serves the four aims. Indicative content plans:

| deck | est → target | plan |
|---|---|---|
| L01 (27) | ~120 | absorb L09 domain examples; expand course structure/schedule slides to the 2h×16 format; add "a day in data" walkthrough, what-is-data taxonomy teaser, running-project intro, how-to-succeed slides, 1–2 MCQs |
| L08 (43) | ~120 | add pathlib & file organisation, JSON + data formats, building a small CLI script, organising code into modules, docstrings & type hints, more Try It runners, 1 MCQ |
| L16 (48) | ~120 | add regression section, clustering/unsupervised, ROC/AUC & cross-validation, feature engineering & leakage, ML-in-HEP case studies (trigger, flavour tagging), responsible-AI depth, second hands-on classifier demo |
| L05 (57) | ~120 | absorb L09 documentation section; add Mermaid diagrams section (course uses them), advanced editing (multi-cursor, regex search/replace, snippets, diff view), data-friendly extensions, README anatomy exercise |
| L07 (57) | ~120 | absorb L09 languages-of-data slides; add f-strings & formatting, reading tracebacks, naming/PEP 8 style, scripts-vs-notebooks, more Try It runners/katas |
| L06 (67) | ~120 | add GitHub collaboration section (PRs, issues, forks, review flow), git in VS Code, stash/tags, GitLab-at-CERN note, second hands-on sequence |
| L15 (74) | ~120 | add parallelism (vectorisation/threads/processes), storage formats for analysis (ROOT/Parquet/HDF5), WLCG/grid + cloud vs HPC, benchmarking your machine |
| L14 (75) | ~120 | absorb L09 DataOps/testing + FAIR section; expand testing hands-on (pytest), add data versioning teaser, pre-commit hooks, workflow tools comparison |
| L02 (81) | ~115 | expand detector/data-flow numbers, open science & WLCG teaser, careers/impact slides (videos undercounted by model — ambient clips run long; modest top-up only) |
| L04 (90) | ~115 | add pipes-and-filters practice, find/grep patterns on real data files, shell scripting mini-section |
| L12 (92) | ~115 | add goodness-of-fit/residuals depth, fit-pitfalls gallery, one more guided fit exercise |
| L03 (101) | ~112 | light top-up: one more hands-on segment (e.g. binary/precision pitfalls in analysis) |

L10 (145), L11 (134), L13 (142): in band — untouched.

### 3. Retime all 16 seminars (90 → 120 min)

Format change per brief (keep the concise-brief style):

- Header: `**~120 min**`.
- Add a one-line **Suggested timing** agenda: `0:00 warm-up recap · 0:10 core
  tasks · 1:20 stretch · 1:50 wrap-up & commit`.
- Add ≥1 substantial core task where the brief is thin (target ≥4–5 tasks).
- Expand stretch goals to ≥3 so fast students never run dry.
- Add a short **Wrap-up** ritual (commit, verify it runs clean, note one
  lesson in the README) — reinforces ♻️/⚙️ every single week.

### 4. Fix stated durations everywhere

- Workbook lecture pages: `Duration: 90–120 minutes` → `~120 minutes (2 h slot)`.
- L01 course-structure/schedule slides state 16 weeks × (2h + 2h).
- `running-project.md` mentions session pacing → align if needed.

### 5. Verification

- `pnpm timing:check` → no UNDER weeks (new gate, documented in CLAUDE.md).
- `pnpm qa` on all touched decks → zero overflow (existing hard gate).

## Non-goals

- No deletion of content; HEAVY is resolved by moving, not cutting.
- No syllabus reordering, no changes to decks.json ordering or blocks.
- No workbook lecture-page rewrites beyond duration lines (they are companion
  notes, not the delivery medium).
