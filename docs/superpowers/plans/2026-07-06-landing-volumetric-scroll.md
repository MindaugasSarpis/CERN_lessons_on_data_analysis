# Landing Volumetric 3D Scroll Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the landing page one continuous 3D world: a revolving grid-network core behind the hero, fed by true-3D fibers, with scroll orbiting a damped camera ~140° around the core and dollying out until it recedes behind the lecture list.

**Architecture:** The existing GPGPU particle sim (`landing/src/sim.js` + `shaders/passes.glsl.js`) goes from 2D-plus-static-z to fully 3D (3D curl velocity, 3D toroidal wrap, depth fog). Two new modules: `core.js` (fibonacci-sphere node network with pulse relays) and `rig.js` (scroll-driven spherical camera path with exponential damping). `fiber.js` is rewritten for 3D curves with view-space billboarding, anchored to core nodes. `main.js` and all DOM/CSS are untouched. QA gains a pixel-sampling pass in `scripts/check-landing.mjs`.

**Tech Stack:** Three.js (already a dependency), Vite (es2019 target), Playwright-chromium with SwiftShader for QA.

**Spec:** `docs/superpowers/specs/2026-07-06-landing-volumetric-scroll-design.md`

## Global Constraints

- **No DOM/CSS/content changes** — only `landing/src/*` and `scripts/check-landing.mjs` change; the no-JS/static/reduced-motion fallbacks must be untouched.
- **No camera roll. Scroll is the only camera input.** Pointer keeps its current role (particle wake, hover impulses).
- **Color language stays:** dim cyan `vec3(0.35, 0.62, 0.78)` → white by energy, additive blending, `depthWrite: false`.
- **Budgets:** core = 160 nodes desktop / 80 coarse-pointer; k-NN edges k=3, max length 1.2·CORE_RADIUS. Sim texture sizes unchanged (160²/256²/448²). FPS guard keeps its two stages.
- **Deterministic core geometry:** seeded mulberry32 PRNG, seed `20260706`.
- **The test is the landing smoke test.** Every task ends with:
  `node scripts/build-landing.mjs --out .qa-dist/__landing__ && node scripts/check-landing.mjs .qa-dist/__landing__` exiting 0.
- Repo has no unit-test infra; visual verification is via the screenshot script added in Task 2 and reviewed between tasks.
- Commit after every task (no pushing; deploys happen from `bs2026` only).

## Numeric constants (single source of truth)

Values referenced by multiple tasks. `world.js` (Task 1) is the only place they live in code.

| Constant | Value | Meaning |
| --- | --- | --- |
| `CORE_CENTER` | `(3.2, 1.2, 0)` | world position of the core (right-of-center, above hero middle) |
| `CORE_RADIUS` | `2.5` | node-sphere radius |
| `BOUNDS` | `(24, 14, 24)` | particle wrap-box half-extents |
| Camera FOV / near / far | `55 / 0.1 / 120` | perspective camera |
| Rig radius | `10 → 20` | dolly-out over the choreography |
| Rig azimuth | `-18° → 122°` | ~140° revolve |
| Rig elevation | `2° → 14°` | rise to look slightly down |
| Choreography length | `1.5 · viewport height` | scroll span mapped to p∈[0,1], smoothstep-eased |
| Damping | `k = 1 − exp(−6·dt)` | camera chase factor (~0.1/frame @60fps) |

---

### Task 1: 3D particle sim (world constants, shaders, sim.js)

The sim textures already carry 4 channels; make velocity `vxyz` (3D curl noise), integrate+wrap xyz in a 3D box, add depth fog to the render pass, and replace the fixed-plane pointer mapping with unprojection onto the plane through `CORE_CENTER` perpendicular to the view direction. Camera stays static this task (rig comes in Task 4); fibers stay 2D (Task 3).

**Files:**
- Create: `landing/src/world.js`
- Modify: `landing/src/shaders/passes.glsl.js` (full rewrite below)
- Modify: `landing/src/sim.js` (full rewrite below)
- Test: `node scripts/build-landing.mjs --out .qa-dist/__landing__ && node scripts/check-landing.mjs .qa-dist/__landing__`

**Interfaces:**
- Consumes: `NOISE` from `./shaders/noise.glsl.js` (unchanged), `addFibers(scene)` from `./fiber.js` (unchanged this task).
- Produces: `world.js` exporting `CORE_CENTER: Vector3`, `CORE_RADIUS: number`, `BOUNDS: Vector3`. `sim.js` still exports `createField(canvas)` returning `{ onPointer, onImpulse, onScroll, setPaused }` (signature unchanged — `main.js` must not change). Internal frame order that later tasks hook into: pointer→world, sim passes, fiber update, render.

- [ ] **Step 1: Create `landing/src/world.js`**

```js
import { Vector3 } from 'three';

// Shared world-space constants — the one source of truth for scene layout.
// The core sits right-of-center (the hero title is left-aligned) and slightly
// above the hero's vertical middle. BOUNDS is the particle wrap box; it must
// contain the camera rig's full orbit (max radius 20 around CORE_CENTER).
export const CORE_CENTER = new Vector3(3.2, 1.2, 0);
export const CORE_RADIUS = 2.5;
export const BOUNDS = new Vector3(24, 14, 24);
```

- [ ] **Step 2: Rewrite `landing/src/shaders/passes.glsl.js`**

Full new content:

