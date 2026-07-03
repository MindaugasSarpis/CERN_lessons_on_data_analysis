# 16-Lecture Curriculum + Blocked Delivery — Design (2026-07-03)

## Goal

Expand and reorganise the course into **16 three-hour lectures + 16 hands-on
seminars/hackathons**, delivered as **per-lecture decks behind a landing page**
(to fix mobile load), with every session tied together by the course's four
core aims and one running project. Advanced material sits last and is fully
droppable if time runs short.

User decisions (2026-07-03): landing page + per-lecture decks (blocks are the
landing-page grouping, not the build boundary) · advanced block = Machine
Learning + AI · scope = restructure + finish the 4 drafts + build the new
ML/AI lecture + 16 seminar workbook pages · seminars = MkDocs workbook pages,
one per lecture.

## The course's four aims (the spine)

Every lecture and seminar advances at least one, and the deck names them with
consistent iconography:

1. **🔧 Tool agnosticism** — concept first, then ≥2 tools; an explicit
   *"the idea, not the tool"* callout on tooling slides.
2. **♻️ Reproducibility** — raw-data-read-only, README, scripts over manual
   edits, version control, environments; a recurring *"Could you rebuild
   this?"* check-slide in every data lecture.
3. **⚙️ Automation** — *do it once by hand, twice by script*: CLI pipelines →
   scripts → workflows/Make → CI; a recurring *"Automate this"* motif.
4. **📁 Efficient work with data & files** — naming, structure, formats, then
   NumPy/Pandas as the payoff.

ML/AI is explicitly **not** the point of the course — it is an optional capstone
that *applies* the four aims. The four-aim spine is what makes the 16 sessions
cohere.

## The running project (interconnection device)

A **single dataset threads through the whole course** — a CERN-Open-Data /
sensor-style tabular set consistent with the existing L06/L09 examples. Each
seminar adds one layer to the *same* reproducible git repo:

- naming & structure → raw-data capture → CLI cleaning → versioned in git →
  parsed in Python → tidied in Pandas → visualised → fitted → automated →
  (optionally) modelled.

By Seminar 16 each student owns one clean, versioned, automated, documented,
tool-agnostic analysis project. Lectures reference it forward
("you'll clean this in Seminar 13") and backward ("the raw file from Seminar 4").
The dataset and a starter repo skeleton live in the workbook.

## The 16 lectures, in 5 blocks (advanced last)

Legend for **aim emphasis**: 🔧 agnostic · ♻️ reproducible · ⚙️ automate ·
📁 data/files. "Source ✓" = existing published lecture; "draft" = existing
draft to finish; "new" = to build.

### Block A — Foundations & Tooling (L1–L6)
| # | Lecture | Aims | Source | Builds on → sets up |
|--|--|--|--|--|
| 1 | Orientation & Data in Your Life | (all, framed) | L01 ✓ | opens the four aims → whole course |
| 2 | Introduction to CERN & the Data Challenge | 📁♻️ | L02 ✓ | motivation → L3 |
| 3 | How Computers Work | 🔧📁 | L03_1_1 ✓ | bits/formats → files (L4), numbers (L11) |
| 4 | Command Line & File Handling | ⚙️📁🔧 | L03_2 + L03_1_2 ✓ | shell/pipes → automation (L14), naming → all data |
| 5 | Markdown & VS Code | 🔧♻️ | L03_3 + L03_4 ✓ | README/notes → Git (L6), notebooks (L13) |
| 6 | Version Control with Git | ♻️🔧 | L08 ✓ | tracks the running project from here on |

### Block B — Programming (L7–L8)
| # | Lecture | Aims | Source | Builds on → sets up |
|--|--|--|--|--|
| 7 | Python Foundations | 🔧 | L05 ✓ (split part 1) | types/control flow → everything Python |
| 8 | Python for Data Work | 📁🔧 | L05 ✓ (split part 2) + new bridge | files/strings/collections → NumPy/Pandas (L13) |

### Block C — Data Analysis Core (L9–L12)
| # | Lecture | Aims | Source | Builds on → sets up |
|--|--|--|--|--|
| 9 | Concepts of Data Analysis | ♻️📁 | L06 ✓ | lifecycle/quality/FAIR → all downstream |
| 10 | Data Visualisation | 🔧 | L07 ✓ | grammar of graphics → fitting (L12), ML (L16) |
| 11 | Probability & Statistics | 🔧 | L09 ✓ | SE/CI/distributions → fitting (L12), ML eval (L16) |
| 12 | Practical Data Fitting | ⚙️🔧 | L10 draft | least squares/χ² → modelling mindset (L16) |

### Block D — Practical Data Work (L13–L14)
| # | Lecture | Aims | Source | Builds on → sets up |
|--|--|--|--|--|
| 13 | NumPy & Pandas | 📁⚙️🔧 | L11 draft | the data-wrangling payoff; folds in Real-Data case studies |
| 14 | Reproducible Workflows & Automation | ♻️⚙️ | L12 draft | environments, Make/CI, pipelines — the aims made explicit |

### Block E — Advanced / Optional, last & droppable (L15–L16)
| # | Lecture | Aims | Source | Builds on → sets up |
|--|--|--|--|--|
| 15 | Computing Infrastructure & HPC | 🔧⚙️ | L04 draft | where reproducible/automated work scales up |
| 16 | Machine Learning & AI | (applies all) | **new** | capstone applying the four aims to a model + case studies |

The Real-Data & Case-Studies draft (small, 46 slides) is **not** a standalone
lecture; its strongest examples are distributed into L13 (Pandas), L14
(workflow), and L16 (ML), keeping every lecture full and non-redundant.

