# Implement all: the batches of 9–10 November 2026

The lecturer, 9 Nov 2026, evening: "Go ahead and implement all and deploy, we
have time all good", then "yes, all good, go ahead". Design:
`docs/superpowers/specs/2026-11-09-weeks-8-12-ideas-and-tools-design.md`.
Sources of the items: the course review of 9 Nov (six reviewers), the Slidev
research and the toolkit survey of the same night.

Every batch: done in the working tree (or a worktree when other work is in
flight), checked (`pnpm qa` for the decks touched, `pnpm qa:runners` for
runner decks, `pnpm timing:check`, screenshots read), committed, pushed, and
called deployed only when the qa.yml run is green and the URLs return 200.
While drafts are mid-rework on `main`, a batch ships from a worktree of
`origin/main` (CLAUDE.md, Deployment).

## Batch 1 — tonight, for the lecture of 10 Nov

- [x] Lecture 7 laconic: every main-path caption one or two lines, reasons in
      the notes; code slides in `# In **Matplotlib**` after For the Curious;
      the four-variable figures on the main path; `lecture_7.md` recounted.
- [x] Lecture 7 interactive: `BinWidthExplorer`, `AxisStartBars`,
      `PaletteHeatmap`, `SmoothingWindow` (if ready) on their slides.
- [x] Lecture 1: the twelve Tuesdays; CERN facts of Nov 2026.
- [x] Cover number from the slug.
- [x] Ship from the worktree `deploy-l07` (origin/main + only these files);
      verify; rebase `main` on it. Deployed 9 Nov, 21:50 (cb908e2, run
      42685082670 green; the four interactive slides checked on the live
      site: no failed request, no console error).

## Batch 2 — invisible improvements

