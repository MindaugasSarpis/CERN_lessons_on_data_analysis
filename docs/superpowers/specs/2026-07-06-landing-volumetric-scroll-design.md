# Landing: volumetric 3D scroll — grid-network core, 3D sim, orbital camera

**Date:** 2026-07-06
**Status:** Approved (design), pending implementation plan
**Builds on:** `2026-07-05-webgl-landing-design.md`, `2026-07-06-landing-fibers-design.md`

## Goal

Give the landing page a genuinely volumetric 3D moment: a revolving grid-network
**core** behind the hero that the fibers visually feed, with scroll driving a
camera that **revolves around** the core and pulls back until it recedes into
the distance behind the lecture list — one continuous 3D world instead of the
current 2.5D parallax.

Decisions made during brainstorming:

- **Intensity:** staged — bold in the hero, calm once the lecture list is in view.
- **Centerpiece:** grid-network core; fibers anchor to it and feed it pulses.
- **Scroll exit:** the core recedes into depth and stays alive (dim, still
  revolving) behind the list; the page keeps one continuous world.
- **Mobile:** full effect at reduced budget (fewer core nodes; existing lower
  particle count and FPS guard).
- **Approach:** full 3D re-architecture (option B) — 3D particle sim, true 3D
  fibers, free camera path — chosen over the cheaper camera-rig-only variant.

## Non-goals

- No DOM/CSS/content changes: the hero, rows, reveals, grain, exit fade, and
  the no-JS/static fallback markup are untouched.
- No camera roll (motion-sickness), no pointer-driven camera.
- No new degradation machinery beyond the existing FPS guard stages.

## 1. World & scene architecture

One continuous 3D scene. The **core center is a fixed world position**,
right-of-center and slightly above the hero's vertical middle (the hero title
is left-aligned; the right two-thirds of the viewport are open). Everything
else is defined relative to it.

### Particle sim → 3D

Current state: pos texture = `(x, y, zStatic, seed)`, vel = `(vx, vy, 0, 1)`;
only xy is simulated, z is static parallax depth.

- `VEL_FRAG`: velocity becomes `vxyz`. Ambient drift uses proper **3D curl
  noise** — three offset simplex samples forming a divergence-free 3D vector
  field (replacing the current 2D curl-of-scalar).
- Pointer wake stays 2D-projected: the cursor maps to the **z=0 plane**; wake
  and hover-impulse influence falls off with `|z|` so mouse interaction still
  feels direct. Same for the lissajous idle attractor on touch.
- `POS_FRAG`: integrate xyz; **toroidal wrap in a 3D box** (`uBounds` becomes
  vec3) sized to contain the full camera orbit with margin.
- Render shaders gain cheap **depth fog**: `alpha *= exp(-k · viewDist)` so
  far particles dim. This is the main volumetric depth cue.
- The 3D box is sparser than today's 2D slab at equal count; compensate with
  slightly larger point sizes and the fog concentrating attention near camera.

### The core: grid-network sphere

- ~**160 nodes desktop / ~80 mobile** (coarse pointer), placed by
  fibonacci-sphere distribution with radial noise so it reads organic, not
  geodesic. Radius ≈ 2.5 world units.
- **Edges:** k-nearest neighbors (k≈3), max-length capped, deduped — a few
  hundred `LineSegments`.
- **Nodes** render as glow point sprites (same visual language as the field
  particles, larger/brighter). **Edges** render with a shader: soft alpha near
  endpoints + **traveling light pulses** (per-edge phase from a hash), echoing
  the fiber pulse language.
- **Animation:** slow self-rotation on two axes with different periods;
  subtle radial "breathing" (noise phase); per-node twinkle by seed.
- **Interaction:** on lecture-row hover the existing fiber burst continues
  into the core — when the burst pulse reaches the fiber's core end, the
  nearest node flashes and relays a pulse across a few adjacent edges.

### Fibers → true 3D

- `curve(t)` returns **vec3**; undulation via 3D noise.
- Far end starts off-screen at the world edge; near end **anchors to a node
  on the core surface** — fibers visually feed the core. Pulses travel
  *toward* the core.
