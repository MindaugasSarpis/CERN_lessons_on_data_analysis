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
pnpm qa --only 05-version-control       # QA just one deck (much faster edit loop)
pnpm qa --changed-since origin/main     # QA only the decks whose slides changed vs main (CI does this vs the last green main commit; shared-file changes widen to all)
pnpm qa:shots                # same + write .qa-shots/<slug>/slide-NNN.png for visual review
pnpm timing                  # estimate delivery minutes per deck + seminar vs the 2h slot (scripts/timing-report.mjs; decks come from decks.json)
pnpm timing:check            # same, exit 1 if any week is UNDER the band
pnpm build:landing          # rebuild only the landing page + its WebGL bundle → dist/
pnpm release 5               # staged release: lectures 01–05 live, rest draft (scripts/release.mjs; `all` = all live; no arg = show)
pnpm videos:fetch <url> --name <Name> --used-in LNN   # yt-dlp → videos/raw/ + manifest entry; then videos:encode + videos:publish (needs yt-dlp + ffmpeg)
pnpm videos:encode-hq        # venue-quality HEVC copy (manifest `hq = true` entries) → public/videos-hq/ (gitignored, never published); `pnpm dev` plays it first, a --keep-videos build uses it offline
pnpm figures                 # regenerate all scripted lecture figures (figures/src/ → public/figures/viz_*.svg; --only <family> to scope)
pnpm figures:lhcb            # regenerate the synthetic LHCb D0→K-π+ figures (lhcb_d0_spectrum/fit.png)

pnpm dev 5                   # dev-serve ONE lecture (scripts/dev.mjs; number, slug, or substring — regenerates entries first)
pnpm dev                     # list all decks

