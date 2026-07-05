import '@fontsource/space-grotesk/400.css';
import '@fontsource/space-grotesk/500.css';
import '@fontsource/space-grotesk/700.css';
import './style.css';

const html = document.documentElement;
html.classList.add('js');

const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

function webgl2Ok() {
  try {
    const gl = document.createElement('canvas').getContext('webgl2');
    return !!gl && (gl.getExtension('EXT_color_buffer_float') !== null
      || gl.getExtension('EXT_color_buffer_half_float') !== null);
  } catch { return false; }
}

if (reduced || !webgl2Ok()) {
  html.classList.add('static-bg');
} else {
  // Task 5 replaces this stub with the particle scene boot.
  html.classList.add('field-on');
}

// Scroll reveal — .reveal elements are hidden by CSS only under .js; observer
// flips them to .in as they enter. Under reduced motion CSS forces visibility,
// but add .in anyway so state stays consistent.
const revealEls = document.querySelectorAll('.reveal');
if (reduced || !('IntersectionObserver' in window)) {
  revealEls.forEach((el) => el.classList.add('in'));
} else {
  const io = new IntersectionObserver((entries) => {
    for (const e of entries) if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
  revealEls.forEach((el) => io.observe(el));
}
