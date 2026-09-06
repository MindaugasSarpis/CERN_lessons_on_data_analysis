import '@fontsource/space-grotesk/400.css';
import '@fontsource/space-grotesk/500.css';
import '@fontsource/space-grotesk/700.css';
import './style.css';
import { createField } from './sim.js';
import { warmAudio, playHum, playSwoosh } from './sound.js';

const html = document.documentElement;
html.classList.add('js');

const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

// Scroll reveal — .reveal elements are hidden by CSS only under .js; observer
// flips them to .in as they enter. Under reduced motion CSS forces visibility,
// but add .in anyway so state stays consistent. This runs before the WebGL
// boot below so content reveal never depends on — and can't be blocked by —
// the scene boot throwing.
const revealEls = document.querySelectorAll('.reveal');
if (reduced || !('IntersectionObserver' in window)) {
  revealEls.forEach((el) => el.classList.add('in'));
} else {
  const io = new IntersectionObserver((entries) => {
    for (const e of entries) if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
  revealEls.forEach((el) => io.observe(el));
}

function webgl2Ok() {
  try {
    const gl = document.createElement('canvas').getContext('webgl2');
    const result = !!gl && (gl.getExtension('EXT_color_buffer_float') !== null
      || gl.getExtension('EXT_color_buffer_half_float') !== null);
    gl?.getExtension('WEBGL_lose_context')?.loseContext();
    return result;
  } catch { return false; }
}

let field = null;
if (reduced || !webgl2Ok()) {
  html.classList.add('static-bg');
} else {
  try {
    field = createField(document.getElementById('field'));
  } catch {
    field = null;
  }
  html.classList.add(field ? 'field-on' : 'static-bg');
}

if (field) {
  addEventListener('pointermove', (e) => field.onPointer(e.clientX, e.clientY), { passive: true });
  addEventListener('scroll', () => field.onScroll(window.scrollY), { passive: true });
  document.querySelectorAll('a.row').forEach((a) =>
    a.addEventListener('pointerenter', (e) => field.onImpulse(e.clientX, e.clientY)));
  document.addEventListener('visibilitychange', () => field.setPaused(document.hidden));
}

// Sound (sound.js). Browsers keep audio blocked until the page has seen a
// click, tap, or key press — hover and scroll don't count — so nothing here
// can play on a cold open by itself. ?qa records each result in
// sessionStorage (survives the row-click navigation) for check-landing.mjs.
// Reduced motion plays nothing: those visitors get the static page.
const qa = new URLSearchParams(location.search).has('qa');
const qaRecord = (key, value) => {
  if (!qa) return;
  try { sessionStorage.setItem(key, JSON.stringify(value)); } catch { /* noop */ }
};

// Low hum — the "machine waking up" drone (~8 s, once per visit). It starts on
// the first activation gesture that is not on a lecture row (rows navigate and
// keep the short swoosh). Every gesture also warms the AudioContext, so a
// swoosh scheduled on a later row click starts without the audio device's
// open latency. Arriving from a deck via a link, the browser carries the
// activation across the same-origin navigation, so the hum is scheduled on
// open; if it turns out blocked, the scheduled nodes simply play from the
// first gesture instead (a suspended context's clock does not advance).
let hummed = false;
const hum = (via) => {
  if (hummed || reduced) return;
  hummed = true;
  qaRecord('qaHum', { ...playHum(), via });
};
if (!reduced) {
  const onGesture = (e) => {
    if (e.type === 'keydown' && (e.key === 'Escape' || e.repeat)) return;
    warmAudio();
    if (e.target && e.target.closest && e.target.closest('a.row')) return;
    hum('gesture');
  };
  // pointerup too: for touch, activation is granted on the release, not the press.
  for (const type of ['pointerdown', 'pointerup', 'keydown']) {
    addEventListener(type, onGesture, { capture: true, passive: true });
  }
  let sameOrigin = false;
  try { sameOrigin = !!document.referrer && new URL(document.referrer).origin === location.origin; } catch { /* noop */ }
  if (sameOrigin) { warmAudio(); hum('load'); }
}

// Row navigation polish — independent of the WebGL field:
// hover prefetches the deck's entry HTML; a plain left-click plays a short
// low swoosh and fades the page out before navigating (modified clicks keep
// browser defaults).
const prefetched = new Set();
document.querySelectorAll('a.row').forEach((a) => {
  a.addEventListener('pointerenter', () => {
    if (prefetched.has(a.href)) return;
    prefetched.add(a.href);
    const link = document.createElement('link');
    link.rel = 'prefetch';
    link.href = a.href;
    document.head.appendChild(link);
  });
  a.addEventListener('click', (e) => {
    if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button !== 0) return;
    e.preventDefault();
    qaRecord('qaSwoosh', reduced ? { played: false, reason: 'reduced-motion' } : playSwoosh());
    html.classList.add('leaving');
    setTimeout(() => { location.href = a.href; }, reduced ? 0 : 320);
  });
});
