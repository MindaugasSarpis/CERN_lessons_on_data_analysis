# Visual Style Upgrade Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Give the Slidev decks a bold, kinetic, modern look via a reusable theme-level system, then apply it fully to one pilot lecture (L01) for sign-off.

**Architecture:** Extend the local `@slidev/theme-scienced` theme with (1) new palette + display-font tokens, (2) a shared `animations.css` motion/effects library that generalizes patterns currently inlined in the video deck & L06, and (3) upgraded `section`/`fact`/`statement` layouts. All additions are opt-in and backward-compatible; existing class names are untouched. The pilot lecture L01 then consumes the new system end-to-end.

**Tech Stack:** Slidev 52 (Vue 3 SFC layouts, UnoCSS), plain CSS custom properties, Google Fonts (Space Grotesk), no build-tool changes, no test framework (verification is visual via the dev server).

## Global Constraints

- **Visual only — no content edits.** Do NOT change any lecture wording, numbers, or slide meaning. In particular, L01's grading slide (Quiz 20% / 20% / Project 60%) and the "48 hours / 212 hours" figures stay exactly as written — those are Workstream-A content concerns.
- **Backward compatible.** Never rename or remove an existing class or layout (`card`, `card-*`, `card-glass`, `grid-*`, `pad-*`, `stack-tight`, `anim-*`, `flow-*`, `dice-*`, `dd-*`, `fig`, etc.). New effects are additive opt-in classes.
- **Motion-safe & mobile-safe.** Every animation MUST have a `@media (prefers-reduced-motion: reduce)` fallback to a static end-state, and heavy effects (blur/aurora/hue-pan) MUST be disabled under `@media (max-width: 768px), (pointer: coarse)` — mirroring the existing `theme/layouts/cover.vue`.
- **No slide overflow (STRICT, blocking gate).** Every rendered slide MUST fit its 16:9 frame with zero content overflow — nothing clipped or spilling past the edges. A `slidev build` does NOT catch this; it must be verified by rendering. The deck-wide font change (Space Grotesk) and any new layout are high-risk for reflow. Gate: `pnpm qa:overflow` (after `pnpm qa:build`) — i.e. `node scripts/check-slides.mjs .qa-dist` — must exit 0 (no offenders). Any slide the scan flags is fixed (shorten/split content, denser `pad-*`, smaller local font-size) before the task is done. Pre-existing offenders unrelated to this work are logged for the owner, not silently ignored. NOTE (attribution done 2026-07-01): the deck has 16 pre-existing overflow slides (8, 76, 91, 166, 187, 188, 199, 202, 219, 222, 226, 254, 272, 370, 390, 451) — identical before and after the font change, so the restyle introduced none.
- **Videos full-screen (STRICT).** Video slides MUST fill the frame edge-to-edge with no letterbox line. `VideoPlayer.vue` uses `object-fit: cover` (not `contain`) over a black full-bleed container. Verify a video slide's `<video>` box equals the slide box.
- **Consistent type scale (STRICT).** Text/element sizes follow the markdown level via one documented type scale — no arbitrary inline `font-size` or one-off size classes on new/edited slides. Authoring `##` always yields the same size. Deck-wide cleanup of pre-existing random sizes is rollout work; the rule binds all new/edited slides and the theme now.
- **No new build tooling / dependencies.** Fonts load via a CSS `@import` from Google Fonts (same provider PT Serif already uses through Slidev). No package installs. (`playwright-chromium` and the overflow-check script are already present.)
- **`bs2026` deploy branch untouched.** Work stays on the `visual-style-work` worktree branch (based on `ff2026`). GitHub Pages deploys from `bs2026`; no risk this cycle.
- **Commit trailer.** End every commit message body with:
  `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`
  `Claude-Session: https://claude.ai/code/session_0129JsBnWt8vxR4US4HbTuXs`

**Working directory:** all paths below are relative to the worktree root
`/home/mindaugas_wsl/CERN_lessons_on_data_analysis/.claude/worktrees/visual-style-work`.

---

## File Structure

