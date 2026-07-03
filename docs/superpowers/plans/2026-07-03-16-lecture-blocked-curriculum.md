# 16-Lecture Blocked Curriculum Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans (inline, phase-gated) to implement this plan. Steps use checkbox (`- [ ]`) syntax. Each phase ends green (all decks build + zero overflow) and is independently shippable.

**Goal:** Deliver the course as 16 per-lecture Slidev decks behind a static landing page (fixing mobile load), organised into 5 blocks with advanced last, tied together by the four course aims and one running project, plus 16 seminar workbook pages.

**Architecture:** A `decks.json` manifest drives a `build-all.mjs` runner that builds each deck from a small entry file (co-located with `theme/`, `src:`-importing its lecture source) to `dist/<slug>/`, then emits `dist/index.html` from a landing template. Multi-deck overflow QA gates every deck. Deploy builds all + assembles `dist/`.

**Tech Stack:** Slidev (build per entry with `--base`), Node ESM scripts, Playwright-chromium QA (existing `check-slides.mjs`), MkDocs (workbook/seminars), GitHub Pages.

## Global Constraints

- Course name: **"Best Research and Data Analysis Practices from CERN"** (verbatim on every cover/landing).
- Zero slide overflow per deck at 6px tolerance, verified by **rendering** (multi-deck QA), not just building.
- Per-lecture decks build only from an **entry file co-located with `lectures/content/theme/`** (a bare `slides/L0X.md` build drops the theme — project memory).
- House style: card system, one type scale (no one-off font-size on content), kinetic accents, emoji-outside-bold headings; videos full-screen; within-file language consistency.
- **Concept-before-tool** framing on every tooling slide (tool-agnosticism is a hard rule).
- Every new/added slide advances a named aim (🔧 agnosticism · ♻️ reproducibility · ⚙️ automation · 📁 data/files) or the running project — no filler.
- Block E (L15–L16) must be removable without breaking L1–L14 — no earlier lecture may depend on it.
- Slug scheme: `NN-kebab-title`, zero-padded, so URL order = delivery order.
- Commit trailer on every commit: `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>` + the `Claude-Session:` line.
- Slidev gotcha: never place raw `<<<<<<<`/`=======`/`>>>>>>>` conflict markers in fenced code (crashes the snippet plugin) — use the `{{'<<<<<<< HEAD'}}` escape.

## Deck manifest (target 16 — reached in P2; P1 ships the 12 published as decks first)

| slug | title | block | entry `src:` | optional |
|--|--|--|--|--|
| 01-orientation | Orientation & Data in Your Life | A | L01 | no |
| 02-cern | Introduction to CERN | A | L02 | no |
| 03-how-computers-work | How Computers Work | A | L03_1_1 | no |
| 04-command-line-and-files | Command Line & File Handling | A | L03_2 + L03_1_2 | no |
| 05-markdown-and-vscode | Markdown & VS Code | A | L03_3 + L03_4 | no |
| 06-version-control | Version Control with Git | A | L08 | no |
| 07-python-foundations | Python Foundations | B | L05a | no |
| 08-python-for-data | Python for Data Work | B | L05b | no |
| 09-concepts-of-data-analysis | Concepts of Data Analysis | C | L06 | no |
| 10-data-visualisation | Data Visualisation | C | L07 | no |
| 11-probability-and-statistics | Probability & Statistics | C | L09 | no |
| 12-data-fitting | Practical Data Fitting | C | L10 | no |
| 13-numpy-and-pandas | NumPy & Pandas | D | L11 | no |
| 14-reproducible-workflows | Reproducible Workflows & Automation | D | L12 | no |
| 15-computing-infrastructure | Computing Infrastructure & HPC | E | L04 | **yes** |
| 16-machine-learning | Machine Learning & AI | E | L16 (new) | **yes** |

---

## Phase P1 — Blocked build + landing page (from EXISTING lectures) — the mobile-load win

Ships a working multi-deck site from the 12 already-published lectures, before any content changes. Manifest starts with the 12 published `src` files as 12 decks (merges/splits deferred to P2).

### Task P1.1: Deck manifest + per-deck entry files

**Files:**
- Create: `lectures/content/decks.json`
- Create: `lectures/content/decks/<slug>.md` (one tiny entry per deck)
- Reference: `lectures/content/lessons_on_data_analysis_from_CERN.md:1-20` (shared frontmatter to copy)

