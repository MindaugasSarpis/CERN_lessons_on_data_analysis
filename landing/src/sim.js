import {
  WebGLRenderer, Scene, PerspectiveCamera, OrthographicCamera, Mesh, Points,
  PlaneGeometry, BufferGeometry, BufferAttribute, ShaderMaterial, DataTexture,
  WebGLRenderTarget, RGBAFormat, FloatType, HalfFloatType, NearestFilter,
  AdditiveBlending, Vector2, Vector4, Clock,
} from 'three';
import { SIM_VERT, COPY_FRAG, VEL_FRAG, POS_FRAG, RENDER_VERT, RENDER_FRAG } from './shaders/passes.glsl.js';

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
  let renderer;
  try {
    renderer = new WebGLRenderer({ canvas, alpha: true, antialias: false, powerPreference: 'high-performance' });
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

  // --- camera / world extents ---
  const camera = new PerspectiveCamera(FOV, 1, 0.1, 100);
  camera.position.z = CAM_Z;
  const halfH = Math.tan((FOV / 2) * (Math.PI / 180)) * CAM_Z;
  let halfW = halfH; // set in resize()
  const bounds = new Vector2(1, 1);

  // --- sim targets (ping-pong pos + vel) ---
  const rt = () => new WebGLRenderTarget(size, size, {
    type, format: RGBAFormat, minFilter: NearestFilter, magFilter: NearestFilter,
    depthBuffer: false, stencilBuffer: false,
  });
  let posA = rt(), posB = rt(), velA = rt(), velB = rt();

  // --- initial positions: random in bounds-ish box, z in [-4,4], w = seed ---
  const init = new Float32Array(count * 4);
  for (let i = 0; i < count; i++) {
    init[i * 4 + 0] = (Math.random() * 2 - 1) * halfH * 2.4; // x (re-wrapped by sim)
    init[i * 4 + 1] = (Math.random() * 2 - 1) * halfH * 1.9; // y
    init[i * 4 + 2] = (Math.random() * 2 - 1) * 4;           // z (static parallax depth)
    init[i * 4 + 3] = Math.random();                         // seed
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
      uPointer: { value: new Vector2(999, 999) }, uPointerVel: { value: new Vector2(0, 0) },
      uImpulse: { value: new Vector4(999, 999, 0, 1.4) },
    },
  });
  const posMat = new ShaderMaterial({
    vertexShader: SIM_VERT, fragmentShader: POS_FRAG,
    uniforms: { uPos: { value: null }, uVel: { value: null }, uDt: { value: 0 }, uBounds: { value: bounds } },
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
    uniforms: { uPos: { value: null }, uVel: { value: null }, uSize: { value: 1.5 }, uPixelRatio: { value: baseDpr } },
  });
  const points = new Points(geo, renderMat);
  points.frustumCulled = false;
  const scene = new Scene();
  scene.add(points);

  // --- pointer state (world-space); Task 6 feeds client coords ---
  const ptrClient = new Vector2(-1e4, -1e4);
  const ptrWorld = new Vector2(999, 999);
  const ptrPrev = new Vector2(999, 999);
  const ptrVel = new Vector2(0, 0);
  let hasPointer = false, lastPointerAt = 0;
  let scrollY = window.scrollY || 0;
  const impulse = velMat.uniforms.uImpulse.value;

  const toWorld = (cx, cy, out) => out.set(
    ((cx / innerWidth) * 2 - 1) * halfW,
    -((cy / innerHeight) * 2 - 1) * halfH + camera.position.y,
  );

  function resize() {
    renderer.setSize(innerWidth, innerHeight);
    camera.aspect = innerWidth / innerHeight;
    camera.updateProjectionMatrix();
    halfW = halfH * camera.aspect;
    bounds.set(halfW * 1.3, halfH * 1.9);
  }
  addEventListener('resize', resize, { passive: true });
  resize();

  // seed sim state: positions from initTex, velocities cleared to zero
  pass(copyMat, posA);
  renderer.setRenderTarget(velA);
  renderer.clear(true, false, false);
  renderer.setRenderTarget(null);

  // --- loop (visibility pause + fps guard hooks used by Task 6) ---
  const clock = new Clock();
  let raf = 0, paused = false, elapsed = 0;
  // fps guard: after 4s warmup, avg over ~2s windows; degrade at <40fps, twice max
  let guardStage = 0, winFrames = 0, winTime = 0;

  function frame() {
    raf = requestAnimationFrame(frame);
    const dt = Math.min(clock.getDelta(), MAX_DT);
    elapsed += dt;

    // pointer velocity in world units/s (smoothed); idle if no pointer yet
    if (hasPointer) {
      toWorld(ptrClient.x, ptrClient.y, ptrWorld);
      if (dt > 0) {
        ptrVel.set((ptrWorld.x - ptrPrev.x) / dt, (ptrWorld.y - ptrPrev.y) / dt).clampLength(0, 30);
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

    impulse.z *= 0.86; // hover impulse decay

    camera.position.y = -scrollY * PARALLAX * halfH;
    renderMat.uniforms.uPos.value = posA.texture;
    renderMat.uniforms.uVel.value = velA.texture;
    renderer.render(scene, camera);

    if (elapsed > 4 && guardStage < 2) {
      winFrames++; winTime += dt;
      if (winTime >= 2) {
        if (winFrames / winTime < 40) {
          if (guardStage === 0) renderMat.uniforms.uPixelRatio.value = baseDpr * 0.7,
            renderer.setPixelRatio(baseDpr * 0.7);
          else geo.setDrawRange(0, Math.floor(count / 2));
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
      const w = toWorld(cx, cy, new Vector2());
      impulse.set(w.x, w.y, 26, 1.4);
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