pnpm dev:combined            # dev-serve the combined all-16 authoring deck
pnpm build:combined          # optional: single "everything" authoring build (not deployed)
pnpm export                  # export the combined deck to PDF
cd lectures/workbook && mkdocs serve     # student workbook (needs mkdocs + mkdocs-material, e.g. conda env from env.yaml); deployed at <site>/workbook/ by build-all when mkdocs is on PATH (CI installs it)
```

There are no unit tests or linting; **`pnpm qa` (zero-overflow gate) is the test.** A second gate, **`pnpm timing:check`**, keeps every week's content sized to the 2h lecture + 2h seminar slots (model + band: `docs/superpowers/specs/2026-07-06-course-timing-rebalance-design.md`) — a deck must estimate 105–145 min, a seminar brief must declare ~120 min; slightly over is preferred to under.

### Build pipeline (manifest-driven)

- **`lectures/content/decks.json`** — the manifest: `decks[]` (each `{slug, title, block, srcs[], optional, draft}`) + `blocks{}`. **`draft: true` = staged release**: the deck is still built + gated by `pnpm qa` / `pnpm timing:check` (so it can't rot while being edited), but a deploy build skips it (no `dist/<slug>/`, no 404 rewrite), and the landing + in-deck ☰ menu list it greyed/unlinked as "coming soon". Flip to `false` on delivery day and redeploy. `pnpm build --include-drafts` previews the full site locally. Optional **`seminar`** = the number of the workbook page the in-deck ☰ menu links (`seminar_NN.md`); `null` = no link (L01), unset = the deck's own number. The link is only emitted when the page exists, and an explicit `seminar` naming a missing page fails `gen-entries.mjs`.
- **`scripts/gen-entries.mjs`** — writes one Slidev entry `lectures/content/deck.<slug>.md` per deck (co-located with `theme/` + `public/` so both resolve at build; a bare `slides/NN_*.md` build drops the theme AND can't resolve `/figures/*`). Entries are **generated + gitignored**, never hand-edited, and are the **only** place deck-level config (theme, routerMode, colorSchema, addons, title) lives. Merged lectures list multiple `srcs`. Entries set **`routerMode: hash`** — GitHub Pages has no SPA rewrites, so history-mode slide URLs (`/<slug>/5`) 404 on reload; the landing build also emits a root `404.html` that rewrites old-style `/<slug>/5` links to `/<slug>/#/5` (Pages ignores the per-deck `404.html` copies Slidev emits in subdirectories).
- **`scripts/build-all.mjs`** — regenerates entries, builds each deck to `<out>/<slug>/` at base `<prefix>/<slug>/` (absolute `--out`; Slidev resolves a relative `--out` against the entry dir), strips per-deck video copies (`videos/` + `videos-hq/`, served from the remote fallback), then emits the landing via **`scripts/gen-landing.mjs`**. Flags: `--out`, `--base <prefix>`, `--only a,b`, `--flat-base` (base `/` for QA, no landing; always includes drafts), `--include-drafts`, `--keep-videos` (with `VITE_VIDEOS_LOCAL_FIRST=1` in the env the kept copies are played first — an offline backup build).
- **`landing/` + `scripts/build-landing.mjs`** — the landing page is an Active Theory-style WebGL page: `landing/` (Three.js particle sim + CSS + fonts) is built by Vite to fixed-name assets; `build-landing.mjs` copies them to `<out>/assets/` and calls `gen-landing.mjs`, which still renders all content (hero, lecture rows) from `decks.json` — the page works fully without JS. `qa-all.mjs` smoke-tests it via `scripts/check-landing.mjs` (links, WebGL boot/fallback gating, reveals, zero console errors). **Sound** lives in `landing/src/sound.js` (Web Audio, synthesised, no assets): a low hum (~8 s, once per visit) on the first click/tap/key press that is not a lecture row, or on open when arriving from a deck link, plus a short swoosh under the row-click fade-out. Browsers block audio until a gesture (hover/scroll don't count), so nothing can play on a cold open; reduced motion plays nothing. `check-landing.mjs` passes 5-7 assert both via `?qa` sessionStorage records.
- **`figures/src/`** — scripted matplotlib pipeline for lecture figures (dark course style via `style.py`; one module per family with a `FIGURES` dict; deterministic output — seeded data, `svg.hashsalt`, no embedded date). Outputs are **committed** as `public/figures/viz_*.svg`; decks never invoke Python at build time. Families by lecture: `arrays` (07), `handson` and the chart families (08), `probability` (09), `fitting` (10), `perceptron` (11), `cleaning` (12), `concepts` (14), `computing` (15), `ml` (16); most of these modules also print every number their slides state when run directly (`python figures/src/fitting.py`). `pnpm figures` runs bare `python3`; `fitting`, `concepts` and `ml` need scipy (and `ml` scikit-learn), `associations` needs seaborn — regenerate those with an env that has them (the conda env `rework`: `~/miniconda3/envs/rework/bin/python figures/src/build.py --only fitting`).
- **`scripts/qa-all.mjs`** — builds all decks `--flat-base` to `.qa-dist/<slug>`, runs `check-slides.mjs` on each; non-zero exit if any deck overflows. `--changed-since <ref>` scopes it to the decks whose slide sources changed (working tree vs merge-base; `scripts/changed-decks.mjs`) — any change to theme, components, setup, `public/`, build/QA scripts, `landing/`, `decks.json`, deps or workflows widens to every deck; zero affected decks still smoke-tests the landing. `qa.yml` passes the last green `main` commit (or the PR base).

### Visual QA workflow (per-deck overflow + content/style review)

Verify the **rendered** decks — a `slidev build` only catches compile errors, not slides whose content overflows the 16:9 frame (silently clipped in build and PDF export).

`scripts/check-slides.mjs <distDir>` renders every slide of one built deck with parallel workers + client-side navigation, measures overflow (neutralizing decorative backdrops and pre-click transforms), and optionally writes `.qa-shots/slide-NNN.png`. Options: `--workers N`, `--tolerance PX`, `--only 8,76,...`, `--shots <dir>`. `pnpm qa` runs it across all decks. Media requests are aborted during QA so video slides don't stall the check.

`scripts/check-overview.mjs <distDir>` gates the cost of Slidev's all-slides **overview** on a phone (no `<video>` or media request inside the overview, no card blur there, thumbnails `content-visibility: auto`); `pnpm qa` runs it once per run on the first video deck under QA. The guards live in `custom-slides.css` (overview block) and `VideoPlayer.vue` (placeholder outside the `slide`/`presenter` render context).

**Video source chain** (`VideoPlayer.vue`): `pnpm dev` tries `videos-hq/<src>` → `videos/<src>` → GitHub release; a production build tries the release first, then the two local dirs (only present in a `--keep-videos` build — the lecture-day offline fallback); `VITE_VIDEOS_LOCAL_FIRST=1` at build time flips a `--keep-videos` build to local-first. Each `<source>` error advances the chain. Clips autoplay on slide activation; `<VideoPlayer :autoplay="false">` makes one wait for the presenter's click (L01's cold open) — it preloads so the first frame and controls show.

**Hard requirements (see project memory):** (1) **zero slide overflow**; (2) **videos full-screen** — `VideoPlayer.vue` uses `object-fit: cover`, no letterbox line; (3) **consistent type scale** — sizes follow the markdown level, no arbitrary one-off `font-size`; (4) build every deck through its generated `deck.<slug>.md` entry (co-located with `theme/`), never a bare `slides/NN_*.md`.

To review content/style, read the `.qa-shots/**/slide-*.png` in batches (or fan out subagents over batches), not all at once.

## Architecture

### Slide Deck (Slidev)

- **Deck manifest**: `lectures/content/decks.json` (see Build pipeline above) — the source of truth for which decks exist and their order/blocks.
- **Lecture sources**: `lectures/content/slides/NN_Title.md` — one file per lecture, **numbered 01–16 in delivery order** (the numeric prefix is the authoritative sort key): 01 Orientation, 02 Introduction to Data, 03 How Computers Work, 04 Command Line & Files, 05 Git, 06 Python Foundations, 07 Python for Data & NumPy, 08 Visualisation, 09 Probability & Statistics, 10 Fitting from First Principles, 11 The Perceptron, 12 Pandas & Data Cleaning, 13 Reproducible Workflows; 14–16 (Concepts of Data Analysis, Computing Infrastructure, Machine Learning & AI) are block E "Further Topics", marked `optional` and not scheduled. The order and what each week may assume are fixed in `docs/superpowers/specs/2026-10-04-course-rework-first-principles-design.md` — read it before reworking a deck. `LX_Python_Interactive.md` is a template (not a lecture) for python-runner slides.
- **Parked slides**: `lectures/content/parked/NN_Title.md` — slides taken out of a deck (to keep it in the timing band, or after feedback). Not in `decks.json`, so not built, gated or deployed; a header comment says where each slide stood. To restore one, move it back into the lecture file.
- **Combined authoring entry** (optional, not deployed): `lectures/content/best_research_and_data_analysis_practices_from_CERN.md` (imports all 16) and `staging.md` — single-file "everything" builds for authoring/PDF export (`pnpm build:combined`).
- **Seminars**: `lectures/workbook/docs/seminars/seminar_NN.md` + `overview.md` — one follow-along page per seminar, written for the person at the front (lead paragraph, numbered steps, "You should now see", one "Watch for"). A page carries the number of its lecture, except Seminar 1, which pairs with Lecture 02; there is no Seminar 2. The follow-along uses two shared files, the pendulum table and the LHCb D⁰ → K⁻π⁺ file (`M, PT, TAU, IPCHI2` only); at home students repeat each step on a dataset of their own. Each student's semester project is separate and entirely their own choice (topic, data, form) — never frame the D⁰ analysis as the course project.
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

- `lectures/workbook/` — MkDocs (Material, dark) site with the seminar briefs + lecture companion notes; built to `dist/workbook/` by `build-all.mjs` when `mkdocs` is on PATH (or `$MKDOCS`), gated by `mkdocs build --strict` in qa.yml, linked from the landing footer
- `lectures/workbook/mkdocs.yml` — site config and nav
- `lectures/workbook/docs/lectures/lecture_N.md` — one page per lecture (N = its number, no leading zero): what it covers, the 90-minute plan with slide numbers and a skip list, "Check yourself", the paired seminar, take-aways. Slide numbers on a page must be recounted whenever its deck gains or loses a slide

### Miscellaneous

- `misc/exams/` — grading/plotting scripts; the grade CSVs they read are **gitignored (student personal data — never commit them)**
- `misc/python/stable/analysis_example/` — the generator→plot→fit demo chain referenced by the workbook
- `docs/svg-figure-recipe.md` — conventions for hand-built SVG figures in `public/figures/`
- `docs/delivery-log.md` — one entry per delivered session (planned, what happened, changed in response, open). Append the lecturer's notes after each lecture and read a lecture's entries before reworking it. The repository is public: no student names
- `lectures/workbook/docs/data/` — files the seminars hand out, named by topic: `pendulum*` (the table cleaned by hand in Seminar 1; `pendulum.csv` is the answer key; `pendulum_plot.py` regenerates the plot and its copy in `public/figures/`), `D0_KPi.csv` (the LHCb file, `root_to_csv.py`), `cli_*` (S4), `perceptron_*` (S11, with the seeded script that makes the points), `workflows_*` (S13: the stage scripts, `run_all.py`, the tests), `concepts_*` (S14), `hpc_*` (S15), `ml_*` (S16). A data file is committed together with the script that makes it

## Slide Authoring Conventions

Each lecture markdown file follows a consistent structure:

1. **Cover frontmatter** — only `layout: cover` + `title: "…"` (same string as the deck's `title` in `decks.json`; `gen-entries.mjs` warns on drift). Decks with `{monaco-run}` Python fences add a `python:` block (installs/prelude) here, because the runner addon reads it from slide 1, which is this cover. **No deck-level config in lecture files** (`theme`, `colorSchema`, `background`, `addons`, `drawings`, `mermaid`, `transition`): it lives only in the generated entry's headmatter (`scripts/gen-entries.mjs`) and is dead once the lecture is imported via `src:` — Slidev takes config from the entry's headmatter alone.
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
10. **Quizzes close the deck, never interrupt it**: `<MCQ>` slides go after the Recap, under a `layout: section` slide titled exactly `# Check **Yourself**`. `timing-report.mjs` counts that section and everything after it as 0 min (self-study, not delivered), so a quiz moved out of the lecture has to be replaced by content, not by nothing. The same questions with answers go on the lecture's workbook page under "Check yourself". Done for L01–L03; L04–L16 still carry inline quizzes until each is reworked.
11. **Content standard**: derive, do not assert. A new slide carries a worked example with real numbers (computed, not guessed) and connects to the slide before it, so a section reads like a textbook chapter and not like a list of facts.