- [ ] **Step 1: Author `decks.json`** as an array of `{slug, title, block, srcs: [..], optional}`. P1 seeds it with the 12 published lectures (one src each), slugs `01-orientation`…`12-…` in the published order from `lessons_on_data_analysis_from_CERN.md`.
- [ ] **Step 2: Create the entry-file generator** `scripts/gen-entries.mjs`: reads `decks.json`, and for each deck writes `lectures/content/decks/<slug>.md` = the shared frontmatter block (theme `./theme`, `colorSchema: dark`, background, transition, `addons: [slidev-addon-python-runner]`, `mermaid: true`) — path-adjusted so `theme` resolves (entries live in `lectures/content/decks/`, so use `theme: ../theme` and `src: ../slides/<file>.md`). Verify theme resolves by building one deck (next task).
- [ ] **Step 3: Generate entries** — run `node scripts/gen-entries.mjs`; confirm 12 files in `lectures/content/decks/`.
- [ ] **Step 4: Commit** — `feat(build): deck manifest + generated per-deck entry files`.

### Task P1.2: `build-all.mjs` runner

**Files:**
- Create: `scripts/build-all.mjs`
- Modify: `package.json` (scripts)

- [ ] **Step 1: Write `build-all.mjs`** — reads `decks.json`; for each deck runs `slidev build lectures/content/decks/<slug>.md --out dist/<slug> --base <BASE>/<slug>/` where `BASE` defaults to `` (local) or the repo path in CI (pass via `--base` arg or `SLIDEV_BASE` env). Accepts `--out <dir>` (default `dist`) and `--only <slug,...>`. Fail the whole run non-zero if any deck build fails.
- [ ] **Step 2: Verify theme loads** — run `node scripts/build-all.mjs --only 06-version-control --out .buildtest`; open `.buildtest/06-version-control/index.html` build output and confirm the custom theme CSS is present (grep the built assets for a theme class e.g. `card-glass`). Expected: present (theme resolved). If absent, fix the `theme:` path in the entry template and re-run.
- [ ] **Step 3: Add scripts** — `"build:all": "node scripts/build-all.mjs"`, keep old `build` for the internal combined authoring build.
- [ ] **Step 4: Full local build** — `node scripts/build-all.mjs --out dist` builds all 12 decks. Confirm `dist/<slug>/index.html` exists for each.
- [ ] **Step 5: Commit** — `feat(build): build-all runner for per-deck builds`.

### Task P1.3: Landing page

**Files:**
- Create: `scripts/gen-landing.mjs`
- Create: `lectures/content/landing/landing.css` (inlined at build)
- Modify: `scripts/build-all.mjs` (call landing generation at the end)

- [ ] **Step 1: Write `gen-landing.mjs`** — reads `decks.json`, emits `dist/index.html`: a self-contained (inline CSS) course-home page titled the course name, presenter line, grouped by block (A–E headings), each deck a card linking to `<base>/<slug>/`, Block E cards marked "Optional". Include a "Seminars" section linking to the workbook (P6 fills these; for now link to the workbook root). Theme-match the deck aesthetic (dark, card-glass look) but **no external assets** (Pages-safe).
- [ ] **Step 2: Wire into build-all** — after decks build, `build-all.mjs` calls the landing generator with the same base.
- [ ] **Step 3: Build + eyeball** — `node scripts/build-all.mjs --out dist`; open `dist/index.html`, confirm all blocks/links render and links resolve to the built deck dirs.
- [ ] **Step 4: Commit** — `feat(build): static landing page generated from the manifest`.

### Task P1.4: Multi-deck overflow QA

**Files:**
- Modify: `scripts/check-slides.mjs` (add manifest mode)
- Create: `scripts/qa-all.mjs` (thin wrapper: build all to `.qa-dist/<slug>`, run overflow on each)
- Modify: `package.json` (`qa` → manifest mode)