```js
import { NOISE } from './noise.glsl.js';

// Fullscreen-quad vertex shader shared by all sim passes.
export const SIM_VERT = /* glsl */ `
varying vec2 vUv;
void main() { vUv = uv; gl_Position = vec4(position, 1.0); }`;

// Seeds a render target from a DataTexture (initial positions).
export const COPY_FRAG = /* glsl */ `
uniform sampler2D uSrc;
varying vec2 vUv;
void main() { gl_FragColor = texture2D(uSrc, vUv); }`;

// Velocity update: 3D curl drift + cursor wake + hover impulse + damping.
export const VEL_FRAG = /* glsl */ `
uniform sampler2D uPos, uVel;
uniform float uDt, uTime;
uniform vec3 uPointer, uPointerVel;
uniform vec4 uImpulse;   // xyz = world pos; w = strength
varying vec2 vUv;
${NOISE}
// Divergence-free 3D field: curl of a vector potential whose components are
// three domain-offset simplex samples. 12 snoise taps per texel — the texel
// budget (160^2 mobile … 448^2 big desktops) keeps this affordable.
vec3 curl3(vec3 p) {
  const float e = 0.35;
  vec3 ex = vec3(e, 0.0, 0.0), ey = vec3(0.0, e, 0.0), ez = vec3(0.0, 0.0, e);
  vec3 o1 = vec3(31.4, 17.7, 5.3), o2 = vec3(-12.1, 70.8, 43.9);
  float dcdy = snoise(p + o2 + ey) - snoise(p + o2 - ey);
  float dbdz = snoise(p + o1 + ez) - snoise(p + o1 - ez);
  float dadz = snoise(p + ez) - snoise(p - ez);
  float dcdx = snoise(p + o2 + ex) - snoise(p + o2 - ex);
  float dbdx = snoise(p + o1 + ex) - snoise(p + o1 - ex);
  float dady = snoise(p + ey) - snoise(p - ey);
  return vec3(dcdy - dbdz, dadz - dcdx, dbdx - dady) / (2.0 * e);
}
void main() {
  vec4 pos = texture2D(uPos, vUv);
  vec3 v = texture2D(uVel, vUv).xyz;
  // ambient drift
  v += curl3(pos.xyz * 0.11 + vec3(0.0, 0.0, uTime * 0.04)) * 0.7 * uDt;
  // cursor wake: drag particles along the pointer's world velocity
  vec3 toP = pos.xyz - uPointer;
  v += uPointerVel * exp(-dot(toP, toP) / 2.6) * 2.6 * uDt;
  // hover impulse: radial push from the impulse point, decays JS-side (w)
  vec3 toI = pos.xyz - uImpulse.xyz;
  float di = length(toI) + 1e-4;
  v += (toI / di) * uImpulse.w * exp(-di * di / 1.4) * uDt;
  // frame-rate-independent damping + speed clamp
  v *= exp(-1.6 * uDt);
  float sp = length(v);
  if (sp > 3.0) v *= 3.0 / sp;
  gl_FragColor = vec4(v, 1.0);
}`;

// Position update: integrate + toroidal wrap inside the 3D box uBounds.
export const POS_FRAG = /* glsl */ `
uniform sampler2D uPos, uVel;
uniform float uDt;
uniform vec3 uBounds;
varying vec2 vUv;
void main() {
  vec4 pos = texture2D(uPos, vUv);
  vec3 v = texture2D(uVel, vUv).xyz;
  vec3 p = pos.xyz + v * uDt;
  p = mod(p + uBounds, 2.0 * uBounds) - uBounds;
  gl_FragColor = vec4(p, pos.w);
}`;

// Points: position.xy carries the sim-texture ref UV. Depth fog dims far
// particles — the main volumetric cue once the camera moves in 3D.
export const RENDER_VERT = /* glsl */ `
uniform sampler2D uPos, uVel;
uniform float uSize, uPixelRatio;
varying float vAlpha;
varying vec3 vColor;
void main() {
  vec2 ref = position.xy;
  vec4 pos = texture2D(uPos, ref);
  vec3 vel = texture2D(uVel, ref).xyz;
  float seed = pos.w;
  vec4 mv = modelViewMatrix * vec4(pos.xyz, 1.0);
  gl_Position = projectionMatrix * mv;
  gl_PointSize = uSize * uPixelRatio * mix(0.5, 1.6, fract(seed * 7.31)) * (12.0 / max(-mv.z, 0.1));
  float sp = clamp(length(vel) * 0.9, 0.0, 1.0);
  vColor = mix(vec3(0.30, 0.55, 0.72), vec3(0.98, 0.99, 1.0), sp);  // dim cyan -> white by speed
  float fog = exp(-0.04 * max(length(mv.xyz) - 6.0, 0.0));
  vAlpha = mix(0.25, 0.9, sp) * mix(0.4, 1.0, fract(seed * 3.17)) * fog;
}`;

export const RENDER_FRAG = /* glsl */ `
varying float vAlpha;
varying vec3 vColor;
void main() {
  float d = length(gl_PointCoord - 0.5);
  float a = smoothstep(0.5, 0.05, d) * vAlpha;
  gl_FragColor = vec4(vColor * a, a);
}`;
```

- [ ] **Step 3: Rewrite `landing/src/sim.js`**