| File | Responsibility | Task |
|---|---|---|
| `lectures/content/theme/styles/fonts.css` | **Create** — `@import` Space Grotesk display font | 1 |
| `lectures/content/theme/styles/custom-slides.css` | **Modify** `:root` — add accent/gradient/glow/`--font-display` tokens | 1 |
| `lectures/content/theme/styles/layouts.css` | **Modify** — apply `--font-display` to headings | 1 |
| `lectures/content/theme/styles/index.ts` | **Modify** — import `fonts.css` (first) and `animations.css` | 1, 2 |
| `lectures/content/theme/styles/animations.css` | **Create** — shared motion & effects library | 2 |
| `lectures/content/theme/layouts/section.vue` | **Modify** — kinetic section divider | 3 |
| `lectures/content/theme/layouts/fact.vue` | **Modify** — gradient/glow big fact | 4 |
| `lectures/content/theme/layouts/statement.vue` | **Modify** — gradient/glow big statement | 4 |
| `lectures/content/slides/L01_Course_Orientation.md` | **Modify** — pilot re-author to new system | 5 |

**Design decision (resolves spec §9 open question):** the "metric / big number" is delivered as **utility classes** (`.stat`, `.stat-num`, `.stat-grid`) in `animations.css`, **not** a new `metric.vue` layout — simpler, YAGNI, and enough for L01's needs.

**No automated tests exist in this repo** (project convention). "Verify" steps below run the Slidev dev server and check specific visual outcomes. Each task ends with a commit.

---

### Task 1: Palette, display font & typography tokens

**Files:**
- Create: `lectures/content/theme/styles/fonts.css`
- Modify: `lectures/content/theme/styles/custom-slides.css` (`:root`, ends line ~97)
- Modify: `lectures/content/theme/styles/layouts.css` (append)
- Modify: `lectures/content/theme/styles/index.ts`

**Interfaces:**
- Produces (consumed by all later tasks): CSS custom properties
  `--font-display`, `--accent-cyan`, `--accent-cyan-soft`, `--accent-violet`,
  `--accent-violet-soft`, `--accent-amber`, `--grad-kinetic`, `--grad-energy`,
  `--glow-cyan`, `--glow-violet`.

- [ ] **Step 1: Define the acceptance check**

After this task: every heading (`h1`/`h2`/`h3`, including card titles) renders in **Space Grotesk**; the new CSS variables resolve to real values in DevTools. Body prose stays PT Serif. No layout regressions.

- [ ] **Step 2: Create `fonts.css`**

Create `lectures/content/theme/styles/fonts.css` with exactly:

```css
/* Display font for headings (2026-07 visual upgrade).
   Loaded from Google Fonts — the same provider Slidev already uses for
   PT Serif, so this adds no new offline dependency. @import MUST stay at
   the very top of this file (CSS requires @import before other rules). */
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap');
```

- [ ] **Step 3: Add tokens to `:root` in `custom-slides.css`**

In `lectures/content/theme/styles/custom-slides.css`, find the end of the `:root` block (the `--shadow-lg:` line, ~line 96) and insert BEFORE the closing `}`:

```css

  /* === Kinetic accent layer (2026-07 visual upgrade) === */
  --font-display: 'Space Grotesk', 'PT Serif', ui-sans-serif, system-ui, sans-serif;
  --accent-cyan: #22d3ee;
  --accent-cyan-soft: #5ec4c4;
  --accent-violet: #8b5cf6;
  --accent-violet-soft: #a78bfa;
  --accent-amber: #fbbf24;
  --grad-kinetic: linear-gradient(100deg, var(--accent-cyan), var(--accent-violet));
  --grad-energy: linear-gradient(100deg, var(--accent-amber), var(--accent-cyan));
  --glow-cyan: 0 0 22px rgba(34, 211, 238, 0.45), 0 0 60px rgba(34, 211, 238, 0.18);
  --glow-violet: 0 0 22px rgba(139, 92, 246, 0.45), 0 0 60px rgba(139, 92, 246, 0.18);
```

- [ ] **Step 4: Apply the display font in `layouts.css`**

Append to the end of `lectures/content/theme/styles/layouts.css`:

```css

/* Modern display font for headings (2026-07 visual upgrade).
   Body prose keeps PT Serif (theme fonts default) for readability. */
.slidev-layout h1,
.slidev-layout h2,
.slidev-layout h3,
.card h2 {
  font-family: var(--font-display);
  letter-spacing: -0.015em;
}
```

