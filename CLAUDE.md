# CLAUDE.md

Guidance for Claude Code in this repository. The rules are short here; their full wording, reasons, dates and the lecturer's words are in `docs/authoring.md` (same headings), which still holds.

## Project Overview

University course "Best Research and Data Analysis Practices from CERN": Slidev lecture decks plus an MkDocs student workbook (a seminar page per week), on four aims: 🔧 tool-agnosticism, ♻️ reproducibility, ⚙️ automation, 📁 efficient work with data & files. The site is a landing page (`dist/index.html`) and one independently built deck per lecture at `dist/<slug>/`; the manifest `lectures/content/decks.json` defines the decks, their order and blocks A–E.

## Commands

From the repository root:

```bash
pnpm install                  # pnpm pinned in package.json (`packageManager`); settings in pnpm-workspace.yaml
pnpm dev 5                    # dev-serve ONE deck (number, slug or substring); `pnpm dev` lists the decks
pnpm review 7                 # one deck: build, overflow gate, screenshots, contact sheets, timing line
pnpm review 7 --since prev    # + what changed since the run before (or a folder, or a git ref); --from N --to M
pnpm qa                       # every deck at base '/' + overflow gate + landing smoke test (scripts/qa-all.mjs)
pnpm qa --only 06-version-control        # one deck
pnpm qa --changed-since origin/main      # decks whose slides changed (CI: vs the last green main)
pnpm qa:shots                 # same + .qa-shots/<slug>/slide-NNN.png
pnpm qa:runners --only 03-how-computers-work   # press ▶ on every runner block (needs the Pyodide CDN; not in CI)
pnpm timing                   # estimated minutes per deck + seminar vs the 2h slot (scripts/timing-report.mjs)
pnpm timing:check             # same, exit 1 if any week is UNDER the band
python3 scripts/contact-sheets.py <slug> [--from N --to M]         # four screenshots per PNG (Pillow)
python3 scripts/shots-diff.py <old_dir> <new_dir> [--threshold 0.001]   # changed slides, side by side
pnpm build                    # all decks + landing (+ workbook if mkdocs is on PATH) → dist/; build:landing = landing
pnpm release 5                # lectures 01–05 live, the rest draft (`all` = all live; no arg = show)
pnpm week 8 --dry-run         # release day: release 8 + the workbook's "This week"; --verify after the push
~/micromamba/envs/figures/bin/python figures/src/build.py --only <family>   # regenerate scripted figures
pnpm figures | figures:lhcb   # the same with bare python3 (no seaborn, SciPy) | the LHCb D0 PNGs
pnpm videos:fetch <url> --name <Name> --used-in LNN    # then videos:encode, videos:publish; videos:encode-hq
pnpm dev:combined | build:combined | export   # the combined all-16 authoring deck (not deployed; export = PDF)
cd lectures/workbook && mkdocs serve          # the workbook (mkdocs-material, e.g. the conda env of env.yaml)
```

No unit tests or linting: **`pnpm qa` (zero overflow) is the test**, **`pnpm timing:check`** the second gate: a deck estimates 105–145 min, a seminar page declares `<!-- ~120 min -->` under its header; slightly over beats under. A hands-on week moves time to its seminar with `"split": {"lecture": 105, "seminar": 135}` on its deck (the band scales, 92–127 for 105; the seminar declares at least its minutes). Model: `docs/superpowers/specs/2026-07-06-course-timing-rebalance-design.md`. Full comments: `docs/authoring.md#commands`.

### Build pipeline

