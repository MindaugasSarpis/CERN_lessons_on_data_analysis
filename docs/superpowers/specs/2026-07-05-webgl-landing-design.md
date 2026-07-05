# WebGL Landing Page ("Active Theory" style) — Design Spec

**Status:** Approved (author, 2026-07-05) · **Date:** 2026-07-05 · **Branch:** `ff2026`
**Owner:** Mindaugas Šarpis · **Related:** `2026-07-01-ff2026-multi-deck-landing-design.md` (the landing this replaces visually)

> Redesign the course landing page (`dist/index.html`, emitted by
> `scripts/gen-landing.mjs`) into an immersive, activetheory.net-style
> experience: a full-screen GPU particle field behind oversized typography,
> with the 16 lectures presented as a scrolling typographic list. The page
> stays manifest-driven from `decks.json`, fully usable without JS, and
> deployable to GitHub Pages with no external requests.

---

## 1. Goal & scope

**Goal.** Replace the current utilitarian card-grid landing with a
"full WebGL experience" landing modeled on activetheory.net: dark, immersive,
mouse-reactive particle background, huge minimal typography, staggered
reveals, and refined hover states — while preserving every piece of current
content and the manifest-driven build.

**In scope**
- New visual design + WebGL particle scene for `index.html`.
- New `landing/` source directory (JS, GLSL, CSS, fonts) built by Vite.
- Changes to `scripts/gen-landing.mjs` (new HTML structure, asset links) and
  `scripts/build-all.mjs` (build/copy landing assets).
- Palette retouch of the generated `404.html` (logic untouched).
- New smoke test `scripts/check-landing.mjs`, wired into `pnpm qa`.

**Out of scope**
- Any change to the Slidev decks, theme, workbook, or deploy workflow.
- The `404.html` redirect script (kept byte-for-byte in behavior).
- Per-deck pages' look; only the landing (and 404 colors) change.

**Decisions locked during brainstorming**
1. **Fidelity:** full WebGL experience (not a lightweight homage, not CSS-only).
2. **Scene:** abstract particle field with cursor wake — faithful to
   activetheory.net, no explicit physics metaphor.
3. **Layout:** fixed full-page canvas; hero + scrolling typographic list of
   lectures (no hidden menu; all 16 lectures one scroll away).
4. **Stack:** Three.js + Vite prebuilt bundle, progressively enhancing
   HTML that `gen-landing.mjs` still generates from `decks.json`.

---

## 2. Visual & interaction design

### 2.1 Palette & texture
- Base near-black `#050507`; type white/off-white (`#f2f5f9` / dimmed
  `#8b97a6`); single accent = course cyan `#7dd3fc` (particle tint ramp,
  hover states, block markers). No other hues.
- Subtle film-grain overlay (tiny tiling data-URI or CSS `repeating`
  gradient at ~3–4% opacity) over the whole page for the Active Theory
  texture.

### 2.2 Typography
- Self-hosted **Space Grotesk** (OFL) subset WOFF2, two weights
  (~35 KB each), declared with `font-display: swap`; system grotesque
  fallback stack. No external font requests (CSP/GitHub-Pages safe).
- Hero title: uppercase, `clamp(3rem, 8vw, 7rem)`, tight leading/tracking.
- Metadata (presenter, block headers, tags, footer): small uppercase,
  letter-spaced (`.08–.14em`), ~0.7–0.8rem.
- Lecture rows: title `clamp(1.4rem, 2.6vw, 2.2rem)`; number in dimmed
  tabular figures.

### 2.3 Page structure (top → bottom)
1. **Hero** (100 vh): presenter line (small caps) → course title (huge) →
   one-line course description (small caps, dimmed) → animated scroll hint
   (thin vertical line + "SCROLL"). Title reveals with a staggered
   per-line fade/translate on load.
2. **Blocks A–E**: each a section with a small-caps header
   (`BLOCK A — FOUNDATIONS & TOOLING`, Block E keeps the
   "drop if short on time" tag) followed by lecture rows.
3. **Lecture row** (the link, full width): dimmed two-digit number,
   large title, `optional` tag where applicable, arrow glyph that slides
   in on hover. Hover also nudges particles behind the row (§2.4) and
   brightens the title. Rows stagger-reveal (fade + translate-up) as they
   enter the viewport (IntersectionObserver toggling a class; CSS does the
   animation).
4. **Upcoming** (only if `upcoming[]` non-empty): same row style, greyed,
   non-interactive, "in preparation" tag.
5. **Footer**: existing seminar note, small caps, hairline top border.

### 2.4 Particle scene
- Fixed, full-viewport `<canvas>` behind all content (`position: fixed;
  z-index: 0`; content wrapper `z-index: 1`; canvas `pointer-events: none`).
- GPU-simulated point field: positions/velocities in ping-pong float FBO
  textures updated by a simulation shader (curl-noise drift + damping),
  rendered as soft round additive-blended sprites, size/alpha variance,
  tint ramp cyan→white by speed.
- **Cursor wake** (signature interaction): pointer position + velocity
  uniform injects a directional force with falloff radius, so particles
  swirl and trail behind the cursor.
- **Hover impulse:** entering a lecture row emits a one-frame radial
  impulse at the row's canvas-space position.