- [ ] **Step 5: Import `fonts.css` first in `index.ts`**

Edit `lectures/content/theme/styles/index.ts` so `fonts.css` is imported before the layout styles. Full new contents:

```ts
import '@slidev/client/styles/layouts-base.css'
import './fonts.css'
import './layouts.css'
import './custom-slides.css'
import './mermaid-styles.css'
```

- [ ] **Step 6: Verify in the dev server**

Run: `pnpm dev:lecture lectures/content/slides/L01_Course_Orientation.md`
Open the printed localhost URL. Expected:
- The cover title and all card headings render in Space Grotesk (geometric sans), not PT Serif.
- Body paragraphs inside cards remain PT Serif.
- In DevTools console: `getComputedStyle(document.documentElement).getPropertyValue('--accent-cyan').trim()` → `#22d3ee`.
- No console errors; slides 1–3 look intact (no overflow/wrapping breakage).

Stop the server (Ctrl-C).

- [ ] **Step 7: Commit**

```bash
git add lectures/content/theme/styles/fonts.css \
        lectures/content/theme/styles/custom-slides.css \
        lectures/content/theme/styles/layouts.css \
        lectures/content/theme/styles/index.ts
git commit -m "$(cat <<'EOF'
feat(theme): add kinetic palette tokens + Space Grotesk display font

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_0129JsBnWt8vxR4US4HbTuXs
EOF
)"
```

---

### Task 2: Shared animations & effects library

**Files:**
- Create: `lectures/content/theme/styles/animations.css`
- Modify: `lectures/content/theme/styles/index.ts`

**Interfaces:**
- Consumes (from Task 1): `--font-display`, `--accent-*`, `--grad-*`, `--glow-*`.
- Produces (opt-in classes used by Tasks 3–5): `.gradient-text` (+`.energy`),
  `.kinetic`, `.glow`, `.glow-violet`, `.aurora`, `.reveal-left`, `.reveal-up`,
  `.reveal-scale`, `.reveal-blur`, `.stat`, `.stat-num`, `.stat-unit`,
  `.stat-label`, `.stat-grid`, plus the generalized `.anim-card` / `.anim-sub` /
  `.anim-ex` and `.flow-container` / `.flow-row` / `.flow-arrow` / `.flow-label` /
  `.flow-text` (same behaviour as the current inline copies in the video deck & L06).

- [ ] **Step 1: Define the acceptance check**

After this task: a test element with `class="gradient-text"` shows cyan→violet gradient text; an element with `class="reveal-up"` + `v-click` slides up + fades in on click; `.aurora` paints a soft moving glow; all effects freeze to static end-states under reduced-motion.

- [ ] **Step 2: Create `animations.css`**

Create `lectures/content/theme/styles/animations.css` with exactly:

