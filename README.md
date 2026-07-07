# Best Research and Data Analysis Practices from CERN

A 16-lecture + 16-seminar university course delivered as interactive [Slidev](https://sli.dev) decks with a companion [MkDocs](https://www.mkdocs.org) student workbook. The published site is a landing page plus **one independently built deck per lecture**, so students (especially on mobile) download only the lecture they open.

- **Live site**: https://mindaugassarpis.github.io/CERN_lessons_on_data_analysis
- **Deck manifest**: `lectures/content/decks.json` — the single source of truth for which lectures exist, their order, blocks A–E, and which are optional.
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
pnpm qa:shots                      # also write .qa-shots/<slug>/slide-NNN.png for visual review
pnpm timing:check                  # every week must fill its 2h lecture + 2h seminar slot
```

There are no unit tests — **`pnpm qa` (zero overflow) and `pnpm timing:check` (content sized to the slots) are the tests.** Both also run in CI on every push to `ff2026` (`.github/workflows/qa.yml`). The overflow checker re-verifies borderline slides on a fresh page before failing, so a red result is a real regression.

### Figures, videos, workbook

```bash
pnpm figures            # regenerate scripted matplotlib figures (figures/src/ → public/figures/viz_*.svg)
pnpm figures:lhcb       # regenerate the synthetic LHCb D⁰→K⁻π⁺ spectrum/fit figures
pnpm videos:fetch <url> --name <Name> --used-in LNN    # then videos:encode + videos:publish
cd lectures/workbook && mkdocs serve                   # student workbook (conda env "lecture")
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
lectures/content/decks.json      # THE manifest: decks, order, blocks, optional flags
lectures/content/slides/         # one markdown file per lecture (01–16)
lectures/content/theme/          # custom Slidev theme (cards, layouts, type scale)
lectures/content/public/figures/ # committed figure assets (viz_*.svg are scripted)
figures/src/                     # matplotlib pipeline behind `pnpm figures`
landing/                         # WebGL landing page source (Three.js + Vite)
scripts/                         # build-all / gen-entries / qa-all / check-slides / timing-report / dev / videos
lectures/workbook/               # MkDocs student workbook (16 seminar briefs, running project)
videos/manifest.toml             # video pipeline manifest (raw/web files are gitignored)
docs/superpowers/                # curriculum specs and implementation plans
misc/                            # course admin (grading scripts; grade CSVs are gitignored)
```

## Deployment

Work happens on **`ff2026`**; GitHub Pages deploys from **`bs2026`** (`.github/workflows/deploy.yml`). To publish:

```bash
git push origin ff2026:bs2026   # only after qa.yml is green on ff2026
```

A change is **not live** until it reaches `bs2026`.