- `decks.json`: `decks[]` of `{slug, title, block, srcs[], optional, draft}` (+ `seminar`, `split`); array order = delivery order. `draft: true`: built and gated, not deployed, "coming soon" on the landing and ☰ menu; flip it on release day. `seminar`: the workbook page the ☰ menu links (`null` none, unset = own number; naming a missing page fails `gen-entries.mjs`).
- `scripts/gen-entries.mjs` writes `lectures/content/deck.<slug>.md`: generated, gitignored, **never hand-edited, the only place for deck-level config**.
- Glossary: `lectures/content/glossary/NN.md`, one hand-edited table `| Term | Meaning | First on |` (8–25 rows; First on = the `# ` title of the slide that explains the term). `scripts/gen-glossary.mjs` (run by `gen-entries.mjs`; alone `pnpm glossary`) appends the deck's Glossary slides after the quizzes (0 min) and writes the workbook's A–Z `glossary.md`; a First-on matching no slide is a warning, so re-run it after renaming a title.
- Theme defaults in `theme/package.json` (`slidev.defaults`): tab title, favicon, countdown timer; `gen-entries.mjs` writes each deck's `duration` from `scripts/timing-model.mjs` (shared with `timing-report.mjs`). `lectures/content/vite.config.mts` keeps Shiki and the Monaco types out of slide 1 (0.2 MB of JavaScript first, not 3.6 MB; L07 on a slow phone 4 s, not 41 s). `patches/@slidev__client@53.0.0.patch` fixes the countdown past zero: move its key when Slidev is upgraded.
- `scripts/build-all.mjs` builds each deck to `<out>/<slug>/` and the landing (it empties `<out>` first); `--flat-base` = the QA build, `--keep-videos` = offline backup, `--review` = CI's unlisted report page `dist/ataskaita/` (its private files stay in the gitignored `misc/description/mokslines_iniciatyvos_paraiska/`).
- `figures/src/`: one module per family, deterministic, SVGs committed to `public/figures/viz_*.svg`, no Python at build time. **Regenerate only with the canonical env** `~/micromamba/envs/figures/bin/python figures/src/build.py --only <family>` (made 9 Nov 2026). A family's first regeneration rewrites all its pre-9-Nov SVGs: commit them, or `git checkout` the ones you did not mean to change.
- Flags, landing, families, CI scoping: `docs/authoring.md#build-pipeline`.

### Visual QA

- Check the **rendered** deck: `slidev build` misses overflow (clipped silently).
- **Figures fill the rest of the slide**: frontmatter `class: fill`, the figure block `fig-fill`, no inline `max-height`. After a layout change: a `--flat-base` build, then `node scripts/measure-figures.mjs --only <slug>` in the same command (any build empties `.qa-dist`), then regenerate. One plot beside its caption (`grid-side`, ~3:2); several panels under it, full width.
- Read screenshots in batches (contact sheets; `--since` for the changed ones; subagents), never all at once.
- **Hard requirements:** (1) zero slide overflow; (2) videos full-screen (`object-fit: cover`, no letterbox line); (3) one type scale: sizes follow the markdown level, no one-off `font-size`; (4) build through the generated `deck.<slug>.md`, never a bare `slides/NN_*.md`. (5) **Fidelity: every figure vector and crisp** (lecturer, 9 Nov 2026, for all slides): no `rasterized=True`, no `imshow`, no GIF/PNG/canvas plots; animation and 3D as SVG components; `grep -c '<image' viz_*.svg` = 0; only photos are bitmaps, at ≥ 2× their displayed size.

Checkers, video chain: `docs/authoring.md#visual-qa`.

## Architecture

### Lectures

