<!--
  TurningSurface — one hill, Maunga Whau (Mt Eden, Auckland), as a shaded
  surface in 3D and as a contour map: the same 87 × 61 heights.

    <TurningSurface class="fig-fill mt-sm" />    on a `class: fill` slide: takes the rest of it
    <TurningSurface mode="map" />                start as the map

  Surface: 86 × 60 quads in SVG, in perspective, drawn far to near (the
  painter's algorithm), coloured by height (viridis) and shaded by a light
  from the upper left of the map. Heights are drawn twice their true scale
  (as R's own demo of the data does), and the figure says so. It turns by
  itself once in `turn-seconds` until the first drag; drag to turn and tilt
  (clamped), double-click or double-tap to reset the view, the button
  pauses the turn. Still, it is drawn in full; while it moves, in full too
  as long as frames keep up, else (below about 30 a second) at every second
  point, 43 × 30 quads. Each quad's shade comes from the mean of its
  corners' normals, so the whole-metre steps of the data do not show as
  noise.

  Map: the surface glides flat and seen from above, then the bands between
  the isolines (each in the colour of its middle height), the isolines
  every 10 m (heavier every 50 m), their heights, and a 100 m bar.

  The text and the colour key have the look of the static figures
  (figures/src/style.py): STIX type in the text colour, the key edged 1 px,
  its ticks pointing in on the side of its labels, minor ticks every 5 m
  (./figure-look/figure-look.css).

  Data: public/data/l07_volcano.json (figures/src/interactive_l07_gallery_data.py
  from figures/data/gallery/volcano.csv): R's `volcano`, digitised by Ross
  Ihaka; isolines and bands by contourpy. In presenter mode the audience window
  follows the presenter's drags and buttons (BroadcastChannel, same browser).
-->
<script>
// Module scope (runs once per page): every TurningSurface shares one fetch.
const files = new Map()
function fetchJSON(url) {
  if (!files.has(url)) {
    const p = fetch(url).then((r) => {
      if (!r.ok) throw new Error(`${url}: HTTP ${r.status}`)
      return r.json()
    })
    p.catch(() => files.delete(url))
    files.set(url, p)
  }
  return files.get(url)
}
const DEG = Math.PI / 180
const SVGNS = 'http://www.w3.org/2000/svg'
// The light: from the upper left of the map, about 40° above the horizon.
const LIGHT = (() => {
  const v = [-1, 1, 1.25]
  const n = Math.hypot(...v)
  return v.map((x) => x / n)
})()
const CAM_DIST = 2400 // m from the centre of the hill: a gentle perspective
const r1 = (v) => Math.round(v * 10) / 10
</script>

<script setup>
import { computed, nextTick, onBeforeUnmount, onMounted, ref, shallowRef, watch } from 'vue'
import { useIsSlideActive, useSlideContext } from '@slidev/client'
import './figure-look/figure-look.css'

const props = defineProps({
  src: { type: String, default: 'data/l07_volcano.json' },
  // 'surface' or 'map' at the start.
  mode: { type: String, default: 'surface' },
  // The view at the start and after a reset, in degrees.
  azimuth: { type: Number, default: -35 },
  elevation: { type: Number, default: 34 },
  // Heights drawn this many times their true scale on the surface.
  exaggeration: { type: Number, default: 2 },
  // Seconds per turn while it turns by itself.
  turnSeconds: { type: Number, default: 40 },
  // Two TurningSurfaces on one slide need different ids (presenter ↔ audience sync).
  syncId: { type: String, default: '' },
})

const EL_MIN = 8
const EL_MAX = 85
const reduceMotion = typeof window !== 'undefined'
  && window.matchMedia?.('(prefers-reduced-motion: reduce)').matches
const clamp = (v, lo, hi) => Math.min(hi, Math.max(lo, v))
const ease = (u) => (u < 0.5 ? 4 * u * u * u : 1 - (-2 * u + 2) ** 3 / 2)

// ---- data: vertices, two meshes, colours ---------------------------------------------------
const D = shallowRef(null)
const loadError = ref('')
let V = null

function hexRGB(h) { return [1, 3, 5].map((k) => parseInt(h.slice(k, k + 2), 16)) }

function buildMesh(d, step, pal) {
  const { rows, cols } = d
  const A = []
  for (let i = 0; i + step <= rows - 1; i += step) {
    for (let j = 0; j + step <= cols - 1; j += step) A.push(i * cols + j, (i + step) * cols + j, (i + step) * cols + j + step, i * cols + j + step)
  }
  const n = A.length / 4
  const corners = Int32Array.from(A)
  const fill = new Array(n)
  for (let q = 0; q < n; q++) {
    const [a, b, c, e] = [corners[4 * q], corners[4 * q + 1], corners[4 * q + 2], corners[4 * q + 3]]
    const h = (V.hs[a] + V.hs[b] + V.hs[c] + V.hs[e]) / 4
    // the mean of the corners' normals: the heights are whole metres, and a
    // quad's own slope would show those 1 m steps as noise
    const nx = V.nx[a] + V.nx[b] + V.nx[c] + V.nx[e]
    const ny = V.ny[a] + V.ny[b] + V.ny[c] + V.ny[e]
    const nz = V.nz[a] + V.nz[b] + V.nz[c] + V.nz[e]
    const lam = Math.max(0, (nx * LIGHT[0] + ny * LIGHT[1] + nz * LIGHT[2]) / Math.hypot(nx, ny, nz))
    const shade = 0.4 + 0.72 * lam
    const rgb = pal[Math.round(((h - d.min) / (d.max - d.min)) * (pal.length - 1))]
    fill[q] = `rgb(${rgb.map((v) => Math.min(255, Math.round(v * shade))).join(',')})`
  }
  return { n, corners, fill, keys: new Float32Array(n), order: new Uint32Array(n), pool: [], has: new Int32Array(n).fill(-1) }
}

function prepare(d) {
  const { rows, cols, spacing } = d
  const N = rows * cols
  V = { xs: new Float32Array(N), ys: new Float32Array(N), hs: new Float32Array(N), N }
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      const k = i * cols + j
      V.xs[k] = (i - (rows - 1) / 2) * spacing
      V.ys[k] = (j - (cols - 1) / 2) * spacing
      V.hs[k] = d.heights[k]
    }
  }
  V.zMid = (d.min + d.max) / 2
  // the normal at each vertex, from the heights 10 m on either side (drawn scale)
  V.nx = new Float32Array(N)
  V.ny = new Float32Array(N)
  V.nz = new Float32Array(N)
  const ex = props.exaggeration
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      const ip = Math.min(rows - 1, i + 1), im = Math.max(0, i - 1)
      const jp = Math.min(cols - 1, j + 1), jm = Math.max(0, j - 1)
      const gx = ((V.hs[ip * cols + j] - V.hs[im * cols + j]) * ex) / ((ip - im) * spacing)
      const gy = ((V.hs[i * cols + jp] - V.hs[i * cols + jm]) * ex) / ((jp - jm) * spacing)
      const L = Math.hypot(gx, gy, 1)
      const k = i * cols + j
      V.nx[k] = -gx / L
      V.ny[k] = -gy / L
      V.nz[k] = 1 / L
    }
  }
  V.PX = new Float32Array(N)
  V.PY = new Float32Array(N)
  V.PD = new Float32Array(N)
  const pal = d.palette.map(hexRGB)
  V.full = buildMesh(d, 1, pal)
  V.coarse = buildMesh(d, 2, pal)
  // every second vertex, for fitting the view
  V.fitIdx = []
  for (let i = 0; i < rows; i += 2) for (let j = 0; j < cols; j += 2) V.fitIdx.push(i * cols + j)
  V.fitCache = new Map()
}

