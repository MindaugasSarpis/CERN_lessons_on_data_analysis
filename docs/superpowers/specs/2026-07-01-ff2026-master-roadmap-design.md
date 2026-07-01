# FF-2026 Master Roadmap — Design Spec

**Status:** Draft, awaiting author review · **Date:** 2026-07-01 · **Branch:** `ff2026`
**Owner:** Mindaugas Šarpis · **Target delivery:** September 2026 (autumn semester)

> This is a **living planning dossier**, intended to survive across sessions and
> machines. It bundles (a) the context snapshot from the initial survey, (b) the
> decisions locked so far, and (c) the master roadmap. A fresh session can resume
> from this file alone — see **§0 How to resume**.

---

## 0. How to resume this work

**What this is.** The master roadmap for turning the finished `bs2026` lecture
deck into the **FF-2026** course (Physics Faculty adaptation) for September 2026.
The plan is deliberately staged as a top-level roadmap first; each workstream
(A/B/C) then gets its own spec → implementation-plan → build cycle.

**Where we are.** Roadmap drafted and being reviewed. No lecture content or
pipeline code has been changed yet. `ff2026` currently equals `bs2026`'s deck
plus the two FF course-description `.docx` files.

**To continue in a new session:**
1. Read this file top to bottom — the context snapshot (§2) means you do **not**
   need to re-run the survey.
2. Check the **Change log** (§9) for what's happened since this was written.
3. The immediate next action is in **§7 Decomposition & next steps**.
4. Locked decisions are in **§2.4** — don't relitigate them without the owner.

**Process note.** This was produced via the `superpowers:brainstorming` flow. The
terminal step after roadmap approval is to invoke `superpowers:writing-plans` on
the **first sub-project (Workstream A)** to produce its implementation plan.

---

## 1. Goal & scope

### Goal
Transform the finished `bs2026` deck into the **FF-2026 course**:
**15 modules, 100 %-project grading, flipped classroom, 16 weeks × (2 lectures +
2 seminars)**, deployable for the **September 2026** autumn semester.

### Non-goals (this cycle) — explicitly deferred
- **Recorded / narrated video lectures** and **student-video tooling.** The video
  workstream is scoped to an **asset-pipeline upgrade only** (see §4). (Owner
  decision, 2026-07-01.)
- The actual **seminar exercise scripts** and **project topic menu** — named as
  sub-spec work, not solved in the roadmap.
- Any **BS-2026-specific** changes. FF and BS are distinct, coexisting offerings.

### Constraints
- **FF `.docx` is source-of-truth and stays untouched.** The committed
  `misc/description/*.docx` are the authoritative formatted originals. Any
  description edits go to a synced `.md`; never regenerate/overwrite the `.docx`.
  (See memory: *FF description source of truth*.)
- **File numbering is the authoritative sort key.** Delivery order is expressed in
  the entry-point import list, not by renaming files.
