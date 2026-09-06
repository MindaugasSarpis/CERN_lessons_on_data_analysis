// Landing sounds, synthesised with Web Audio (no assets, no licences,
// deterministic). Two voices:
//
//   playHum()    — a low drone that swells in, holds, and fades out over ~8 s:
//                  the "machine waking up" moment under the particle intro.
//                  Two detuned sawtooths on a 55 Hz fundamental (the beat
//                  between them is the movement) plus a sine an octave up so
//                  small laptop speakers, which reproduce little below ~150 Hz,
//                  still hear it; all through a resonant low-pass whose cutoff
//                  opens with the swell and breathes on a slow LFO.
//   playSwoosh() — a ~0.32 s low whoosh under the exit fade when a lecture row
//                  is clicked: white noise through a resonant low-pass that
//                  sweeps up then down, fast attack / exponential release.
//
// Autoplay policy: browsers keep an AudioContext suspended until the page has
// seen a click, tap, or key press (hover and scroll don't count). warmAudio()
// is called from those gestures in main.js: it creates the context once and
// resumes it, so a sound scheduled later starts without the audio device's
// open latency (a cold device can take longer than the exit fade). Nodes are
// scheduled against ctx.currentTime, which does not advance while suspended,
// so a sound scheduled before the unlock plays intact from the unlock.
//
// Every failure path returns { played: false } quietly: the landing smoke
// test asserts zero console errors, and a rejected resume() would log one.
// There is no prefers-reduced-sound media query — main.js decides (it plays
// nothing under reduced motion).

let ctx = null;
let noise = null;

function getContext() {
  if (ctx) return ctx;
  const AC = window.AudioContext || window.webkitAudioContext;
  if (!AC) return null;
  try { ctx = new AC(); } catch { return null; }
  return ctx;
}

// Create the context (if needed) and ask it to run. Idempotent; call from a
// user gesture. Returns the context or null when Web Audio is unavailable.
export function warmAudio() {
  const ac = getContext();
  if (ac && ac.state !== 'running') { try { ac.resume().catch(() => {}); } catch { /* noop */ } }
  return ac;
}

// ---------------------------------------------------------------- hum ----
const HUM_F0 = 55;          // Hz, fundamental (A1)
const HUM_DETUNE = 7;       // cents between the two saws → slow beating
const HUM_PEAK = 0.12;      // master gain; output peaks near -12 dBFS
const HUM_ATTACK = 1.5;     // s, swell
const HUM_HOLD = 4.5;       // s, end of the plateau
const HUM_END = 8.0;        // s, -40 dB
const HUM_CUT_LO = 90;      // Hz, cutoff closed (start / tail)
const HUM_CUT_HI = 320;     // Hz, cutoff open (plateau)
const HUM_LFO_HZ = 0.25;    // cutoff breathing rate
const HUM_LFO_DEPTH = 40;   // Hz, ± on the cutoff
const HUM_Q = 1.8;

export function playHum() {
  const ac = getContext();
  if (!ac) return { played: false, reason: 'no-webaudio' };
  try {
    const t0 = ac.currentTime;
    const sawA = ac.createOscillator();
    sawA.type = 'sawtooth'; sawA.frequency.value = HUM_F0;
    const sawB = ac.createOscillator();
    sawB.type = 'sawtooth'; sawB.frequency.value = HUM_F0; sawB.detune.value = HUM_DETUNE;
    const octave = ac.createOscillator();
    octave.type = 'sine'; octave.frequency.value = HUM_F0 * 2;
    const octaveGain = ac.createGain();
    octaveGain.gain.value = 0.35;

    const filter = ac.createBiquadFilter();
    filter.type = 'lowpass';
    filter.Q.value = HUM_Q;
    filter.frequency.setValueAtTime(HUM_CUT_LO, t0);
    filter.frequency.exponentialRampToValueAtTime(HUM_CUT_HI, t0 + HUM_ATTACK + 1.0);
    filter.frequency.setValueAtTime(HUM_CUT_HI, t0 + HUM_HOLD);
    filter.frequency.exponentialRampToValueAtTime(HUM_CUT_LO, t0 + HUM_END);

    const lfo = ac.createOscillator();
    lfo.type = 'sine'; lfo.frequency.value = HUM_LFO_HZ;
    const lfoGain = ac.createGain();
    lfoGain.gain.value = HUM_LFO_DEPTH;
    lfo.connect(lfoGain).connect(filter.frequency);

    const master = ac.createGain();
    master.gain.setValueAtTime(0.0001, t0);
    master.gain.linearRampToValueAtTime(HUM_PEAK, t0 + HUM_ATTACK);
    master.gain.setValueAtTime(HUM_PEAK, t0 + HUM_HOLD);
    master.gain.exponentialRampToValueAtTime(HUM_PEAK * 0.01, t0 + HUM_END);
    master.gain.linearRampToValueAtTime(0, t0 + HUM_END + 0.05);

    sawA.connect(filter); sawB.connect(filter);
    octave.connect(octaveGain).connect(filter);
    filter.connect(master).connect(ac.destination);

    const stopAt = t0 + HUM_END + 0.1;
    for (const o of [sawA, sawB, octave, lfo]) { o.start(t0); o.stop(stopAt); }
    sawA.onended = () => {
      try { for (const n of [sawA, sawB, octave, octaveGain, lfo, lfoGain, filter, master]) n.disconnect(); } catch { /* noop */ }
    };
    return { played: true, state: ac.state };
  } catch (e) {
    return { played: false, reason: String(e && e.message || e) };
  }
}

// ------------------------------------------------------------- swoosh ----
// PEAK is the pre-filter gain: the low-pass keeps only a few % of white
// noise's power, so 0.7 here lands the OUTPUT peak near -13 dBFS (~0.23
// linear) — a cushion, not an effect. Rendered offline via
// OfflineAudioContext to check; re-measure if you retune the filter.
const PEAK = 0.7;
const ATTACK = 0.06;      // s to peak
const LENGTH = 0.34;      // s to -40 dB; the nav at 320 ms cuts nothing audible
const FLOOR = 0.01;       // release target, relative to PEAK (-40 dB)
const F_START = 160;      // Hz, cutoff at t=0 (dark)
const F_TOP = 900;        // Hz, cutoff at the crest of the sweep
const F_END = 120;        // Hz, cutoff at the tail (drops "low")
const Q = 1.4;            // resonance: a hint of "voice" on the sweep

function getNoise(ac) {
  if (noise) return noise;
  const n = Math.ceil(ac.sampleRate * (LENGTH + 0.05));
  const buf = ac.createBuffer(1, n, ac.sampleRate);
  const d = buf.getChannelData(0);
  for (let i = 0; i < n; i++) d[i] = Math.random() * 2 - 1;
  noise = buf;
  return noise;
}

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
    gain.gain.exponentialRampToValueAtTime(PEAK * FLOOR, t0 + LENGTH);
    gain.gain.linearRampToValueAtTime(0, t0 + LENGTH + 0.02); // no click at stop

    src.connect(filter).connect(gain).connect(ac.destination);
    src.start(t0);
    src.stop(t0 + LENGTH + 0.03);
    src.onended = () => { try { src.disconnect(); filter.disconnect(); gain.disconnect(); } catch { /* noop */ } };
    return { played: true, state: ac.state };
  } catch (e) {
    return { played: false, reason: String(e && e.message || e) };
  }
}