fetchJSON(import.meta.env.BASE_URL + props.src)
  .then((d) => { prepare(d); D.value = d })
  .catch((e) => { loadError.value = String(e.message || e) })
const ready = computed(() => !!D.value)

// ---- the view -----------------------------------------------------------------------------
// az, el (degrees) of the surface view; m: 0 = surface, 1 = map (the glide between).
let az = props.azimuth
let el = clamp(props.elevation, EL_MIN, EL_MAX)
let m = props.mode === 'map' ? 1 : 0
const mapMode = ref(props.mode === 'map')
const spinning = ref(!reduceMotion)
const mapShown = ref(m === 1) // the isolines, once the glide has landed

const box = ref(null)
const svgRef = ref(null)
const fullG = ref(null)
const coarseG = ref(null)
const W = ref(0)
const H = ref(0)
const KEY_W = 96 // room for the colour key at the right
const LEFT_W = 150 // room for the buttons at the left
const PAD = 10

// Projected bounds (focal length 1, centre 0) of the hill seen from (azDeg, elDeg).
function bounds(azDeg, elDeg, ex) {
  const a = azDeg * DEG
  const e = elDeg * DEG
  const ca = Math.cos(a), sa = Math.sin(a), ce = Math.cos(e), se = Math.sin(e)
  let x0 = Infinity, x1 = -Infinity, y0 = Infinity, y1 = -Infinity
  for (const k of V.fitIdx) {
    const X = V.xs[k], Y = V.ys[k], Z = (V.hs[k] - V.zMid) * ex
    const xr = X * ca - Y * sa
    const yr = X * sa + Y * ca
    const dep = yr * ce - Z * se + CAM_DIST
    const px = xr / dep
    const py = (yr * se + Z * ce) / dep
    if (px < x0) x0 = px
    if (px > x1) x1 = px
    if (py < y0) y0 = py
    if (py > y1) y1 = py
  }
  return [x0, x1, y0, y1]
}
// The union of the bounds over a whole turn: the scale does not breathe as it turns.
function turnBounds(elDeg, ex) {
  const key = `${elDeg.toFixed(2)}|${ex.toFixed(3)}`
  let b = V.fitCache.get(key)
  if (!b) {
    b = [Infinity, -Infinity, Infinity, -Infinity]
    for (let k = 0; k < 24; k++) {
      const c = bounds(k * 15, elDeg, ex)
      b = [Math.min(b[0], c[0]), Math.max(b[1], c[1]), Math.min(b[2], c[2]), Math.max(b[3], c[3])]
    }
    if (V.fitCache.size > 400) V.fitCache.clear()
    V.fitCache.set(key, b)
  }
  return b
}

