# FF-2026 Multi-Deck + Landing Page — Design Spec

**Status:** Approved (author, 2026-07-01) · **Date:** 2026-07-01 · **Branch:** `ff2026`
**Owner:** Mindaugas Šarpis · **Parent roadmap:** `docs/superpowers/specs/2026-07-01-ff2026-master-roadmap-design.md` (Workstream A)

> This spec **supersedes** the master roadmap's original Workstream A shape — a
> single monolithic `physics_faculty_2026.md` entry-point importing every `L*`
> file. Browsing ~1000+ slides in one Slidev bundle is laggy and hard to
> navigate. Instead, FF-2026 becomes a **portal landing deck + one independent
> deck per FF module**, so opening a lecture loads only that lecture's slides.
> Roadmap decision §2.4.3 ("content re-org via new entry-point, not renames")
> still holds — we just create *N* thin entry-points + a landing entry instead
> of one mega-entry, and rename nothing.

---

## 1. Goal & scope

### Goal
Restructure the FF-2026 course from one monolithic Slidev deck into a **themed
landing page** plus **one independently-built deck per FF module (15)**, so that:
- clicking a lecture card loads **only that lecture's bundle** (fixes the lag),
- the landing page is the natural, browsable index of the course, and
- a single source-of-truth manifest keeps the landing cards, in-deck navigation,
  and the build loop in sync.

This workstream delivers the **navigable multi-deck shell**. Per-module content
work (merges, new FAIR/Snakemake/FF-L15 material, the L01 grading fix) is
explicitly *follow-on* and out of scope here (roadmap §3, weeks 5–7).

### Non-goals (this workstream)
- **No content re-writing.** Each module deck imports its existing source
  `slides/*.md` as-is. Merges, new modules, and expansions are follow-on.
- **No file renames.** Existing `slides/L*.md` are reused untouched.
- **BS-2026 untouched.** `lessons_on_data_analysis_from_CERN.md` and its build
  stay exactly as they are. FF and BS coexist.
- **Video pipeline** is a separate workstream (B); not touched here.
- **`crash_course_for_video_lecture.md`, quizzes** untouched.

### Constraints
- FF entry files **must live flat in `lectures/content/`** (see §2 rationale).
- Delivery order is expressed in the manifest, not by renaming files.
- No new test/lint framework is introduced (repo has none); verification is a
  build + manual smoke check (§9).

---

## 2. Decisions locked (2026-07-01, via brainstorming)

1. **Themed portal deck** for the landing page (not a generated static index) —
   a real Slidev deck using the existing card system, editable like any slide.
2. **One independent deck per FF module** (15 decks), each its own Slidev build →
   its own bundle/URL. This is what makes per-lecture loading real (Slidev
   resolves `src:` imports into one bundle at build time; there is no in-deck
   lazy-load of a lecture, so each lecture must be its own build).
3. **Cross-deck nav on the LAST slide only** — `⌂ Index · ← Prev · Next →`, so
   nothing clutters the lecture. Order comes from the shared manifest.
4. **Deploy model: one Pages site, one course live at a time ("switch branch").**
   GitHub gives one Pages site per repo. FF's build owns the site root
   (`/<repo>/`) while the `ff2026` branch is the last to deploy; BS keeps its own
   trigger. No `/ff/` subpath needed.
5. **FF entry files stay flat in `lectures/content/`** (not a `ff/` subfolder with
   symlinked scaffolding). Slidev resolves `theme: ./theme`, `public/`
   (`/figures/…`), `slides/`, and `components/` relative to the *entry file's
   directory*. Keeping FF entries in the same dir as the working BS entry means
   **zero asset-path breakage**. (A `ff/` subdir would make `public/` resolve to
   `lectures/content/ff/public/`, breaking every `/figures/…` reference.)