Full new content. Changes vs. current: 3D init positions in `BOUNDS`; `uBounds` vec3; `uPointer`/`uPointerVel` vec3; `uImpulse` = (xyz, strength) with radius² hard-coded 1.4 in the shader; pointer mapping by unprojection onto the view-perpendicular plane through `CORE_CENTER`; `uSize` 2.4; `preserveDrawingBuffer` behind a `?qa` URL flag (used by Task 5's pixel sampling — WebGL canvases are unreadable after compositing without it). Camera/parallax/fiber wiring unchanged this task.

```js
import {
  WebGLRenderer, Scene, PerspectiveCamera, OrthographicCamera, Mesh, Points,
  PlaneGeometry, BufferGeometry, BufferAttribute, ShaderMaterial, DataTexture,
  WebGLRenderTarget, RGBAFormat, FloatType, HalfFloatType, NearestFilter,
  AdditiveBlending, Vector2, Vector3, Vector4, Clock,
} from 'three';
import { SIM_VERT, COPY_FRAG, VEL_FRAG, POS_FRAG, RENDER_VERT, RENDER_FRAG } from './shaders/passes.glsl.js';
import { addFibers } from './fiber.js';
import { CORE_CENTER, BOUNDS } from './world.js';

const FOV = 55, CAM_Z = 14, PARALLAX = 0.0012, MAX_DT = 1 / 30;

function pickTexSize(coarse) {
  const cores = navigator.hardwareConcurrency || 4;
  const area = (screen.width || 1280) * (screen.height || 800);
  if (coarse || area < 1e6 || cores <= 4) return 160; // ~25.6k particles
  if (cores <= 8) return 256;                         // ~65.5k
  return 448;                                         // ~200.7k
}

export function createField(canvas) {
  const coarse = matchMedia('(pointer: coarse)').matches;
  // ?qa: QA pixel sampling needs to read the canvas after compositing.
  const qa = new URLSearchParams(location.search).has('qa');
  let renderer;
  try {
    renderer = new WebGLRenderer({
      canvas, alpha: true, antialias: false,
      powerPreference: 'high-performance', preserveDrawingBuffer: qa,
    });
  } catch { return null; }
  if (!renderer.capabilities.isWebGL2) { renderer.dispose(); return null; }
  const type = renderer.extensions.has('EXT_color_buffer_float') ? FloatType
    : renderer.extensions.has('EXT_color_buffer_half_float') ? HalfFloatType : null;
  if (!type) { renderer.dispose(); return null; }

  const baseDpr = Math.min(devicePixelRatio || 1, coarse ? 1.5 : 2);
  renderer.setPixelRatio(baseDpr);
  renderer.setClearColor(0x000000, 0); // page gradient shows through

  const size = pickTexSize(coarse);
  const count = size * size;

  // --- camera ---
  const camera = new PerspectiveCamera(FOV, 1, 0.1, 120);
  camera.position.z = CAM_Z;
  const halfH = Math.tan((FOV / 2) * (Math.PI / 180)) * CAM_Z;

  // --- sim targets (ping-pong pos + vel) ---
  const rt = () => new WebGLRenderTarget(size, size, {
    type, format: RGBAFormat, minFilter: NearestFilter, magFilter: NearestFilter,
    depthBuffer: false, stencilBuffer: false,
  });
  let posA = rt(), posB = rt(), velA = rt(), velB = rt();

  // --- initial positions: uniform in the 3D wrap box, w = seed ---
  const init = new Float32Array(count * 4);
  for (let i = 0; i < count; i++) {
    init[i * 4 + 0] = (Math.random() * 2 - 1) * BOUNDS.x;
    init[i * 4 + 1] = (Math.random() * 2 - 1) * BOUNDS.y;
    init[i * 4 + 2] = (Math.random() * 2 - 1) * BOUNDS.z;
    init[i * 4 + 3] = Math.random();
  }
  const initTex = new DataTexture(init, size, size, RGBAFormat, FloatType);
  initTex.needsUpdate = true;

  // --- sim pipeline: fullscreen quad, material swapped per pass ---
  const simScene = new Scene();
  const simCam = new OrthographicCamera(-1, 1, 1, -1, 0, 1);
  const quad = new Mesh(new PlaneGeometry(2, 2));
  simScene.add(quad);
  const copyMat = new ShaderMaterial({ vertexShader: SIM_VERT, fragmentShader: COPY_FRAG, uniforms: { uSrc: { value: initTex } } });
  const velMat = new ShaderMaterial({
    vertexShader: SIM_VERT, fragmentShader: VEL_FRAG,
    uniforms: {
      uPos: { value: null }, uVel: { value: null }, uDt: { value: 0 }, uTime: { value: 0 },
      uPointer: { value: new Vector3(999, 999, 999) }, uPointerVel: { value: new Vector3(0, 0, 0) },
      uImpulse: { value: new Vector4(999, 999, 999, 0) },
    },
  });
  const posMat = new ShaderMaterial({
    vertexShader: SIM_VERT, fragmentShader: POS_FRAG,
    uniforms: { uPos: { value: null }, uVel: { value: null }, uDt: { value: 0 }, uBounds: { value: BOUNDS } },
  });
  const pass = (mat, target) => {
    quad.material = mat;
    renderer.setRenderTarget(target);
    renderer.render(simScene, simCam);
    renderer.setRenderTarget(null);
  };

  // --- points: position.xy = ref UV into the sim textures ---
  const refs = new Float32Array(count * 3);
  for (let j = 0; j < size; j++) for (let i = 0; i < size; i++) {
    const k = j * size + i;
    refs[k * 3 + 0] = (i + 0.5) / size;
    refs[k * 3 + 1] = (j + 0.5) / size;
  }
  const geo = new BufferGeometry();
  geo.setAttribute('position', new BufferAttribute(refs, 3));
  const renderMat = new ShaderMaterial({
    vertexShader: RENDER_VERT, fragmentShader: RENDER_FRAG,
    transparent: true, depthWrite: false, depthTest: false, blending: AdditiveBlending,
    uniforms: { uPos: { value: null }, uVel: { value: null }, uSize: { value: 2.4 }, uPixelRatio: { value: baseDpr } },
  });
  const points = new Points(geo, renderMat);
  points.frustumCulled = false;
  const scene = new Scene();
  scene.add(points);
  const fibers = addFibers(scene);

  // --- pointer state ---
  // Client coords map to world by intersecting the pointer ray with the plane
  // through CORE_CENTER perpendicular to the view direction — stays meaningful
  // from every camera angle the rig reaches.
  const ptrClient = new Vector2(-1e4, -1e4);
  const ptrWorld = new Vector3(999, 999, 999);
  const ptrPrev = new Vector3(999, 999, 999);
  const ptrVel = new Vector3(0, 0, 0);
  const ndc = new Vector3(), rayDir = new Vector3(), camFwd = new Vector3(), tmpV = new Vector3();
  let hasPointer = false, lastPointerAt = 0, ptrFresh = true;
  let scrollY = window.scrollY || 0;
  const impulse = velMat.uniforms.uImpulse.value;

  const toWorld = (cx, cy, out) => {
    ndc.set((cx / innerWidth) * 2 - 1, -(cy / innerHeight) * 2 + 1, 0.5);
    rayDir.copy(ndc).unproject(camera).sub(camera.position).normalize();
    camera.getWorldDirection(camFwd);
    const t = tmpV.copy(CORE_CENTER).sub(camera.position).dot(camFwd)
      / Math.max(rayDir.dot(camFwd), 1e-4);
    return out.copy(camera.position).addScaledVector(rayDir, t);
  };

  function resize() {
    renderer.setSize(innerWidth, innerHeight);
    camera.aspect = innerWidth / innerHeight;
    camera.updateProjectionMatrix();
  }
  addEventListener('resize', resize, { passive: true });
  resize();

  // seed sim state: positions from initTex, velocities cleared to zero
  pass(copyMat, posA);
  renderer.setRenderTarget(velA);
  renderer.clear(true, false, false);
  renderer.setRenderTarget(null);

  // --- loop (visibility pause + fps guard) ---
  const clock = new Clock();
  let raf = 0, paused = false, elapsed = 0;
  // fps guard: after 4s warmup, avg over ~2s windows; degrade at <40fps, twice max
  let guardStage = 0, winFrames = 0, winTime = 0;

  function frame() {
    raf = requestAnimationFrame(frame);
    const dt = Math.min(clock.getDelta(), MAX_DT);
    elapsed += dt;

    camera.position.y = -scrollY * PARALLAX * halfH;
    camera.updateMatrixWorld();

    // Touch devices idle >2.5s (or before any pointer event): roam a lissajous
    // attractor so the field feels alive without a cursor.
    if (coarse && (!hasPointer || elapsed - lastPointerAt > 2.5)) {
      ptrClient.set(
        (0.5 + 0.38 * Math.sin(elapsed * 0.31)) * innerWidth,
        (0.5 + 0.34 * Math.cos(elapsed * 0.21)) * innerHeight,
      );
      hasPointer = true;
    }
    if (hasPointer) {
      toWorld(ptrClient.x, ptrClient.y, ptrWorld);
      // First frame after hasPointer flips true: seed ptrPrev from ptrWorld so
      // this frame contributes zero velocity, not a kick from the sentinel.
      if (ptrFresh) { ptrPrev.copy(ptrWorld); ptrFresh = false; }
      if (dt > 0) {
        ptrVel.copy(ptrWorld).sub(ptrPrev).divideScalar(dt).clampLength(0, 30);
        velMat.uniforms.uPointerVel.value.lerp(ptrVel, 0.15);
      }
      ptrPrev.copy(ptrWorld);
      velMat.uniforms.uPointer.value.copy(ptrWorld);
    }

    velMat.uniforms.uDt.value = dt;
    velMat.uniforms.uTime.value = elapsed;
    posMat.uniforms.uDt.value = dt;

    velMat.uniforms.uPos.value = posA.texture;
    velMat.uniforms.uVel.value = velA.texture;
    pass(velMat, velB);
    posMat.uniforms.uPos.value = posA.texture;
    posMat.uniforms.uVel.value = velB.texture;
    pass(posMat, posB);
    [posA, posB] = [posB, posA];
    [velA, velB] = [velB, velA];

    impulse.w *= 0.86; // hover impulse decay

    fibers.update(elapsed, velMat.uniforms.uPointer.value, camera.position.y);
    renderMat.uniforms.uPos.value = posA.texture;
    renderMat.uniforms.uVel.value = velA.texture;
    renderer.render(scene, camera);

    if (elapsed > 4 && guardStage < 2) {
      winFrames++; winTime += dt;
      if (winTime >= 2) {
        if (winFrames / winTime < 40) {
          if (guardStage === 0) {
            renderMat.uniforms.uPixelRatio.value = baseDpr * 0.7;
            renderer.setPixelRatio(baseDpr * 0.7);
          } else geo.setDrawRange(0, Math.floor(count / 2));
          guardStage++;
        }
        winFrames = 0; winTime = 0;
      }
    }
  }
  frame();

  return {
    onPointer(cx, cy) { ptrClient.set(cx, cy); hasPointer = true; lastPointerAt = elapsed; },
    onImpulse(cx, cy) {
      const w = toWorld(cx, cy, new Vector3());
      impulse.set(w.x, w.y, w.z, 26);
      fibers.burst(); // hover "transmits" a pulse down a fiber
    },
    onScroll(y) { scrollY = y; },
    setPaused(p) {
      if (p === paused) return;
      paused = p;
      if (p) cancelAnimationFrame(raf);
      else { clock.getDelta(); frame(); }
    },
  };
}
```

Note for this task only: `fiber.js` is still the old 2D version. Its `update(elapsed, pointer, camY)` copies the pointer into a `Vector2` (`Vector2.copy` reads `.x/.y` off a `Vector3`, so passing the new `Vector3` works), and `fibers.resize(halfW, halfH)` is no longer called — the old fibers therefore keep their constructor-default `uA/uB` of `(0,0)` and effectively vanish until Task 3 rewrites them. That is acceptable mid-refactor: the smoke test asserts boot/errors, not fiber pixels.

- [ ] **Step 4: Build and run the smoke test**

```bash
node scripts/build-landing.mjs --out .qa-dist/__landing__ && node scripts/check-landing.mjs .qa-dist/__landing__
```

Expected: `✅ landing check passed.` (all three passes; zero console errors — a GLSL compile error would surface as a console error and fail pass 1).

- [ ] **Step 5: Commit**

```bash
git add landing/src/world.js landing/src/shaders/passes.glsl.js landing/src/sim.js
git commit -m "feat(landing): 3D particle sim — 3D curl velocity, box wrap, depth fog, ray-plane pointer"
```

---

### Task 2: Grid-network core (`core.js`) + screenshot review script

The revolving core: nodes on a noised fibonacci sphere, k-NN edges with traveling pulses, two-axis self-rotation, breathing, per-node twinkle, and a flash/relay mechanism for Task 3's burst handoff. Also adds the scratch screenshot script used to visually review this and every later task.

**Files:**
- Create: `landing/src/core.js`
- Modify: `landing/src/sim.js` (hookup — small edits listed below)
- Create: `.qa-dist/shot-landing.mjs` (scratch, gitignored — do not commit)
- Test: smoke test + screenshots

**Interfaces:**
- Consumes: `CORE_CENTER`, `CORE_RADIUS` from `./world.js`; `NOISE` from `./shaders/noise.glsl.js`.
- Produces: `addCore(scene, { coarse }) → { update(elapsed), flashAt(nodeIdx), anchorNode(dir: Vector3): number, nodeWorld(idx: number, out: Vector3): Vector3, setPixelRatio(dpr: number) }`. Task 3 uses `anchorNode`/`nodeWorld`/`flashAt`; Task 4 does not touch it.

- [ ] **Step 1: Create `landing/src/core.js`**

```js
import {
  Group, Points, LineSegments, BufferGeometry, BufferAttribute,
  ShaderMaterial, AdditiveBlending, Vector3,
} from 'three';
import { CORE_CENTER, CORE_RADIUS } from './world.js';
import { NOISE } from './shaders/noise.glsl.js';

// Grid-network core: nodes on a radially-noised fibonacci sphere, k-nearest
// edges with traveling light pulses. Self-rotates on two axes with different
// periods; "breathes" via radial simplex noise (identical displacement in the
// node and edge vertex shaders so endpoints stay glued). flashAt(node) makes
// the node flare, sweeps a relay pulse down its edges, and flares its
// neighbors 0.45s later (aFlash holds the flash time; step() gates the future).

const NODE_VERT = /* glsl */ `
uniform float uTime, uPixelRatio;
attribute float aSeed, aFlash;
varying float vAlpha;
${NOISE}
void main() {
  vec3 p = position;
  p *= 1.0 + snoise(normalize(p) * 1.6 + vec3(0.0, uTime * 0.13, 0.0)) * 0.05;
  vec4 mv = modelViewMatrix * vec4(p, 1.0);
  gl_Position = projectionMatrix * mv;
  float tw = 0.75 + 0.25 * sin(uTime * (0.6 + aSeed * 1.7) + aSeed * 40.0);
  float flash = step(aFlash, uTime) * exp(-(uTime - aFlash) * 2.2);
  gl_PointSize = uPixelRatio * (26.0 + flash * 30.0) / max(-mv.z, 0.1);
  vAlpha = (0.5 + 0.5 * tw) * (0.55 + flash * 2.0);
}`;

const NODE_FRAG = /* glsl */ `
varying float vAlpha;
void main() {
  float d = length(gl_PointCoord - 0.5);
  float a = smoothstep(0.5, 0.08, d) * vAlpha;
  vec3 col = mix(vec3(0.45, 0.72, 0.88), vec3(1.0), smoothstep(0.6, 1.6, vAlpha));
  gl_FragColor = vec4(col * a, a);
}`;

const EDGE_VERT = /* glsl */ `
uniform float uTime;
attribute float aT, aPhase, aFlash;
varying float vT, vPhase, vFlash;
${NOISE}
void main() {
  vec3 p = position;
  p *= 1.0 + snoise(normalize(p) * 1.6 + vec3(0.0, uTime * 0.13, 0.0)) * 0.05;
  gl_Position = projectionMatrix * modelViewMatrix * vec4(p, 1.0);
  vT = aT; vPhase = aPhase; vFlash = aFlash;
}`;

const EDGE_FRAG = /* glsl */ `
uniform float uTime;
varying float vT, vPhase, vFlash;
void main() {
  float base = 0.10;
  float pp = fract(uTime * 0.11 + vPhase);
  float d = abs(vT - pp);
  float pulse = exp(-(d * d) / 0.006);
  // relay: after a flash, a bright front sweeps the edge over ~0.45s, fading
  float on = step(vFlash, uTime);
  float fp = clamp((uTime - vFlash) * 2.2, 0.0, 1.0);
  float fd = abs(vT - fp);
  float relay = on * exp(-(fd * fd) / 0.01) * exp(-(uTime - vFlash) * 1.2) * 2.0;
  float b = base + pulse * 0.5 + relay;
  vec3 col = mix(vec3(0.35, 0.62, 0.78), vec3(1.0), clamp(pulse + relay, 0.0, 1.0));
  gl_FragColor = vec4(col * b, b * 0.9);
}`;

const mulberry32 = (a) => () => {
  a |= 0; a = (a + 0x6D2B79F5) | 0;
  let t = Math.imul(a ^ (a >>> 15), 1 | a);
  t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
  return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
};

export function addCore(scene, { coarse } = {}) {
  const N = coarse ? 80 : 160;
  const rand = mulberry32(20260706);

  // Nodes: fibonacci sphere + radial noise so it reads organic, not geodesic.
  const nodes = [];
  for (let i = 0; i < N; i++) {
    const t = (i + 0.5) / N;
    const y = 1 - 2 * t;
    const rxy = Math.sqrt(Math.max(1 - y * y, 0));
    const phi = i * 2.399963229728653; // golden angle
    const r = CORE_RADIUS * (1 + (rand() - 0.5) * 0.36);
    nodes.push(new Vector3(Math.cos(phi) * rxy * r, y * r, Math.sin(phi) * rxy * r));
  }

  // Edges: k-nearest neighbors (k=3), capped length, deduped (i<j).
  const K = 3, MAXL = CORE_RADIUS * 1.2;
  const edgeSet = new Set();
  const edges = [];               // [i, j] node index pairs
  const adjacency = nodes.map(() => []); // node idx -> [{edge, other}]
  for (let i = 0; i < N; i++) {
    const near = nodes.map((p, j) => ({ j, d: i === j ? Infinity : p.distanceTo(nodes[i]) }))
      .sort((a, b) => a.d - b.d).slice(0, K);
    for (const { j, d } of near) {
      if (d > MAXL) continue;
      const key = i < j ? `${i}-${j}` : `${j}-${i}`;
      if (edgeSet.has(key)) continue;
      edgeSet.add(key);
      const e = edges.length;
      edges.push([i, j]);
      adjacency[i].push({ edge: e, other: j });
      adjacency[j].push({ edge: e, other: i });
    }
  }

  // Node geometry
  const nPos = new Float32Array(N * 3);
  const nSeed = new Float32Array(N);
  const nFlash = new Float32Array(N).fill(-1e3);
  nodes.forEach((p, i) => { p.toArray(nPos, i * 3); nSeed[i] = rand(); });
  const nGeo = new BufferGeometry();
  nGeo.setAttribute('position', new BufferAttribute(nPos, 3));
  nGeo.setAttribute('aSeed', new BufferAttribute(nSeed, 1));
  const nFlashAttr = new BufferAttribute(nFlash, 1);
  nGeo.setAttribute('aFlash', nFlashAttr);
  const nMat = new ShaderMaterial({
    vertexShader: NODE_VERT, fragmentShader: NODE_FRAG,
    transparent: true, depthWrite: false, depthTest: false, blending: AdditiveBlending,
    uniforms: { uTime: { value: 0 }, uPixelRatio: { value: Math.min(devicePixelRatio || 1, 2) } },
  });
  const pts = new Points(nGeo, nMat);
  pts.frustumCulled = false;

  // Edge geometry (2 verts per edge)
  const E = edges.length;
  const ePos = new Float32Array(E * 2 * 3);
  const eT = new Float32Array(E * 2);
  const ePhase = new Float32Array(E * 2);
  const eFlash = new Float32Array(E * 2).fill(-1e3);
  edges.forEach(([i, j], e) => {
    nodes[i].toArray(ePos, e * 6);
    nodes[j].toArray(ePos, e * 6 + 3);
    eT[e * 2] = 0; eT[e * 2 + 1] = 1;
    const ph = rand();
    ePhase[e * 2] = ph; ePhase[e * 2 + 1] = ph;
  });
  const eGeo = new BufferGeometry();
  eGeo.setAttribute('position', new BufferAttribute(ePos, 3));
  eGeo.setAttribute('aT', new BufferAttribute(eT, 1));
  eGeo.setAttribute('aPhase', new BufferAttribute(ePhase, 1));
  const eFlashAttr = new BufferAttribute(eFlash, 1);
  eGeo.setAttribute('aFlash', eFlashAttr);
  const eMat = new ShaderMaterial({
    vertexShader: EDGE_VERT, fragmentShader: EDGE_FRAG,
    transparent: true, depthWrite: false, depthTest: false, blending: AdditiveBlending,
    uniforms: { uTime: { value: 0 } },
  });
  const lines = new LineSegments(eGeo, eMat);
  lines.frustumCulled = false;

  const group = new Group();
  group.add(lines, pts);
  group.position.copy(CORE_CENTER);
  scene.add(group);

  let lastElapsed = 0;
  const tmp = new Vector3();
  return {
    update(elapsed) {
      lastElapsed = elapsed;
      group.rotation.y = elapsed * 0.06;      // two axes, different periods
      group.rotation.x = elapsed * 0.017;
      group.updateMatrixWorld();
      nMat.uniforms.uTime.value = elapsed;
      eMat.uniforms.uTime.value = elapsed;
    },
    // Flash a node now; relay down its edges; neighbors flare 0.45s later.
    flashAt(idx) {
      nFlash[idx] = lastElapsed;
      for (const { edge, other } of adjacency[idx]) {
        eFlash[edge * 2] = lastElapsed;
        eFlash[edge * 2 + 1] = lastElapsed;
        nFlash[other] = lastElapsed + 0.45;
      }
      nFlashAttr.needsUpdate = true;
      eFlashAttr.needsUpdate = true;
    },
    // Node whose (local) direction best matches dir — fiber anchor picking.
    anchorNode(dir) {
      let best = 0, bd = -Infinity;
      nodes.forEach((p, i) => {
        const d = tmp.copy(p).normalize().dot(dir);
        if (d > bd) { bd = d; best = i; }
      });
      return best;
    },
    // Current world position of a node (rotation applied; breathing ignored —
    // it is a ±5% shader effect, small next to the fiber's own end fade).
    nodeWorld(idx, out) {
      return out.copy(nodes[idx]).applyMatrix4(group.matrixWorld);
    },
    setPixelRatio(dpr) { nMat.uniforms.uPixelRatio.value = dpr; },
  };
}
```

- [ ] **Step 2: Hook the core into `landing/src/sim.js`**

Four edits:

1. Import:
```js
import { addCore } from './core.js';
```
2. After `const fibers = addFibers(scene);` add:
```js
  const core = addCore(scene, { coarse });
  core.setPixelRatio(baseDpr);
```
3. In `frame()`, immediately before `fibers.update(...)`:
```js
    core.update(elapsed);
```
4. In the FPS guard stage-0 branch (next to `renderer.setPixelRatio(baseDpr * 0.7)`):
```js
            core.setPixelRatio(baseDpr * 0.7);
```

- [ ] **Step 3: Create the screenshot review script `.qa-dist/shot-landing.mjs`**

Scratch tool (gitignored, never committed) — serves a built landing dir and screenshots it at several scroll offsets for human/agent review:

```js
// node .qa-dist/shot-landing.mjs <distDir>  → .qa-dist/shots/scroll-*.png
import { createServer } from 'node:http';
import { readFile, stat, mkdir } from 'node:fs/promises';
import { join, extname, normalize } from 'node:path';
import { chromium } from 'playwright-chromium';

const distDir = process.argv[2];
if (!distDir) { console.error('usage: node .qa-dist/shot-landing.mjs <distDir>'); process.exit(2); }
const MIME = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.svg': 'image/svg+xml', '.png': 'image/png', '.woff2': 'font/woff2' };
const server = createServer(async (req, res) => {
  try {
    let fp = normalize(join(distDir, decodeURIComponent(req.url.split('?')[0])));
    let s = await stat(fp).catch(() => null);
    if (s && s.isDirectory()) fp = join(fp, 'index.html');
    res.setHeader('Content-Type', MIME[extname(fp)] || 'application/octet-stream');
    res.end(await readFile(fp));
  } catch { res.statusCode = 404; res.end(); }
});
const port = await new Promise((r) => server.listen(0, '127.0.0.1', () => r(server.address().port)));
const browser = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
await page.goto(`http://127.0.0.1:${port}/`, { waitUntil: 'load' });
await page.waitForFunction(() => document.documentElement.classList.contains('field-on'), null, { timeout: 20000 });
await mkdir('.qa-dist/shots', { recursive: true });
for (const f of [0, 0.5, 1, 1.5, 2.5, 5]) {
  await page.evaluate((y) => window.scrollTo(0, y * innerHeight), f);
  await page.waitForTimeout(1600); // let the (Task 4) camera damping settle
  await page.screenshot({ path: `.qa-dist/shots/scroll-${String(f).replace('.', '_')}vh.png` });
  console.log(`scroll-${f}vh ✓`);
}
await browser.close(); server.close();
```

- [ ] **Step 4: Build, smoke-test, screenshot**

```bash
node scripts/build-landing.mjs --out .qa-dist/__landing__ && node scripts/check-landing.mjs .qa-dist/__landing__
node .qa-dist/shot-landing.mjs .qa-dist/__landing__
```

Expected: smoke test passes; `scroll-0vh.png` shows a glowing node-network sphere right-of-center behind/beside the hero title, hairline edges, visible pulses. Review the screenshots before committing.

- [ ] **Step 5: Commit**

```bash
git add landing/src/core.js landing/src/sim.js
git commit -m "feat(landing): grid-network core — noised fibonacci sphere, k-NN pulse edges, flash relay"
```

---

### Task 3: Fibers in 3D — view-space billboard, core anchors, burst handoff

Rewrite `fiber.js`: `curve(t)` returns vec3, ribbons billboard in view space (never edge-on under orbit), the far end sits at a fixed world point, the near end tracks an assigned core node every frame, pulses flow toward the core, and a hover burst flashes the anchored node on arrival.

**Files:**
- Modify: `landing/src/fiber.js` (full rewrite below)
- Modify: `landing/src/sim.js` (anchor wiring + handoff queue)
- Test: smoke test + screenshots

**Interfaces:**
- Consumes: `CORE_CENTER` from `./world.js`; `core.anchorNode(dir)`, `core.nodeWorld(idx, out)`, `core.flashAt(idx)` from Task 2.
- Produces: `addFibers(scene) → { update(elapsed, pointerWorld: Vector3, getAnchor: (fiberIdx, anchorDir: Vector3, out: Vector3) => void), burst(): { fiberIdx: number, anchorDir: Vector3, arriveIn: number } }`. Note the signature change: no more `resize()`, no more `camY` tracking — fibers are fixed world objects. `sim.js` resolves `anchorDir → node idx` via `core.anchorNode` once at startup and passes a closure.

- [ ] **Step 1: Rewrite `landing/src/fiber.js`**

```js
import {
  Group, Mesh, BufferGeometry, BufferAttribute, ShaderMaterial,
  AdditiveBlending, Vector2, Vector3,
} from 'three';
import { NOISE } from './shaders/noise.glsl.js';

// Three glowing "data-link fiber" ribbons in 3D. Each spans a fixed far-world
// point uA to a core node uB (updated per frame as the core rotates), so the
// fibers visibly feed the core. The ribbon offsets perpendicular to both the
// curve tangent and the view ray (view-space billboard), so it never turns
// edge-on while the camera orbits. Pulses travel t:0→1, i.e. toward the core.

const VERT = /* glsl */ `
uniform vec3 uA, uB;
uniform float uTime, uAmp, uFreq, uSeed, uWidth;
varying float vT, vSide;
varying vec3 vWorld;
${NOISE}
vec3 curve(float t) {
  vec3 p = mix(uA, uB, t);
  // envelope pins both ends (hard at the core end so it lands on the node)
  float env = smoothstep(0.0, 0.2, t) * smoothstep(1.0, 0.85, t);
  p.y += snoise(vec3(t * uFreq, uTime * 0.12, uSeed)) * uAmp * env;
  p.x += snoise(vec3(t * uFreq * 0.7, uTime * 0.09, uSeed + 31.7)) * uAmp * 0.35 * env;
  p.z += snoise(vec3(t * uFreq * 0.55, uTime * 0.10, uSeed + 77.3)) * uAmp * 0.6 * env;
  return p;
}
void main() {
  float t = position.x;
  float side = position.y;
  vec3 p = curve(t);
  vWorld = p;
  vec4 mvP = modelViewMatrix * vec4(p, 1.0);
  vec3 tanV = normalize((modelViewMatrix * vec4(curve(min(t + 0.004, 1.0)), 1.0)).xyz
                      - (modelViewMatrix * vec4(curve(max(t - 0.004, 0.0)), 1.0)).xyz);
  vec3 viewDir = normalize(mvP.xyz);
  vec3 offV = cross(tanV, viewDir);
  float ol = length(offV);
  offV = ol < 1e-3 ? vec3(0.0, 1.0, 0.0) : offV / ol; // head-on fallback
  vT = t;
  vSide = side;
  gl_Position = projectionMatrix * vec4(mvP.xyz + offV * side * uWidth, 1.0);
}`;

const FRAG = /* glsl */ `
uniform float uTime, uPulseSpeed, uPhase, uBaseAlpha, uBurstStart;
uniform vec3 uPointer;
varying float vT, vSide;
varying vec3 vWorld;
void main() {
  float core = exp(-vSide * vSide * 9.0);
  float glow = exp(-vSide * vSide * 2.0) * 0.35;
  float p = fract(uTime * uPulseSpeed + uPhase);
  float d = abs(vT - p);
  d = min(d, 1.0 - d);
  float pulse = exp(-(d * d) / 0.0009);
  // hover burst: one-shot pulse from the far end toward the core
  float bp = (uTime - uBurstStart) * 0.55;
  if (bp >= 0.0 && bp <= 1.15) {
    float bd = vT - bp;
    pulse += exp(-(bd * bd) / 0.0011) * 1.3;
  }
  vec3 toP = vWorld - uPointer;
  float near = exp(-dot(toP, toP) / 6.0) * 0.6;
  float ends = smoothstep(0.0, 0.06, vT) * smoothstep(1.0, 0.985, vT);
  float b = (uBaseAlpha + near) * (core + glow) * ends * (1.0 + pulse * 2.6);
  vec3 col = mix(vec3(0.35, 0.62, 0.78), vec3(1.0), clamp(pulse * 0.8 + near * 0.3, 0.0, 1.0));
  gl_FragColor = vec4(col * b, b);
}`;

export function addFibers(scene) {
  const S = 240;
  const pos = new Float32Array((S + 1) * 2 * 3);
  for (let i = 0; i <= S; i++) {
    const t = i / S;
    pos[i * 6 + 0] = t; pos[i * 6 + 1] = 1;
    pos[i * 6 + 3] = t; pos[i * 6 + 4] = -1;
  }
  const idx = [];
  for (let i = 0; i < S; i++) {
    const a = i * 2;
    idx.push(a, a + 1, a + 2, a + 1, a + 3, a + 2);
  }
  const geo = new BufferGeometry();
  geo.setAttribute('position', new BufferAttribute(pos, 3));
  geo.setIndex(idx);

  const group = new Group();
  const make = (cfg) => {
    const mat = new ShaderMaterial({
      vertexShader: VERT, fragmentShader: FRAG,
      transparent: true, depthWrite: false, depthTest: false, blending: AdditiveBlending,
      uniforms: {
        uA: { value: cfg.A.clone() }, uB: { value: new Vector3() },
        uTime: { value: 0 }, uAmp: { value: cfg.amp }, uFreq: { value: cfg.freq },
        uSeed: { value: cfg.seed }, uWidth: { value: cfg.width },
        uPulseSpeed: { value: cfg.pulseSpeed }, uPhase: { value: cfg.phase },
        uBaseAlpha: { value: cfg.baseAlpha }, uBurstStart: { value: -1e3 },
        uPointer: { value: new Vector3(999, 999, 999) },
      },
    });
    const mesh = new Mesh(geo, mat);
    mesh.frustumCulled = false;
    group.add(mesh);
    return { mat, cfg };
  };

  // Three approach azimuths so orbiting reveals depth. anchorDir is the
  // preferred core-surface direction (local space) for the near end.
  const fibers = [
    make({ A: new Vector3(-34, 10, -8), anchorDir: new Vector3(-0.55, 0.55, -0.2).normalize(),
      amp: 1.6, freq: 2.1, seed: 7.3, width: 0.07, pulseSpeed: 0.10, phase: 0.0, baseAlpha: 0.5 }),
    make({ A: new Vector3(-30, -12, 6), anchorDir: new Vector3(-0.65, -0.5, 0.4).normalize(),
      amp: 2.0, freq: 1.6, seed: 42.0, width: 0.09, pulseSpeed: 0.06, phase: 0.55, baseAlpha: 0.34 }),
    make({ A: new Vector3(6, -4, -34), anchorDir: new Vector3(0.15, -0.25, -0.95).normalize(),
      amp: 1.8, freq: 1.8, seed: 19.1, width: 0.08, pulseSpeed: 0.075, phase: 0.3, baseAlpha: 0.4 }),
  ];
  scene.add(group);

  let lastElapsed = 0;
  let burstIdx = 0;
  const BURST_SPEED = 0.55; // must match the shader's bp rate
  return {
    // getAnchor(fiberIdx, anchorDir, out) fills the current world position of
    // the fiber's core node — supplied by sim.js (closure over core).
    update(elapsed, pointerWorld, getAnchor) {
      lastElapsed = elapsed;
      fibers.forEach(({ mat, cfg }, i) => {
        getAnchor(i, cfg.anchorDir, mat.uniforms.uB.value);
        mat.uniforms.uTime.value = elapsed;
        mat.uniforms.uPointer.value.copy(pointerWorld);
      });
    },
    // one-shot pulse toward the core, alternating fibers; the caller schedules
    // core.flashAt when it arrives (arriveIn seconds).
    burst() {
      const i = burstIdx;
      burstIdx = (burstIdx + 1) % fibers.length;
      fibers[i].mat.uniforms.uBurstStart.value = lastElapsed;
      return { fiberIdx: i, anchorDir: fibers[i].cfg.anchorDir, arriveIn: 1 / BURST_SPEED };
    },
  };
}
```

- [ ] **Step 2: Wire anchors + burst handoff in `landing/src/sim.js`**

Three edits:

1. After the `const core = addCore(...)` lines, resolve each fiber's node once and build the anchor closure (node indices are stable; `nodeWorld` applies the live rotation):
```js
  const anchorIdx = new Map(); // fiberIdx -> core node idx (resolved lazily)
  const getAnchor = (fiberIdx, anchorDir, out) => {
    if (!anchorIdx.has(fiberIdx)) anchorIdx.set(fiberIdx, core.anchorNode(anchorDir));
    core.nodeWorld(anchorIdx.get(fiberIdx), out);
  };
  const arrivals = []; // { at, node } — burst pulses in flight toward the core
```
2. Replace the `fibers.update(...)` call in `frame()` with:
```js
    core.update(elapsed);
    fibers.update(elapsed, velMat.uniforms.uPointer.value, getAnchor);
    for (let i = arrivals.length - 1; i >= 0; i--) {
      if (elapsed >= arrivals[i].at) {
        core.flashAt(arrivals[i].node);
        arrivals.splice(i, 1);
      }
    }
```
(the `core.update(elapsed)` line moves here from wherever Task 2 placed it — keep exactly one call)
3. In `onImpulse`, replace `fibers.burst();` with:
```js
      const b = fibers.burst();
      arrivals.push({ at: elapsed + b.arriveIn, node: anchorIdx.get(b.fiberIdx) ?? core.anchorNode(b.anchorDir) });
```

- [ ] **Step 3: Build, smoke-test, screenshot**

```bash
node scripts/build-landing.mjs --out .qa-dist/__landing__ && node scripts/check-landing.mjs .qa-dist/__landing__
node .qa-dist/shot-landing.mjs .qa-dist/__landing__
```

Expected: pass; screenshots show three fibers converging on the core from different directions, ends landing on the sphere. (Camera is still static until Task 4, so all offsets look similar apart from parallax.)

- [ ] **Step 4: Commit**

```bash
git add landing/src/fiber.js landing/src/sim.js
git commit -m "feat(landing): 3D fibers — view-space billboard ribbons anchored to core nodes, burst handoff"
```

---

### Task 4: Scroll camera rig (`rig.js`) + framing tune

The scroll choreography: damped spherical orbit (azimuth −18°→122°, radius 10→20, elevation 2°→14°) over the first 1.5 viewport heights, look-at drifting from beside the core to below it, calm creep + descent past p=1. Replaces the old Y-parallax.

**Files:**
- Create: `landing/src/rig.js`
- Modify: `landing/src/sim.js` (replace parallax with the rig)
- Test: smoke test + screenshots at all offsets

**Interfaces:**
- Consumes: `CORE_CENTER` from `./world.js`.
- Produces: `createRig(camera) → { setScroll(y: number), update(dt: number) }`. `update` writes `camera.position` and calls `camera.lookAt` + `camera.updateMatrixWorld()`; sim.js must call `rig.update(dt)` before any pointer unprojection each frame.

- [ ] **Step 1: Create `landing/src/rig.js`**

```js
import { Vector3 } from 'three';
import { CORE_CENTER } from './world.js';

// Scroll-driven orbital camera. Spherical path around CORE_CENTER: azimuth
// sweeps ~140° while the radius dollies 10→20 and elevation rises 2°→14°,
// over the first 1.5 viewport-heights of scroll (smoothstep-eased). The
// look-at starts beside the core (framing it right-of-center behind the
// left-aligned hero title) and sinks below it as we pull out, drifting the
// core into the upper third. Past p=1: slow azimuth creep + gentle descent
// (the calm state behind the lecture list). The camera chases its target
// with exponential damping so wheel steps / touch momentum never snap.
// No roll, ever; scroll is the only input.

const D2R = Math.PI / 180;
const R0 = 10, R1 = 20;
const AZI0 = -18 * D2R, AZI1 = 122 * D2R;
const EL0 = 2 * D2R, EL1 = 14 * D2R;
const SCROLL_VH = 1.5;      // choreography span, in viewport heights
const LOOK_ASIDE = 3.5;     // p=0: look this far left of the core → core sits right
const LOOK_DROP = 3.4;      // p=1: look this far below the core → core sits high
const CREEP = 3e-5;         // rad of azimuth per px past p=1
const DESCEND = 0.003;      // world units per px past p=1 (gentle drift)
const DAMP = 6;             // 1/s → k ≈ 0.1/frame at 60fps

const smooth = (t) => t * t * (3 - 2 * t);

export function createRig(camera) {
  let p = 0, over = 0;
  let azi = AZI0, r = R0, el = EL0, aside = LOOK_ASIDE, drop = 0, sink = 0;
  const pos = new Vector3(), look = new Vector3();

  return {
    setScroll(y) {
      const span = Math.max(innerHeight * SCROLL_VH, 1);
      p = smooth(Math.min(Math.max(y / span, 0), 1));
      over = Math.max(y - span, 0);
    },
    update(dt) {
      const k = 1 - Math.exp(-DAMP * dt);
      azi += (AZI0 + (AZI1 - AZI0) * p + over * CREEP - azi) * k;
      r += (R0 + (R1 - R0) * p - r) * k;
      el += (EL0 + (EL1 - EL0) * p - el) * k;
      aside += (LOOK_ASIDE * (1 - p) - aside) * k;
      drop += (LOOK_DROP * p - drop) * k;
      sink += (over * DESCEND - sink) * k;
      pos.set(
        CORE_CENTER.x + r * Math.cos(el) * Math.sin(azi),
        CORE_CENTER.y + r * Math.sin(el) - sink,
        CORE_CENTER.z + r * Math.cos(el) * Math.cos(azi),
      );
      look.set(CORE_CENTER.x - aside, CORE_CENTER.y - drop - sink, CORE_CENTER.z);
      camera.position.copy(pos);
      camera.lookAt(look);
      camera.updateMatrixWorld();
    },
  };
}
```

- [ ] **Step 2: Replace the parallax with the rig in `landing/src/sim.js`**

Five edits:

1. Import:
```js
import { createRig } from './rig.js';
```
2. Delete `PARALLAX` from the constants line and the `halfH` line (`const halfH = ...` — no longer used); the constants line becomes:
```js
const FOV = 55, CAM_Z = 14, MAX_DT = 1 / 30;
```
3. After the camera is created, add:
```js
  const rig = createRig(camera);
  rig.setScroll(scrollY);
```
   …but note `scrollY` is declared later in the file; instead place `rig.setScroll(window.scrollY || 0);` — or simply rely on `onScroll`/first `update`. Concretely: create the rig right after `camera.position.z = CAM_Z;` and drop the explicit seed call — `rig.update` on the first frame with `p=0` already frames the hero correctly when the page loads at the top, and a mid-page reload gets its scroll via the `onScroll` wiring in `main.js` plus the initial `let scrollY = window.scrollY || 0;` — so ALSO call `rig.setScroll(scrollY)` once right after `let scrollY = window.scrollY || 0;`.
4. In `frame()`, replace
```js
    camera.position.y = -scrollY * PARALLAX * halfH;
    camera.updateMatrixWorld();
```
with
```js
    rig.update(dt);
```
(rig.update calls `updateMatrixWorld` itself; it must stay before the pointer block).
5. In `onScroll`, forward to the rig:
```js
    onScroll(y) { scrollY = y; rig.setScroll(y); },
```

- [ ] **Step 3: Build, smoke-test, screenshot all offsets**

```bash
node scripts/build-landing.mjs --out .qa-dist/__landing__ && node scripts/check-landing.mjs .qa-dist/__landing__
node .qa-dist/shot-landing.mjs .qa-dist/__landing__
```

Expected: smoke test passes. Screenshots: `scroll-0vh` — core right-of-center, roughly ⅓–½ of frame height, fibers feeding it; `scroll-0_5vh`/`scroll-1vh` — viewpoint visibly swung around the core (different fiber/edge arrangement, not just shifted); `scroll-1_5vh`+ — core small, upper third, lecture rows readable over a calm field; `scroll-5vh` — near-identical to 2.5vh plus slight drift.

- [ ] **Step 4: Framing tune (screenshot-driven)**

Judge the screenshots against the checklist below and adjust ONLY these constants, then rebuild + re-screenshot (repeat up to ~3 rounds):
- Core too big/small at p=0 → `R0` in `rig.js` (10 → 8–13 range).
- Core not right-of-center enough → `LOOK_ASIDE` (2.5–4.5).
- Core not high enough behind the list at p=1 → `LOOK_DROP` (2.5–4.5).
- Field too sparse/dense → `uSize` in `sim.js` (2.0–3.0) and fog coefficient `0.04` in `RENDER_VERT` (0.03–0.06).
- Fibers too thin/thick → `width` values in `fiber.js` (0.05–0.12).

Checklist: hero title fully readable at p=0; core majority-visible (not clipped past ~40% at either end of the orbit); lecture rows readable at 1.5vh+ (no bright core behind row text); particles show clear near/far size+brightness contrast.

- [ ] **Step 5: Commit**

```bash
git add landing/src/rig.js landing/src/sim.js landing/src/fiber.js landing/src/shaders/passes.glsl.js
git commit -m "feat(landing): scroll camera rig — damped 140° orbit + dolly-out around the core"
```

---

### Task 5: QA pixel pass in `check-landing.mjs`

Extend the smoke test: with `?qa` (which enables `preserveDrawingBuffer` — added in Task 1), sample the WebGL canvas at two scroll offsets; assert both render non-blank AND differ (proves the scroll→camera wiring). Verify the new pass by mutation: break rendering, watch it fail, restore.

**Files:**
- Modify: `scripts/check-landing.mjs`
- Test: the script itself (pass + deliberate-failure run)

**Interfaces:**
- Consumes: the `?qa` flag in `sim.js` (Task 1). No production interface produced.

- [ ] **Step 1: Add pass 4 to `scripts/check-landing.mjs`**

Insert before the closing `} finally {` of the outer `try` (after pass 3's block):

```js
  console.log('— pass 4: scene pixels at scroll offsets (?qa) —');
  {
    let ctx;
    try {
      const ctx2 = await browser.newContext({ viewport: { width: 1280, height: 800 }, reducedMotion: 'no-preference' });
      ctx = ctx2;
      const page = await ctx2.newPage();
      const errors = [];
      page.on('console', (m) => { if (m.type() === 'error') errors.push(m.text()); });
      page.on('pageerror', (e) => errors.push(String(e)));
      await page.goto(home + '?qa', { waitUntil: 'load' });
      const gated = await page.waitForFunction(() => {
        const c = document.documentElement.classList;
        return (c.contains('field-on') || c.contains('static-bg')) ? (c.contains('field-on') ? 'field-on' : 'static-bg') : false;
      }, null, { timeout: 20000 }).then((h) => h.jsonValue()).catch(() => null);
      if (gated !== 'field-on') {
        console.log(`  - skipped (no WebGL scene: ${gated})`);
      } else {
        // Downsample the field canvas to 64×40 and return luminance samples.
        // Works because ?qa builds the renderer with preserveDrawingBuffer.
        const sample = () => page.evaluate(() => new Promise((resolveP) => {
          requestAnimationFrame(() => requestAnimationFrame(() => {
            const src = document.getElementById('field');
            const w = 64, h = 40;
            const c = document.createElement('canvas');
            c.width = w; c.height = h;
            const g = c.getContext('2d', { willReadFrequently: true });
            g.drawImage(src, 0, 0, w, h);
            const d = g.getImageData(0, 0, w, h).data;
            const px = []; let lit = 0;
            for (let i = 0; i < d.length; i += 4) {
              const l = 0.2126 * d[i] + 0.7152 * d[i + 1] + 0.0722 * d[i + 2];
              px.push(l);
              if (l > 8) lit++;
            }
            resolveP({ lit, total: w * h, px });
          }));
        }));
        await page.waitForTimeout(1200); // first frames + reveal settle
        const s0 = await sample();
        await page.evaluate(() => window.scrollTo(0, innerHeight * 2));
        await page.waitForTimeout(1600); // camera damping settle
        const s1 = await sample();
        ok(s0.lit / s0.total > 0.005, `hero frame lit (${s0.lit}/${s0.total} px)`);
        ok(s1.lit / s1.total > 0.005, `scrolled frame lit (${s1.lit}/${s1.total} px)`);
        const diff = s0.px.reduce((a, v, i) => a + Math.abs(v - s1.px[i]), 0) / s0.px.length;
        ok(diff > 1.5, `scroll changes the scene (mean |Δ| = ${diff.toFixed(2)})`);
        ok(errors.length === 0, `no console/page errors${errors.length ? ` — got: ${errors.join(' | ').slice(0, 300)}` : ''}`);
      }
    } catch (e) {
      ok(false, `pass aborted: ${e.message}`);
    } finally {
      if (ctx) await ctx.close().catch(() => {});
    }
  }
```

Also update the header comment (line 3–6) to mention pass 4:

```js
 * check-landing.mjs — smoke-test a BUILT landing directory (index.html +
 * assets/). Asserts: title, every manifest deck link, JS boot (js class),
 * scene-or-fallback gating (field-on | static-bg), reveal-on-scroll, the
 * reduced-motion fallback, zero console/page errors, and (with ?qa +
 * preserveDrawingBuffer) that the WebGL scene renders non-blank pixels that
 * change with scroll.
```

- [ ] **Step 2: Run — expect pass**

```bash
node scripts/check-landing.mjs .qa-dist/__landing__
```

Expected: `✅ landing check passed.` including three `✓` lines from pass 4 (lit ×2, scene-diff).

- [ ] **Step 3: Mutation check — verify the pass can fail**

Temporarily comment out `renderer.render(scene, camera);` in `sim.js`'s `frame()` (the main render, NOT the sim passes), rebuild, rerun:

```bash
node scripts/build-landing.mjs --out .qa-dist/__landing__ && node scripts/check-landing.mjs .qa-dist/__landing__
```

Expected: pass 4 FAILS both `hero frame lit` and `scrolled frame lit` (the canvas stays transparent). If it doesn't fail, the sampling is broken — stop and fix before proceeding. Then restore the line, rebuild, rerun, expect pass.

- [ ] **Step 4: Full QA + commit**

Run the complete gate once (builds all decks too — slow but it is *the* test):

```bash
pnpm qa
```

Expected: `✅ All 16 deck(s) + landing pass QA.` (deck builds are untouched by this feature; failures there are pre-existing and out of scope — report them, don't fix here).

```bash
git add scripts/check-landing.mjs
git commit -m "test(landing): QA pixel pass — scene renders and changes with scroll (?qa sampling)"
```

---

## Self-review notes

- **Spec coverage:** 3D sim (Task 1), depth fog (Task 1), pointer-plane wake (Task 1 — realized as view-perpendicular plane through the core, the working generalization of the spec's z=0 plane), core + relays (Task 2), mobile node budget (Task 2, `coarse ? 80 : 160`), 3 fibers/billboard/anchors/pulses-inward (Task 3), burst→core handoff (Task 3), orbit/dolly/damping/no-roll/calm-state (Task 4), FPS-guard + fallbacks untouched (Tasks 1–2 keep both stages; DOM/CSS untouched throughout), QA extension (Task 5), acceptance criteria 1–5 (Task 4 step 3 + Task 5).
- **Type consistency:** `addCore` returns `{ update, flashAt, anchorNode, nodeWorld, setPixelRatio }` — used exactly so in Tasks 3–4. `addFibers.update(elapsed, pointerWorld, getAnchor)` and `burst() → { fiberIdx, anchorDir, arriveIn }` — wired identically in Task 3 step 2. `createRig → { setScroll(y), update(dt) }` — used so in Task 4 step 2. `uImpulse.w` = strength everywhere (decay line updated in Task 1).
- **Known intentional roughness:** fibers render with stale `uA/uB` during Task 1 only (invisible, smoke test doesn't assert them); framing constants are tuned by screenshot in Task 4 step 4 within listed ranges.