// The camera now: the surface view glides to the map as m goes 0 → 1.
let azFrom = 0 // the azimuth the glide to the map starts from
function camera() {
  const u = ease(m)
  const azMap = Math.round(azFrom / 360) * 360
  const a = m > 0 ? azFrom + (azMap - azFrom) * u : az
  const e = el + (90 - el) * u
  const ex = props.exaggeration * (1 - u)
  const bu = turnBounds(e, ex)
  const bc = bounds(a, e, ex)
  const b = bu.map((v, k) => v + (bc[k] - v) * u)
  const pw = Math.max(40, W.value - KEY_W - LEFT_W - 2 * PAD)
  const ph = Math.max(40, H.value - 2 * PAD)
  const F = 0.97 * Math.min(pw / (b[1] - b[0]), ph / (b[3] - b[2]))
  return {
    ca: Math.cos(a * DEG), sa: Math.sin(a * DEG), ce: Math.cos(e * DEG), se: Math.sin(e * DEG), ex, F,
    cx: LEFT_W + PAD + pw / 2 - (F * (b[0] + b[1])) / 2,
    cy: PAD + ph / 2 + (F * (b[2] + b[3])) / 2,
  }
}

function project(c) {
  const { xs, ys, hs, PX, PY, PD, zMid, N } = V
  for (let k = 0; k < N; k++) {
    const Z = (hs[k] - zMid) * c.ex
    const xr = xs[k] * c.ca - ys[k] * c.sa
    const yr = xs[k] * c.sa + ys[k] * c.ca
    const dep = yr * c.ce - Z * c.se + CAM_DIST
    const s = c.F / dep
    PX[k] = c.cx + xr * s
    PY[k] = c.cy - (yr * c.se + Z * c.ce) * s
    PD[k] = dep
  }
}

// Far to near, then one <path> per quad: the pool of paths is reused, each
// gets the quad at its place in the order (no DOM nodes move).
const EPS = 0.45 // px each corner is pushed outwards, so no seam shows between quads
function paint(mesh, g) {
  const { n, corners, keys, order, pool, has, fill } = mesh
  const { PX, PY, PD } = V
  for (let q = 0; q < n; q++) {
    keys[q] = PD[corners[4 * q]] + PD[corners[4 * q + 1]] + PD[corners[4 * q + 2]] + PD[corners[4 * q + 3]]
    order[q] = q
  }
  order.sort((p, q) => keys[q] - keys[p])
  while (pool.length < n) {
    const p = document.createElementNS(SVGNS, 'path')
    g.appendChild(p)
    pool.push(p)
  }
  for (let k = 0; k < n; k++) {
    const q = order[k]
    const o = 4 * q
    const a = corners[o], b = corners[o + 1], c = corners[o + 2], e = corners[o + 3]
    const mx = (PX[a] + PX[b] + PX[c] + PX[e]) / 4
    const my = (PY[a] + PY[b] + PY[c] + PY[e]) / 4
    let s = ''
    for (let t = 0; t < 4; t++) {
      const v = corners[o + t]
      const dx = PX[v] - mx
      const dy = PY[v] - my
      const L = Math.hypot(dx, dy) || 1
      s += `${t ? 'L' : 'M'}${r1(PX[v] + (dx / L) * EPS)} ${r1(PY[v] + (dy / L) * EPS)}`
    }
    const p = pool[k]
    p.setAttribute('d', `${s}Z`)
    if (has[k] !== q) { p.setAttribute('fill', fill[q]); has[k] = q }
  }
}

