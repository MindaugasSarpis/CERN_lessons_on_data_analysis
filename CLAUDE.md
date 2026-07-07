# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

University-level lecture course "Best Research and Data Analysis Practices from CERN" — a 16-lecture + 16-seminar course delivered as interactive slide decks using **Slidev**, with a companion student workbook built with **MkDocs**. The course's spine is four aims: 🔧 tool-agnosticism, ♻️ reproducibility, ⚙️ automation, 📁 efficient work with data & files.

**Delivery architecture (blocked per-lecture decks):** the site is a static **landing page** (`dist/index.html`) plus **one independently-built Slidev deck per lecture** at `dist/<slug>/`. This fixes mobile load — a visitor downloads only one lecture (~4–28M) instead of a single 500+-slide monolith. The set of decks is defined by the manifest **`lectures/content/decks.json`**; lectures are grouped into blocks A–E on the landing page (advanced blocks last / optional).

## Commands

All commands run from the repository root.

```bash
pnpm install                 # install dependencies

pnpm build                   # build ALL decks + landing → dist/ (scripts/build-all.mjs)
pnpm qa                      # build every deck at base '/' + gate each for overflow (scripts/qa-all.mjs) (includes the landing smoke test)
pnpm qa --only 06-version-control       # QA just one deck (much faster edit loop)
pnpm qa:shots                # same + write .qa-shots/<slug>/slide-NNN.png for visual review
pnpm timing                  # estimate delivery minutes per deck + seminar vs the 2h slot (scripts/timing-report.mjs; decks come from decks.json)
pnpm timing:check            # same, exit 1 if any week is UNDER the band
pnpm build:landing          # rebuild only the landing page + its WebGL bundle → dist/
pnpm videos:fetch <url> --name <Name> --used-in LNN   # yt-dlp → videos/raw/ + manifest entry; then videos:encode + videos:publish (needs yt-dlp + ffmpeg)
pnpm figures                 # regenerate all scripted lecture figures (figures/src/ → public/figures/viz_*.svg; --only <family> to scope)
pnpm figures:lhcb            # regenerate the synthetic LHCb D0→K-π+ figures (lhcb_d0_spectrum/fit.png)

pnpm dev 6                   # dev-serve ONE lecture (scripts/dev.mjs; number, slug, or substring — regenerates entries first)
pnpm dev                     # list all decks

pnpm dev:combined            # dev-serve the combined all-16 authoring deck
pnpm build:combined          # optional: single "everything" authoring build (not deployed)
pnpm export                  # export the combined deck to PDF
cd lectures/workbook && mkdocs serve     # student workbook (needs conda env from env.yaml)
```

There are no unit tests or linting; **`pnpm qa` (zero-overflow gate) is the test.** A second gate, **`pnpm timing:check`**, keeps every week's content sized to the 2h lecture + 2h seminar slots (model + band: `docs/superpowers/specs/2026-07-06-course-timing-rebalance-design.md`) — a deck must estimate 105–145 min, a seminar brief must declare ~120 min; slightly over is preferred to under.

### Build pipeline (manifest-driven)