```css
/* ============================================================
   ANIMATIONS & KINETIC EFFECTS  (2026-07 visual upgrade)
   Opt-in classes. Every animation degrades to a static end-state
   under prefers-reduced-motion and disables heavy effects on
   coarse-pointer / small screens. v-click states rely on Slidev's
   `.slidev-vclick-hidden`. Generalizes patterns previously inlined
   in crash_course_for_video_lecture.md and L06.
   ============================================================ */

/* ---------- Gradient / kinetic text ---------- */
.gradient-text {
  background: var(--grad-kinetic);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
}
.gradient-text.energy {
  background: var(--grad-energy);
  -webkit-background-clip: text;
  background-clip: text;
}

.kinetic {
  background: linear-gradient(100deg, var(--accent-cyan), var(--accent-violet), var(--accent-cyan));
  background-size: 200% auto;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  animation: kinetic-pan 6s linear infinite;
}
@keyframes kinetic-pan { to { background-position: 200% center; } }

/* ---------- Glow ---------- */
.glow { box-shadow: var(--glow-cyan) !important; }
.glow-violet { box-shadow: var(--glow-violet) !important; }

/* ---------- Aurora backdrop ----------
   Add <div class="aurora"></div> as the first child of a
   position:relative, overflow:hidden, full-height container. */
.aurora {
  position: absolute;
  inset: -20%;
  z-index: 0;
  pointer-events: none;
  background:
    radial-gradient(40% 50% at 20% 30%, rgba(34, 211, 238, 0.18), transparent 60%),
    radial-gradient(40% 50% at 80% 60%, rgba(139, 92, 246, 0.16), transparent 60%),
    radial-gradient(35% 45% at 55% 85%, rgba(251, 191, 36, 0.10), transparent 60%);
  filter: blur(40px);
  animation: aurora-drift 24s ease-in-out infinite alternate;
  will-change: transform;
}
@keyframes aurora-drift {
  0%   { transform: translate(0, 0) scale(1); }
  50%  { transform: translate(2%, -1.5%) scale(1.08); }
  100% { transform: translate(-1.5%, 1%) scale(1.04); }
}

/* ---------- Reveal helpers (pair with v-click) ---------- */
.reveal-left, .reveal-up, .reveal-scale, .reveal-blur {
  transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1),
              opacity 0.5s ease, filter 0.5s ease;
}
.reveal-left.slidev-vclick-hidden  { transform: translateX(-40px); opacity: 0 !important; visibility: visible !important; }
.reveal-up.slidev-vclick-hidden    { transform: translateY(28px);  opacity: 0 !important; visibility: visible !important; }
.reveal-scale.slidev-vclick-hidden { transform: scale(0.9);        opacity: 0 !important; visibility: visible !important; }
.reveal-blur.slidev-vclick-hidden  { filter: blur(10px);           opacity: 0 !important; visibility: visible !important; }

/* ---------- Big stat / metric (utility, not a layout) ---------- */
.stat { text-align: center; line-height: 1; }
.stat-num  { font-family: var(--font-display); font-weight: 700; font-size: 5.5rem; letter-spacing: -0.02em; }
.stat-unit { font-family: var(--font-display); font-weight: 600; font-size: 2rem; opacity: 0.8; margin-left: 0.15em; }
.stat-label { margin-top: 0.6rem; font-size: 1rem; opacity: 0.7; letter-spacing: 0.02em; }
.stat-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; align-items: end; }

/* ---------- Generalized card animation (was inline: video deck / L06) ---------- */
.anim-card {
  transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1),
              opacity 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}
.anim-card.slidev-vclick-hidden {
  transform: translateX(-40px); opacity: 0 !important;
  visibility: visible !important; pointer-events: none;
}
.anim-card h2 {
  font-size: 1.3em; line-height: 1.2; margin: 0;
  transition: font-size 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
.anim-card:has(.anim-ex:not(.slidev-vclick-hidden)) h2 { font-size: 1em; }
.anim-sub {
  display: block; font-size: 0.75em; opacity: 0.6; font-style: italic;
  margin-top: 0.1em; transition: font-size 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
.anim-card:has(.anim-ex:not(.slidev-vclick-hidden)) .anim-sub { font-size: 0.7em; }
.anim-ex {
  max-height: 200px; opacity: 0.7; overflow: hidden; font-size: 0.7em; margin-top: 0.2rem;
  transition: max-height 0.4s cubic-bezier(0.4, 0, 0.2, 1),
              opacity 0.3s ease, margin-top 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
.anim-ex.slidev-vclick-hidden {
  max-height: 0 !important; opacity: 0 !important; visibility: visible !important;
  margin-top: 0 !important; pointer-events: none;
}
.anim-ex ul { margin: 0; padding-left: 1.4em; }
.anim-ex li { margin: 0.15em 0; }

/* ---------- Flow pyramid (was inline: video deck) ---------- */
.flow-container { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; gap: 0; }
.flow-row { display: flex !important; align-items: center; gap: 1rem; width: 90%; padding: 1rem 1.5rem !important; }
.flow-row.slidev-vclick-hidden { transform: translateX(-30px); opacity: 0 !important; visibility: visible !important; }
.flow-label { font-weight: 700; font-size: 1.15em; white-space: nowrap; min-width: 9rem; }
.flow-text { font-size: 1.05em; opacity: 0.9; }
.flow-arrow { font-size: 1.4em; opacity: 0.4; margin: 0.3rem 0; transition: opacity 0.5s ease; }
.flow-arrow.slidev-vclick-hidden { opacity: 0 !important; visibility: visible !important; }

/* ---------- Motion & mobile guards ---------- */
@media (max-width: 768px), (pointer: coarse) {
  .aurora { animation: none; }
  .kinetic { animation: none; }
}
@media (prefers-reduced-motion: reduce) {
  .aurora { animation: none; }
  .kinetic { animation: none; background-position: 0 center; }
  .reveal-left, .reveal-up, .reveal-scale, .reveal-blur { transition: opacity 0.3s ease; }
  .reveal-left.slidev-vclick-hidden, .reveal-up.slidev-vclick-hidden,
  .reveal-scale.slidev-vclick-hidden, .reveal-blur.slidev-vclick-hidden { transform: none; filter: none; }
  .anim-card, .anim-ex, .flow-row { transition: opacity 0.3s ease; }
  .anim-card.slidev-vclick-hidden, .flow-row.slidev-vclick-hidden { transform: none; }
}
```

