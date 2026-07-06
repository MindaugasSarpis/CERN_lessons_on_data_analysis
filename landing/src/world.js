import { Vector3 } from 'three';

// Shared world-space constants — the one source of truth for scene layout.
// The core sits right-of-center (the hero title is left-aligned) and slightly
// above the hero's vertical middle. BOUNDS is the particle wrap box; it must
// contain the camera rig's full orbit (max radius 20 around CORE_CENTER).
export const CORE_CENTER = new Vector3(3.2, 1.2, 0);
export const CORE_RADIUS = 2.5;
export const BOUNDS = new Vector3(24, 14, 24);
