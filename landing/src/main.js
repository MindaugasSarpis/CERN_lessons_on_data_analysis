import '@fontsource/space-grotesk/400.css';
import '@fontsource/space-grotesk/500.css';
import '@fontsource/space-grotesk/700.css';
import './style.css';
import { createField } from './sim.js';

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

// Row navigation polish — independent of the WebGL field:
// hover prefetches the deck's entry HTML; a plain left-click fades the page
// out before navigating (modified clicks keep browser defaults).
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
    html.classList.add('leaving');
    setTimeout(() => { location.href = a.href; }, reduced ? 0 : 320);
  });
});
