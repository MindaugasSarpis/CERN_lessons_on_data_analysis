# FF-2026 Workstream A — Multi-Deck + Landing Shell Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the FF-2026 course into a themed **landing/portal deck + 15 independently-built lecture decks**, so opening a lecture loads only that lecture's bundle, driven by a single JSON module manifest.

**Architecture:** One JSON manifest (`lectures/content/ff/modules.json`) is the source of truth for three consumers: a landing deck (`<LectureGrid>` card grid), in-deck nav (`<CourseNav>` on each lecture's last slide), and a multi-deck build script (`scripts/build-ff.mjs`). FF entry files stay **flat in `lectures/content/`** so Slidev's userRoot (theme/public/slides/components) resolution is unchanged. Deploy is branch-aware ("switch branch" model): on `ff2026`, `build:ff` emits landing → `dist/` + each lecture → `dist/<slug>/`.

**Tech stack:** Slidev 52 (`@slidev/cli`), Vue 3 SFCs, Vite JSON import, Node ESM build script, GitHub Actions Pages.

**Spec:** `docs/superpowers/specs/2026-07-01-ff2026-multi-deck-landing-design.md` (approved 2026-07-01). Read it for rationale; this plan implements it.

**Scope reminder:** This builds the **navigable shell only**. Content merges, new FAIR/Snakemake/FF-L15 material, and the L01 grading fix (Quiz 20% / Quiz 20% / Project 60% at `slides/L01_Course_Orientation.md:175-207` → 100% project) are **follow-on**, not in this plan.

## Files

- Create: `lectures/content/ff/modules.json`
- Create: `lectures/content/FF_syllabus_map.md`
- Create: `lectures/content/components/CourseNav.vue`
- Create: `lectures/content/components/LectureGrid.vue`
- Create: `lectures/content/physics_faculty_2026.md` (landing)
- Create: `scripts/scaffold-ff.mjs` (+ generates the 15 `ff_L*.md` entries)
- Create: `scripts/build-ff.mjs`
- Modify: `package.json` (add `dev:ff`, `build:ff`, `scaffold:ff`)
- Modify: `.github/workflows/deploy.yml` (branch-aware, add `ff2026`)

---

## Task 1: Module manifest + human-readable map

**Files:**
- Create: `lectures/content/ff/modules.json`
- Create: `lectures/content/FF_syllabus_map.md`

- [ ] **Step 1: Write `lectures/content/ff/modules.json`** (source-file names verified against `lectures/content/slides/`):

```json
{
  "course": "FF-2026 — Methods of Data Analysis from CERN",
  "repo": "CERN_lessons_on_data_analysis",
  "modules": [
    { "id": "L01", "num": 1,  "slug": "L01", "title": "Course Orientation & Intro to CERN",                 "entry": "ff_L01_orientation_and_cern.md",   "sources": ["slides/L01_Course_Orientation.md", "slides/L02_Introduction_to_CERN.md"], "status": "draft" },
    { "id": "L02", "num": 2,  "slug": "L02", "title": "Crash Course on CS",                                  "entry": "ff_L02_crash_course_cs.md",        "sources": ["slides/L03_1_1_Crash_Course_on_Computer_Science.md"], "status": "draft" },
    { "id": "L03", "num": 3,  "slug": "L03", "title": "File Handling, Directories & Command Line",           "entry": "ff_L03_files_dirs_cmdline.md",     "sources": ["slides/L03_1_2_File_Handling_and_Directory_Structure.md", "slides/L03_2_Command_Line.md"], "status": "draft" },
    { "id": "L04", "num": 4,  "slug": "L04", "title": "Markdown & VS Code",                                  "entry": "ff_L04_markdown_vscode.md",        "sources": ["slides/L03_3_Markdown.md", "slides/L03_4_VS_Code.md"], "status": "draft" },
    { "id": "L05", "num": 5,  "slug": "L05", "title": "Version Control (Git/GitHub)",                        "entry": "ff_L05_version_control.md",        "sources": ["slides/L08_Version_Control.md"], "status": "ready" },
    { "id": "L06", "num": 6,  "slug": "L06", "title": "Data-Analysis Project Organization",                 "entry": "ff_L06_project_organization.md",   "sources": [], "status": "draft" },
    { "id": "L07", "num": 7,  "slug": "L07", "title": "Python Crash Course",                                 "entry": "ff_L07_python_crash_course.md",    "sources": ["slides/L05_Crash_Course_on_Python_Programming.md"], "status": "draft" },
    { "id": "L08", "num": 8,  "slug": "L08", "title": "NumPy, Pandas & Real-Data Case Studies",             "entry": "ff_L08_numpy_pandas_realdata.md",  "sources": ["slides/L11_NumPy_Pandas_Real_Data.md", "slides/L11_Real_Data_and_Case_Studies.md"], "status": "draft" },
    { "id": "L09", "num": 9,  "slug": "L09", "title": "Concepts of Data Analysis & FAIR",                   "entry": "ff_L09_concepts_fair.md",          "sources": ["slides/L06_Concepts_of_Data_Analysis.md"], "status": "draft" },
    { "id": "L10", "num": 10, "slug": "L10", "title": "Data Visualisation",                                 "entry": "ff_L10_data_visualisation.md",     "sources": ["slides/L07_Data_Visualisation.md"], "status": "draft" },
    { "id": "L11", "num": 11, "slug": "L11", "title": "Probability & Statistics",                           "entry": "ff_L11_probability_statistics.md", "sources": ["slides/L09_Probability_and_Statistics.md"], "status": "ready" },
    { "id": "L12", "num": 12, "slug": "L12", "title": "Data Fitting",                                        "entry": "ff_L12_data_fitting.md",           "sources": ["slides/L10_Data_Fitting.md"], "status": "ready" },
    { "id": "L13", "num": 13, "slug": "L13", "title": "Computing Infrastructure",                            "entry": "ff_L13_computing_infrastructure.md","sources": ["slides/L04_Computing_Infrastructure.md"], "status": "ready" },
    { "id": "L14", "num": 14, "slug": "L14", "title": "Reproducible Workflows, Automation & Modularization", "entry": "ff_L14_reproducible_workflows.md", "sources": ["slides/L12_Reproducible_Workflows.md"], "status": "draft" },
    { "id": "L15", "num": 15, "slug": "L15", "title": "Project Review & Presentations",                     "entry": "ff_L15_project_review.md",         "sources": [], "status": "draft" }
  ]
}
```

- [ ] **Step 2: Write `lectures/content/FF_syllabus_map.md`** — a human-readable table mirroring the manifest (FF module → source `slides/*` → shell action), copied from the spec §5 table, with a one-line note that `modules.json` is the machine source of truth.

- [ ] **Step 3: Validate JSON** — `node -e "JSON.parse(require('fs').readFileSync('lectures/content/ff/modules.json','utf8')).modules.forEach(m=>console.log(m.id,m.slug,m.entry))"` prints 15 rows, no parse error.

- [ ] **Step 4: Commit**

```bash
git add lectures/content/ff/modules.json lectures/content/FF_syllabus_map.md
git commit -m "feat(ff): module manifest + syllabus map (single source of truth)"
```

---

## Task 2: `CourseNav.vue` + `LectureGrid.vue`

**Files:**
- Create: `lectures/content/components/CourseNav.vue`
- Create: `lectures/content/components/LectureGrid.vue`

Both import `../ff/modules.json` (from `components/` → `ff/`). Auto-imported by Slidev (userRoot = `lectures/content/`).

- [ ] **Step 1: Write `CourseNav.vue`** (last-slide nav; base-relative links so it works under any `--base`):

```vue
<script setup>
import modulesData from '../ff/modules.json'

const props = defineProps({ current: { type: String, required: true } })
const base = import.meta.env.BASE_URL || '/'
const mods = modulesData.modules
const idx = mods.findIndex(m => m.id === props.current)
const prev = idx > 0 ? mods[idx - 1] : null
const next = idx >= 0 && idx < mods.length - 1 ? mods[idx + 1] : null
const indexHref = `${base}../`
const href = (m) => `${base}../${m.slug}/`
</script>

<template>
  <div class="course-nav">
    <a :href="indexHref" class="nav-link nav-home">⌂ Index</a>
    <a v-if="prev" :href="href(prev)" class="nav-link">← {{ prev.id }} · {{ prev.title }}</a>
    <span v-else class="nav-spacer"></span>
    <a v-if="next" :href="href(next)" class="nav-link nav-next">{{ next.id }} · {{ next.title }} →</a>
    <span v-else class="nav-spacer"></span>
  </div>
</template>

<style scoped>
.course-nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.5rem;
  width: 100%;
  max-width: 60rem;
  margin: 0 auto;
  font-size: 1.1rem;
}
.nav-link {
  color: #93c5fd;
  text-decoration: none;
  padding: 0.4rem 0.9rem;
  border: 1px solid rgba(147, 197, 253, 0.35);
  border-radius: 0.5rem;
  transition: background 0.2s;
  white-space: nowrap;
}
.nav-link:hover { background: rgba(147, 197, 253, 0.15); }
.nav-next { margin-left: auto; }
.nav-spacer { flex: 0 0 1px; }
</style>
```

- [ ] **Step 2: Write `LectureGrid.vue`** (landing card grid; uses the theme's real classes `card card-glass pad-tight` + `grid-3 gap-md`):

```vue
<script setup>
import modulesData from '../ff/modules.json'

const base = import.meta.env.BASE_URL || '/'
const mods = modulesData.modules
const href = (m) => `${base}${m.slug}/`
const palette = ['card-primary', 'card-secondary', 'card-accent', 'card-info', 'card-success', 'card-warning']
const color = (i) => palette[i % palette.length]
</script>

<template>
  <div class="grid-3 gap-md mt-md">
    <a
      v-for="(m, i) in mods"
      :key="m.id"
      :href="href(m)"
      class="card card-glass pad-tight lecture-card"
      :class="color(i)"
    >
      <div class="lecture-num">{{ m.id }}</div>
      <div class="lecture-title">{{ m.title }}</div>
      <span v-if="m.status === 'draft'" class="lecture-badge">draft</span>
    </a>
  </div>
</template>

<style scoped>
.lecture-card {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  text-decoration: none;
  color: inherit;
  position: relative;
  min-height: 6.5rem;
  transition: transform 0.15s ease;
}
.lecture-card:hover { transform: translateY(-3px); }
.lecture-num { font-size: 1.4rem; font-weight: 700; opacity: 0.85; }
.lecture-title { font-size: 1rem; line-height: 1.25; }
.lecture-badge {
  position: absolute;
  top: 0.5rem;
  right: 0.6rem;
  font-size: 0.65rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  opacity: 0.6;
  border: 1px solid currentColor;
  border-radius: 0.35rem;
  padding: 0 0.35rem;
}
</style>
```

- [ ] **Step 3: Commit**

```bash
git add lectures/content/components/CourseNav.vue lectures/content/components/LectureGrid.vue
git commit -m "feat(ff): CourseNav + LectureGrid components (manifest-driven)"
```

---

## Task 3: Landing portal deck

**Files:**
- Create: `lectures/content/physics_faculty_2026.md`

- [ ] **Step 1: Write the landing deck** (flat in `lectures/content/`, so `theme: ./theme` and `/figures/…` resolve as in the BS deck):

```md
---
theme: ./theme
colorSchema: dark
routerMode: hash
background: /figures/background_intro.jpg
class: text-left
mermaid: true
hideInToc: true
---

# FF-2026
## Methods of Data Analysis from CERN

Physics Faculty · autumn 2026 · Dr. Mindaugas Šarpis

---
hideInToc: true
---

# **Lectures**

<LectureGrid />
```

- [ ] **Step 2: Dev smoke** — `pnpm dev:ff` (added in Task 5; if not yet, `npx slidev lectures/content/physics_faculty_2026.md`). Landing renders the cover + a 15-card grid. Cards are inert in dev (single-deck) — expected per spec §7.

- [ ] **Step 3: Commit**

```bash
git add lectures/content/physics_faculty_2026.md
git commit -m "feat(ff): themed landing portal deck (LectureGrid)"
```

---

## Task 4: Scaffold the 15 lecture entry files

**Files:**
- Create: `scripts/scaffold-ff.mjs`
- Create (generated): `lectures/content/ff_L01_*.md` … `ff_L15_*.md`

- [ ] **Step 1: Write `scripts/scaffold-ff.mjs`** — idempotent generator (skips existing entries so hand-edits survive re-runs):

```js
import { readFileSync, writeFileSync, existsSync } from 'node:fs'
import { fileURLToPath } from 'node:url'
import { dirname, resolve } from 'node:path'

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..')
const contentDir = resolve(root, 'lectures/content')
const { modules } = JSON.parse(readFileSync(resolve(contentDir, 'ff/modules.json'), 'utf8'))

// The deck's FIRST slide must carry content, else Slidev renders a blank
// leading slide (the headmatter fence followed immediately by `---\nsrc:`
// yields an empty slide 0). So slide 1 is a cover holding the module title
// IN the headmatter block's body, THEN the src imports (or placeholder),
// THEN the nav slide.
function deck(m) {
  const head = `---
theme: ./theme
colorSchema: dark
routerMode: hash
addons:
  - slidev-addon-python-runner
mermaid: true
defaults:
  preload: false
layout: cover
---

# ${m.id} · ${m.title}

Methods of Data Analysis from CERN
`
  const middle = m.sources.length
    ? m.sources.map((src) => `\n---\nsrc: ${src}\n---\n`).join('')
    : `\n---\n\n> Module content in development.\n`
  const nav = `\n---\nlayout: center\nhideInToc: true\n---\n\n<CourseNav current="${m.id}" />\n`
  return head + middle + nav
}

let created = 0, skipped = 0
for (const m of modules) {
  const path = resolve(contentDir, m.entry)
  if (existsSync(path)) { skipped++; continue }
  writeFileSync(path, deck(m))
  created++
  console.log(`+ ${m.entry}`)
}
console.log(`\nScaffold done: ${created} created, ${skipped} skipped (already existed).`)
```

- [ ] **Step 2: Run it** — `node scripts/scaffold-ff.mjs`. Expected: 15 created. Confirm files exist: `ls lectures/content/ff_L*.md | wc -l` → 15.

- [ ] **Step 3: Spot-check a `ready` entry** — `cat lectures/content/ff_L05_version_control.md` shows the headmatter with `layout: cover` and a `# L05 · …` cover body as slide 1, then `src: slides/L08_Version_Control.md`, then a trailing `<CourseNav current="L05" />` slide. Confirm there is **no** empty slide between the headmatter fence and the cover title.

- [ ] **Step 4: Spot-check a placeholder** — `ff_L06_project_organization.md` and `ff_L15_project_review.md` show the cover title (slide 1), an "in development" slide, then CourseNav (no `src:`).

- [ ] **Step 5: Commit**

```bash
git add scripts/scaffold-ff.mjs lectures/content/ff_L*.md
git commit -m "feat(ff): scaffold 15 lecture entry decks from manifest"
```

---

## Task 5: Build script + package.json scripts

**Files:**
- Create: `scripts/build-ff.mjs`
- Modify: `package.json`

- [ ] **Step 1: Write `scripts/build-ff.mjs`** — landing first (emits `dist/` root), then each lecture into `dist/<slug>/`. `--out` is relative to the entry dir (`lectures/content/`), so paths are `../../dist` (matches the existing deploy's `--out ../../dist`):

```js
import { execSync } from 'node:child_process'
import { readFileSync, rmSync } from 'node:fs'
import { fileURLToPath } from 'node:url'
import { dirname, resolve } from 'node:path'

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..')
const repo = process.env.REPO_NAME || 'CERN_lessons_on_data_analysis'
const { modules } = JSON.parse(readFileSync(resolve(root, 'lectures/content/ff/modules.json'), 'utf8'))

// Fresh dist/ (slidev won't empty an outDir outside userRoot).
rmSync(resolve(root, 'dist'), { recursive: true, force: true })

function build(entry, base, out) {
  console.log(`\n=== ${entry} -> ${out} (base ${base}) ===`)
  execSync(
    `npx -y @slidev/cli@latest build lectures/content/${entry} --base ${base} --out ${out}`,
    { stdio: 'inherit', cwd: root, env: { ...process.env, NODE_OPTIONS: '--max-old-space-size=4096' } }
  )
}

// '--out' is resolved relative to the entry's dir (lectures/content), hence ../../dist.
build('physics_faculty_2026.md', `/${repo}/`, '../../dist')
for (const m of modules) build(m.entry, `/${repo}/${m.slug}/`, `../../dist/${m.slug}`)

console.log(`\n✓ FF build complete: dist/ (landing) + ${modules.length} lecture decks`)
```

- [ ] **Step 2: Add scripts to `package.json`.** Alongside the existing `dev`/`dev:staging`/`dev:lecture`/`build`, add:

```json
    "dev:ff": "slidev lectures/content/physics_faculty_2026.md",
    "scaffold:ff": "node scripts/scaffold-ff.mjs",
    "build:ff": "node scripts/build-ff.mjs",
```

- [ ] **Step 3: Verify** `pnpm run | grep -E "dev:ff|build:ff|scaffold:ff"` lists all three.

- [ ] **Step 4: Commit**

```bash
git add scripts/build-ff.mjs package.json
git commit -m "feat(ff): build-ff.mjs (landing + 15 decks) + dev:ff/build:ff scripts"
```

---

## Task 6: Branch-aware deploy workflow

**Files:**
- Modify: `.github/workflows/deploy.yml`

- [ ] **Step 1: Add `ff2026` to the trigger and make the build branch-aware.** Replace the `on.push.branches` and the `Build` step:

```yaml
on:
  workflow_dispatch:
  push:
    branches: [bs2026, ff2026]
```

```yaml
      - name: Build
        env:
          NODE_OPTIONS: --max-old-space-size=4096
          REPO_NAME: ${{ github.event.repository.name }}
        run: |
          if [ "${{ github.ref_name }}" = "ff2026" ]; then
            pnpm build:ff
          else
            npx -y @slidev/cli@latest build --out ../../dist \
              lectures/content/lessons_on_data_analysis_from_CERN.md \
              --base "/${{ github.event.repository.name }}/"
          fi
```

The `Upload artifact` step keeps `path: dist` (both branches emit `dist/` at repo root). Under the "switch branch" model, whichever branch pushes last owns the single Pages site (`concurrency: group: pages`).

- [ ] **Step 2: Lint the YAML** — `python3 -c "import yaml,sys; yaml.safe_load(open('.github/workflows/deploy.yml'))" && echo OK`.

- [ ] **Step 3: Commit**

```bash
git add .github/workflows/deploy.yml
git commit -m "ci(ff): branch-aware deploy — ff2026 builds multi-deck via build:ff"
```

---

## Task 7: End-to-end verification

- [ ] **Step 1: Full FF build** — `pnpm build:ff`. Expected: completes; `dist/index.html` (landing) exists and `dist/<slug>/index.html` exists for all 15 slugs:

```bash
ls dist/index.html && for s in L01 L02 L03 L04 L05 L06 L07 L08 L09 L10 L11 L12 L13 L14 L15; do test -f "dist/$s/index.html" && echo "ok $s" || echo "MISSING $s"; done
```

- [ ] **Step 2: Serve + click-through** — serve `dist/` at a base that matches (`--base` was `/<repo>/`, so serve so that `/<repo>/` maps to `dist/`):

```bash
mkdir -p _serve/CERN_lessons_on_data_analysis && cp -r dist/* _serve/CERN_lessons_on_data_analysis/ && (cd _serve && python3 -m http.server 8099)
```
Open `http://localhost:8099/CERN_lessons_on_data_analysis/`: the landing shows the 15-card grid; clicking **L05** loads `…/L05/` (its own bundle); its **last slide** shows `⌂ Index · ← L04 · L06 →`; those links resolve to `…/`, `…/L04/`, `…/L06/`. Clean up `_serve/` after.

- [ ] **Step 3: Asset resolution on a `ready` deck** — in the L05 deck, confirm figures (`/figures/…`), any `VideoPlayer`, `MCQ`, and python-runner render — proving flat-entry userRoot resolution. (L05←`L08_Version_Control` is the safe `ready` check.)

- [ ] **Step 4: Confirm imported sources render** — L10 imports `slides/L07_Data_Visualisation.md`; L03 imports `slides/L03_2_Command_Line.md`; L04 imports `slides/L03_3_Markdown.md` + `slides/L03_4_VS_Code.md`. These are **not** deck-level disabled (verified: no `disabled` key in their headmatter — the roadmap's "disabled:true" annotation was inaccurate; the current BS deck already imports and renders them). Just confirm their slides appear in `dist/L10/`, `dist/L03/`, `dist/L04/`. **Do NOT edit `slides/*`** — the interior per-slide `disabled: true` blocks (e.g. 13 in `L07`) are intentional author hides *shared with the BS deck*; stripping them would corrupt both decks. Selectively surfacing hidden slides for FF is content work, out of this shell's scope.

- [ ] **Step 5: BS deck untouched** — `pnpm build` (BS single-deck) still succeeds; nothing in `lessons_on_data_analysis_from_CERN.md` or `slides/*` content changed (only possibly a `disabled:` flag removal from Step 4, which is intended).

- [ ] **Step 6: Clean build junk + final commit — explicit paths, not `git add -A`** (so a parallel Workstream B checkout and build artifacts aren't swept in):

```bash
rm -rf _serve dist
git add lectures/content/ff/modules.json lectures/content/FF_syllabus_map.md \
  lectures/content/components/CourseNav.vue lectures/content/components/LectureGrid.vue \
  lectures/content/physics_faculty_2026.md lectures/content/ff_L*.md \
  scripts/scaffold-ff.mjs scripts/build-ff.mjs package.json .github/workflows/deploy.yml
git commit -m "test(ff): verify multi-deck build, click-through nav, asset render"
```

---

## Self-review checklist (run after drafting, before execution)
- **Spec coverage:** landing portal ✓ (T3); per-module decks ✓ (T4); manifest SoT ✓ (T1); CourseNav last-slide ✓ (T2,T4); flat entries ✓ (T4 headmatter, T7§3); build/deploy ✓ (T5,T6); dev scripts ✓ (T5); 15-module mapping ✓ (T1 == spec §5).
- **Name consistency:** `slug`/`entry`/`id`/`status` identical across `modules.json`, `CourseNav`, `LectureGrid`, `scaffold-ff.mjs`, `build-ff.mjs`. `<CourseNav current="Lxx">` matches `modules[].id`.
- **`--out` relativity:** `../../dist` (entry-dir-relative) matches the existing working deploy — not a guess.
- **No content work leaked in:** merges/FAIR/Snakemake/FF-L15/L01-grading are explicitly follow-on (header + spec §1).
```
