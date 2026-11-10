# 3D explainers, built in the toolkit

Date: 10 November 2026. Status: built; the four slides are on the branch
`explain3d`, not on `main`.

## What the lecturer asked for

- "launch a new session for lectures … to build a few 3D explainers for the
  course. Make them versioned and repeatable, implement in tools."
- On the proposal of four explainers: "Yes, and add to tools when finished".
- "Make the style uniform, make sure it fits well into the curriculum".
- On the release, the missing figure font and SVG as the renderer: "All good
  go ahead".

## What was built

The package `slidev-addon-explain3d` in the toolkit
(github.com/MindaugasSarpis/slidev-videos, `packages/explain3d`), released in
the toolkit's tags `v0.12.0` (0.1.0) and `v0.12.1` (0.1.1); the course pins
`v0.12.1` in `package.json`. Its engine is extracted from this course's
`TurningSurface.vue` and `TurningScatter.vue`, which stay as they are.

| Explainer | Deck, slide | The idea | Numbers checked against the deck |
|--|--|--|--|
| `hours-columns` | L08, 43, after "Temperature and Humidity of Every Hour" | a histogram of two columns of the file at once: a column per cell of 2 °C × 5 % | 87 552 hours, all in a cell; r = −0.70; the mean 7.16 |
| `line-fit-valley` | L09, 53, after "The Path Downhill" | S(a, b) is a narrow valley; the 500 descent steps cross it, then creep along it | −0.56 per decade, 7.41, χ² 8.56, start (0, 7) |
| `neuron-plane` | L10, 17, after "The Decision Boundary Is a Line" | z is a plane over the two inputs; where it crosses 0 is the boundary, a straight line | 3646 evenings, 3490 and 3494 right, z = 1.2 and 1.4 on 8 Dec 2025 |
| `xor-ridge` | L11, 19, after "XOR Learned from Random Weights" | each hidden neuron is one slope; the output is a ridge | loss 0.696 → 0.003; h₁ = 0.03, 0.98, 0.98, 1.00; h₂ = 0.00, 0.05, 0.05, 0.93 |

## Decisions

1. **SVG, not canvas or WebGL.** The four scenes hold 300 to 6300 paths,
   which SVG draws; fidelity rule (5) holds as written and needs no
   exception. The fallbacks: slow frames draw every second grid line while
   the scene moves; slower still it stops turning by itself; a scene that
   cannot be drawn shows the package's golden picture of its opening view.
2. **One look, set in the package**: that of the static figures
   (`--font-figure`, tick labels 13.75 px, axis names 15.625 px, ticks and
   text in the text colour, the colour key edged, the box's edges faint). A
   scene cannot restyle it. The path and the lowest point of
   `line-fit-valley` have the colours of the same marks in
   `viz_fitting_descent_line.svg`; frost is the accent and no frost the
   warning colour, as in `PerceptronPlayground`.
3. **Each explainer on a slide of its own, right after the flat figure of
   the same numbers**, as "The Four-Variable Scatter, Turning" in Lecture 7.
   Each adds 1.5 min; all four decks stay in the band (118, 119, 122, 124).
4. **The slide's own axes, units and numbers.** Nothing an explainer shows is
   introduced later in its deck: `hours-columns` does not state r, which
   comes three slides after it.
5. **Repeatable from the tag.** A scene is `spec.json`; its numbers come from
   `make.mjs` (no clock, no random numbers, no network) out of `input.json`,
   which records the SHA-256 of `weather.csv`
   (3f1ad06d3bb5773eac79dfc964cdf8af998689ef58aa8623f25d2050fbe00756); the
   opening view is a committed golden SVG that the package's tests compare.
   `xor-ridge` starts from the nine weights of `figures/src/language.py`,
   `xor_trained(seed=0)`, and trains them again; it agrees with the Python to
   16 digits.
6. **One correction**: Lecture 11 said h₂ = 0.94 at (1, 1); the value is
   0.9348, so the slide now says 0.93.

## Open

- The figure face `Figure Serif` (`components/figure-look/`) was not on
  `main` when this branch was cut; until it is, the explainers' text falls
  back to a system serif. Once it is there, `--font-figure` has to be set in
  every deck that shows an explainer (it is set when a component of the deck
  imports `figure-look.css`; Lecture 11 may have none that does).
- Decks 08 and 09 and their lecture pages were being reworked in the main
  checkout when this branch was made; the slide numbers of the lecture pages
  here are those of `origin/main` plus the new slide.
- On a machine without a GPU the valley turns on its coarse mesh (1974 paths,
  about 17 ms a frame) and is drawn in full (6260 paths) at rest.
- At a few angles while turning an axis name touches a tick label.
