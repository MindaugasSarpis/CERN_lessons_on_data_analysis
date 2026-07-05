# Landing Iteration: Copy Trim + Glowing Data Fibers — Design Spec

**Status:** Approved (author, 2026-07-06) · **Branch:** `ff2026`
**Parent:** `2026-07-05-webgl-landing-design.md` (iteration on the shipped WebGL landing)

## 1. Copy trim

`scripts/gen-landing.mjs` hero sub-line drops ", even on a phone":
"…Each lecture opens on its own so it loads fast." Nothing else changes.

## 2. Persistent glowing fibers

Two thin glowing "data-link fiber" ribbons live permanently in the WebGL
scene (user-requested persistent element; carries motion on touch devices
where there is no cursor wake). Approved option: **two ambient fibers** —
not a single hero fiber, no CSS fallback change.

- **Module:** new `landing/src/fiber.js` exporting
  `addFibers(scene) → { resize(halfW, halfH), update(elapsed, pointerWorld, camY) }`.
  Self-contained shaders (reuses `NOISE` from `shaders/noise.glsl.js`);
  no changes to the particle sim's own pipeline.
- **Geometry:** per fiber one ~240-segment triangle strip; vertex shader
  spans endpoints `uA→uB` (set off-screen left/right by `resize`),
  displaces the curve with slow simplex noise (`uTime * ~0.12`), and
  offsets vertices along the curve normal by `side * uWidth`.
- **Look:** narrow bright core + soft glow falloff (gaussian in the
  across-fiber coordinate), course cyan; a white light pulse (gaussian
  packet in the along-fiber coordinate) travels each fiber on a loop —
  the optical-fiber read. Ends fade out via smoothstep so no hard edges.
- **Placement:** fiber 1 high diagonal behind the hero, z≈−2, brighter;
  fiber 2 lower, deeper (z≈−5), dimmer, slower pulse, phase-offset.
- **Persistence:** both sit in a `Group` whose `y` tracks the camera at
  ~0.9× — gentle drift against the scroll, but on screen at every scroll
  depth.
- **Interaction:** fragment shader brightens near `uPointer` (the sim's
  existing pointer/attractor world position, passed via `update`).
- **Fallbacks:** reduced-motion / no-WebGL static page unchanged.
- **Cost:** ~1k vertices + 2 draw calls; no measurable budget impact.

## 3. Verification & ship

`pnpm build:landing` + all 3 `check-landing.mjs` passes green (no new
assertions needed); fresh desktop + 390×844 screenshots (hero + scrolled)
reviewed; then push `ff2026` and deploy `ff2026:bs2026` (user approved
deploy with the design).
