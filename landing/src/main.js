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
