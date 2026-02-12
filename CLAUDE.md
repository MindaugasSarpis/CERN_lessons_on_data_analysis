# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

University-level lecture course "Lessons on Data Analysis from CERN" — 12 lectures delivered as interactive slide decks using **Slidev**, with a companion student workbook built with **MkDocs**.

## Commands

All commands run from the repository root. There are no npm scripts defined; use Slidev CLI directly via pnpm/npx.

```bash
# Install dependencies
pnpm install

# Dev server (serves the main deck at localhost:3030)
npx slidev lectures/content/lessons_on_data_analysis_from_CERN.md

# Dev server for a single lecture
npx slidev lectures/content/slides/L9_Probability_and_Statistics.md

# Production build
npx slidev build lectures/content/lessons_on_data_analysis_from_CERN.md

# Export to PDF
npx slidev export lectures/content/slides/L9_Probability_and_Statistics.md

# Student workbook (MkDocs) — requires conda env from env.yaml
cd lectures/workbook && mkdocs serve
```

There are no tests or linting configured.

## Architecture

### Slide Deck (Slidev)

- **Entry point**: `lectures/content/lessons_on_data_analysis_from_CERN.md` — master deck that imports all lectures via `src:` frontmatter directives
- **Individual lectures**: `lectures/content/slides/L{N}_*.md` — each is a standalone Slidev markdown file (L1–L12, plus LX template)
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

Each lecture markdown file follows a consistent structure (see `PLAN.md` for the full reference):

1. **Frontmatter**: `colorSchema: dark`, `background: /background_intro.jpg`, `theme: ./theme`, `transition: fade`
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

## Deployment

GitHub Actions workflow (`.github/workflows/deploy.yml`) builds and deploys to GitHub Pages from the `ff2025` branch.
