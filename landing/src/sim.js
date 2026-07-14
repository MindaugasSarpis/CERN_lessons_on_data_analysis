import {
  WebGLRenderer, Scene, PerspectiveCamera, OrthographicCamera, Mesh, Points,
  PlaneGeometry, BufferGeometry, BufferAttribute, ShaderMaterial, DataTexture,
  WebGLRenderTarget, RGBAFormat, FloatType, HalfFloatType, NearestFilter,
  AdditiveBlending, Vector2, Vector3, Vector4, Clock,
} from 'three';
import { SIM_VERT, COPY_FRAG, VEL_FRAG, POS_FRAG, RENDER_VERT, RENDER_FRAG } from './shaders/passes.glsl.js';
import { addFibers } from './fiber.js';
import { addCore } from './core.js';
import { addCollisions } from './collisions.js';
import { createRig } from './rig.js';
import { CORE_CENTER, BOUNDS } from './world.js';

const FOV = 55, MAX_DT = 1 / 30;

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
  const rig = createRig(camera);
  if (qa) window.__qaCam = camera.position; // live ref; QA reads it after scrolling

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
      uBurst: { value: new Vector4(999, 999, 999, 0) },
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
  const core = addCore(scene, { coarse });
  core.setPixelRatio(baseDpr);
  const collisions = addCollisions(scene, { coarse });
  collisions.setPixelRatio(baseDpr);
  if (qa) window.__qaCollide = () => {
    const p = collisions.spawnNow(camera);
    velMat.uniforms.uBurst.value.set(p.x, p.y, p.z, 22);
  };
  if (qa) window.__qaElapsed = () => elapsed;

  const anchorIdx = new Map(); // fiberIdx -> core node idx (resolved lazily)
  const getAnchor = (fiberIdx, anchorDir, out) => {
    if (!anchorIdx.has(fiberIdx)) anchorIdx.set(fiberIdx, core.anchorNode(anchorDir));
    core.nodeWorld(anchorIdx.get(fiberIdx), out);
  };
  const arrivals = []; // { at, node } — burst pulses in flight toward the core

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
  const burst = velMat.uniforms.uBurst.value;

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
    rig.setScroll(window.scrollY || 0);
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

    rig.update(dt);

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

    core.update(elapsed);
    fibers.update(elapsed, velMat.uniforms.uPointer.value, getAnchor);
    const ev = collisions.update(elapsed, camera);
    if (ev) burst.set(ev.x, ev.y, ev.z, 22); // kick the field at the vertex
    burst.w *= 0.9;
    for (let i = arrivals.length - 1; i >= 0; i--) {
      if (elapsed >= arrivals[i].at) {
        core.flashAt(arrivals[i].node);
        arrivals.splice(i, 1);
      }
    }
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
            core.setPixelRatio(baseDpr * 0.7);
            collisions.setPixelRatio(baseDpr * 0.7);
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
      const b = fibers.burst();
      arrivals.push({ at: elapsed + b.arriveIn, node: anchorIdx.get(b.fiberIdx) ?? core.anchorNode(b.anchorDir) });
    },
    onScroll(y) { scrollY = y; rig.setScroll(y); },
    setPaused(p) {
      if (p === paused) return;
      paused = p;
      if (p) cancelAnimationFrame(raf);
      else { clock.getDelta(); frame(); }
    },
  };
}