- Ribbon strips **billboard in view space** (offset perpendicular to the view
  direction) so they never appear edge-on while the camera orbits.
- **Three fibers**, approaching from different azimuths so orbiting reveals
  depth (today: two).

## 2. Scroll choreography & camera rig

Raw `scrollY` maps to progress `p` over the first **~1.5 viewport heights**,
smoothstep-eased. Each frame the camera **lerps toward** the path position for
`p` (exponential smoothing ≈ 0.1/frame at 60 fps, frame-rate independent).
Damping absorbs wheel steps and touch momentum — the camera never snaps.

Path in spherical coordinates around the core center:

| Phase | Camera |
| --- | --- |
| `p = 0` (hero) | radius ≈ 7; core framed right-of-center, ~⅓ frame height, self-revolving; fibers sweep past the camera into it |
| `p: 0 → 1` | azimuth sweeps **~140°** around the core; radius pulls out to ≈ 20; elevation arcs up ~+12°; look-at blends from core center toward a point below it, drifting the core into the upper third |
| `p = 1` onward (list) | calm state: core small and distant, still revolving with pulses arriving; further scroll adds only a slow azimuth creep + slight descent (same magnitude as today's parallax) |

- **Roll stays 0.** Orbit + dolly gives the volumetric feel; roll causes nausea.
- **Pointer keeps its current role** (particle wake, hover impulses); scroll is
  the only camera input.
- **Reduced motion / no WebGL2:** unchanged — static gradient, choreography
  never runs.

## 3. Performance & fallbacks

- Sim cost ~unchanged: same texture sizes (160²/256²/448² by device class),
  one more simulated channel in already-running passes.
- Core cost trivial: ≤160 sprites + ≤500 line segments. Fog is one `exp()`
  per fragment.
- **FPS guard unchanged** (pixel-ratio drop at stage 1, half particles at
  stage 2). Mobile starts at ~half core nodes.
- Fallback ladder unchanged: reduced motion or no WebGL2 → `static-bg`; boot
  throw → catch → `static-bg`. The DOM/CSS layer is untouched, so the no-JS
  path cannot regress.

## 4. Module layout

| File | Change |
| --- | --- |
| `landing/src/core.js` | **new** — grid-network build (nodes, k-NN edges), self-rotation, breathing, pulse relays; `update(elapsed)`, `flashAt(nodeIdx)`, node-budget option |
| `landing/src/rig.js` | **new** — camera path: `setScroll(y)`, `update(dt, camera)`; owns easing, damping, spherical path constants |
| `landing/src/shaders/passes.glsl.js` | 3D curl in `VEL_FRAG`; 3D integrate/wrap in `POS_FRAG`; depth fog in render shaders |
| `landing/src/sim.js` | 3D init positions; pointer-plane wake; rig + core hookup |
| `landing/src/fiber.js` | 3D curves; view-space billboarding; core-anchored endpoints; burst→core handoff |
| `landing/src/main.js` | unchanged (scroll/pointer already forwarded) |

## 5. QA / acceptance

- `pnpm build:landing` builds clean; `pnpm qa`'s landing smoke test
  (`scripts/check-landing.mjs`: links, WebGL boot/fallback gating, reveals,
  zero console errors) passes.
- **Extend `check-landing.mjs`:** screenshot the booted page at 2–3 scroll
  offsets (e.g. 0, 0.75·vh, 2·vh) and assert the canvas is not blank —
  catches shader compile/link regressions in CI cheaply.
- Manual visual pass: desktop at several scroll positions; coarse-pointer
  emulation; hero text readability with the core behind/near the title zone.
- Static fallback path verified untouched (reduced-motion emulation).

## Acceptance criteria

1. Scrolling the hero visibly **revolves the viewpoint around** the core and
   pulls back; the core settles small in the upper third behind the list and
   keeps living (rotation + pulses).
2. Particles read as a **volume** (near ones large/bright, far ones dim), not
   a plane.
3. Fibers stay ribbon-like from every orbit angle (no edge-on vanishing) and
   visibly terminate at the core.
4. Row hover still bursts a fiber pulse; the pulse now lands in the core and
   relays.
5. No regression in fallbacks, FPS-guard behavior, or the landing smoke test;
   zero console errors.