- `lectures/content/slides/NN_Title.md`, the prefix = delivery order: 01 Orientation, 02 Introduction to Data, 03 How Computers Work, 04 Command Line & Files, 05 Python Foundations, 06 Git, 07 Data Visualisation, 08 Data Quality and Uncertainty, 09 Parameter Estimation and Fitting, 10 Classification and the Perceptron, 11 From Neurons to Language Models, 12 Code That Lasts; no 13; 14–16 optional (block E). The NumPy and Pandas decks are parked in `lectures/content/parked/decks/` (Seminars 8–9 teach those tools); single slides in `lectures/content/parked/`.
- **Since 9 Nov 2026 a lecture teaches the idea, a seminar the tools** (spec `docs/superpowers/specs/2026-11-09-weeks-8-12-ideas-and-tools-design.md`): a lecture is a textbook chapter, **each mathematical expression followed by a real number or list from the weather log pushed through it**, plain Python, **no library calls on a slide**; a seminar brings the real library, **one per week**, one step at a time like the Python Tutorial and HSF training, for first-time coders. Weeks 1–7: `2026-10-04-course-rework-first-principles-design.md` + `2026-11-05-visualisation-before-numpy-design.md`. Read the specs and the deck's `docs/delivery-log.md` entries before reworking it.
- **A deck is self-contained**: every step on its slide with its output; no visible text leans on another lecture ("the temperatures of Lecture 5": lecturer, 9 Nov 2026; say what it is, or point to a slide of the same deck); nothing sends the room to the workbook or a file (exceptions: planned `**Live:**` moments, L04's zip link). Live showing is the seminar's job.

Details: `docs/authoring.md#lectures`.

### Seminars

- `lectures/workbook/docs/seminars/seminar_NN.md` (+ `overview.md`), numbered as its lecture (Seminar 1 = Lecture 02; no Seminar 2), taught live from the page alone: `docs/seminar-page-recipe.md`, model `seminar_05.md`.
- **All in class**: no homework, installs included (Seminar 4). **Python from Miniforge**; an environment is conda's `environment.yml` (`conda env export --from-history`): no python.org, venv or `requirements.txt`.
- **One project, the weather station** (`weather-project`, `data/raw/weather.csv`, mean 7.16 °C), for lectures and seminars. A student's semester project is their own: never frame a course example as it.
- **Every seminar is self-contained**: Seminars 1–5 download nothing (data typed from the page); from 6 on, section 1 unzips `weather-sNN.zip` (release `seminar-files` of `MindaugasSarpis/weather-project`, built by `misc/weather_repo/seminar_zips.py` from `starts/sNN/`) and makes its conda environment (weeks 8–12: one environment, `analysis`; spec §3.3). Nothing from an earlier session, no `git pull`, no pushes outside the Git seminars; never rewrite `weather-project`'s history once a room has cloned it.
- No "made up" or "generated for the course" labels on slides, pages or handed-out READMEs.

Details: `docs/authoring.md#seminars`.

### Theme, workbook, misc

- `lectures/content/theme/` shares one design system with the landing: colours only in `styles/tokens.css`; `--dim` for labels and captions only, body text `--fg`; the heading scale only in `styles/layouts.css`. Details: `docs/authoring.md#theme-and-assets`.
- Lecture pages `lectures/workbook/docs/lectures/lecture_N.md` give the plan by slide numbers (no clock): **recount them whenever the deck gains or loses a slide**. CI runs `mkdocs build --strict`.
- Grade CSVs in `misc/exams/` are student data: **never commit them**. `docs/delivery-log.md`: append the lecturer's notes after each lecture; no student names (the repository is public).
- Recipes: `docs/seminar-page-recipe.md`, `docs/python-runner-recipe.md`, `docs/svg-figure-recipe.md`. A handed-out data file is committed with the script that makes it. Details: `docs/authoring.md#miscellaneous`.

## Slide Authoring Conventions

Dates, quotes and which decks are done: `docs/authoring.md#slide-authoring-conventions`.

1. **Cover**: only `layout: cover` + `title` (= `decks.json`), plus a runner deck's `python:` block. No `theme`, `colorSchema`, `background`, `addons`, `drawings`, `mermaid`, `transition` in lecture files.
2. **Cover** → **Quote** (motivational) → **Motivation** (bullet list).
3. **Sections**: `layout: section` + `hideInToc: true` + `# Section **KeyWord**`.
4. **Cards**: `<div class="card card-primary pad-tight">`, then `## 📊 **Title**` and the content on their own lines.
5. **Card colours**: `card-primary`, `card-secondary`, `card-accent`, `card-info`, `card-success`, `card-warning`.
6. **Padding**: `pad-tight` (default), `pad-compact` (dense), `pad-snug`, `pad-balanced`.
7. **Grids**: `grid-2`, `grid-3` with `gap-md mt-md`.
8. **Emoji outside the bold**: `## 📊 **Title**`.
9. **Separators**: `---`, optional YAML frontmatter between.
10. **Quizzes close the deck**: `<MCQ>` after the Recap, under a `layout: section` slide titled exactly `# Check **Yourself**`; answers on the workbook page. **Internals last**: `# For the **Curious**` (same form) between the Recap and the quizzes. Both count 0 min: the main path fills the band. The generated Glossary follows the quizzes.
11. **Derive, do not assert**: a worked example with real, computed numbers, connected to the slide before.
12. **zsh on macOS, Git Bash on Windows**: one `## 💻 **zsh · Git Bash**` card, 🍎/🪟 cards only for a real difference; tools both have (no `grep -P`, `find -printf`, `hexdump`, `tree`, `jq`, `make`, `rsync`, `man`, `sed -i`, `stat`); `python`, never `python3`.
13. **Speaker notes**: `**Live:**` (+ `class: live`), `**Do:**` (never a file beside the deck), `**Say:**`, `**Ask:**`, `**If asked:**`, a line or two each when they apply, then `(~N min)`. One step per slide, ≲40 words of prose.
14. **Python snippets are runner blocks** ```` ```py {monaco-run} {autorun:false} ````: results `print`ed, value in a comment; lines fit the editor (~50 chars in a `grid-2` card, ~115 full); ≲10 lines; never restyled. Static fences for terminal sessions and code a browser cannot run. Recipe `docs/python-runner-recipe.md`; check `pnpm qa:runners`.
15. **Every line carries information**: a title says what the slide does or answers; no slogans, number play, repeated card headings or narration; section slides stay, as pauses. Use the skill `writing-lecture-slides`.
16. **No walls of code or output**: over ~5 lines, cut to what matters (`...`) or build it up with magic-move, one command per click.
17. **Laconic slides** (9 Nov 2026): no paragraphs; a caption is one or two short lines, or two or three fragments with their numbers; reasons go into the note; every important number stays on the slide.

## Slidev Gotchas

- **Runner blocks**: `setup/shiki.ts` lists every fence language, the alias too (`'py'`); `setup/code-runners.ts` sends `plt.show()` into the 11rem output box, so a plotting fence stays ≲10 lines.
- No class starting `sm-`, `md-`, `lg-`, `xl-` (UnoCSS reads a breakpoint and collapses it).
- CI fonts set slides 15–20 px taller than macOS: leave ~25 px at the bottom; a quiz question ≤ 3 lines.
- Tables in cards overflow: add `table-compact`.
- One-line HTML is not parsed as markdown: `<em>`/`<strong>`/`<code>`, or blank lines around the text; `<MCQ question=…>` takes `code` spans only.
- `$$` inside HTML: a blank line after the tag, no empty line inside the math.
- Mermaid: keep `setup/mermaid.ts`'s settings (dagre, classic look) and its global styling; no `%%{init}%%` colour blocks.
- Git conflict markers in a fence crash the build: use a raw `<pre class="slidev-code"><code>&lt;…` block (L06 "A Merge Conflict").

Details: `docs/authoring.md#slidev-gotchas`. Slidev's own docs: the skill `.agents/skills/slidev/`.

## Deployment

- `.github/workflows/qa.yml`: every push to `main` (and PRs) runs both gates; on `main`, a green run builds and deploys to GitHub Pages (~8 min); a red one deploys nothing. `git push origin main` is the deploy; `gh workflow run qa.yml --ref main` redeploys. Unfinished edits to a live deck go on a PR branch; drafts are safe to push. `ff2026`, `bs2026` are frozen.
- **Drafts are gated too**: while a draft on `main` fails a gate, ship a finished deck from a worktree: `git worktree add <dir> -b deploy-x origin/main`, copy its files, commit, `git push origin deploy-x:main`, then rebase `main` on it.

## Releasing lectures during the semester

`pnpm week <N> --dry-run`, then `pnpm week <N>` (runs `pnpm release <N>`: 01–N live, the rest draft; rewrites the workbook's "This week"), `pnpm qa --only <slug>`, commit on `main`, push, `pnpm week <N> --verify`: deployed = green run + 200 from the pages. Drafts stay gated in CI and `pnpm dev <NN>` serves them; `pnpm build --include-drafts` previews everything.

## Adding / removing a lecture

Add: `lectures/content/slides/NN_Title.md`, its `decks.json` entry, `seminar_NN.md` with `<!-- ~120 min -->`, the workbook page + `mkdocs.yml` nav line; author with `pnpm dev <NN>` / `pnpm review <NN>`, gate with `pnpm qa --only <slug>` + `pnpm timing:check`. Remove: the entry, the file (or park it), its seminar page and nav line. Walkthrough: README.md.