// ---- drawing and the clock --------------------------------------------------------------------
const { $page, $renderContext } = useSlideContext()
const isActive = useIsSlideActive()
const live = computed(() => $renderContext?.value === 'slide' || $renderContext?.value === 'presenter')
const thumb = computed(() => $renderContext?.value === 'overview' || $renderContext?.value === 'previewNext')
const stats = { fullMs: 0, fullN: 0, coarseMs: 0, coarseN: 0, slow: false } // read by the tests (svg.__tsfStats)
let shownFull = null // which mesh is on screen
let raf = 0
let last = 0
let dragging = null
let glide = null // a reset of the view: { az0, el0, az1, el1, t0, T }
let morph = null // { from, to, t0, T }

function draw(full) {
  if (!V || !W.value || !fullG.value) return
  const t0 = performance.now()
  project(camera())
  const useFull = full && !thumb.value
  paint(useFull ? V.full : V.coarse, useFull ? fullG.value : coarseG.value)
  if (shownFull !== useFull) {
    fullG.value.style.display = useFull ? '' : 'none'
    coarseG.value.style.display = useFull ? 'none' : ''
    shownFull = useFull
  }
  const ms = performance.now() - t0
  if (useFull) { stats.fullMs += ms; stats.fullN++ } else { stats.coarseMs += ms; stats.coarseN++ }
  stats.slow = slowFull
}
const canSpin = () => spinning.value && isActive.value && live.value && !mapMode.value && m === 0
  && typeof document !== 'undefined' && !document.hidden

function frame(now) {
  raf = 0
  const dt = last ? Math.min(0.1, (now - last) / 1000) : 0
  last = now
  let moving = false
  if (canSpin() && !dragging && !glide) { az = (az + (360 / props.turnSeconds) * dt) % 360; moving = true }
  if (glide) {
    const u = Math.min(1, (now - glide.t0) / glide.T)
    const e = ease(u)
    az = glide.az0 + (glide.az1 - glide.az0) * e
    el = glide.el0 + (glide.el1 - glide.el0) * e
    if (u >= 1) glide = null
    moving = true
  }
  if (morph) {
    const u = Math.min(1, (now - morph.t0) / morph.T)
    m = morph.from + (morph.to - morph.from) * u
    if (u >= 1) { m = morph.to; morph = null; mapShown.value = m === 1 }
    moving = true
  }
  moving = moving || !!dragging
  // In motion the full mesh too, while frames keep up: below about 30 per
  // second it falls back to the mesh of every second point, for good.
  const full = !moving || !slowFull
  draw(full)
  if (moving && full) {
    if (fullAt) {
      const gap = now - fullAt
      fullGap = fullN ? 0.8 * fullGap + 0.2 * gap : gap
      fullN++
      if (fullN > 8 && fullGap > 34) slowFull = true
      stats.fullGap = Math.round(fullGap * 10) / 10
    }
    fullAt = now
  } else fullAt = 0
  if (moving) kick()
  else last = 0
}
let slowFull = false
let fullAt = 0
let fullGap = 0
let fullN = 0
function kick() { if (!raf) raf = requestAnimationFrame(frame) }
watch([ready, W, H], () => nextTick(() => draw(true)))
watch([isActive, live, spinning], () => kick(), { immediate: true })

// ---- pointer: drag to turn and tilt, double-click to reset ---------------------------------------
let lastTap = { t: 0, x: 0, y: 0 }
function onDown(e) {
  if (!ready.value || (e.pointerType === 'mouse' && e.button !== 0)) return
  e.stopPropagation() // no Slidev swipe while turning
  e.preventDefault()
  const now = performance.now()
  if (e.pointerType !== 'mouse' && now - lastTap.t < 350 && Math.hypot(e.clientX - lastTap.x, e.clientY - lastTap.y) < 30) {
    lastTap.t = 0
    resetView()
    return
  }
  lastTap = { t: now, x: e.clientX, y: e.clientY }
  if (mapMode.value || m !== 0) return
  const r = box.value.getBoundingClientRect()
  dragging = { id: e.pointerId, x: e.clientX, y: e.clientY, w: r.width, h: r.height, moved: false }
  e.currentTarget.setPointerCapture(e.pointerId)
  glide = null
}
function onMove(e) {
  if (!dragging || e.pointerId !== dragging.id) return
  const dx = e.clientX - dragging.x
  const dy = e.clientY - dragging.y
  if (!dragging.moved && Math.hypot(dx, dy) < 3) return
  if (!dragging.moved) { dragging.moved = true; spinning.value = false; touched = true }
  dragging.x = e.clientX
  dragging.y = e.clientY
  az = (az - (dx / dragging.w) * 300) % 360
  el = clamp(el + (dy / dragging.h) * 110, EL_MIN, EL_MAX)
  schedulePost()
  kick()
}
function onUp(e) {
  if (!dragging || e.pointerId !== dragging.id) return
  dragging = null
  kick() // the still frame, in full
}
function resetView() {
  if (mapMode.value) return
  touched = true
  const az1 = props.azimuth
  const az0 = az1 + ((((az - az1) % 360) + 540) % 360) - 180 // the short way round
  const el1 = clamp(props.elevation, EL_MIN, EL_MAX)
  if (reduceMotion) { az = az1; el = el1; glide = null } else glide = { az0, el0: el, az1, el1, t0: performance.now(), T: 700 }
  schedulePost()
  kick()
}
function onDblClick(e) {
  e.stopPropagation()
  if (e.pointerType === 'mouse' || e.detail >= 2) resetView()
}

