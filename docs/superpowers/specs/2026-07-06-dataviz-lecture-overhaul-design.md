# Lecture 10 (Data Visualisation) Overhaul — Design Spec

**Status:** Approved (author, 2026-07-06) · **Branch:** `ff2026`
**Sequencing:** starts only after the 2026-07-06 course-wide content wave passes full QA and is pushed (a content editor is touching this same file in that wave).

## Goal

Replace the deck's ~80 third-party (Claus Wilke) light-styled SVGs with a
self-owned, scripted matplotlib pipeline in a unified dark course style;
add a click-by-click "anatomy of a figure" showpiece; add live in-slide
Python examples; restyle the Monaco runner theme-wide. Deck structure and
teaching text stay (the "What's Wrong → Corrected" arc was reviewed as
excellent); this is a visual/interactivity overhaul, not a rewrite.

## 1. Figure pipeline

- New `figures/src/` Python package, run by `pnpm figures`
  (`python3 figures/src/build.py [--only family]`):
  - `style.py` — the single course style: dark-transparent background,
    light strokes/text, colorblind-safe palette with course cyan `#7dd3fc`
    as the primary series color, vendored Space Grotesk TTF (OFL) for all
    text, consistent grid/spine/tick idiom. (Consult the dataviz skill's
    palette/mark rules at implementation.)
  - ~12–15 family modules (`amounts.py`, `distributions.py`,
    `associations.py`, `proportions.py`, `coordinates.py`, `color.py`,
    `balance.py`, `uncertainty.py`, `timeseries.py`, `anatomy.py`, …), one
    function per figure, registered so `build.py` can run all or one family.
- Outputs: SVG to `lectures/content/public/figures/viz_*.svg`, committed
  (deck builds never invoke Python). Old `cwilke_*` files removed from the
  repo once no deck references them.
- Data: seaborn bundled datasets (mpg, titanic, iris, penguins, flights)
  where they fit the existing pedagogical point; deterministic synthetic
  data elsewhere (fixed seeds — reproducibility is the course's own aim).
- Every deck-10 image ref updates `cwilke_*` → the matching `viz_*`.
  Non-data images (photos, backgrounds) stay.

## 2. Anatomy fly-in slide (showpiece)

- `anatomy.py` renders the flagship LHCb D⁰→K⁻π⁺ spectrum in ~6 cumulative
  stages: frame → axes+units → data points → √N error bars →
  annotation/legend → title+caption. Identical geometry/limits across
  stages (same figure, elements added), exported as aligned SVGs.
- New slide stacks the stages absolutely with `v-click` fades — each
  element "flies in" per click; talking track: every element must earn its
  place. Replaces/augments the current static "Running Project" figure
  moment.

## 3. Live Monaco examples in deck 10

- 2–3 `python {monaco-run}` slides following deck 12's existing pattern:
  bin-width explorer (histogram), axis/log-scale toggle. Short blocks
  (≤ ~14 lines) so slides cannot overflow.

## 4. Monaco restyle (theme-wide)

- New `lectures/content/theme/styles/monaco.css` (imported with the other
  theme styles): rounded corners, hairline border, subtle header strip,
  padding, shadow, and output-area styling for `monaco-run` blocks.
- Applies to every deck; deck 12's four existing interactive slides are
  the regression surface (QA + screenshots).

## 5. QA & ship

- `pnpm figures` regenerates the full set idempotently; committed SVGs.
- `pnpm qa --only 10-data-visualisation,12-data-fitting` during iteration;
  full `pnpm qa` before push (zero-overflow gate).
- Screenshot review of every regenerated-figure slide (qa:shots for deck
  10) — dark figures must read correctly on the dark theme.
- Push `ff2026` + deploy `ff2026:bs2026` per the established flow.

## Out of scope

- Restructuring the deck's sections or cutting slides (option declined).
- Physics-first example rewrite beyond the anatomy slide (declined).
- Touching other decks' content (only the Monaco CSS is global).