- [ ] **Step 3: Import `animations.css` in `index.ts`**

Edit `lectures/content/theme/styles/index.ts` — append the import last so it can override earlier rules. Full new contents:

```ts
import '@slidev/client/styles/layouts-base.css'
import './fonts.css'
import './layouts.css'
import './custom-slides.css'
import './mermaid-styles.css'
import './animations.css'
```

- [ ] **Step 4: Verify with a scratch slide**

Run: `pnpm dev:lecture lectures/content/slides/L01_Course_Orientation.md`
In DevTools console, inject a quick probe on any slide:
```js
document.querySelector('.slidev-page').insertAdjacentHTML('beforeend',
  '<div style="position:fixed;top:10px;left:10px;z-index:9999" class="gradient-text">GRADIENT TEST</div>')
```
Expected: "GRADIENT TEST" shows a cyan→violet gradient fill. Remove it by reloading.
Then emulate reduced motion (DevTools → Rendering → "Emulate prefers-reduced-motion: reduce") and confirm no console errors. Stop the server.

- [ ] **Step 5: Commit**

```bash
git add lectures/content/theme/styles/animations.css \
        lectures/content/theme/styles/index.ts
git commit -m "$(cat <<'EOF'
feat(theme): add shared animations & kinetic effects library

Generalizes anim-card/flow patterns previously inlined in the video
deck and L06; adds reveal-*, gradient-text, kinetic, glow, aurora, and
stat utilities. Reduced-motion and mobile guards included.

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_0129JsBnWt8vxR4US4HbTuXs
EOF
)"
```

---

### Task 3: Kinetic section divider (`section.vue`)

**Files:**
- Modify: `lectures/content/theme/layouts/section.vue`

**Interfaces:**
- Consumes (Tasks 1–2): `--font-display`, `--accent-cyan`, `--accent-violet`,
  `--accent-cyan-soft`, `.aurora`.
- Produces: an upgraded `layout: section` — same markup contract
  (`# Section **Keyword**`), new look. Applies deck-wide.

- [ ] **Step 1: Define the acceptance check**