// ---- buttons ---------------------------------------------------------------------------------------
let touched = false
function toggleSpin(e) {
  spinning.value = !spinning.value
  touched = true
  schedulePost()
  kick()
  if (e?.detail) e.currentTarget.blur()
}
function setMap(on, e, quiet) {
  if (e?.detail) e.currentTarget.blur()
  if (mapMode.value === on) return
  mapMode.value = on
  if (!quiet) touched = true
  glide = null
  if (on) azFrom = az
  mapShown.value = false
  if (reduceMotion || !live.value) { m = on ? 1 : 0; mapShown.value = on; morph = null; draw(true); }
  else { morph = { from: m, to: on ? 1 : 0, t0: performance.now(), T: 1300 }; kick() }
  if (!quiet) schedulePost()
}

// ---- the map's isolines, labels and scale bar (the camera of m = 1) ------------------------------------
const mapCam = computed(() => {
  const d = D.value
  if (!d || !W.value) return null
  const saveM = m
  const saveFrom = azFrom
  m = 1
  azFrom = 0
  const c = camera()
  m = saveM
  azFrom = saveFrom
  const s = c.F / CAM_DIST // px per m on the flat map
  const X = (gx) => c.cx + (gx - (d.rows - 1) / 2) * d.spacing * s
  const Y = (gy) => c.cy - (gy - (d.cols - 1) / 2) * d.spacing * s
  return { s, X, Y }
})
// A light line where the palette is dark (low ground), a dark one where it is light.
function lightLine(d, h) {
  const [r, g, b] = hexRGB(d.palette[Math.round(((h - d.min) / (d.max - d.min)) * (d.palette.length - 1))])
  return 0.2126 * r + 0.7152 * g + 0.0722 * b < 110
}
const isolines = computed(() => {
  const d = D.value
  const c = mapCam.value
  if (!d || !c) return []
  return d.contours.map((ct) => ({
    level: ct.level,
    index: ct.level % 50 === 0,
    light: lightLine(d, ct.level),
    d: ct.lines.map((l) => {
      let s = ''
      for (let k = 0; k < l.xy.length; k += 2) s += `${k ? 'L' : 'M'}${r1(c.X(l.xy[k]))} ${r1(c.Y(l.xy[k + 1]))}`
      return l.closed ? `${s}Z` : s
    }).join(''),
  }))
})
// The bands between the isolines, each in the colour of its middle height.
const bands = computed(() => {
  const d = D.value
  const c = mapCam.value
  if (!d || !c) return []
  return d.bands.map((b) => ({
    lo: b.lo,
    fill: d.palette[Math.round((((b.lo + b.hi) / 2 - d.min) / (d.max - d.min)) * (d.palette.length - 1))],
    d: b.rings.map((xy) => {
      let s = ''
      for (let k = 0; k < xy.length; k += 2) s += `${k ? 'L' : 'M'}${r1(c.X(xy[k]))} ${r1(c.Y(xy[k + 1]))}`
      return `${s}Z`
    }).join(''),
  }))
})
// Heights written on every second isoline, along a line from the summit to the lower right.
const isoLabels = computed(() => {
  const d = D.value
  const c = mapCam.value
  if (!d || !c) return []
  let top = 0
  d.heights.forEach((h, k) => { if (h > d.heights[top]) top = k })
  const si = Math.floor(top / d.cols)
  const sj = top % d.cols
  const dir = [1, -0.45]
  const dn = Math.hypot(...dir)
  const out = []
  for (const ct of d.contours) {
    if (ct.level % 20 !== 0 || !ct.lines.length) continue
    const xy = ct.lines[0].xy // the longest line of the level
    let best = -1
    let bestCos = -2
    for (let k = 0; k < xy.length; k += 2) {
      if (xy[k] < 3 || xy[k] > d.rows - 4 || xy[k + 1] < 3 || xy[k + 1] > d.cols - 4) continue // off the edge
      const vx = xy[k] - si
      const vy = xy[k + 1] - sj
      const cos = (vx * dir[0] + vy * dir[1]) / ((Math.hypot(vx, vy) || 1) * dn)
      if (cos > bestCos) { bestCos = cos; best = k }
    }
    const n = xy.length
    const kp = (best - 2 + n) % n
    const kn = (best + 2) % n
    let ang = Math.atan2(c.Y(xy[kn + 1]) - c.Y(xy[kp + 1]), c.X(xy[kn]) - c.X(xy[kp])) / DEG
    if (ang > 90) ang -= 180
    if (ang < -90) ang += 180
    out.push({ level: ct.level, x: c.X(xy[best]), y: c.Y(xy[best + 1]), ang })
  }
  return out
})
const scaleBar = computed(() => {
  const d = D.value
  const c = mapCam.value
  if (!d || !c) return null
  return { x: c.X(2.5), y: c.Y(2.5), w: 100 * c.s }
})