- **Scroll parallax:** field's y-offset follows `scrollY * ~0.1`, so the
  scene drifts slower than content.
- Scene fades in (~1s opacity ramp) once the first frame renders.

---

## 3. Architecture

### 3.1 New source directory `landing/`
```
landing/
  src/main.js        # boot, adaptive tier pick, scroll/hover/reveal glue
  src/sim.js         # particle system: FBO ping-pong setup, materials
  src/shaders/*.glsl # simulation + render shaders (imported as strings)
  src/style.css      # full landing stylesheet (incl. @font-face, grain)
  fonts/*.woff2      # vendored Space Grotesk subsets
  vite.config.mjs    # build config (see §3.2)
```

### 3.2 Build
- Add `three` + `vite` as explicit devDependencies (Vite already present
  transitively via Slidev; declare it).
- `vite build` with fixed output filenames — `assets/landing.js`,
  `assets/landing.css`, `assets/fonts/*` — and **relative base** (`./`)
  so the page works under any `--base` prefix. No hashing: GitHub Pages'
  short cache TTL makes fixed names acceptable, and `gen-landing.mjs` can
  reference them statically.
- `scripts/build-all.mjs`: after deck builds, run the landing Vite build
  (skipped in `--flat-base` QA mode, which emits no landing today) and
  copy its output into `<out>/assets/` before calling `genLanding()`.
- `package.json`: add `build:landing` script for standalone iteration.

### 3.3 `gen-landing.mjs` changes
- Still exports `genLanding(manifest, outDir, prefix)`; still renders
  **all** content server-side from `decks.json` (hero, block sections,
  lecture rows, upcoming, footer) — adding/reordering decks never touches
  landing JS.
- Emits: `<link rel="stylesheet" href="./assets/landing.css">`, a small
  inline critical-CSS block (background color + font fallback so first
  paint isn't unstyled), `<canvas id="field">` mount, and
  `<script type="module" src="./assets/landing.js" defer>`.
- **Progressive enhancement contract:** with JS disabled the page is fully
  readable and navigable (static backdrop, no canvas, rows visible without
  reveal animation — reveal classes default to visible, JS opts them into
  hidden state before animating).
- `gen404()` keeps its script verbatim; colors updated to the new palette.

### 3.4 Content parity (must not regress)
- Every deck from `decks.json` in block order, linked to `<base>/<slug>/`.
- `optional` tags, Block E header tag, `upcoming[]` section, presenter,
  course title, seminar footer note.
- Works under any `--base` prefix; `deploy.yml` untouched.

---

## 4. Performance & fallbacks

- **Adaptive tiers** chosen at boot from screen area × capped DPR and
  `hardwareConcurrency`: ~150–200k particles (desktop), ~60k (mid),
  ~25k (phones). DPR capped at 2 (1.5 on phones).
- **FPS guard:** if sustained fps < ~40 over a rolling window, halve the
  particle count once (rebuild FBOs at smaller size).
- **Loop hygiene:** `requestAnimationFrame` paused on `document.hidden`.
- **Touch devices:** autonomous roaming attractor animates the field
  without a cursor; touch-drag injects force like pointer movement.
- **Reduced motion / no WebGL2:** `prefers-reduced-motion: reduce` or
  failed WebGL2 context → canvas never boots; static CSS radial-gradient
  backdrop; reveals render instantly. Same path covers JS errors (the
  page is already fully rendered HTML).
- **Load budget:** JS ≈ 150 KB gz (tree-shaken three + app), CSS ≈ 8 KB,
  fonts ≈ 2×35 KB. JS deferred → first paint is HTML+CSS; scene fades in
  when ready.

---

## 5. QA & testing

- **New `scripts/check-landing.mjs`** (reuses the headless-browser tooling
  already used by `check-slides.mjs`): serves/loads a built `dist/`,
  asserts (a) HTTP 200 + title, (b) all manifest deck links present with
  correct hrefs, (c) no console errors, (d) canvas obtains a WebGL2
  context (or cleanly falls back when forced via reduced-motion
  emulation), (e) rows become visible after reveal.
- Wire into `pnpm qa` alongside the per-deck overflow gate. Note
  `qa-all.mjs` builds decks `--flat-base` with **no landing**, so it gains
  a landing step: build the Vite assets + run `genLanding()` into
  `.qa-dist/__landing__/` and point `check-landing.mjs` at that directory.
- Manual pass: `pnpm build` + local serve — desktop Chrome/Firefox,
  Chrome mobile emulation (mid-tier throttle), reduced-motion, no-JS.

---

## 6. Risks & mitigations

| Risk | Mitigation |
|---|---|
| three.js bundle pushes mobile load up | deferred JS; content paints first; tree-shaken build; tiers keep GPU cost low |
| Float-texture FBOs unsupported on some mobile GPUs | require WebGL2 + `EXT_color_buffer_float`; else static fallback |
| Fixed asset names cached stale by Pages CDN | Pages TTL is ~10 min; acceptable for a course site |
| Vite/Slidev version conflicts | landing has its own `vite.config.mjs`; uses the workspace Vite version |
| QA flakiness in headless WebGL | swiftshader flag in the check; fallback assertion path if context denied |

---

## 7. Change log

- **2026-07-05** — Spec drafted and approved (fidelity, scene, layout,
  stack decisions locked via brainstorming Q&A).
