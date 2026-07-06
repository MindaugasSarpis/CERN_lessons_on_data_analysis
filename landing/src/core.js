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
  gl_PointSize = uPixelRatio * (46.0 + flash * 40.0) / max(-mv.z, 0.1);
  vAlpha = (0.5 + 0.5 * tw) * (0.8 + flash * 2.2);
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
  float base = 0.2;
  float pp = fract(uTime * 0.11 + vPhase);
  float d = abs(vT - pp);
  float pulse = exp(-(d * d) / 0.006);
  // relay: after a flash, a bright front sweeps the edge over ~0.45s, fading
  float on = step(vFlash, uTime);
  float fp = clamp((uTime - vFlash) * 2.2, 0.0, 1.0);
  float fd = abs(vT - fp);
  float relay = on * exp(-(fd * fd) / 0.01) * exp(-(uTime - vFlash) * 1.2) * 2.0;
  float b = base + pulse * 0.75 + relay;
  vec3 col = mix(vec3(0.35, 0.62, 0.78), vec3(1.0), clamp(pulse + relay, 0.0, 1.0));
  gl_FragColor = vec4(col * b, b);
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