// ---- colour key: the palette from the lowest to the highest point --------------------------------------
const key = computed(() => {
  const d = D.value
  if (!d || !H.value) return null
  const top = 34
  const bottom = H.value - 22
  const y = (h) => bottom - ((h - d.min) / (d.max - d.min)) * (bottom - top)
  const x = W.value - KEY_W + 16
  const LABELS = [100, 120, 140, 160, 180]
  // Ticks pointing in from the side of the labels (style.py): major at the
  // labels, minor every 5 m (Matplotlib's AutoMinorLocator for a step of 20).
  const xr = x + 10
  let major = ''
  let minor = ''
  for (const h of LABELS) major += `M${xr} ${y(h)}h-6.25`
  for (let h = Math.ceil(d.min / 5) * 5; h < d.max; h += 5) {
    if (h > d.min && !LABELS.includes(h)) minor += `M${xr} ${y(h)}h-3.125`
  }
  return {
    x,
    top,
    bottom,
    major,
    minor,
    stops: d.palette.map((col, k) => ({ off: k / (d.palette.length - 1), col })),
    labels: LABELS.map((h) => ({ h, y: y(h) })),
    marks: d.levels.map((h) => ({ h, y: y(h), light: lightLine(d, h) })),
    steps: d.bands.map((b) => ({
      y: y(b.hi),
      h: y(b.lo) - y(b.hi),
      fill: d.palette[Math.round((((b.lo + b.hi) / 2 - d.min) / (d.max - d.min)) * (d.palette.length - 1))],
    })),
  }
})
const gid = `tsf-grad-${Math.random().toString(36).slice(2)}`

// ---- presenter ↔ audience: drags and buttons are posted -----------------------------------------------
const instance = Math.random().toString(36).slice(2)
const syncKey = () => `TurningSurface:${$page.value}:${props.syncId}`
let chan = null
let pending = 0
const state = () => ({ az: Math.round(az * 100) / 100, el: Math.round(el * 100) / 100, map: mapMode.value, spin: spinning.value })
function post(msg) { chan?.postMessage({ key: syncKey(), from: instance, ...msg }) }
function schedulePost() {
  if (!chan || pending) return
  pending = requestAnimationFrame(() => { pending = 0; post({ type: 'state', state: state() }) })
}
function openSync() {
  if (chan || typeof BroadcastChannel === 'undefined' || !live.value) return
  chan = new BroadcastChannel('course-interactive-figures')
  chan.onmessage = ({ data: msg }) => {
    if (!msg || msg.key !== syncKey() || msg.from === instance) return
    if (msg.type === 'state') {
      const s = msg.state
      touched = true
      spinning.value = s.spin
      if (s.map !== mapMode.value) setMap(s.map, null, true)
      if (!s.map) { az = s.az; el = s.el; glide = null }
      kick()
    } else if (msg.type === 'hello' && touched) {
      post({ type: 'state', state: state() })
    }
  }
  post({ type: 'hello' })
}
watch(ready, (r) => { if (r) nextTick(openSync) }, { immediate: true })

let ro = null
onMounted(() => {
  ro = new ResizeObserver(([e]) => {
    W.value = Math.round(e.contentRect.width)
    H.value = Math.round(e.contentRect.height)
  })
  if (box.value) ro.observe(box.value)
  if (svgRef.value) svgRef.value.__tsfStats = stats
})
onBeforeUnmount(() => {
  ro?.disconnect()
  if (raf) cancelAnimationFrame(raf)
  if (pending) cancelAnimationFrame(pending)
  chan?.close()
  chan = null
})
</script>