## Slidev Gotchas

- **Monaco runner blocks (`{monaco-run}`)** — three defaults to know: (1) they **autorun on slide load** unless the fence says `{monaco-run} {autorun:false}` (course convention: always opt out); (2) Monaco highlights at **runtime** via a shiki bundle that only ships Slidev's default languages — `lectures/content/setup/shiki.ts` must list every language used in monaco fences, INCLUDING the exact fence alias (` ```py ` needs `'py'` in the list, not just `'python'`); (3) runner output styling (bounded height + scroll) lives in `theme/styles/monaco.css`; (4) **matplotlib figures** reach the runner output only because `lectures/content/setup/code-runners.ts` wraps the addon's Python runner and points `document.pyodideMplTarget` at a per-run container — without it `plt.show()` draws into `document.body`, below the slide frame (the "plot doesn't show" bug). Figure chrome/sizing is styled under `.slidev-python-figures` in `monaco.css`; the output box is capped at 11rem, so a plotting fence should stay ≲10 lines or the box (and the figure) sits below the frame at runtime.
- **Class names that UnoCSS reads as utilities** — a custom class such as `md-h1` is parsed as "height 0.25rem at the `md` breakpoint" and silently collapses the element. Do not start a class name with a breakpoint prefix (`sm-`, `md-`, `lg-`, `xl-`); the rendered-Markdown boxes of L02 use `rendered-md` / `rendered-title` for that reason.
- **A slide that just fits on macOS can overflow on CI** — the runner's Linux fonts set some slides 15–20 px taller (seen on a figure slide of L11 and a long quiz question of L13, both green locally and red in `qa.yml`). Leave about 25 px of room at the bottom of a full slide, and keep a quiz question to three lines.
- **Tables inside cards** render at slide scale and overflow. Add `table-compact` to the card for a reference table on the card's body scale (L02 key sheet).
- **Markdown inside one-line HTML** — a single-line `<div class="note-text">text with *em* or `code`</div>` is an HTML block: markdown is NOT parsed and prints literal asterisks/backticks. Either use `<em>/<strong>/<code>` inside the div, or put blank lines between the tags and the text (multi-line form) so markdown-it parses it. Same for the `question=` prop of `<MCQ>` — it accepts `code` spans only (the component converts them); no other markdown.
- **`$$` math blocks inside HTML** — Slidev ≥ 52.19 wraps `$$ … $$` in a KaTeX wrapper component; a `$$` line directly after an opening tag (no blank line), or an empty line inside the math, makes the build fail with `Element is missing end tag`. Always leave a blank line between a tag and `$$`, and keep the math contiguous.
- **Mermaid styling is global** — the course look for every diagram lives in `lectures/content/setup/mermaid.ts` (`themeVariables` + `themeCSS`); the canonical semantic `classDef`s are in `theme/mermaid-config.md`. Slidev renders each diagram into a **shadow root**, so page CSS (`mermaid-styles.css`) cannot style nodes/edges — it only holds the light-DOM measuring container's label font + a measure-only padding (Chrome lays out scaled foreignObject text a few px wider than measured, which clips the last glyph without it). Don't add `%%{init: …}%%` colour blocks to fences; layout-only directives (spacing, `showCommitLabel`) are fine.
- **Git conflict markers inside fenced code blocks** — Slidev's snippet plugin interprets `<<<<<<< HEAD` as a file-import directive and crashes with `ENOENT`. Fenced code is `v-pre`, so the old `{{'<<<<<<< HEAD'}}` trick renders literally — do NOT use it. Show a conflict as a raw HTML block instead: `<pre class="slidev-code"><code>&lt;&lt;&lt;&lt;&lt;&lt;&lt; HEAD … &gt;&gt;&gt;&gt;&gt;&gt;&gt; branch</code></pre>` (see L05 "Merge Conflicts — What They Look Like").