Any `layout: section` slide (e.g. L01's "Data in **Your Life**") shows: a giant gradient-tinted heading in Space Grotesk, a centered accent line that sweeps out on entry, a slow aurora glow behind, and the heading fading up on entry. Under reduced-motion the accent line and heading are shown in final state with no animation.

- [ ] **Step 2: Replace `section.vue`**

Overwrite `lectures/content/theme/layouts/section.vue` with:

```vue
<script setup lang="ts">
import { ref, onMounted } from 'vue'

const mounted = ref(false)
onMounted(() => { setTimeout(() => { mounted.value = true }, 50) })
</script>

<template>
  <div class="slidev-layout section section-kinetic">
    <!-- animated colour-shifting backdrop (class from animations.css) -->
    <div class="aurora"></div>

    <div class="section-inner my-auto text-center">
      <div class="section-body" :class="{ 'is-mounted': mounted }">
        <slot />
      </div>
      <div class="section-accent" :class="{ 'is-mounted': mounted }"></div>
    </div>
  </div>
</template>

<style scoped>
.section-kinetic {
  position: relative;
  overflow: hidden;
}
.section-inner {
  position: relative;
  z-index: 2;
}
.section-body {
  opacity: 0;
  transform: translateY(18px);
  transition: opacity 0.7s ease-out 0.1s,
              transform 0.7s cubic-bezier(0.16, 1, 0.3, 1) 0.1s;
}
.section-body.is-mounted {
  opacity: 1;
  transform: none;
}
.section-accent {
  margin: 1.2rem auto 0;
  width: 0;
  height: 3px;
  background: linear-gradient(90deg, transparent, var(--accent-cyan), var(--accent-violet), transparent);
  transition: width 0.9s cubic-bezier(0.16, 1, 0.3, 1) 0.3s;
}
.section-accent.is-mounted {
  width: min(48%, 520px);
}

/* Gradient-tinted heading */
.section-kinetic :deep(h1) {
  font-family: var(--font-display);
  font-weight: 600;
  background: linear-gradient(100deg, #f2f2f2 20%, var(--accent-cyan-soft));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
}
/* keep **bold** words legible within the gradient heading */
.section-kinetic :deep(h1 strong) {
  -webkit-text-fill-color: transparent;
  font-weight: 800;
}

@media (prefers-reduced-motion: reduce) {
  .section-body { transition: none; opacity: 1; transform: none; }
  .section-accent { transition: none; width: min(48%, 520px); }
}
</style>
```

- [ ] **Step 3: Verify on L01's section slide**

Run: `pnpm dev:lecture lectures/content/slides/L01_Course_Orientation.md`
Navigate to the "Data in **Your Life**" slide (~slide 13). Expected:
- Heading is large, gradient-tinted, Space Grotesk; "Your Life" (bold) is heavier weight.
- On slide entry, heading fades up and the accent line sweeps to ~half width.
- A faint aurora glow drifts behind. Toggle reduced-motion → static, no animation.

- [ ] **Step 4: Smoke-test other decks (deck-wide change)**

Run: `pnpm dev:staging`
Page through to any `layout: section` slide in the imported deck(s). Confirm section slides render without overflow or broken layout (this change is global). Stop the server.

- [ ] **Step 5: Commit**

```bash
git add lectures/content/theme/layouts/section.vue
git commit -m "$(cat <<'EOF'
feat(theme): kinetic section divider (gradient heading + aurora + sweep)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_0129JsBnWt8vxR4US4HbTuXs
EOF
)"
```

---

### Task 4: Gradient/glow `fact.vue` & `statement.vue`

**Files:**
- Modify: `lectures/content/theme/layouts/fact.vue`
- Modify: `lectures/content/theme/layouts/statement.vue`

**Interfaces:**
- Consumes (Tasks 1–2): `--font-display`, `--accent-cyan`, `--accent-violet`, `--accent-amber`.
- Produces: upgraded `layout: fact` and `layout: statement` — same markup, gradient + glow big text.

- [ ] **Step 1: Define the acceptance check**

L01's `layout: fact` slides ("Breaks...", "Who am I talking to?") render their big heading with a cyan→violet gradient fill and a soft glow. `statement` slides get an energy (amber→cyan) gradient. Sizing/centering unchanged from `layouts.css`.

- [ ] **Step 2: Replace `fact.vue`**

Overwrite `lectures/content/theme/layouts/fact.vue` with:

```vue
<template>
  <div class="slidev-layout fact fact-kinetic">
    <div class="my-auto">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.fact-kinetic :deep(h1) {
  font-family: var(--font-display);
  background: linear-gradient(100deg, var(--accent-cyan), var(--accent-violet));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  filter: drop-shadow(0 0 30px rgba(34, 211, 238, 0.25));
}
.fact-kinetic :deep(h1 strong) { -webkit-text-fill-color: transparent; }
</style>
```

- [ ] **Step 3: Replace `statement.vue`**

Overwrite `lectures/content/theme/layouts/statement.vue` with:

```vue
<template>
  <div class="slidev-layout statement statement-kinetic">
    <div class="my-auto">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.statement-kinetic :deep(h1) {
  font-family: var(--font-display);
  background: linear-gradient(100deg, var(--accent-amber), var(--accent-cyan));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  filter: drop-shadow(0 0 26px rgba(251, 191, 36, 0.20));
}
.statement-kinetic :deep(h1 strong) { -webkit-text-fill-color: transparent; }
</style>
```

- [ ] **Step 4: Verify**

Run: `pnpm dev:lecture lectures/content/slides/L01_Course_Orientation.md`
Navigate to the two `fact` slides at the end ("Breaks...", "Who am I talking to?"). Expected: big gradient heading with a soft glow, Space Grotesk. Stop the server.

- [ ] **Step 5: Commit**

```bash
git add lectures/content/theme/layouts/fact.vue \
        lectures/content/theme/layouts/statement.vue
git commit -m "$(cat <<'EOF'
feat(theme): gradient + glow fact and statement layouts

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_0129JsBnWt8vxR4US4HbTuXs
EOF
)"
```

---

### Task 5: Apply the new system to the L01 pilot

**Files:**
- Modify: `lectures/content/slides/L01_Course_Orientation.md`

**Interfaces:**
- Consumes (Tasks 1–4): all new classes/layouts.
- Produces: the reference pilot deck for owner sign-off.

**Reminder (Global Constraints):** wording, numbers, and slide order stay identical. Only add visual classes/`v-click` and the one stat-block reformat (same numbers).

- [ ] **Step 1: Define the acceptance check**

L01 clicks through cleanly with: staged card reveals on the multi-card slides, a big-number stat treatment for the contact/self-study hours (same figures), at least one gradient keyword in a heading, selective `glow` on a hero card, and the auto-upgraded section/fact slides from Tasks 3–4. No content changed; no overflow.

- [ ] **Step 2: Gradient keyword on the "Main Goals" heading**

In `L01_Course_Orientation.md`, change the heading (currently `# **Main Goals**`, ~line 71) to:

```md
# <span class="gradient-text">Main Goals</span>
```

- [ ] **Step 3: Stagger the "Main Goals" cards with reveal + glow**

Replace the five goal cards block (the `<div class="stack-tight mt-sm">` … `</div>` at ~lines 73–105) with the same cards, each gaining `reveal-left` + a staged `v-click`, and a `glow` on the final "own projects" card:

```md
<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact reveal-left" v-click>

🧠 Build intuition for **good practices**

</div>

<div class="card card-secondary card-glass pad-compact reveal-left" v-click>

🧰 Be aware of a **plethora of available free tools**

</div>

<div class="card card-accent card-glass pad-compact reveal-left" v-click>

💪 Build **competences** in relevant areas

</div>

<div class="card card-success card-glass pad-compact reveal-left glow" v-click>

🚀 Use what you learned for your **own projects**

</div>

<div class="card card-info card-glass pad-compact reveal-left" v-click>

🤝 Work together and practice **problem solving**

</div>

</div>
```

- [ ] **Step 4: Convert the contact-hours info card into a stat block**

Replace the Course-Structure hours card (currently
`<div class="card card-info card-glass pad-compact mt-md" style="text-align: center;">` … `⏱️ **48 hours** contact … **212 hours** self study` … `</div>`, ~lines 61–65) with a big-number stat grid — **same numbers**:

```md
<div class="card card-info card-glass pad-tight mt-md">

<div class="stat-grid">
  <div class="stat">
    <span class="stat-num gradient-text">48</span><span class="stat-unit">h</span>
    <div class="stat-label">Contact hours</div>
  </div>
  <div class="stat">
    <span class="stat-num gradient-text energy">212</span><span class="stat-unit">h</span>
    <div class="stat-label">Self study</div>
  </div>
  <div class="stat">
    <span class="stat-num gradient-text">1</span>
    <div class="stat-label">Semester project</div>
  </div>
</div>

</div>
```

- [ ] **Step 5: Stagger the "Course Content" grid**

In the "Course Content" slide (~lines 111–175), add `reveal-scale` + `v-click` to each of the ten topic cards so they pop in on click. For every `<div class="card card-… card-glass pad-compact">` in that grid, add ` reveal-scale" v-click` — i.e. change each opening tag to end with `pad-compact reveal-scale" v-click>`. (Ten cards; the trailing summary `card-success` card stays un-clicked so the full arc is visible at the end.)

Example — the first topic card becomes:

```md
<div class="card card-primary card-glass pad-compact reveal-scale" v-click>

🖥️ Working with computers — command line & common pitfalls

</div>
```

- [ ] **Step 6: Stagger the Learning-Outcomes cards**

On both "Learning Outcomes (1/2)" and "(2/2)" slides (~lines 302–364), add `reveal-up` + `v-click` to each `card … card-glass pad-compact` — change each opening tag to end with `pad-compact reveal-up" v-click>`, mirroring Step 3's pattern.

- [ ] **Step 7: Verify the full pilot click-through**

Run: `pnpm dev:lecture lectures/content/slides/L01_Course_Orientation.md`
Click through ALL slides start to finish. Expected:
- Cover + quote intact; "Main Goals" heading is gradient; its cards fly in from the left one per click; the "own projects" card glows.
- Course Structure shows the three big gradient numbers **48 / 212 / 1** with labels (same figures).
- Course Content cards pop in (scale) per click; Learning Outcomes cards rise in per click.
- "Data in Your Life" is the kinetic section divider (Task 3); "Breaks..." / "Who am I talking to?" are gradient facts (Task 4).
- No text overflow, no clipped cards, no console errors.
- Toggle DevTools reduced-motion: everything still reaches its final state and is readable.

- [ ] **Step 7b: Run the strict no-overflow gate**

Build the published entry point and scan every slide for overflow (this is a blocking Global Constraint):
```bash
pnpm qa:build
node scripts/check-slides.mjs .qa-dist --shots .qa-shots   # or: pnpm qa
```
Expected: the L01 slides (in the published deck, L01 is roughly slides 1–18) show no overflow. Known pre-existing offender in L01: **slide 8 "Grading Structure"** (the "Project — 60%" card's last bullet clips off the bottom) — fix it here (shorten/split content or denser `pad-*` — NOT by changing wording/figures) and re-scan until L01 is clean. Flagged slides in *other* lectures (pre-existing, not caused by this pilot) are recorded in the ledger for the owner, not fixed here. Review the `.qa-shots/slide-0NN.png` for L01 to confirm content and styling look right.

- [ ] **Step 8: Capture before/after screenshots for review**

With the dev server running, screenshot (a) the cover, (b) the "Data in Your Life" section divider, (c) the stat-block slide. Save under `docs/superpowers/plans/assets/` (create the dir) as `L01-after-cover.png`, `L01-after-section.png`, `L01-after-stats.png`. These accompany the owner review message. Stop the server.

- [ ] **Step 9: Commit**

```bash
mkdir -p docs/superpowers/plans/assets
git add lectures/content/slides/L01_Course_Orientation.md docs/superpowers/plans/assets
git commit -m "$(cat <<'EOF'
feat(L01): apply kinetic visual system to Course Orientation pilot

Staged reveals, gradient headings, big-number stat block, glow accents,
kinetic section/fact layouts. Content (wording, figures, order) unchanged.

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_0129JsBnWt8vxR4US4HbTuXs
EOF
)"
```

---

## Self-Review

**Spec coverage** (spec §4 deliverables → task):
- §4.1 `animations.css` (anim/flow generalized + reveal/gradient/kinetic/glow/aurora/stat) → Task 2 ✓
- §4.2 palette + type tokens → Task 1 ✓
- §4.3 `section.vue` upgrade → Task 3 ✓
- §4.4 `fact`/`statement` enhance → Task 4 ✓
- §4.5 metric → resolved as `.stat` utilities in Task 2 (documented decision) ✓
- §4.6 font wiring → Task 1 (fonts.css + layouts.css + index.ts) ✓
- §5 L01 pilot → Task 5 ✓
- §6 verification (dev server, staging smoke, reduced-motion, mobile, screenshots) → Tasks 1–5 verify steps + Task 5 Step 8 ✓
- Global constraints (no content edits, backward compat, motion/mobile guards, bs2026 untouched) → Global Constraints block + per-task reminders ✓

**Placeholder scan:** no TBD/TODO/"handle edge cases"; every code step shows full code. ✓

**Type/name consistency:** class names produced in Task 2 (`.reveal-left/up/scale/blur`, `.gradient-text`/`.energy`, `.kinetic`, `.glow`/`.glow-violet`, `.aurora`, `.stat`/`.stat-num`/`.stat-unit`/`.stat-label`/`.stat-grid`, `.anim-*`, `.flow-*`) are exactly the ones consumed in Tasks 3–5. Tokens produced in Task 1 (`--font-display`, `--accent-*`, `--grad-*`, `--glow-*`) match all later `var(--…)` references. ✓

**Note on `metric.vue`:** intentionally NOT created — replaced by `.stat*` utilities (spec §9 open question resolved toward the simpler option).