- [ ] **Step 1: Add `qa-all.mjs`** — builds every deck to `.qa-dist/<slug>` (reuse build-all with `--out .qa-dist`), then for each slug runs the existing overflow measurement against `.qa-dist/<slug>`; aggregate: non-zero exit if any deck overflows or any slide fails to render. Print per-deck summary.
- [ ] **Step 2: Point `pnpm qa`** at `qa-all.mjs`; keep `qa:overflow` for a single dir.
- [ ] **Step 3: Run** `pnpm qa` — expect every deck `✅ No overflow`. Fix any deck that regresses (the split entries shouldn't change layout, so expect clean).
- [ ] **Step 4: Commit** — `feat(qa): multi-deck overflow gate`.

### Task P1.5: Deploy workflow

**Files:**
- Modify: `.github/workflows/deploy.yml`

- [ ] **Step 1: Replace the single build step** with `pnpm install` then `node scripts/build-all.mjs --out dist --base /${{ github.event.repository.name }}` (base applied per-deck as `/<repo>/<slug>/`, landing at `/<repo>/`). Keep `NODE_OPTIONS=--max-old-space-size=4096`, keep upload of `dist`, keep `bs2026` trigger.
- [ ] **Step 2: Sanity-check base handling** — build locally with `--base /CERN_lessons_on_data_analysis` and confirm landing links and in-deck asset URLs use the repo-prefixed path.
- [ ] **Step 3: Commit** — `ci: build and deploy per-deck blocked site`.

**P1 exit:** `pnpm qa` green across all decks; `dist/` has a landing page + 12 deck dirs; deploy workflow updated. Mobile-load win is live once deployed. **Ship P1 before P2.**

---

## Phase P2 — Restructure to the final 16 lectures

Adjust the manifest and source files to the 16-lecture structure. Merges use multi-`src` entries (no file surgery); the one split needs file surgery.

### Task P2.1: Merge tooling decks
- [ ] Update `decks.json`: deck `04-command-line-and-files` `srcs: [L03_2, L03_1_2]`; deck `05-markdown-and-vscode` `srcs: [L03_3, L03_4]`. Regenerate entries (each entry emits multiple `src:` lines in order). Build + QA those two decks. Commit `feat(curriculum): merge CLI+files and markdown+vscode into single decks`.

### Task P2.2: Split Python into two lectures
- [ ] Split `L05_Crash_Course_on_Python_Programming.md` at the natural Data-Structures / Files-&-Modules boundary into `L05a_Python_Foundations.md` (setup, types, control flow, functions/exceptions, comprehensions) and `L05b_Python_for_Data.md` (collections, strings-for-data, files, modules, the data bridge). Preserve the cover frontmatter on both; L05b gets its own cover. Add manifest decks `07-python-foundations` (L05a) and `08-python-for-data` (L05b). Build + QA. Commit `feat(curriculum): split Python into foundations + data-work lectures`.

### Task P2.3: Add the 4 drafts + ML placeholder to the manifest
- [ ] Add decks `12-data-fitting` (L10), `13-numpy-and-pandas` (L11), `14-reproducible-workflows` (L12), `15-computing-infrastructure` (L04, optional), and a stub `16-machine-learning` entry pointing at a new `L16_Machine_Learning_and_AI.md` containing only a cover (filled in P4). Renumber slugs to the final 16 order. Build + QA (drafts must already be overflow-clean or are fixed here). Commit `feat(curriculum): add drafts and ML slot to the 16-deck manifest`.

**P2 exit:** manifest = the final 16 decks; all build + QA green; landing shows 16 lectures in 5 blocks.

---

## Phase P3 — Finish the 4 drafts to publishable standard

One task per draft. Each follows the **proven per-lecture enrichment workflow** from this session: read fully → gap-check vs the block's aims → verify facts (WebSearch/WebFetch) → edit in house style weaving the four aims + running-project references → `pnpm qa` for that deck green → screenshot-review changed slides → commit. Sources per the spec.

- [ ] **Task P3.1 — L10 Practical Data Fitting** (deck 12). Ensure it delivers least-squares/MLE/χ² cleanly, ties back to L11 stats (SE/CI) and forward to L16; add "Could you rebuild this?" + "Automate this" motifs. QA green. Commit `feat(L10): finish Practical Data Fitting to publishable standard`.
- [ ] **Task P3.2 — L11 NumPy & Pandas** (deck 13). The data-wrangling payoff; fold in the strongest Real-Data case-study examples; concept-before-tool (arrays/tables as ideas, NumPy/Pandas as one implementation). QA green. Commit `feat(L11): finish NumPy & Pandas to publishable standard`.
- [ ] **Task P3.3 — L12 Reproducible Workflows & Automation** (deck 14). The aims made explicit: environments, Make/CI, pipelines; references the running project's one-command rebuild. QA green. Commit `feat(L12): finish Reproducible Workflows to publishable standard`.
- [ ] **Task P3.4 — L04 Computing Infrastructure & HPC** (deck 15, optional). Where reproducible/automated work scales; keep self-contained and droppable. QA green. Commit `feat(L04): finish Computing Infrastructure to publishable standard`.

**P3 exit:** decks 12–15 publishable; full `pnpm qa` green.

---

## Phase P4 — New lecture: Machine Learning & AI (deck 16)

- [ ] **Task P4.1 — Build `L16_Machine_Learning_and_AI.md`** as a capstone that *applies* the four aims (not a math course): the ML framing (features→model→evaluation), train/validation/test & overfitting (callback to L06 MCQ + L11 stats), a worked scikit-learn-style classifier on the running-project data, honest evaluation, then a short, current AI/LLM-tooling section (verify model/tooling facts via the claude-api/WebSearch as needed). House style, four-aim callouts, zero overflow. Sources: intro-ML texts + official docs. QA green. Commit `feat(L16): new Machine Learning & AI capstone lecture`.

**P4 exit:** all 16 decks build + QA green; landing complete.

---

## Phase P5 — Weave the four-aim spine + running-project references across all lectures

One light pass per deck adding: the named-aim callouts where missing, the recurring "Could you rebuild this?" (data lectures) and "Automate this" (tooling/data lectures) slides, and forward/back running-project references ("you'll clean this in Seminar 13" / "the raw file from Seminar 4"). Keep additions minimal and overflow-safe.

- [ ] **Task P5.1 — Aim callouts + motifs, decks 01–08** (Foundations + Programming). QA green. Commit `feat(spine): four-aim callouts and motifs across blocks A–B`.
- [ ] **Task P5.2 — Aim callouts + motifs, decks 09–16** (Data + Advanced). QA green. Commit `feat(spine): four-aim callouts and motifs across blocks C–E`.

**P5 exit:** every deck names the aims it advances and references the running project; full QA green.

---

## Phase P6 — 16 seminar workbook pages + the running project

**Files:**
- Create: `lectures/workbook/docs/seminars/seminar_NN.md` × 16
- Create: `lectures/workbook/docs/seminars/running-project.md` (dataset + starter repo skeleton + how each seminar layers on)
- Modify: `lectures/workbook/mkdocs.yml` (nav: add a "Seminars" section with the 16 pages)
- Modify: `scripts/gen-landing.mjs` (link each seminar from the landing "Seminars" section)

- [ ] **Task P6.1 — Running-project page + dataset.** Choose the dataset (CERN-Open-Data / sensor-style tabular, consistent with L06/L09 examples), commit it under the workbook (or a documented fetch step), write `running-project.md` (goal, the repo skeleton, the layer-per-seminar map). Commit `feat(seminars): running-project dataset + overview page`.
- [ ] **Task P6.2 — Seminars 1–8 pages.** Each: goal · prerequisites · step-by-step tasks · stretch goals · solution notes; each adds its layer (skeleton→dataset→encoding→CLI-clean→README→git→parse→ingest). Add to mkdocs nav. `mkdocs build` succeeds. Commit `feat(seminars): S1–S8 workbook pages`.
- [ ] **Task P6.3 — Seminars 9–16 pages.** (quality-audit→figure→uncertainty→fit→pandas-clean→make-reproducible→remote-run→model). S15–16 marked optional. Add to nav. `mkdocs build` succeeds. Commit `feat(seminars): S9–S16 workbook pages`.
- [ ] **Task P6.4 — Landing links + final full QA.** Landing "Seminars" section links to each workbook page; run full `pnpm qa` (all decks) + `mkdocs build`. Commit `feat(seminars): link seminars from landing; final QA`.

**P6 exit:** 16 lecture decks + landing + 16 seminar pages + running project; `pnpm qa` green; `mkdocs build` clean.

---

## Self-Review

- **Spec coverage:** architecture (P1), 16-lecture restructure incl. split/merge (P2), finish 4 drafts (P3), new ML/AI (P4), four-aim spine + running project references (P5), 16 seminars + dataset (P6), deploy/QA changes (P1.4/P1.5). Advanced-last & droppable enforced (Block E optional in manifest; P3.4/P4 self-contained). Course-name constraint in Global Constraints. All spec sections map to a phase.
- **Placeholders:** none — the only deliberately-deferred item is the ML lecture *content*, which is Task P4.1's whole job, and the dataset choice, which is Task P6.1's whole job (both are tasks, not gaps).
- **Consistency:** slugs and manifest fields (`slug/title/block/srcs/optional`) are used identically across P1–P6; QA command (`pnpm qa` → `qa-all.mjs`) consistent; the theme-path caveat is stated in Global Constraints and enforced in P1.1/P1.2.