## The 16 seminars (one per lecture, workbook pages)

Each is a MkDocs page: **goal · prerequisites · step-by-step tasks · stretch
goals · solution notes**, and each adds a layer to the running project.

| S | Seminar (hackathon where marked ⚡) | Adds to the running project |
|--|--|--|
| 1 | Set up your toolkit & first repo | project skeleton + README |
| 2 | Find & document a dataset | dataset chosen, provenance recorded |
| 3 | Bit/number/format explorer ⚡ | understand the raw file's encoding |
| 4 | Tame a messy project from the CLI ⚡ | raw/ processed/ structure, cleaned filenames |
| 5 | Write the project's README & notes in Markdown | documentation layer |
| 6 | Branch, break, merge — collaborate in Git ⚡ | project under version control |
| 7 | Python warm-up: parse a line of data | first parsing script |
| 8 | Read the raw file into Python | ingest script (no Pandas yet) |
| 9 | Data-quality audit of your dataset | quality checklist applied |
| 10 | Reproduce a Wilke figure ⚡ | first committed figure |
| 11 | Quantify uncertainty on a measurement | SE/CI on a real number |
| 12 | Fit a model and report it ± error ⚡ | fit + diagnostics |
| 13 | Clean the dataset with Pandas ⚡ | tidy processed/ table by script |
| 14 | Make it reproducible: env + Makefile ⚡ | one-command rebuild of all results |
| 15 | Run your pipeline on a remote/HPC-style job | scaled run (optional) |
| 16 | Train & honestly evaluate a first model ⚡ | model + evaluation (optional) |

Seminars 15–16 are the droppable tail, matching Block E.

## Deployment architecture

- **Per-lecture decks.** Each of the 16 lectures builds to its own base path,
  e.g. `dist/03-how-computers-work/`. A student loads one lecture (~40–140
  slides + only that lecture's dependencies) — the mobile-load fix.
- **Landing page** at `dist/index.html`: static, self-contained, theme-matched;
  shows the five blocks, 16 lectures (linked), and 16 seminars (linked to the
  workbook). Marks Block E as optional. This is the course home.
- **Blocks are a landing-page grouping**, not a build unit.
- **Slug scheme:** `NN-kebab-title` (zero-padded) so URL order = delivery order.
- **Cross-lecture links** become landing-page/back-to-home links; within-lecture
  forward/back references stay textual (already the style).

## Build / deploy / QA changes

- `scripts/build-all.mjs` — reads a single `lectures/content/decks.json`
  manifest (`{slug, title, block, entry, optional}` × 16) and builds each entry
  to `dist/<slug>/ --base /<repo>/<slug>/`, then emits `dist/index.html` from a
  landing-page template populated from the manifest.
- `check-slides.mjs` — add a manifest mode: build all decks to `.qa-dist/<slug>`
  and gate every deck for overflow (same 6px rule), so the zero-overflow
  guarantee holds per deck. `pnpm qa` runs the whole set.
- `.github/workflows/deploy.yml` — replace the single build step with a matrix
  (one job per deck) or a `build-all` step, then assemble `dist/` and upload.
  Keeps deploying on `bs2026`.
- `package.json` — `dev:lecture` unchanged; add `build:all`, `qa` points at the
  manifest runner. Old single-entry `lessons_on_data_analysis_from_CERN.md`
  retained as an internal "everything" build for authoring convenience but not
  the deployed artifact.

## Scope of this pass (what gets built)

1. **Architecture**: `decks.json` manifest, `build-all.mjs`, landing page,
   multi-deck QA, deploy workflow.
2. **Restructure** existing published material into the 16-lecture slugs: split
   L05 → L7+L8; keep L03 sub-lectures mapped to L4/L5; no content loss.
3. **Finish 4 drafts** (L04→L15, L10→L12, L11→L13, L12→L14) to the same
   textbook-grounded, overflow-clean, four-aims-woven standard as the done 12.
4. **New**: Lecture 16 (Machine Learning & AI) + its case studies.
5. **Weave the spine**: add the four-aim callouts, the "Could you rebuild
   this?" / "Automate this" recurring slides, and forward/back running-project
   references across all lectures.
6. **16 seminar workbook pages** + the running-project dataset & starter repo.

## Constraints & invariants

- Zero slide overflow per deck, verified by rendering (multi-deck QA), not just
  building.
- House style throughout (card system, type scale, kinetic accents, emoji
  format); videos full-screen; within-file language consistency.
- Concept-before-tool framing on every tooling slide (the agnosticism aim is a
  hard style rule, not a suggestion).
- Every new/added slide advances a named aim or the running project; no filler.
- Course name stays "Best Research and Data Analysis Practices from CERN".
- Advanced (Block E) must be removable without breaking earlier lectures — no
  earlier lecture may depend on L15/L16.

## Non-goals

- No change to the four owner-level course-wide items still open in the ledger
  beyond the naming (already done).
- Not rebuilding the 12 finished lectures' content — only restructuring them
  into decks and weaving the spine.
- No LMS/quiz-platform integration; seminars are static workbook pages.

## Decomposition (for the implementation plan)

This spec is large; the plan will sequence it as: **(P1)** architecture +
manifest + landing + multi-deck QA + deploy (produces a working blocked site
from the *existing* lectures first — immediate mobile-load win), then **(P2)**
restructure/split, **(P3)** finish drafts one at a time, **(P4)** new ML/AI
lecture, **(P5)** spine-weaving pass, **(P6)** 16 seminar pages + dataset.
Each phase ends green (all decks build + zero overflow) and is independently
shippable.