<template>
  <section class="tsf" :class="{ 'tsf-wait': !ready, 'tsf-map': mapMode }">
    <figure ref="box" class="tsf-plot">
      <svg
        ref="svgRef"
        class="tsf-svg ixf"
        :viewBox="`0 0 ${Math.max(W, 1)} ${Math.max(H, 1)}`"
        :width="Math.max(W, 1)"
        :height="Math.max(H, 1)"
        role="img"
        :aria-label="mapMode ? 'Maunga Whau as a contour map, isolines every 10 metres' : 'Maunga Whau as a shaded surface, heights 94 to 195 metres, drawn twice their true scale'"
        :style="{ cursor: mapMode ? 'default' : 'grab' }"
        @pointerdown="onDown"
        @pointermove="onMove"
        @pointerup="onUp"
        @pointercancel="onUp"
        @dblclick="onDblClick"
      >
        <defs v-if="key">
          <linearGradient :id="gid" x1="0" y1="1" x2="0" y2="0">
            <stop v-for="s in key.stops" :key="s.off" :offset="s.off" :stop-color="s.col" />
          </linearGradient>
        </defs>
        <g ref="coarseG" class="tsf-mesh" />
        <g ref="fullG" class="tsf-mesh" />

        <g class="tsf-iso" :class="{ on: mapShown }">
          <path v-for="b in bands" :key="'b' + b.lo" class="tsf-band" :d="b.d" :fill="b.fill" fill-rule="evenodd" />
          <path v-for="l in isolines" :key="l.level" :d="l.d" :class="{ index: l.index, light: l.light }" />
          <text
            v-for="l in isoLabels"
            :key="'t' + l.level"
            :transform="`translate(${l.x.toFixed(1)} ${l.y.toFixed(1)}) rotate(${l.ang.toFixed(1)})`"
            class="ixf-text"
            dominant-baseline="central"
            text-anchor="middle"
          >{{ l.level }}</text>
          <g v-if="scaleBar" class="tsf-bar">
            <path :d="`M${scaleBar.x} ${scaleBar.y - 5}V${scaleBar.y}H${scaleBar.x + scaleBar.w}V${scaleBar.y - 5}`" />
            <text class="ixf-text" :x="scaleBar.x + scaleBar.w + 8" :y="scaleBar.y" dominant-baseline="central">100 m</text>
          </g>
        </g>

        <g v-if="key" class="tsf-key">
          <text class="tsf-keyhead ixf-label" :x="key.x + 5" :y="key.top - 16" text-anchor="middle">height</text>
          <rect :x="key.x" :y="key.top" width="10" :height="key.bottom - key.top" :fill="`url(#${gid})`" />
          <rect v-for="(k, n) in key.steps" :key="'s' + n" class="tsf-step" :class="{ on: mapShown }" :x="key.x" :y="k.y" width="10" :height="k.h" :fill="k.fill" />
          <line v-for="k in key.marks" :key="'m' + k.h" :x1="key.x" :x2="key.x + 10" :y1="k.y" :y2="k.y" class="tsf-mark" :class="{ on: mapShown, light: k.light }" />
          <rect class="ixf-frame" :x="key.x" :y="key.top" width="10" :height="key.bottom - key.top" />
          <path class="ixf-minor" :d="key.minor" />
          <path class="ixf-ticks" :d="key.major" />
          <text v-for="k in key.labels" :key="'k' + k.h" class="ixf-tl" :x="key.x + 16.25" :y="k.y" dominant-baseline="central">{{ k.h }} m</text>
        </g>
        <text v-if="loadError" class="tsf-msg ixf-text" :x="W / 2" :y="H / 2" text-anchor="middle">{{ loadError }}</text>
      </svg>
    </figure>

    <nav class="tsf-controls">
      <button
        type="button"
        class="tsf-play"
        tabindex="-1"
        :disabled="!ready || mapMode"
        :aria-label="spinning ? 'Stop turning' : 'Turn'"
        @mousedown.prevent
        @pointerdown.stop
        @click="toggleSpin"
      >
        <svg viewBox="0 0 20 20" aria-hidden="true">
          <g v-if="spinning && !mapMode"><rect x="5" y="4" width="3.4" height="12" rx="0.8" /><rect x="11.6" y="4" width="3.4" height="12" rx="0.8" /></g>
          <path v-else d="M6 3.8v12.4a.8.8 0 0 0 1.2.7l10-6.2a.8.8 0 0 0 0-1.4l-10-6.2A.8.8 0 0 0 6 3.8z" />
        </svg>
      </button>
      <span class="tsf-seg" role="group" aria-label="View">
        <button type="button" tabindex="-1" :class="{ on: !mapMode }" :disabled="!ready" @mousedown.prevent @pointerdown.stop @click="setMap(false, $event)">surface</button>
        <button type="button" tabindex="-1" :class="{ on: mapMode }" :disabled="!ready" @mousedown.prevent @pointerdown.stop @click="setMap(true, $event)">map</button>
      </span>
    </nav>
    <p class="tsf-note"><template v-if="mapMode">isolines every 10 m,<br>heavier every 50 m</template><template v-else>heights drawn × {{ exaggeration }}</template></p>
  </section>
</template>

