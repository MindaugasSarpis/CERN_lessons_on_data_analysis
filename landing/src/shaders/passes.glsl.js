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

// Velocity update: ambient curl drift + cursor wake + hover impulse + damping.
export const VEL_FRAG = /* glsl */ `
uniform sampler2D uPos, uVel;
uniform float uDt, uTime;
uniform vec2 uPointer, uPointerVel;
uniform vec4 uImpulse;   // x,y = world pos; z = strength; w = radius^2
varying vec2 vUv;
${NOISE}
vec2 curl(vec3 p) {
  const float e = 0.35;
  float dy = snoise(p + vec3(0.0, e, 0.0)) - snoise(p - vec3(0.0, e, 0.0));
  float dx = snoise(p + vec3(e, 0.0, 0.0)) - snoise(p - vec3(e, 0.0, 0.0));
  return vec2(dy, -dx) / (2.0 * e);
}
void main() {
  vec4 pos = texture2D(uPos, vUv);
  vec2 v = texture2D(uVel, vUv).xy;
  // ambient drift
  v += curl(vec3(pos.xy * 0.16, pos.z * 0.2 + uTime * 0.05)) * 0.55 * uDt;
  // cursor wake: drag particles along the pointer's velocity, gaussian falloff
  vec2 toP = pos.xy - uPointer;
  v += uPointerVel * exp(-dot(toP, toP) / 2.2) * 0.9 * uDt;
  // hover impulse: radial push, decays JS-side via uImpulse.z
  vec2 toI = pos.xy - uImpulse.xy;
  float di = length(toI) + 1e-4;
  v += (toI / di) * uImpulse.z * exp(-di * di / uImpulse.w) * uDt;
  // frame-rate-independent damping + speed clamp
  v *= exp(-1.6 * uDt);
  float sp = length(v);
  if (sp > 3.0) v *= 3.0 / sp;
  gl_FragColor = vec4(v, 0.0, 1.0);
}`;

// Position update: integrate + toroidal wrap inside uBounds.
export const POS_FRAG = /* glsl */ `
uniform sampler2D uPos, uVel;
uniform float uDt;
uniform vec2 uBounds;
varying vec2 vUv;
void main() {
  vec4 pos = texture2D(uPos, vUv);
  vec2 v = texture2D(uVel, vUv).xy;
  vec2 p = pos.xy + v * uDt;
  p = mod(p + uBounds, 2.0 * uBounds) - uBounds;
  gl_FragColor = vec4(p, pos.zw);
}`;

// Points: position.xy carries the sim-texture ref UV.
export const RENDER_VERT = /* glsl */ `
uniform sampler2D uPos, uVel;
uniform float uSize, uPixelRatio;
varying float vAlpha;
varying vec3 vColor;
void main() {
  vec2 ref = position.xy;
  vec4 pos = texture2D(uPos, ref);
  vec2 vel = texture2D(uVel, ref).xy;
  float seed = pos.w;
  vec4 mv = modelViewMatrix * vec4(pos.xyz, 1.0);
  gl_Position = projectionMatrix * mv;
  gl_PointSize = uSize * uPixelRatio * mix(0.5, 1.6, fract(seed * 7.31)) * (12.0 / -mv.z);
  float sp = clamp(length(vel) * 0.9, 0.0, 1.0);
  vColor = mix(vec3(0.30, 0.55, 0.72), vec3(0.98, 0.99, 1.0), sp);  // dim cyan -> white by speed
  vAlpha = mix(0.25, 0.9, sp) * mix(0.4, 1.0, fract(seed * 3.17));
}`;

export const RENDER_FRAG = /* glsl */ `
varying float vAlpha;
varying vec3 vColor;
void main() {
  float d = length(gl_PointCoord - 0.5);
  float a = smoothstep(0.5, 0.05, d) * vAlpha;
  gl_FragColor = vec4(vColor * a, a);
}`;
