// Exit swoosh — a short, low "whoosh" played when a lecture row is clicked,
// under the 320 ms fade-out in main.js. Synthesised with Web Audio (no asset,
// no licence, deterministic): a burst of white noise through a resonant
// low-pass whose cutoff sweeps up then down, shaped by a fast-attack /
// exponential-release gain envelope. The whole gesture lands in ~0.32 s so
// the navigation that follows never cuts an audible tail.
//
// Autoplay policy: the AudioContext is created lazily INSIDE the click
// handler (a user gesture), which is what unlocks audio on iOS/Safari and
// keeps Chrome from logging "AudioContext was not allowed to start". Every
// failure path returns { played: false } quietly — the landing smoke test
// asserts zero console errors, and a rejected play/resume promise would log
// one. There is no prefers-reduced-sound media query, so the caller decides
// whether to invoke this at all (main.js skips it under reduced motion).

const PEAK = 0.18;        // linear gain; low, a cushion rather than an effect
const ATTACK = 0.06;      // s to peak
const LENGTH = 0.32;      // s total; matches the fade-out window
const F_START = 160;      // Hz, cutoff at t=0 (dark)
const F_TOP = 900;        // Hz, cutoff at the crest of the sweep
const F_END = 120;        // Hz, cutoff at the tail (drops "low")
const Q = 1.4;            // resonance: a hint of "voice" on the sweep

let ctx = null;
let noise = null;

function getContext() {
  if (ctx) return ctx;
  const AC = window.AudioContext || window.webkitAudioContext;
  if (!AC) return null;
  try { ctx = new AC(); } catch { return null; }
  return ctx;
}

function getNoise(ac) {
  if (noise) return noise;
  const n = Math.ceil(ac.sampleRate * LENGTH);
  const buf = ac.createBuffer(1, n, ac.sampleRate);
  const d = buf.getChannelData(0);
  for (let i = 0; i < n; i++) d[i] = Math.random() * 2 - 1;
  noise = buf;
  return noise;
}

// Play the swoosh now. Returns a small record for the ?qa hook.
export function playSwoosh() {
  const ac = getContext();
  if (!ac) return { played: false, reason: 'no-webaudio' };
  try {
    if (ac.state === 'suspended') ac.resume().catch(() => {});
    const t0 = ac.currentTime;
    const src = ac.createBufferSource();
    src.buffer = getNoise(ac);

    const filter = ac.createBiquadFilter();
    filter.type = 'lowpass';
    filter.Q.value = Q;
    filter.frequency.setValueAtTime(F_START, t0);
    filter.frequency.exponentialRampToValueAtTime(F_TOP, t0 + ATTACK * 1.4);
    filter.frequency.exponentialRampToValueAtTime(F_END, t0 + LENGTH);

    const gain = ac.createGain();
    gain.gain.setValueAtTime(0.0001, t0);
    gain.gain.exponentialRampToValueAtTime(PEAK, t0 + ATTACK);
    gain.gain.exponentialRampToValueAtTime(0.0001, t0 + LENGTH);

    src.connect(filter).connect(gain).connect(ac.destination);
    src.start(t0);
    src.stop(t0 + LENGTH + 0.02);
    src.onended = () => { try { src.disconnect(); filter.disconnect(); gain.disconnect(); } catch { /* noop */ } };
    return { played: true, state: ac.state };
  } catch (e) {
    return { played: false, reason: String(e && e.message || e) };
  }
}