6. **Single JSON module manifest** (`lectures/content/ff/modules.json`, a *data*
   file — does not affect Slidev's userRoot) is the source of truth for the
   landing cards, `CourseNav`, and the build loop.

---

## 3. Architecture

```
                    ff/modules.json  (ordered list of 15 FF modules)
                    /       |         \
                   /        |          \
        physics_faculty  CourseNav.vue   scripts/build-ff.mjs
        _2026.md         (prev/next/     (builds landing + each
        (renders cards)   index links)    deck to dist/<slug>/)
             |                 |                    |
        landing deck      last slide of        deployed site:
        at site root      every lecture        /<repo>/       (landing)
                          deck                 /<repo>/<slug>/ (lecture ×15)
```

Three consumers, one list. Editing `modules.json` (order, title, slug, sources)
updates cards, nav, and build together — no drift.

---

## 4. File layout (exact)

```
lectures/content/
├── physics_faculty_2026.md          # NEW — themed landing/portal deck (→ dist/ root)
├── ff_L01_orientation_and_cern.md   # NEW — thin per-module entry (×15, flat dir)
├── ff_L02_crash_course_cs.md        # NEW
├── ff_L03_files_dirs_cmdline.md     # NEW
├── ff_L04_markdown_vscode.md        # NEW
├── ff_L05_version_control.md        # NEW
├── ff_L06_project_organization.md   # NEW (placeholder — no single source yet)
├── ff_L07_python_crash_course.md    # NEW
├── ff_L08_numpy_pandas_realdata.md  # NEW
├── ff_L09_concepts_fair.md          # NEW
├── ff_L10_data_visualisation.md     # NEW
├── ff_L11_probability_statistics.md # NEW
├── ff_L12_data_fitting.md           # NEW
├── ff_L13_computing_infrastructure.md # NEW
├── ff_L14_reproducible_workflows.md # NEW
├── ff_L15_project_review.md         # NEW (placeholder — brand-new module)
├── ff/
│   └── modules.json                 # NEW — single source of truth
├── FF_syllabus_map.md               # NEW — human-readable FF-module → source map
├── components/
│   ├── CourseNav.vue                # NEW — ⌂ Index · ← Prev · Next → (last slide)
│   ├── MCQ.vue                      # UNCHANGED
│   └── VideoPlayer.vue             # UNCHANGED (Workstream B updates this separately)
├── slides/                          # UNCHANGED — L*.md reused, no renames
└── lessons_on_data_analysis_from_CERN.md  # UNCHANGED — BS deck

scripts/
└── build-ff.mjs                     # NEW — reads modules.json, builds landing + 15 decks

package.json                         # MODIFY — add dev:ff, build:ff
.github/workflows/deploy.yml         # MODIFY — trigger on ff2026, run build:ff
```

---

## 5. Module manifest — `lectures/content/ff/modules.json`

Schema (array of module objects, in delivery order):

```json
{
  "course": "FF-2026 — Methods of Data Analysis (CERN)",
  "repo": "CERN_lessons_on_data_analysis",
  "modules": [
    {
      "id": "L01",
      "num": 1,
      "slug": "L01",
      "title": "Course Orientation & Intro to CERN",
      "entry": "ff_L01_orientation_and_cern.md",
      "sources": ["slides/L01_Course_Orientation.md", "slides/L02_Introduction_to_CERN.md"],
      "status": "draft"
    }
  ]
}
```

Field meanings:
- `id` / `num` — FF module identity (display: "L1"…"L15"; `num` for sorting).
- `slug` — URL path segment and `dist/` subfolder (`/<repo>/<slug>/`). FF module
  number, zero-padded (`L01`…`L15`). Documented as FF module numbers, not source
  file numbers.
- `entry` — the thin entry markdown in `lectures/content/`.
- `sources` — existing `slides/*.md` this deck imports (0..n). Empty for
  placeholder modules (L06, L15).
- `status` — `"ready"` (source imports directly, final for the shell) or
  `"draft"` (merge/expand/new content pending; deck is navigable but marked).

### The 15 modules (from roadmap §3 mapping)

| id  | FF title                                              | sources (existing slides/*)                              | status | shell action |
|-----|-------------------------------------------------------|----------------------------------------------------------|--------|--------------|
| L01 | Course Orientation & Intro to CERN                    | `L01_Course_Orientation`, `L02_Introduction_to_CERN`     | draft  | import both  |
| L02 | Crash Course on CS                                    | `L03_1_1_Crash_Course_on_Computer_Science`               | draft  | import (enable) |
| L03 | File Handling, Directories & Command Line             | `L03_1_2_File_Handling_and_Directory_Structure`, `L03_2_Command_Line` | draft | import both |
| L04 | Markdown & VS Code                                    | `L03_3_Markdown`, `L03_4_VS_Code`                        | draft  | import both  |
| L05 | Version Control (Git/GitHub)                          | `L08_Version_Control`                                     | ready  | import       |
| L06 | Data-Analysis Project Organization                   | — (assemble later from L06/L03_1_2/L12)                   | draft  | placeholder  |
| L07 | Python Crash Course                                   | `L05_Crash_Course_on_Python_Programming`                 | draft  | import (expand later) |
| L08 | NumPy, Pandas & Real-Data Case Studies               | `L11_NumPy_Pandas_Real_Data`, `L11_Real_Data_and_Case_Studies` | draft | import both |
| L09 | Concepts of Data Analysis & FAIR                     | `L06_Concepts_of_Data_Analysis`                          | draft  | import (add FAIR later) |
| L10 | Data Visualisation                                   | `L07_Data_Visualisation`                                 | draft  | import (enable) |
| L11 | Probability & Statistics                             | `L09_Probability_and_Statistics`                         | ready  | import       |
| L12 | Data Fitting                                          | `L10_Data_Fitting`                                       | ready  | import       |
| L13 | Computing Infrastructure                             | `L04_Computing_Infrastructure`                           | ready  | import       |
| L14 | Reproducible Workflows, Automation & Modularization  | `L12_Reproducible_Workflows`                             | draft  | import (add Snakemake later) |
| L15 | Project Review & Presentations                       | — (brand-new module)                                     | draft  | placeholder  |

The disabled source decks (`L03_2`, `L03_3`, `L03_4`, `L07`) are enabled by being
imported into a fresh entry (the `disabled: true` in their headmatter is a
per-deck flag; imported via `src:` their slides render — to be confirmed in §9,
and the frontmatter flag removed if it suppresses import).

---

## 6. Per-lecture entry template

Each `ff_Lxx_*.md` is thin: shared headmatter, `src:` import(s), a final
`CourseNav` slide. Example (`ff_L05_version_control.md`):

```md
---
theme: ./theme
colorSchema: dark
routerMode: hash
addons:
  - slidev-addon-python-runner
mermaid: true
defaults:
  preload: false
---

---
src: slides/L08_Version_Control.md
---

---
layout: center
hideInToc: true
---

<CourseNav current="L05" />
```

- `routerMode: hash` — deep links (`/#/12`) survive refresh on GitHub Pages.
- `defaults: { preload: false }` — lazy-mount (already the repo convention).
- **Placeholder entries** (L06, L15) omit the `src:` import and instead carry a
  single title slide + a "content in development" note, then the `CourseNav`
  slide — so the site is navigable end-to-end from day one.

---

## 7. `CourseNav.vue` (last slide only)

**Responsibility:** given the current module `id`, render base-relative links to
the landing and to the previous/next module. Rendered only where the entry
places it (the final slide), so it never overlays lecture content.

**Interface:** `<CourseNav current="L05" />`.

**Depends on:** `../ff/modules.json` (import) and `import.meta.env.BASE_URL`.

**Logic:**
- Find current module by `id`; compute `prev`/`next` by array position.
- Index link: `${BASE_URL}../` (from `/<repo>/<slug>/` → `/<repo>/`).
- Prev/next: `${BASE_URL}../<slug>/`.
- Hide the prev arrow on the first module, next on the last.
- Renders with the theme's card/utility classes for visual consistency.

**Dev caveat:** in `slidev` dev only one deck runs, so cross-deck links are inert
locally; they resolve in the built site. Documented, not a bug.

---

## 8. Landing deck — `physics_faculty_2026.md`

A themed portal deck. Imports `./ff/modules.json`, renders a responsive card grid
(`card-primary`/`secondary`/… + `grid-2`/`grid-3`) — one card per module showing
`num`, `title`, and a `status` badge for `draft`. Each card is an anchor to
`${BASE_URL}<slug>/`. A short cover/header slide precedes the grid. Built to the
`dist/` root with `--base /<repo>/`.

Because the card grid is data-driven, adding/reordering modules is a manifest
edit — the landing needs no hand-editing per module.

---

## 9. Dev / build / deploy

### Dev (`package.json` scripts)
- `dev:ff` → `slidev lectures/content/physics_faculty_2026.md` (landing).
- Existing `dev:lecture` (`slidev`) reused for a single lecture:
  `pnpm dev:lecture lectures/content/ff_L05_version_control.md`.

### Build (`scripts/build-ff.mjs`)
A small Node ESM script:
1. Read `lectures/content/ff/modules.json`.
2. `slidev build lectures/content/physics_faculty_2026.md --base /<repo>/ --out dist`.
3. For each module: `slidev build lectures/content/<entry> --base /<repo>/<slug>/ --out dist/<slug>`.
4. `<repo>` from an env var (`REPO_NAME`, default `CERN_lessons_on_data_analysis`).

Exposed as `build:ff` in `package.json`. Uses `execSync` per deck (sequential is
fine; CI has time). `NODE_OPTIONS=--max-old-space-size=4096` as the current
workflow already sets.

### Deploy (`.github/workflows/deploy.yml`)
- Add `ff2026` to the `push.branches` trigger (keep `bs2026`).
- Branch-aware build step: on `ff2026`, run `pnpm build:ff` (multi-deck →
  `dist/`); on `bs2026`, keep the current single-deck build. Whichever branch
  pushes last owns the single Pages site (user's "switch branch" model;
  `concurrency: group: pages`).
- Upload `dist/` as the Pages artifact (unchanged deploy job).

### Verification (smoke check — no test framework)
1. `pnpm build:ff` completes; `dist/` contains `index.html` (landing) +
   `dist/<slug>/index.html` for all 15 modules.
2. Serve `dist/` (e.g. `python3 -m http.server`) with a `/<repo>/` base emulation
   (or set `--base /` locally for the check): landing renders the card grid;
   clicking a card loads that lecture; the last slide's `CourseNav` links resolve
   to the right sibling paths.
3. A `status:"ready"` deck (e.g. L05 ← `L08_Version_Control`) renders its figures
   (`/figures/…`), `MCQ`, and any `VideoPlayer`/python-runner correctly —
   confirming flat-entry asset resolution.
4. A previously-`disabled` source (e.g. `L07_Data_Visualisation` via `ff_L10`)
   renders its slides when imported; if `disabled: true` suppresses the import,
   remove that flag from the source deck's headmatter.

---

## 10. Open questions (non-blocking; resolve during build or later)

- **Slug casing** (`L01` vs `l01`): default to `L01`; trivial, lock in the plan.
- **`disabled: true` interaction with `src:` import** — confirmed in §9 step 4;
  if it suppresses rendering, strip the flag (that's the "enable" action anyway).
- **Landing dev links** — inert in dev (single-deck). Acceptable; optionally add
  a dev-only hint. Not blocking.
- **Placeholder copy** for L06/L15 — minimal "in development" slide now; real
  content is follow-on.

---

## 11. Change log
- **2026-07-01** — Drafted from brainstorming; design approved by author.
  Decisions §2 locked: themed portal deck, per-module decks, last-slide nav,
  switch-branch deploy, flat entries, JSON manifest.