- **No new tests/lint** exist in the repo; keep it that way unless a workstream
  needs a check (the video pipeline's `check` subcommand is the model).

---

## 2. Context snapshot (so a fresh session needn't re-survey)

### 2.1 Current state of the repo
- **`ff2026` = `bs2026` deck + 2 `.docx`.** `git diff bs2026..ff2026` touches only
  `.claude/settings.local.json` and the two course-description `.docx` files. The
  lecture *content* is bs2026's; the FF adaptation of the slides hasn't started.
- **Entry points:** `lectures/content/lessons_on_data_analysis_from_CERN.md`
  (published subset) and `lectures/content/staging.md` (WIP; currently imports only
  L07). FF will get a **new** entry-point (see §3).
- **Slide files** in `lectures/content/slides/` (numeric prefix = authoritative
  sort key; delivery order is independent):

  | File | ~slides | Status |
  |---|---|---|
  | `L01_Course_Orientation` | 30 | finished; **grading slide stale (20/20/60)** |
  | `L02_Introduction_to_CERN` | 40 | finished; 16 VideoPlayer embeds |
  | `L03_1_1_Crash_Course_on_Computer_Science` | 129 | `disabled:true` |
  | `L03_1_2_File_Handling_and_Directory_Structure` | 43 | finished |
  | `L03_2_Command_Line` | 36 | `disabled:true` (draft) |
  | `L03_3_Markdown` | 31 | `disabled:true` (draft) |
  | `L03_4_VS_Code` | 34 | `disabled:true` (draft) |
  | `L04_Computing_Infrastructure` | 86 | finished |
  | `L05_Crash_Course_on_Python_Programming` | 68 | finished; python-runner |
  | `L06_Concepts_of_Data_Analysis` | 184 | finished |
  | `L07_Data_Visualisation` | 182 | `disabled:true` (draft) |
  | `L08_Version_Control` | 58 | finished |
  | `L09_Probability_and_Statistics` | 124 | finished |
  | `L10_Data_Fitting` | 94 | finished; python-runner |
  | `L11_NumPy_Pandas_Real_Data` | 108 | finished; python-runner |
  | `L11_Real_Data_and_Case_Studies` | 46 | finished; **parallel L11 track** |
  | `L12_Reproducible_Workflows` | 94 | finished |
  | `LX_Python_Interactive` | 4 | template only |

- **Authoring conventions:** card system (`card-primary/secondary/accent/info/
  warning/success` + `card-glass`), pad variants, `grid-2/3`, Mermaid, LaTeX,
  `<v-click>`, `slidev-addon-python-runner` (L05/L10/L11×2/LX). Components:
  `MCQ.vue`, `VideoPlayer.vue`. Custom theme under `lectures/content/theme/`.
- **Workbook** (MkDocs, `lectures/workbook/`): ~10 substantial lecture notes,
  ~6 stubs (lectures 2–4, data_visualisation, statistics, python_fundamentals).
- **Quizzes:** `quiz_1_feedback.md`, `quiz_2_feedback.md` (BS-era; FF has no quizzes).

### 2.2 FF course requirements (from the authoritative `.docx`)
Source: `misc/description/Sandas_EN_CERN_methods_of_data_analysis.docx` (EN, official)
and `misc/description/2025-10-28-Koreguota_Edukacines_iniciatyvos_paraiska.docx`
(LT funding application).

- **Structure:** 16 weeks; 32 lecture-h + 32 seminar-h = **64 contact-h**;
  **5 ECTS**; 140 total student-h (64 contact + 76 self-study).
- **Grading: 100 % final project** (no interim tests/quizzes — differs from BS's
  40 % tests + 60 % project). Deliverables: semester-long GitHub repo with
  incremental history; English report + full code appendix; analysis results
  (plots + numbers); **30–60 s video walkthrough** linked from the repo; **live
  final presentation** (peer attendance mandatory).
- **Audience / mode:** Physics Faculty undergraduates; **English**; flipped
  classroom + individual GitHub-based project. Prereqs: English B1, high-school
  maths, laptop with Python 3.10+.
- **15-module syllabus (contact / self-study hours):**

  | FF module | h (contact/self) | Notes |
  |---|---|---|
  | L1 Course Orientation & Intro to CERN | 4 / 3 | |
  | L2 Crash Course on CS | 4 / 4 | |
  | L3 File Handling, Directories & Command Line | 4 / 4 | |
  | L4 Markdown & VS Code | 2 / 2 | |
  | L5 Version Control (Git/GitHub) | 4 / 6 | |
  | L6 Data-Analysis Project Organization | 4 / 5 | 1-2-3 data principle |
  | L7 Python Crash Course | **8 / 8** | deepest |
  | L8 NumPy, Pandas & Real-Data Case Studies | 4 / 6 | CERN open data |
  | L9 Concepts of Data Analysis & FAIR | 4 / 4 | FAIR principles |
  | L10 Data Visualisation | 4 / 5 | |
  | L11 Probability & Statistics | **6 / 7** | full stats |
  | L12 Data Fitting | **6 / 7** | full fitting |
  | L13 Computing Infrastructure | 4 / 4 | |
  | L14 Reproducible Workflows, Automation & Modularization | 4 / 6 | Snakemake |
  | L15 Project Review & Presentations | 2 / 5 | **new** |
  | **Total** | **64 / 76** | |

- **FF vs BS deltas:** tool-specific and deeper (explicit Git, Snakemake, CERN open
  data); full probability/statistics (6 h) + fitting (6 h) vs BS's ~2 h "basics";
  reproducibility with Snakemake vs BS's lighter treatment; 100 % project vs tests+project.

### 2.3 The two video pipelines
- **Teaching repo (current, simpler):** `scripts/videos.py` (~15 KB) with
  `sync`/`encode`/`publish`/`check`. Single tier: encodes raw → `lectures/content/
  public/videos/` and publishes to one GitHub Release (`videos`). **Uses HEVC
  (libx265) for the web tier** (a compatibility liability — see §4).
  `videos/manifest.toml` is source-of-truth (24 clips, `used_in` tags). `VideoPlayer.vue`
  has a single local→remote fallback (release `videos`). Also present:
  `crash_course_for_video_lecture.md` — a "recording deck, not shipped to students"
  (with a 1.8 GB `VU_VM.mp4`); evidence of prior recorded-lecture experiments.
- **Outreach repo (mature superset — the inspiration):** `scripts/videos.py`
  (~42 KB). **Two-tier:** web (H.264, ≤1920 px, browser hardware-decode) + HQ
  (HEVC venue masters). Subcommands: `sync`, `encode`, `encode-hq`, `publish`,
  `publish-hq`, `pull`, `pull-hq`, `check`, `shared-check`. **Shared-clip registry**
  (`/videos/shared.toml`) so multiple decks reuse clips without duplication.
  Per-video `hq_crf` / `long_edge_px` / `hq_from_raw` overrides. `VideoPlayer`
  fallback chain: HQ-local → web-local → talk release → shared release, configured
  via `VITE_VIDEO_REPO` / `VITE_VIDEO_RELEASE` / `VITE_VIDEO_SHARED_RELEASE`.
  Deps: `ffmpeg`, `rclone` (Google Drive raws), `gh` (Releases).

### 2.4 Decisions locked (2026-07-01)
1. **Master roadmap first**, then per-workstream spec → plan → build.
2. **Video = asset-pipeline upgrade only.** Port outreach's two-tier pipeline;
   **no** recorded lectures, **no** student-video tooling this cycle.
3. **Content re-org via new entry-point, not renames.** New
   `physics_faculty_2026.md` importing existing `L*` files in FF order + a mapping
   doc; keep file numbering.
4. **FF `.docx` untouched;** description edits go to a synced `.md`.
5. **Sub-project order A → B → C** (B and C depend on A's final module structure).

---

## 3. Workstream A — Content re-sequencing (bs2026 → 15 FF modules)

### Approach
Create a new entry-point `lectures/content/physics_faculty_2026.md` importing the
existing `L*` files **in FF module order**, plus a mapping doc
`lectures/content/FF_syllabus_map.md`. No disruptive renames — this mirrors how
`lessons_…md` / `staging.md` already work. Add a `pnpm dev:ff` script analogous to
the existing dev scripts.

### Mapping table (FF module → source → work)

| FF module | Source file(s) | Work bucket |
|---|---|---|
| L1 Orientation **+ Intro to CERN** | `L01` + `L02` | **merge**; fix grading → 100 % project |
| L2 Crash Course on CS | `L03_1_1` | **enable** (disabled) |
| L3 File Handling / Dirs / **Command Line** | `L03_1_2` + `L03_2` | **merge**; `L03_2` disabled |
| L4 Markdown **& VS Code** | `L03_3` + `L03_4` | **merge**; both disabled |
| L5 Version Control (Git/GitHub) | `L08` | reuse |
| L6 Data-Analysis **Project Organization** | extract from `L06`/`L03_1_2`/`L12` | **assemble** (1-2-3 data principle) |
| L7 Python Crash Course (**8 h, deepest**) | `L05` | **expand** |
| L8 NumPy/Pandas **+ Real-Data cases** | `L11_NumPy_Pandas` **+** `L11_Real_Data` | **merge two parallel L11 drafts** |
| L9 Concepts of Data Analysis **+ FAIR** | `L06` | **add FAIR** |
| L10 Data Visualisation | `L07` | **finish/enable** (182 slides, disabled) |
| L11 Probability & Statistics (6 h) | `L09` | reuse (comprehensive) |
| L12 Data Fitting (6 h) | `L10` | reuse (comprehensive) |
| L13 Computing Infrastructure | `L04` | reuse |
| L14 Reproducible Workflows **+ Snakemake** | `L12` | **add Snakemake** |
| **L15 Project Review & Presentations** | — | **new module** |

### Work buckets (summary)
- **Reuse as-is (4):** L5←`L08`, L11←`L09`, L12←`L10`, L13←`L04`.
- **Merge (4):** FF-L1, FF-L3, FF-L4, FF-L8.
- **Enable disabled (already-written, needs QA):** `L03_2/3/4`, `L07`.
- **New / expanded content (4):** FAIR (into FF-L9), Snakemake (into FF-L14),
  Python depth (FF-L7), and the brand-new **FF-L15**.
- **Fix:** `L01` grading 20/20/60 → 100 % project; reconcile contact-hour figures
  to the `.docx` (64 contact).

### Deliverables
`physics_faculty_2026.md` entry-point · `FF_syllabus_map.md` · a per-module task
list (its own sub-spec) · `L01` grading fix.

---

## 4. Workstream B — Video asset-pipeline upgrade (outreach-inspired)

Port the outreach **two-tier** design into the teaching repo:
- **Web tier → H.264** (fixes the current HEVC-for-web compatibility liability) +
  **HQ tier → HEVC** venue masters (`encode-hq`).
- Add `pull` / `pull-hq` (multi-machine), a **shared-clip registry**
  (`videos/shared.toml`), per-video `hq_crf` / `long_edge_px` / `hq_from_raw`
  overrides, and the richer profile set.
- **`VideoPlayer.vue`** → full fallback chain (HQ-local → web-local → talk release →
  shared release) with `VITE_VIDEO_*` env config.
- **Migrate `manifest.toml`** to the superset schema (add `release_tag_hq`,
  `web_long_edge_px`, etc.). Existing 24 clips + `used_in` tags carry over.

Self-contained engineering port; depends on A only insofar as new modules may add
clips. Deliverable: upgraded `scripts/videos.py`, `VideoPlayer.vue`, `manifest.toml`,
`videos/shared.toml`, and updated `pnpm` scripts + `CLAUDE.md` docs.

---

## 5. Workstream C — Project (100 %) + seminar framework *(net-new)*

Nothing here exists yet.
- **FF-L15** module: incremental review + final presentations.
- **Student GitHub template repo:** 1-2-3 data layout, README, English-report
  skeleton + code-appendix convention, a CI sanity check, a Snakemake stub.
- **Grading rubric** mapped to the `.docx` deliverables (repo history, report +
  appendix, plots/numbers, 30–60 s video, live presentation).
- **Seminar plan:** 32 h ≈ one hands-on seminar per lecture-week, each building
  toward the project; fill the 6 MkDocs workbook stubs.
- **Update `L01`** to reflect FF grading (100 % project) + course structure.

Deliverables: FF-L15 slides · template-repo spec (or the repo itself) · rubric ·
seminar plan · workbook content.

---

## 6. Timeline (D) — runway to September 2026

Not additional work — this is the **calendar** ordering A/B/C so the course is
ready for the first September lecture. ~9 weeks from 2026-07-01.

| When | What lands | Workstream |
|---|---|---|
| **Weeks 1–2** (early–mid Jul) | FF entry-point + `FF_syllabus_map.md`; enable `L03_2/3/4` + `L07`; fix `L01` grading | **A** (structure) |
| **Weeks 3–4** (late Jul) | Two-tier video pipeline port; manifest + `VideoPlayer` migration | **B** |
| **Weeks 5–7** (Aug) | New content: FAIR (L9), Snakemake (L14), FF-L15; the merges; finish `L07` | **A** (content) |
| **Week 8** (late Aug) | Project framework: template repo, rubric, seminar plan, workbook | **C** |
| **Week 9** (early Sep) | Dry-run, deploy to GitHub Pages, PDF export | all |

Dates are inferred from "September" — adjust if the semester start is fixed, or if
you want to reorder (e.g. do B first, as it's independent engineering).

---

## 7. Decomposition & next steps

Each workstream is its own spec → plan → build cycle. Recommended order **A → B → C**
(B and C both depend on A's final module structure), with §6 as the connecting schedule.

**Immediate next action:** on roadmap approval, invoke `superpowers:writing-plans`
for **Workstream A** to produce its implementation plan (FF entry-point + syllabus
map + enable-disabled + grading fix + the per-module merge/gap task list).

---

## 8. Open questions (deferred to sub-specs — not blocking the roadmap)
- Seminar exercise content per module.
- Project topic menu: student-chosen vs. from a list.
- AI-tool policy for projects (`L01` mentions "can use AI, must understand your
  code" — confirm the FF stance).
- Hosting target: GitHub vs. CERN GitLab (`VideoPlayer` currently points at
  `github.com/MindaugasSarpis/CERN_lessons_on_data_analysis`).
- FF `.docx` ↔ `.md` sync mechanics (keep `.docx` authoritative).
- Which L11 track is canonical, or whether FF-L8 fully absorbs both.
- Contact-hour discrepancy between the `L01` slide and the `.docx` (use `.docx`).

---

## 9. Change log
- **2026-07-01** — Initial roadmap drafted from the planning survey. Decisions
  locked (§2.4). Awaiting author review.
