# Decks match the landing page — design

**Date:** 2026-10-05 · **Status:** approved in conversation, implemented on `main`

## Problem

The landing page (near-black, Space Grotesk, hairlines, one cyan accent, grain) and
the lecture decks (particle-wave photo behind every slide, PT Serif body, glowing
gradient cards with coloured left borders) look like two design systems. Opening a
lecture from the landing feels like a step down.

## Decisions (made with the maintainer)

| Question | Choice |
|---|---|
| Scope | The whole deck look, not only the cover |
| Slide backdrop | The landing's static backdrop: `#050507`, two faint cyan radial glows, 5 % grain. No photo, no WebGL |
| Cards | Hairline panels: near-transparent fill, 1 px hairline border, no glow/shadow/blur. Colour only in the card title (kicker) and a short rule above it |
| Type | Space Grotesk everywhere (PT Serif retired), Space Mono for code. Cover/section titles large; content titles sentence case with the `**keyword**` in accent |
| Colour | One accent (`#7dd3fc`). Only `card-warning` (amber) and `card-success` (teal) keep a colour of their own |
| Approach | Shared token file imported by both the landing and the Slidev theme, then a rewrite of the theme CSS and layouts (not an override layer) |

## Design

**Foundations.** `lectures/content/theme/styles/tokens.css` (inside the theme so the Slidev dev server may read it) holds the tokens both sides use (`--bg`, `--fg`,
`--dim`, `--accent`, `--hair`, `--warn`, `--ok`, `--ease`, backdrop glows, grain).
`landing/src/style.css` and `theme/styles/index.ts` import it. Fonts come from
`@fontsource` (bundled; an offline lecture-day build needs no network), with the
theme's Slidev font provider set to `none`. Body text stays at full `--fg`; `--dim` is
for labels, captions and attributions only (projector contrast).

**Layouts.**
- *Cover* mirrors the landing hero: author as accent kicker, the course title as a small
  dim link home, the lecture title as the big uppercase hero with the staggered line-in
  reveal, the aims badge as a tracked sub-line, corner labels `AUTUMN 2026` and
  `LECTURE NN · BLOCK X` (read from `decks.json` via the deck slug in `BASE_URL`; hidden
  when no deck matches).
- *Section*: left-aligned, accent kicker, large Grotesk title, keyword in accent, a
  hairline that draws in from the left. The aurora goes.
- *Quote*, *fact*, *statement*, *intro*, *center-bkg*: same tokens, no gradient text,
  no photo.
- *Default*: sentence-case title, keyword in accent, a hairline under the title row in
  place of the gradient bar (no layout height).

**Content components.** Cards as above (the `pad-*` spacing and `card-glass` stay as
classes, so slide sources do not change). Tables with hairline row rules and a tracked
header. `<MCQ>` options as hairline rows with the landing's row hover. Mermaid nodes
with transparent fill and hairline strokes. `gradient-text`/`glow` become plain accent.
Monaco output and Slidev's chrome on the same tokens. Figure SVGs untouched.

## Changed during implementation

- **Card titles are not uppercased.** The first build set card titles as uppercase
  kickers, like the landing's labels. The slide-by-slide review found that this changes
  meaning in a science course: `σ` became `Σ`, `$h_j$` became `H_J`, `clean.py` became
  `CLEAN.PY`. Card titles are now sentence case in the card's tone (accent / amber /
  teal) with the short rule above; uppercase stays for chrome labels only (cover kicker
  and corners, section kicker, badges).
- **Code colours:** a small course shiki theme (`setup/shiki.ts`) replaces vitesse —
  cyan keywords, mint strings, and comments readable on a projector, because many decks
  print a result as a `# …` comment.
- **Mermaid `classDef` colours** in slide sources are stripped at build time by
  `setup/transformers.ts` (Slidev markdown transformer), not by patching mermaid.
- Quizzes (`<MCQ>`) are top-aligned so the question sits in the same place on every
  quiz slide; a warning/success card without a title shows its tone as a 2 px left rule.

## Follow-ups (not in this change)

- **Figures** (`figures/src/`, separate pipeline): several scripted SVGs still use
  violet/pink/navy series colours (L07 arrays, L11 perceptron, L12 dataframe, L16 ROC /
  cross-validation), and their tick/label text is often 6–9 px once a slide shrinks the
  figure — too small for a projector. A pass over `style.py` (label size, palette) would
  fix all families at once. A few legacy assets are white-canvas PNGs (L08 legend
  examples, L13 pendulum plots) or old navy SVGs (L06 `python_debugger.svg`, L05
  `play-changes.svg`).
- `scripts/check-slides.mjs` waits for the layout, not for mermaid's async render, so a
  screenshot can miss a diagram (seen on L05 s58, L13 s8); the overflow measurement may
  under-count such slides.
- Space Mono's `@` is small and can read as `a` at code size (L11 matmul `X @ w`).

## Constraints

Zero overflow on all 16 decks (`pnpm qa`), one type scale driven by the markdown
level (any size change is made once, in the theme), full-screen videos, no lecture
markdown edits, `prefers-reduced-motion` honoured, the landing's own check
(`check-landing.mjs`) still passes.

## Verification

`pnpm qa` (all decks + landing), `pnpm timing:check`, and a screenshot review of
every deck for contrast, crowding and leftovers of the old style.
