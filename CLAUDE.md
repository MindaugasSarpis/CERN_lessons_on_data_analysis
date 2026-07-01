# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

University-level lecture course "Lessons on Data Analysis from CERN" — 12 lectures delivered as interactive slide decks using **Slidev**, with a companion student workbook built with **MkDocs**.

## Commands

All commands run from the repository root.

```bash
# Install dependencies
pnpm install

# Dev server for the published deck (current-term subset)
pnpm dev

# Dev server for the full WIP deck (all lectures, incl. drafts)
pnpm dev:staging

# Dev server for a single lecture file
pnpm dev:lecture lectures/content/slides/L09_Probability_and_Statistics.md

# Production build (published deck only)
pnpm build

# Export to PDF
pnpm export

# Student workbook (MkDocs) — requires conda env from env.yaml
cd lectures/workbook && mkdocs serve
```

There are no tests or linting configured.

### Visual QA workflow (whole-deck overflow + content/style review)

When iterating on styling, verify the **rendered** deck — a `slidev build` only catches compile errors, not slides whose content overflows the 16:9 frame (silently clipped in the build and PDF export).

```bash
pnpm qa            # build the published deck + render every slide: overflow report + a screenshot per slide in .qa-shots/
pnpm qa:overflow   # overflow report only (needs a prior `pnpm qa:build`), ~8s for the full deck
```

`scripts/check-slides.mjs` renders all slides with parallel workers + client-side navigation (fast — full 482-slide deck in ~8s), measures each slide root's overflow (neutralizing decorative backdrops and pre-click transforms), and optionally writes `.qa-shots/slide-NNN.png` for visual review. Options: `--workers N`, `--tolerance PX`, `--only 8,76,...`, `--shots <dir>`. Exit code is non-zero if any slide overflows, so it works as a gate.

**Hard requirements enforced by this workflow (see project memory):** (1) **zero slide overflow**; (2) **videos full-screen** — `VideoPlayer.vue` uses `object-fit: cover`, no letterbox line; (3) **consistent type scale** — sizes follow the markdown level, no arbitrary one-off `font-size`. Must build through an entry point co-located with `theme/` (e.g. the published deck) — a single `slides/L0X.md` build silently drops the custom theme.

To review content/style across the deck, read the `.qa-shots/*.png` in batches (or fan out subagents over batches), not all at once.

## Architecture

### Slide Deck (Slidev)

- **Published entry point**: `lectures/content/lessons_on_data_analysis_from_CERN.md` — the deck that `pnpm build` ships to GitHub Pages. It imports only the subset of lectures currently delivered in-term.
- **Staging entry point**: `lectures/content/staging.md` — full WIP deck importing every lecture file (including parallel drafts of L6 and L11). Use `pnpm dev:staging` to preview everything.
- **Individual lectures**: `lectures/content/slides/L{NN}_*.md` — each is a standalone Slidev markdown file. Numbering is zero-padded to two digits (`L01_`…`L12_`). Lecture 3 is split into sub-lectures (`L03_1_1_`, `L03_1_2_`, `L03_2_`, `L03_3_`, `L03_4_`). The `LX_Python_Interactive.md` file is a template, not part of the course. Lecture ordering occasionally shifts between terms — the numeric prefix is the authoritative sort key, independent of delivery order.
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

- `misc/exams/` — quiz YAML definitions and grading scripts
- `misc/python/` — standalone Python examples for students

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

- **Git conflict markers inside fenced code blocks** — Slidev's snippet plugin interprets `<<<<<<< HEAD` as a file-import directive and crashes with `ENOENT`. If you must show a merge conflict in a code block, wrap the markers in a Vue template expression, e.g. `{{'<<<<<<< HEAD'}}`, inside a ```` ```text {*}{lines:false} ```` block.

## Available Tooling

- **Slidev reference skill**: a full Slidev documentation skill is installed at `.agents/skills/slidev/` (SKILL.md + `references/`). Consult it when authoring advanced slide features (Monaco, magic-move, layouts, etc.).

## Deployment

GitHub Actions workflow (`.github/workflows/deploy.yml`) builds and deploys to GitHub Pages on pushes to the `bs2026` branch.
