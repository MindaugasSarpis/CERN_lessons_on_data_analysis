import { Vector3 } from 'three';
import { CORE_CENTER } from './world.js';

// Scroll-driven orbital camera. Spherical path around CORE_CENTER: azimuth
// sweeps ~140° while the radius dollies 10→20 and elevation rises 2°→14°,
// over the first 1.5 viewport-heights of scroll (smoothstep-eased). The
// look-at starts beside the core (framing it right-of-center behind the
// left-aligned hero title) and sinks below it as we pull out, drifting the
// core into the upper third. Past p=1: slow azimuth creep + gentle descent
// (the calm state behind the lecture list). The camera chases its target
// with exponential damping so wheel steps / touch momentum never snap.
// No roll, ever; scroll is the only input.

const D2R = Math.PI / 180;
const R0 = 10, R1 = 20;
const AZI0 = -18 * D2R, AZI1 = 122 * D2R;
const EL0 = 2 * D2R, EL1 = 14 * D2R;
const SCROLL_VH = 1.5;      // choreography span, in viewport heights
const LOOK_ASIDE = 3.5;     // p=0: look this far left of the core → core sits right
const LOOK_DROP = 3.4;      // p=1: look this far below the core → core sits high
const CREEP = 3e-5;         // rad of azimuth per px past p=1
const DESCEND = 0.003;      // world units per px past p=1 (gentle drift)
const DAMP = 6;             // 1/s → k ≈ 0.1/frame at 60fps

const smooth = (t) => t * t * (3 - 2 * t);

export function createRig(camera) {
  let p = 0, over = 0, fresh = true;
  let azi = AZI0, r = R0, el = EL0, aside = LOOK_ASIDE, drop = 0, sink = 0;
  const pos = new Vector3(), look = new Vector3();

  return {
    setScroll(y) {
      const span = Math.max(innerHeight * SCROLL_VH, 1);
      p = smooth(Math.min(Math.max(y / span, 0), 1));
      // cap: the calm-state drift must stay bounded no matter how long the
      // page grows (sink ≤ 12 world units, creep ≤ ~7°)
      over = Math.min(Math.max(y - span, 0), 4000);
    },
    update(dt) {
      // first update snaps to the scroll target (mid-page reloads must not
      // replay the orbit); damping applies from the second frame on
      const k = fresh ? 1 : 1 - Math.exp(-DAMP * dt);
      fresh = false;
      azi += (AZI0 + (AZI1 - AZI0) * p + over * CREEP - azi) * k;
      r += (R0 + (R1 - R0) * p - r) * k;
      el += (EL0 + (EL1 - EL0) * p - el) * k;
      aside += (LOOK_ASIDE * (1 - p) - aside) * k;
      drop += (LOOK_DROP * p - drop) * k;
      sink += (over * DESCEND - sink) * k;
      pos.set(
        CORE_CENTER.x + r * Math.cos(el) * Math.sin(azi),
        CORE_CENTER.y + r * Math.sin(el) - sink,
        CORE_CENTER.z + r * Math.cos(el) * Math.cos(azi),
      );
      look.set(CORE_CENTER.x - aside, CORE_CENTER.y - drop - sink, CORE_CENTER.z);
      camera.position.copy(pos);
      camera.lookAt(look);
      camera.updateMatrixWorld();
    },
  };
}