- **`lectures/content/decks.json`** — the manifest: `decks[]` (each `{slug, title, block, srcs[], optional, draft?}`) + `upcoming[]` (roadmap items shown greyed on the landing) + `blocks{}`.
- **`scripts/gen-entries.mjs`** — writes one Slidev entry `lectures/content/deck.<slug>.md` per deck (co-located with `theme/` + `public/` so both resolve at build; a bare `slides/NN_*.md` build drops the theme AND can't resolve `/figures/*`). Entries are **generated + gitignored**, never hand-edited. Merged lectures list multiple `srcs`. Entries set **`routerMode: hash`** — GitHub Pages has no SPA rewrites, so history-mode slide URLs (`/<slug>/5`) 404 on reload; the landing build also emits a root `404.html` that rewrites old-style `/<slug>/5` links to `/<slug>/#/5` (Pages ignores the per-deck `404.html` copies Slidev emits in subdirectories).
- **`scripts/build-all.mjs`** — regenerates entries, builds each deck to `<out>/<slug>/` at base `<prefix>/<slug>/` (absolute `--out`; Slidev resolves a relative `--out` against the entry dir), strips per-deck video copies (served from the remote fallback), then emits the landing via **`scripts/gen-landing.mjs`**. Flags: `--out`, `--base <prefix>`, `--only a,b`, `--flat-base` (base `/` for QA, no landing), `--keep-videos`.
- **`landing/` + `scripts/build-landing.mjs`** — the landing page is an Active Theory-style WebGL page: `landing/` (Three.js particle sim + CSS + fonts) is built by Vite to fixed-name assets; `build-landing.mjs` copies them to `<out>/assets/` and calls `gen-landing.mjs`, which still renders all content (hero, lecture rows) from `decks.json` — the page works fully without JS. `qa-all.mjs` smoke-tests it via `scripts/check-landing.mjs` (links, WebGL boot/fallback gating, reveals, zero console errors).
- **`figures/src/`** — scripted matplotlib pipeline for lecture figures (dark course style via `style.py`; one module per family with a `FIGURES` dict; deterministic output — seeded data, `svg.hashsalt`, no embedded date). Outputs are **committed** as `public/figures/viz_*.svg`; decks never invoke Python at build time.
- **`scripts/qa-all.mjs`** — builds all decks `--flat-base` to `.qa-dist/<slug>`, runs `check-slides.mjs` on each; non-zero exit if any deck overflows.

### Visual QA workflow (per-deck overflow + content/style review)

Verify the **rendered** decks — a `slidev build` only catches compile errors, not slides whose content overflows the 16:9 frame (silently clipped in build and PDF export).

`scripts/check-slides.mjs <distDir>` renders every slide of one built deck with parallel workers + client-side navigation, measures overflow (neutralizing decorative backdrops and pre-click transforms), and optionally writes `.qa-shots/slide-NNN.png`. Options: `--workers N`, `--tolerance PX`, `--only 8,76,...`, `--shots <dir>`. `pnpm qa` runs it across all decks. Media requests are aborted during QA so video slides don't stall the check.

**Hard requirements (see project memory):** (1) **zero slide overflow**; (2) **videos full-screen** — `VideoPlayer.vue` uses `object-fit: cover`, no letterbox line; (3) **consistent type scale** — sizes follow the markdown level, no arbitrary one-off `font-size`; (4) build every deck through its generated `deck.<slug>.md` entry (co-located with `theme/`), never a bare `slides/NN_*.md`.

To review content/style, read the `.qa-shots/**/slide-*.png` in batches (or fan out subagents over batches), not all at once.

## Architecture

### Slide Deck (Slidev)

- **Deck manifest**: `lectures/content/decks.json` (see Build pipeline above) — the source of truth for which decks exist and their order/blocks.
- **Lecture sources**: `lectures/content/slides/NN_Title.md` — one file per lecture, **numbered 01–16 in delivery order** (the numeric prefix is the authoritative sort key). All 16 are live in `decks.json`; 15–16 are marked `optional` (advanced/droppable). `LX_Python_Interactive.md` is a template (not a lecture) for python-runner slides.
- **Combined authoring entry** (optional, not deployed): `lectures/content/best_research_and_data_analysis_practices_from_CERN.md` (imports all 16) and `staging.md` — single-file "everything" builds for authoring/PDF export (`pnpm build:combined`).
- **Seminars**: `lectures/workbook/docs/seminars/` — 16 hands-on briefs + a running-project overview, all building one reproducible analysis of the LHCb D⁰ → K⁻π⁺ open-data sample (invariant-mass peak near 1865 MeV).
- **Design/plan docs**: `docs/superpowers/specs/` and `docs/superpowers/plans/` — the curriculum spec and the P1–P6 implementation plan.
- **Custom theme**: `lectures/content/theme/` — local Slidev theme (`@slidev/theme-scienced`)
  - `styles/custom-slides.css` — card system, grid layouts, spacing utilities, typography
  - `styles/mermaid-styles.css` — Mermaid diagram styling
  - `styles/layouts.css` — layout-specific styles
  - `layouts/` — custom Vue layouts: cover, section, quote, fact, statement, intro, center-bkg
  - `mermaid-config.md` — reusable Mermaid init blocks and classDef styles
- **Components**: `lectures/content/components/MCQ.vue` — multiple-choice question component
- **Static assets**: `lectures/content/public/` — images and backgrounds referenced as `/filename.png` in slides

### Student Workbook (MkDocs)

- `lectures/workbook/` — MkDocs site with lecture companion materials
- `lectures/workbook/mkdocs.yml` — site config and nav
- `lectures/workbook/docs/lectures/` — per-lecture markdown pages

### Miscellaneous

- `misc/exams/` — grading/plotting scripts; the grade CSVs they read are **gitignored (student personal data — never commit them)**
- `misc/python/stable/analysis_example/` — the generator→plot→fit demo chain referenced by the workbook
- `docs/svg-figure-recipe.md` — conventions for hand-built SVG figures in `public/figures/`

## Slide Authoring Conventions

Each lecture markdown file follows a consistent structure:

1. **Frontmatter**: `colorSchema: dark`, `background: /figures/background_intro.jpg`, `theme: ./theme`, `transition: fade`
2. **Cover slide** → **Quote slide** (motivational) → **Motivation slide** (bullet list)
3. **Section breaks**: `layout: section` + `hideInToc: true` + `# Section **KeyWord**`
4. **Content slides** use the card system:
   ```html
   <div class="card card-primary pad-tight">
     ## 📊 **Title**
     Content here
   </div>
   ```
5. **Card colors**: `card-primary`, `card-secondary`, `card-accent`, `card-info`, `card-success`, `card-warning`
6. **Padding**: `pad-tight` (default), `pad-compact` (dense content), `pad-snug`, `pad-balanced`
7. **Grid layouts**: `grid-2`, `grid-3` with `gap-md mt-md`
8. **Emoji format**: Always `## 📊 **Title**` — emoji outside bold
9. **Slide separators**: `---` with optional YAML frontmatter between them

## Slidev Gotchas

- **Monaco runner blocks (`{monaco-run}`)** — three defaults to know: (1) they **autorun on slide load** unless the fence says `{monaco-run} {autorun:false}` (course convention: always opt out); (2) Monaco highlights at **runtime** via a shiki bundle that only ships Slidev's default languages — `lectures/content/setup/shiki.ts` must list every language used in monaco fences, INCLUDING the exact fence alias (` ```py ` needs `'py'` in the list, not just `'python'`); (3) runner output styling (bounded height + scroll) lives in `theme/styles/monaco.css`.
- **Git conflict markers inside fenced code blocks** — Slidev's snippet plugin interprets `<<<<<<< HEAD` as a file-import directive and crashes with `ENOENT`. If you must show a merge conflict in a code block, wrap the markers in a Vue template expression, e.g. `{{'<<<<<<< HEAD'}}`, inside a ```` ```text {*}{lines:false} ```` block.

## Available Tooling

- **Slidev reference skill**: a full Slidev documentation skill is installed at `.agents/skills/slidev/` (SKILL.md + `references/`). Consult it when authoring advanced slide features (Monaco, magic-move, layouts, etc.).

## Deployment

Two GitHub Actions workflows:

- **`.github/workflows/qa.yml`** — runs both gates (`pnpm qa` + `pnpm timing:check`) on every push to the working branch `ff2026` (and on PRs / manual dispatch).
- **`.github/workflows/deploy.yml`** — builds and deploys to GitHub Pages on pushes to the `bs2026` branch. Day-to-day work happens on `ff2026`; a fix is only live after `git push origin ff2026:bs2026` — check the qa.yml result first.

## Adding / removing a lecture

The manifest drives everything, so the checklist is short (full walkthrough in README.md):

1. **Add**: create `lectures/content/slides/NN_Title.md` (copy an existing lecture's frontmatter/cover/quote/motivation skeleton), add a `{slug, title, block, srcs}` entry to `decks.json` (delivery order = array order), write the seminar brief `lectures/workbook/docs/seminars/seminar_NN.md` (declare **~120 min**), and add the workbook page + `mkdocs.yml` nav line. Then `pnpm dev <NN>` to author, `pnpm qa --only <slug>` + `pnpm timing:check` to gate.
2. **Remove**: delete the deck's entry from `decks.json`, delete (or park outside `slides/`) the source file, delete its seminar brief and workbook nav line. `timing-report.mjs` only gates files listed in `decks.json`, so nothing ghost-gates after removal.