<style scoped>
/* The plot's type, the key's edge and ticks: ./figure-look/figure-look.css;
   the buttons and the note keep the slides' type.
   The root takes `fig-fill` on a `class: fill` slide. The theme turns every
   direct div child of a .fig-fill into a flex column, so the parts are a
   <figure> and a <nav>, out of reach of that rule. */
.tsf {
  position: relative;
  height: 22rem; /* off a `class: fill` slide */
  min-height: 0;
  user-select: none;
  -webkit-user-select: none;
  color: var(--fg);
  font-family: var(--font-sans);
  font-variant-numeric: tabular-nums;
}
.tsf-plot {
  position: absolute;
  inset: 0;
  margin: 0;
}
.tsf-svg {
  position: absolute;
  inset: 0;
  display: block;
  touch-action: none;
  -webkit-tap-highlight-color: transparent;
}
.tsf-svg:active { cursor: grabbing; }
.tsf-mesh path { stroke: none; }
.tsf-iso { opacity: 0; transition: opacity 0.5s var(--ease); pointer-events: none; }
.tsf-iso.on { opacity: 1; }
.tsf-iso .tsf-band { stroke: none; }
.tsf-iso path:not(.tsf-band) { fill: none; stroke: var(--bg); stroke-opacity: 0.62; stroke-width: 1; stroke-linejoin: round; }
.tsf-iso path.index:not(.tsf-band) { stroke-width: 2; stroke-opacity: 0.8; }
.tsf-iso path.light { stroke: var(--fg); stroke-opacity: 0.55; }
.tsf-iso path.light.index { stroke-opacity: 0.8; }
.tsf-step { opacity: 0; transition: opacity 0.5s var(--ease); }
.tsf-step.on { opacity: 1; }
.tsf-iso text {
  fill: var(--fg);
  font-weight: 600;
  paint-order: stroke;
  stroke: var(--bg);
  stroke-width: 3.5px;
  stroke-linejoin: round;
}
.tsf-iso .tsf-bar path { fill: none; stroke: var(--fg); stroke-opacity: 1; stroke-width: 1.6; }
.tsf-iso .tsf-bar text { font-weight: 400; }
.tsf-key text { fill: var(--fg); }
.tsf-mark { stroke: var(--bg); stroke-width: 1; opacity: 0; transition: opacity 0.5s var(--ease); }
.tsf-mark.on { opacity: 0.7; }
.tsf-mark.light { stroke: var(--fg); }
.tsf-msg { fill: var(--warn); }

/* ---- controls ---- */
/* The buttons and the note sit in the free column at the left of the hill. */
.tsf-controls {
  position: absolute;
  left: 0.2rem;
  top: 0.4rem;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 0.8rem;
}
.tsf-play {
  width: 34px;
  height: 34px;
  display: grid;
  place-items: center;
  padding: 0;
  border: 1px solid color-mix(in srgb, var(--accent) 55%, transparent);
  border-radius: 50%;
  background: none;
  color: var(--accent);
  cursor: pointer;
  transition: border-color 0.3s var(--ease), background-color 0.3s var(--ease), opacity 0.3s var(--ease);
}
.tsf-play:hover:not(:disabled) { border-color: var(--accent); background: color-mix(in srgb, var(--accent) 12%, transparent); }
.tsf-play:focus { outline: none; }
.tsf-play:disabled { opacity: 0.3; cursor: default; }
.tsf-play svg { width: 18px; height: 18px; fill: currentColor; }
.tsf-seg { display: flex; flex-direction: column; border: 1px solid var(--hair-strong); border-radius: 4px; overflow: hidden; }
.tsf-seg button {
  font-family: var(--font-sans);
  font-size: 0.875rem;
  font-weight: 500;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--fg-2);
  background: none;
  border: none;
  padding: 0.42rem 0.85rem;
  text-align: left;
  cursor: pointer;
  transition: color 0.3s var(--ease), background-color 0.3s var(--ease);
}
.tsf-seg button + button { border-top: 1px solid var(--hair-strong); }
.tsf-seg button:focus { outline: none; }
.tsf-seg button:hover:not(:disabled) { color: var(--accent); }
.tsf-seg button.on { color: var(--accent); background: color-mix(in srgb, var(--accent) 12%, transparent); }
.tsf-note {
  position: absolute;
  left: 0.2rem;
  bottom: 0.2rem;
  margin: 0;
  font-size: 0.875rem;
  line-height: 1.35;
  color: var(--dim);
  letter-spacing: 0.04em;
  pointer-events: none;
}
.tsf-wait .tsf-controls { opacity: 0.35; }

@media (prefers-reduced-motion: reduce) {
  .tsf-iso,
  .tsf-step,
  .tsf-mark,
  .tsf-play,
  .tsf-seg button { transition: none; }
}
</style>