- [x] Mobile load: `lectures/content/vite.config.ts` chunk override (tested
      in the research scratch build: L07's first load 3.69 → 0.20 MB).
- [x] Theme defaults in `theme/package.json` `slidev.defaults`: `titleTemplate`,
      a local favicon, `timer: countdown`; per-deck `duration` from the timing
      estimate in `gen-entries.mjs`.
- [x] Tools: `pnpm review`, `pnpm week`, `scripts/shots-diff.py`; CLAUDE.md
      trimmed to ~14 KB with `docs/authoring.md`.

## Batch 3 — visible changes, each with before/after screenshots

- [ ] Fade transitions (~0.25 s, the landing's ease) as a theme default.
- [ ] Larger type for projector and phones (card text 13.6 → ~16–17 px, code
      12 → 14 px, Monaco 13–14 px); fix what the overflow gate then flags.
- [ ] Emoji → monochrome icons (Phosphor via `@iconify-json/ph`) in card
      headings; decorative emoji in captions dropped; the convention in
      CLAUDE.md updated. (Builder's call under "implement all": the research
      recommends it; the lecturer had asked to avoid an AI-made look.)
- [ ] Readable slide sources: layouts `figure`, `figure-side`, `pair` with
      named slots; a conversion script; proof by pixel-identical screenshots.
- [ ] KaTeX click-stepping for formulas with numbers (`$$ {1|1-2|...}`, the
      substituted values in the accent colour) in decks 08–12.
- [x] Figures baseline: every family redrawn once with the canonical
      `figures` environment; screenshots compared.
- [ ] Lecture 1 (and 02, 03, 15): the toolkit's video addon and library clips
      (H.264, no freeze after ~10 clips); L03's HEVC clip re-encoded.
- [ ] Lecture 1's cover: the toolkit's live particle field (`StageHero`),
      L01 only, static fallback without WebGL.
- [ ] Fact citations for CERN numbers (L01, L02, L14–16) against the facts
      bank of `outreach_talks`; `pages_check.mjs` in CI.

## Batch 4 — weeks 8–12 and the interactive components

- [x] Integrate the five week builders' decks, seminar pages, lecture pages
      and start folders; QA and timing for every deck.
- [x] `MeanSpread` (8), `FitLine` (9), `PerceptronPlayground` (10),
      `SoftmaxTemperature` (11) on their slides.
- [ ] Zips `weather-s08`…`s12` uploaded to the release `seminar-files`.
- [x] Deploy (drafts stay drafts), 9–10 Nov.
- [ ] Release week 8 on 16 Nov with `pnpm week 8`.
- [ ] The interactive components back to the toolkit `slidev-videos` on a
      worktree branch, for the lecturer's approval.
- [ ] Seminar pages machine-checkable (a marker per code block) and a replay
      command.

## Added on the night of 9–10 November (the lecturer's requests)

- [x] Glossary at the end of every deck (`lectures/content/glossary/NN.md`,
      `scripts/gen-glossary.mjs`) and the workbook's A–Z page.
- [x] Fidelity: every figure vector (no `rasterized=True`, no `imshow`, no
      GIF/PNG plots); `scripts/check-fidelity.mjs` in `pnpm qa` and CI; Lecture 7's
      turning scatter and month animation as SVG components; Lecture 6's VS
      Code screenshots removed; Lecture 3's photos shown no larger than their
      pixels.
- [x] Figure style v2 (real font weights, the tokens' colours, a CVD-checked
      palette, projector sizes, `save()` refuses bitmaps); every family
      redrawn with the canonical environment.
- [x] Lecture 7, Classics and Maps (slides 85–90): Nightingale, Minard,
      Rosling's bubble chart, Maunga Whau, CERN to scale and as a schematic.
- [x] Every slide self-contained: no visible "of Lecture N" (decks 4–12).
- [x] Lecture 7, "The Parts of a Figure" reworked on 10 November (the lecturer:
      "Rework, more expressed error bars, more complicated curve, 16:9 ratio",
      then "legend with no frame"). Decisions: the figure is the D⁰ mass peak
      of `D0_KPi.csv` in place of the weather log's monthly means (their error
      bars are 0.3 °C on a range of 30, and their only structure is one
      cosine); the first 1500 rows, so that a bar is 10 % of its count at the
      top of the peak (with every row it is 1.3 %, shorter than the marker);
      30 bins of 3 MeV/c² (with 2 MeV a bin centre lies on the known mass);
      the fit is a Gaussian on a straight line, drawn as the sum, the straight
      line and the filled area between them; the legend has no frame and the
      fit result is plain text without its box; the slide has no visible
      heading (`title:` in the frontmatter), so the 16:9 figure is 839 × 472 px
      and not 723 × 407.
- [x] Lecture 7, "The Parts of a Figure" full screen, 10 November (the
      lecturer, on the version above: "Full screen, it's important"). Read
      as: the figure covers the whole slide, at every click. Decisions: the
      stack of stages is an absolute box over the slide's full frame with
      `object-fit: cover`, as a video slide, so the figure is 980 × 551 px
      and not 839 × 472; it is drawn at 10.89 × 6.13 in (90 px/in, the type
      as large as on every other figure, the plot larger); the lower panel
      is drawn from the first stage, empty until its pulls come at the fifth
      click (with the room only kept for it, the bottom quarter of the
      screen was blank for five clicks); the deck's two buttons lie over the
      top right corner, and no part of the figure goes under them
      (`anatomy.py` checks the name of the title); the dashed frame that
      names the Figure runs outside the buttons; `class: fill` stays on the
      slide so that `scripts/measure-figures.mjs` still measures the stages.
- [x] Lecture 7, slide 10 full screen: the deploy of 10 November. The push
      of `f74ea2a` (the mass peak inside the slide's padding) passed qa and
      build; its GitHub Pages deployment stayed in `syncing_files` for
      10 minutes and timed out, so that version was never live. `066ef99`
      (full screen) was deployed by run 42809854887 at 13:56:43 EET. At
      13:56:21 the failed run of `f74ea2a` was started again (attempt 2);
      its deploy job would have put the older build over the new one.
      Decision: that job was cancelled at 13:57:42, and the seven live
      stage files were compared with `066ef99` after it: equal. Until
      14:07 a browser that had loaded slide 10 in the ten minutes before
      the deploy showed the old figure files in the new layout (the
      lecturer's screenshot of 13:58: the monthly means of `6ab9c2e`,
      694 × 290 pt, cut at both sides by `object-fit: cover`); a reload
      that skips the cache (Cmd+Shift+R) shows the new files. Decision: no
      further push during the lecture, because a deploy replaces the deck's
      hashed files under an open tab.
- [ ] Open: John Snow's cholera map (not drawn); Lecture 3's bulb and
      transistor photos at a higher resolution; `preloadImages` off for phones;
      the zips `weather-s08`…`s12` (need the lecturer's go-ahead to upload);
      Lecture 7's `viz_gallery_nightingale` and `viz_gallery_cern` (Classics
      and Maps): `scripts/measure-figures.mjs` on 10 Nov gives their boxes as
      9.41 × 3.09 and 9.41 × 3.33 in, `figures/src/sizes.json` holds
      9.41 × 3.56 for both: drawn 15 % and 7 % too tall for their box, they
      show smaller, with a margin at each side. Not redrawn on 10 Nov (the
      lecture was hours away and only slide 10 was asked for): re-measure,
      redraw the family `gallery` and look at both figures before pushing.
- [ ] Open: a figure in `public/figures/` keeps its URL when its content
      changes, and GitHub Pages lets a browser keep a file for 10 minutes
      (`max-age=600`): after a deploy that changes a slide's layout
      together with its figure, a browser that loaded the slide shortly
      before shows the old figure in the new layout (10 Nov, 13:58, above).
      A remedy: a content hash in the figure's URL at build time
      (`viz_x.svg?v=<hash>`), written by `scripts/gen-entries.mjs` or a
      Vite plugin.
