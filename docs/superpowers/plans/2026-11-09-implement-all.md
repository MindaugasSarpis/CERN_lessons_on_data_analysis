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

- [ ] Lecture 7 laconic: every main-path caption one or two lines, reasons in
      the notes; code slides in `# In **Matplotlib**` after For the Curious;
      the four-variable figures on the main path; `lecture_7.md` recounted.
- [ ] Lecture 7 interactive: `BinWidthExplorer`, `AxisStartBars`,
      `PaletteHeatmap`, `SmoothingWindow` (if ready) on their slides.
- [x] Lecture 1: the twelve Tuesdays; CERN facts of Nov 2026.
- [x] Cover number from the slug.
- [ ] Ship from the worktree `deploy-l07` (origin/main + only these files);
      verify; rebase `main` on it.

## Batch 2 — invisible improvements

- [ ] Mobile load: `lectures/content/vite.config.ts` chunk override (tested
      in the research scratch build: L07's first load 3.69 → 0.20 MB).
- [ ] Theme defaults in `theme/package.json` `slidev.defaults`: `titleTemplate`,
      a local favicon, `timer: countdown`; per-deck `duration` from the timing
      estimate in `gen-entries.mjs`.
- [ ] Tools: `pnpm review`, `pnpm week`, `scripts/shots-diff.py`; CLAUDE.md
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
- [ ] Figures baseline: every family redrawn once with the canonical
      `figures` environment; screenshots compared.
- [ ] Lecture 1 (and 02, 03, 15): the toolkit's video addon and library clips
      (H.264, no freeze after ~10 clips); L03's HEVC clip re-encoded.
- [ ] Lecture 1's cover: the toolkit's live particle field (`StageHero`),
      L01 only, static fallback without WebGL.
- [ ] Fact citations for CERN numbers (L01, L02, L14–16) against the facts
      bank of `outreach_talks`; `pages_check.mjs` in CI.

## Batch 4 — weeks 8–12 and the interactive components

- [ ] Integrate the five week builders' decks, seminar pages, lecture pages
      and start folders; QA and timing for every deck.
- [ ] `MeanSpread` (8), `FitLine` (9), `PerceptronPlayground` (10),
      `SoftmaxTemperature` (11) on their slides.
- [ ] Zips `weather-s08`…`s12` uploaded to the release `seminar-files`.
- [ ] Deploy (drafts stay drafts); release week 8 on 16 Nov with `pnpm week 8`.
- [ ] The interactive components back to the toolkit `slidev-videos` on a
      worktree branch, for the lecturer's approval.
- [ ] Seminar pages machine-checkable (a marker per code block) and a replay
      command.
