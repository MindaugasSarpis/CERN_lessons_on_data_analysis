# Best Research and Data Analysis Practices from CERN

A 16-lecture + 16-seminar university course delivered as interactive [Slidev](https://sli.dev) decks with a companion [MkDocs](https://www.mkdocs.org) student workbook. The published site is a landing page plus **one independently built deck per lecture**, so students (especially on mobile) download only the lecture they open.

- **Live site**: https://mindaugassarpis.github.io/CERN_lessons_on_data_analysis
- **Deck manifest**: `lectures/content/decks.json` — the single source of truth for which lectures exist, their order, blocks A–E, which are optional, and which are still `draft` (listed but not yet deployed).
- **Course spine**: 🔧 tool-agnosticism · ♻️ reproducibility · ⚙️ automation · 📁 efficient work with data & files.

## Setup

Prerequisites: Node.js 20+, pnpm, and (for the workbook + figure pipeline) Conda/Mamba.

```bash
pnpm install                    # Slidev, theme, QA tooling (Playwright Chromium)
conda env create -f env.yaml    # Python env "lecture" (figures pipeline + MkDocs workbook)
```

## Everyday workflows

### Edit a lecture

```bash
pnpm dev 6            # serve lecture 06 (also accepts a slug or substring: pnpm dev version)
pnpm dev              # list all decks
```

Lecture sources live in `lectures/content/slides/NN_Title.md`. Decks are always served/built through a generated entry (`deck.<slug>.md`) that carries the custom theme — never run Slidev on a bare `slides/NN_*.md`.

### Quality gates (run before pushing)

```bash
pnpm qa                            # build every deck + fail on any slide overflowing its frame
pnpm qa --only 06-version-control  # gate just the deck you touched (fast loop)
pnpm qa --changed-since origin/main  # gate only the decks whose slides changed vs main (what CI does)
pnpm qa:shots                      # also write .qa-shots/<slug>/slide-NNN.png for visual review
pnpm timing:check                  # every week must fill its 2h lecture + 2h seminar slot
```

There are no unit tests — **`pnpm qa` (zero overflow) and `pnpm timing:check` (content sized to the slots) are the tests.** Both also run in CI on every push to `main` and on pull requests (`.github/workflows/qa.yml`), with `pnpm qa` scoped to the decks whose slides changed since the last green `main` run (a change to anything shared — theme, components, scripts, `public/`, `decks.json`, deps — re-checks every deck); a green run on `main` goes on to deploy the site. The overflow checker re-verifies borderline slides on a fresh page before failing, so a red result is a real regression.

### Figures, videos, workbook

```bash
pnpm figures            # regenerate scripted matplotlib figures (figures/src/ → public/figures/viz_*.svg)
pnpm figures:lhcb       # regenerate the synthetic LHCb D⁰→K⁻π⁺ spectrum/fit figures
pnpm videos:fetch <url> --name <Name> --used-in LNN    # then videos:encode + videos:publish
cd lectures/workbook && mkdocs serve     # student workbook (mkdocs + mkdocs-material; deployed at <site>/workbook/)
```

Scripted figure outputs are committed; decks never run Python at build time.

### Full build

```bash
pnpm build              # all decks + landing page → dist/
pnpm build:landing      # just the landing page (WebGL + static fallback)
pnpm dev:combined       # optional single all-16 authoring deck (not deployed); pnpm export → PDF
```

## Adding or removing a lecture

Everything is driven by `lectures/content/decks.json`, so the checklist is short:

**Add**
1. Create `lectures/content/slides/NN_Title.md` — copy the frontmatter + cover/quote/motivation skeleton from an existing lecture (authoring conventions are in `CLAUDE.md`; `LX_Python_Interactive.md` is the template for interactive-Python slides).
2. Add `{ "slug": "NN-short-name", "title": "…", "block": "A–E", "srcs": ["NN_Title.md"] }` to `decks.json` — array order is delivery order; the landing page, per-deck nav, entries, and timing gate all follow automatically.
3. Write the seminar brief `lectures/workbook/docs/seminars/seminar_NN.md` (declare **~120 min**) and a workbook page + nav line in `lectures/workbook/mkdocs.yml`.
4. `pnpm dev NN` to author, then `pnpm qa --only <slug>` and `pnpm timing:check`.

**Remove**
1. Delete the deck's entry from `decks.json` and delete the slide source (git history keeps it).
2. Delete its seminar brief and the workbook nav line.
3. `pnpm timing:check` — only manifest-listed files gate, so nothing lingers.

## Repository map

```
lectures/content/decks.json      # THE manifest: decks, order, blocks, optional + draft flags
lectures/content/slides/         # one markdown file per lecture (01–16)
lectures/content/theme/          # custom Slidev theme (cards, layouts, type scale)
lectures/content/public/figures/ # committed figure assets (viz_*.svg are scripted)
figures/src/                     # matplotlib pipeline behind `pnpm figures`
landing/                         # WebGL landing page source (Three.js + Vite)
scripts/                         # build-all / gen-entries / qa-all / check-slides / timing-report / dev / videos
lectures/workbook/               # MkDocs student workbook (16 seminar briefs + overview)
videos/manifest.toml             # video pipeline manifest (raw/web files are gitignored)
docs/superpowers/                # curriculum specs and implementation plans
misc/                            # course admin (grading scripts; grade CSVs are gitignored)
```

## Deployment

One branch: **`main`**. Every push to `main` runs `.github/workflows/qa.yml`, which chains the two gates → build → deploy to GitHub Pages, so a push is live about 8 minutes later **only if the gates pass** — a red run deploys nothing and the previous site stays up. Pull requests run the gates only. To publish:

```bash
git push origin main            # QA gates → build → deploy, ~8 min
```

Keep unfinished edits to a **live** deck on a branch and open a PR (the gates run there too); drafts (`"draft": true`) are safe to push directly — gated, never deployed. To redeploy without a new commit: `gh workflow run qa.yml --ref main`. The old `ff2026` (work) and `bs2026` (deploy) branches are frozen at the 2026-09-06 cutover; nothing deploys from them.

### Releasing lectures one at a time

Staged release is one boolean per deck in `decks.json` — flip it by hand or with `pnpm release <NN>` (lectures 01–NN live, the rest draft; `pnpm release all` = everything live; no argument = show state):

```jsonc
{ "slug": "09-concepts-of-data-analysis", "…": "…", "draft": true }   // listed "coming soon", not deployed
{ "slug": "09-concepts-of-data-analysis", "…": "…", "draft": false }  // live
```

- A **draft** deck is still built and gated by `pnpm qa` and `pnpm timing:check` (CI too), so you can keep editing it without it silently breaking.
- A deploy build (`pnpm build`, the Pages workflow) **skips** drafts — no `dist/<slug>/` exists, the landing page and the in-deck ☰ menu list the title greyed and unlinked, and old `/<slug>/5` links fall through to the home page instead of being rewritten.
- On lecture day: set `"draft": false` (or `pnpm release NN`), commit on `main`, `git push origin main` — the deck is live once `qa.yml` is green (~8 min).
- `pnpm dev <NN>` serves drafts as usual; `pnpm build --include-drafts` builds the whole site locally for a preview.