## Available Tooling

- **Slidev reference skill**: a full Slidev documentation skill is installed at `.agents/skills/slidev/` (SKILL.md + `references/`). Consult it when authoring advanced slide features (Monaco, magic-move, layouts, etc.).

## Deployment

One branch (`main`) and one GitHub Actions workflow:

- **`.github/workflows/qa.yml`** — on every push to `main` (and on PRs / manual dispatch) runs both gates (`pnpm qa` + `pnpm timing:check`); then, on `main` only, a `build` job (`needs: qa`) builds all decks + landing + workbook and a `deploy` job publishes to GitHub Pages. A push is live ~8 min later **only if the gates are green**; a red run deploys nothing and the previous site stays up.
- **No second branch.** `git push origin main` is the deploy. Keep unfinished edits to a live deck on a PR branch (gates run there, no deploy); drafts are safe to push. `gh workflow run qa.yml --ref main` redeploys without a commit. `ff2026` (old work branch) and `bs2026` (old deploy branch) are frozen at the 2026-09-06 cutover — nothing deploys from them.

## Releasing lectures during the semester

`pnpm release <NN>` marks lectures 01–NN live and the rest draft (`pnpm release all` = all live; no arg = show state) — or edit `"draft"` by hand. On lecture day: `pnpm release NN`, commit on `main`, `git push origin main` — live once `qa.yml` is green (~8 min). Drafts stay fully gated in CI, so keep editing them freely. `pnpm dev <NN>` works on drafts; `pnpm build --include-drafts` builds a full local preview.

## Adding / removing a lecture

The manifest drives everything, so the checklist is short (full walkthrough in README.md):

1. **Add**: create `lectures/content/slides/NN_Title.md` (copy an existing lecture's frontmatter/cover/quote/motivation skeleton), add a `{slug, title, block, srcs}` entry to `decks.json` (delivery order = array order), write the seminar brief `lectures/workbook/docs/seminars/seminar_NN.md` (declare **~120 min**), and add the workbook page + `mkdocs.yml` nav line. Then `pnpm dev <NN>` to author, `pnpm qa --only <slug>` + `pnpm timing:check` to gate.
2. **Remove**: delete the deck's entry from `decks.json`, delete (or park outside `slides/`) the source file, delete its seminar brief and workbook nav line. `timing-report.mjs` only gates files listed in `decks.json`, so nothing ghost-gates after removal.
