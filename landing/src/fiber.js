import {
  Group, Mesh, BufferGeometry, BufferAttribute, ShaderMaterial,
  AdditiveBlending, Vector2,
} from 'three';
import { NOISE } from './shaders/noise.glsl.js';

// Two persistent glowing "data-link fiber" ribbons. Each is a triangle strip
// whose vertex shader spans uA→uB, undulates the curve with slow simplex
// noise, and offsets vertices along the curve normal. The fragment shader
// draws a bright core + soft glow with a light pulse traveling the fiber.
// The group tracks the camera's y at ~0.9x so the fibers drift gently
// against the scroll but never leave the viewport.

const VERT = /* glsl */ `
uniform vec2 uA, uB;
uniform float uTime, uAmp, uFreq, uSeed, uWidth;
varying float vT, vSide;
varying vec2 vWorld;
${NOISE}
vec2 curve(float t) {
  vec2 p = mix(uA, uB, t);
  p.y += snoise(vec3(t * uFreq, uTime * 0.12, uSeed)) * uAmp;
  p.x += snoise(vec3(t * uFreq * 0.7, uTime * 0.09, uSeed + 31.7)) * uAmp * 0.35;
  return p;
}
void main() {
  float t = position.x;
  float side = position.y;
  vec2 p = curve(t);
  vec2 tang = normalize(curve(min(t + 0.004, 1.0)) - curve(max(t - 0.004, 0.0)));
  p += vec2(-tang.y, tang.x) * side * uWidth;
  vT = t;
  vSide = side;
  vec4 world = modelMatrix * vec4(p, 0.0, 1.0);
  vWorld = world.xy;
  gl_Position = projectionMatrix * viewMatrix * world;
}`;

const FRAG = /* glsl */ `
uniform float uTime, uPulseSpeed, uPhase, uBaseAlpha, uBurstStart;
uniform vec2 uPointer;
varying float vT, vSide;
varying vec2 vWorld;
void main() {
  float core = exp(-vSide * vSide * 9.0);
  float glow = exp(-vSide * vSide * 2.0) * 0.35;
  float p = fract(uTime * uPulseSpeed + uPhase);
  float d = abs(vT - p);
  d = min(d, 1.0 - d);
  float pulse = exp(-(d * d) / 0.0009);
  // hover burst: an extra one-shot pulse launched from the fiber start
  float bp = (uTime - uBurstStart) * 0.55;
  if (bp >= 0.0 && bp <= 1.15) {
    float bd = vT - bp;
    pulse += exp(-(bd * bd) / 0.0011) * 1.3;
  }
  vec2 toP = vWorld - uPointer;
  float near = exp(-dot(toP, toP) / 6.0) * 0.6;
  float ends = smoothstep(0.0, 0.06, vT) * smoothstep(1.0, 0.94, vT);
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
        uA: { value: new Vector2() }, uB: { value: new Vector2() },
        uTime: { value: 0 }, uAmp: { value: cfg.amp }, uFreq: { value: cfg.freq },
        uSeed: { value: cfg.seed }, uWidth: { value: cfg.width },
        uPulseSpeed: { value: cfg.pulseSpeed }, uPhase: { value: cfg.phase },
        uBaseAlpha: { value: cfg.baseAlpha }, uBurstStart: { value: -1e3 },
        uPointer: { value: new Vector2(999, 999) },
      },
    });
    const mesh = new Mesh(geo, mat);
    mesh.position.z = cfg.z;
    mesh.frustumCulled = false;
    group.add(mesh);
    return { mat, cfg };
  };

  // fiber 1: high diagonal behind the hero, brighter; fiber 2: lower,
  // deeper, dimmer, slower pulse, phase-offset so pulses never sync.
  const fibers = [
    make({ amp: 1.1, freq: 2.3, seed: 7.3, width: 0.045, pulseSpeed: 0.09, phase: 0.0, baseAlpha: 0.45, z: -2, aY: 0.55, bY: -0.10 }),
    make({ amp: 1.5, freq: 1.7, seed: 42.0, width: 0.06, pulseSpeed: 0.055, phase: 0.55, baseAlpha: 0.30, z: -5, aY: -0.70, bY: -0.25 }),
  ];
  scene.add(group);

  let lastElapsed = 0;
  let burstIdx = 0;
  return {
    resize(halfW, halfH) {
      for (const { mat, cfg } of fibers) {
        mat.uniforms.uA.value.set(-halfW * 1.4, halfH * cfg.aY);
        mat.uniforms.uB.value.set(halfW * 1.4, halfH * cfg.bY);
      }
    },
    update(elapsed, pointerWorld, camY) {
      lastElapsed = elapsed;
      group.position.y = camY * 0.9;
      for (const { mat } of fibers) {
        mat.uniforms.uTime.value = elapsed;
        mat.uniforms.uPointer.value.copy(pointerWorld);
      }
    },
    // one-shot pulse from the fiber start, alternating fibers per call
    burst() {
      fibers[burstIdx].mat.uniforms.uBurstStart.value = lastElapsed;
      burstIdx = (burstIdx + 1) % fibers.length;
    },
  };
}
