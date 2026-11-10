<!--
  TurningScatter — the four-variable scatter of slide 81, turned by hand.

    <TurningScatter />              in a grid-side cell or a `fig-fill` block
    <TurningScatter :azim="-55" :elev="18" :period="40" />

  Every day of the log (3648): x the mean temperature, y the mean humidity,
  z the mean wind, the colour its month (beyond.py's cyclic month colours).
  Vector throughout (SVG), so it stays sharp at any scale. Mild perspective;
  the points are drawn in depth layers, far ones first, smaller and dimmer.
  It turns by itself, one turn in `period` seconds, until the first drag
  (never with reduced motion); dragging turns it about the vertical axis and
  tilts it (clamped); the button pauses and plays; a double-click resets the
  view (azimuth −55°, elevation 18°, as on slide 81). No control takes the
  keyboard focus and a drag never moves the slide. In presenter mode the
  audience window follows (BroadcastChannel).

  The text has the look of the static figures (figures/src/style.py): STIX
  type, tick and axis labels in the text colour, ticks 1 px; the box edges
  stay faint, as the panes of the static 3D figure (beyond.py, _dark_3d)
  (./figure-look/figure-look.css).

  Data: public/data/l07_scatter4.json (figures/src/interactive_l07_data.py).
-->
<script>
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
const fmt = (v, d) => {
  const s = Number(v).toFixed(d)
  return (/^-0\.?0*$/.test(s) ? s.slice(1) : s).replace('-', '−')
}
// The box: axis limits and a few ticks for temperature, humidity, wind, and
// the box aspect of the old GIF (1.6 : 1.2 : 1).
const AXES = [
  { lo: -14, hi: 28, ticks: [-10, 0, 10, 20], len: 1.6 },
  { lo: 46, hi: 100, ticks: [50, 75, 100], len: 1.2 },
  { lo: 0, hi: 10, ticks: [0, 5, 10], len: 1.0 },
]
const LAYERS = 6                 // depth layers, drawn far to near
const DIST = 5                   // camera distance, in box units: mild perspective
const R0 = 2.1                   // point radius, slide px, at the box centre
const ELEV = [-5, 75]            // the tilt is clamped to this, degrees
</script>

<script setup>
import { computed, nextTick, onBeforeUnmount, onMounted, ref, shallowRef, watch } from 'vue'
import { useIsSlideActive, useSlideContext } from '@slidev/client'
import './figure-look/figure-look.css'

const props = defineProps({
  azim: { type: Number, default: -55 },
  elev: { type: Number, default: 18 },
  // Seconds for one turn while it turns by itself.
  period: { type: Number, default: 40 },
  src: { type: String, default: 'data/l07_scatter4.json' },
  syncId: { type: String, default: '' },
})

const reduceMotion = typeof window !== 'undefined'
  && window.matchMedia?.('(prefers-reduced-motion: reduce)').matches
const clamp = (v, lo, hi) => Math.min(hi, Math.max(lo, v))

// ---- data: each day as a point in box units --------------------------------------
const D = shallowRef(null)
const loadError = ref('')
fetchJSON(import.meta.env.BASE_URL + props.src)
  .then((d) => {
    const n = d.temp.length
    const P = new Float64Array(n * 3)
    const cols = [d.temp, d.hum, d.wind]
    for (let i = 0; i < n; i++) {
      for (let k = 0; k < 3; k++) {
        const a = AXES[k]
        P[i * 3 + k] = ((cols[k][i] - a.lo) / (a.hi - a.lo) - 0.5) * a.len
      }
    }
    D.value = { n, P, month: d.month, colors: d.colors, months: d.months, labels: d.labels }
  })
  .catch((e) => { loadError.value = String(e.message || e) })
const ready = computed(() => !!D.value)

// ---- the view ------------------------------------------------------------------------
const azim = ref(props.azim)
const elev = ref(props.elev)
const turning = ref(!reduceMotion)        // turns by itself until the first drag
const dragged = ref(false)
let touched = false

const root = ref(null)
const W = ref(0)
const H = ref(0)
let ro = null
onMounted(() => {
  ro = new ResizeObserver(([e]) => {
    W.value = Math.round(e.contentRect.width)
    H.value = Math.round(e.contentRect.height)
  })
  if (root.value) ro.observe(root.value)
})

const LEG_W = 74                          // the month legend on the right
const PAD = { l: 34, r: 18, t: 18, b: 46 }

// The camera of matplotlib's view_init(elev, azim): eye direction v, screen
// right r, screen up u; a point's depth is its distance towards the eye.
const cam = computed(() => {
  const a = (azim.value * Math.PI) / 180
  const e = (elev.value * Math.PI) / 180
  const ce = Math.cos(e), se = Math.sin(e), ca = Math.cos(a), sa = Math.sin(a)
  const v = [ce * ca, ce * sa, se]
  const r = [-sa, ca, 0]
  const u = [-se * ca, -se * sa, ce]
  const pw = W.value - LEG_W - PAD.l - PAD.r
  const ph = H.value - PAD.t - PAD.b
  // Scale: the widest the box can be at this tilt, whatever the azimuth.
  const kmax = DIST / (DIST - 1.1)
  const extW = Math.hypot(AXES[0].len, AXES[1].len)
  const extH = extW * Math.abs(se) + AXES[2].len * ce
  const S = Math.max(10, Math.min(pw / (extW * kmax), ph / (extH * kmax)))
  return { v, r, u, S, cx: PAD.l + pw / 2, cy: PAD.t + ph / 2 }
})
function project(x, y, z, c) {
  const d = x * c.v[0] + y * c.v[1] + z * c.v[2]
  const k = DIST / (DIST - d)
  return {
    x: c.cx + c.S * k * (x * c.r[0] + y * c.r[1] + z * c.r[2]),
    y: c.cy - c.S * k * (x * c.u[0] + y * c.u[1] + z * c.u[2]),
    d,
    k,
  }
}

// The points as LAYERS x 12 paths of small circles, far layers first. Recomputed
// only when the view (or the size) changes.
const layers = computed(() => {
  const data = D.value
  if (!data || !W.value) return []
  const c = cam.value
  const half = 0.5 * Math.hypot(AXES[0].len, AXES[1].len, AXES[2].len)
  const buf = Array.from({ length: LAYERS }, () => Array.from({ length: 12 }, () => []))
  const P = data.P
  for (let i = 0; i < data.n; i++) {
    const p = project(P[i * 3], P[i * 3 + 1], P[i * 3 + 2], c)
    const L = clamp(Math.floor(((p.d + half) / (2 * half)) * LAYERS), 0, LAYERS - 1)
    const r = R0 * p.k
    const x0 = (p.x - r).toFixed(1)
    const y0 = p.y.toFixed(1)
    const rr = r.toFixed(2)
    const dd = (2 * r).toFixed(2)
    buf[L][data.month[i] - 1].push(`M${x0} ${y0}a${rr} ${rr} 0 1 0 ${dd} 0a${rr} ${rr} 0 1 0 -${dd} 0`)
  }
  const out = []
  for (let L = 0; L < LAYERS; L++) {
    for (let m = 0; m < 12; m++) {
      if (buf[L][m].length) {
        out.push({ key: `${L}-${m}`, d: buf[L][m].join(''), fill: data.colors[m], op: 0.42 + (0.53 * (L + 0.5)) / LAYERS })
      }
    }
  }
  return out
})

// The box: its 12 edges, faint; ticks and names on the edges that face the viewer.
const corners = (() => {
  const h = AXES.map((a) => a.len / 2)
  const out = []
  for (const sx of [-1, 1]) for (const sy of [-1, 1]) for (const sz of [-1, 1]) out.push([sx * h[0], sy * h[1], sz * h[2]])
  return out
})()
const box = computed(() => {
  if (!W.value) return null
  const c = cam.value
  const pc = corners.map(([x, y, z]) => project(x, y, z, c))
  const edges = []
  for (let i = 0; i < 8; i++) {
    for (let j = i + 1; j < 8; j++) {
      const diff = corners[i].map((v, k) => (v !== corners[j][k] ? 1 : 0)).reduce((a, b) => a + b, 0)
      if (diff === 1) edges.push({ x1: pc[i].x, y1: pc[i].y, x2: pc[j].x, y2: pc[j].y, d: (pc[i].d + pc[j].d) / 2 })
    }
  }
  const centre = project(0, 0, 0, c)
  const h = AXES.map((a) => a.len / 2)
  // For each axis, the edge it is read on.
  const pick = (k) => {
    let best = null
    for (const s1 of [-1, 1]) {
      for (const s2 of [-1, 1]) {
        const at = (t) => {
          const p = [0, 0, 0]
          p[k] = t
          const others = [0, 1, 2].filter((q) => q !== k)
          p[others[0]] = s1 * h[others[0]]
          p[others[1]] = s2 * h[others[1]]
          return p
        }
        const a = project(...at(-h[k]), c)
        const b = project(...at(h[k]), c)
        const mid = { x: (a.x + b.x) / 2, y: (a.y + b.y) / 2, d: (a.d + b.d) / 2 }
        // temperature and humidity: a bottom edge in front; wind: the leftmost upright edge
        let score
        if (k < 2) score = (at(0)[2] < 0 ? 1000 : 0) + mid.d * 10 + (mid.y - centre.y) * 0.001
        else score = -mid.x
        if (!best || score > best.score) best = { score, at, a, b, mid }
      }
    }
    // outward: the edge's normal on the screen, on the side away from the box
    // centre; ticks and the name sit along it, anchored by its direction, so
    // a steep edge puts them beside it instead of over its own ticks
    let ox = -(best.b.y - best.a.y)
    let oy = best.b.x - best.a.x
    const n = Math.hypot(ox, oy) || 1
    ox /= n
    oy /= n
    if ((best.mid.x - centre.x) * ox + (best.mid.y - centre.y) * oy < 0) { ox = -ox; oy = -oy }
    if (k === 2) { ox = -1; oy = 0 }
    const anchor = ox < -0.45 ? 'end' : ox > 0.45 ? 'start' : 'middle'
    const ax = AXES[k]
    const ticks = ax.ticks.map((t) => {
      const p = project(...best.at(((t - ax.lo) / (ax.hi - ax.lo) - 0.5) * ax.len), c)
      return { t, x: p.x, y: p.y, lx: p.x + ox * 12, ly: p.y + oy * 12 }
    })
    const width = D.value.labels[k].length * 6.6               // about the name's width
    let name
    if (k === 2) name = { x: best.b.x, y: best.b.y - 16, anchor: 'middle' }
    else {
      const far = anchor === 'middle' ? 30 : 36
      name = { x: best.mid.x + ox * far, y: best.mid.y + oy * far, anchor }
    }
    const lo = name.anchor === 'start' ? 4 : name.anchor === 'end' ? 4 + width : 4 + width / 2
    const hi = W.value - LEG_W - 4 - (name.anchor === 'start' ? width : name.anchor === 'end' ? 0 : width / 2)
    name.x = clamp(name.x, lo, hi)
    name.y = clamp(name.y, 12, H.value - 12)
    return { k, ticks, ox, oy, anchor, name }
  }
  return { edges, axes: [pick(0), pick(1), pick(2)] }
})

// ---- the month legend, as on slide 81: January at the bottom -------------------------------
const legend = computed(() => {
  if (!W.value || !D.value) return null
  const x = W.value - LEG_W + 8
  const top = PAD.t + 26
  const bottom = H.value - PAD.b
  const step = (bottom - top) / 12
  return {
    x,
    titleY: PAD.t + 8,
    items: D.value.months.map((name, m) => ({
      name, color: D.value.colors[m], y: bottom - (m + 1) * step, h: step,
    })),
  }
})

// ---- turning by itself ------------------------------------------------------------------------
const { $page, $renderContext } = useSlideContext()
const isActive = useIsSlideActive()
const live = computed(() => $renderContext?.value === 'slide' || $renderContext?.value === 'presenter')
let raf = 0
let last = 0
function tick(now) {
  raf = 0
  if (!turning.value || !isActive.value || !live.value) return
  if (last) azim.value = ((azim.value + ((now - last) / 1000) * (360 / props.period) + 540) % 360) - 180
  last = now
  raf = requestAnimationFrame(tick)
}
function startTurning() {
  if (raf || !turning.value || !isActive.value || !live.value) return
  last = 0
  raf = requestAnimationFrame(tick)
}
function stopTurning() { if (raf) cancelAnimationFrame(raf); raf = 0 }
watch([turning, isActive, ready], () => { stopTurning(); if (ready.value) startTurning() })

// ---- drag to turn and tilt; double-click resets -----------------------------------------------
const grabbing = ref(false)
let lastDown = { t: 0, x: 0, y: 0 }
function onDown(e) {
  if (!ready.value || (e.pointerType === 'mouse' && e.button !== 0)) return
  e.stopPropagation()                      // never a Slidev swipe
  e.preventDefault()
  const el = e.currentTarget
  const k = el.getBoundingClientRect().width / (W.value || 1) || 1   // screen px per slide px
  // a double-click or double-tap: back to the start
  const now = performance.now()
  if (now - lastDown.t < 380 && Math.hypot(e.clientX - lastDown.x, e.clientY - lastDown.y) < 14 * k) {
    lastDown = { t: 0, x: 0, y: 0 }
    resetView()
    return
  }
  lastDown = { t: now, x: e.clientX, y: e.clientY }
  const x0 = e.clientX
  const y0 = e.clientY
  const a0 = azim.value
  const e0 = elev.value
  let moved = false
  el.setPointerCapture(e.pointerId)
  grabbing.value = true
  const move = (ev) => {
    if (ev.pointerId !== e.pointerId) return
    const dx = (ev.clientX - x0) / k
    const dy = (ev.clientY - y0) / k
    if (!moved && Math.hypot(dx, dy) < 3) return
    if (!moved) {
      moved = true
      dragged.value = true
      turning.value = false
    }
    azim.value = ((a0 - dx * 0.45 + 540) % 360) - 180
    elev.value = clamp(e0 + dy * 0.35, ELEV[0], ELEV[1])
    touched = true
    schedulePost()
  }
  const up = (ev) => {
    if (ev.pointerId !== e.pointerId) return
    el.removeEventListener('pointermove', move)
    el.removeEventListener('pointerup', up)
    el.removeEventListener('pointercancel', up)
    grabbing.value = false
  }
  el.addEventListener('pointermove', move)
  el.addEventListener('pointerup', up)
  el.addEventListener('pointercancel', up)
}
function resetView() {
  azim.value = props.azim
  elev.value = props.elev
  touched = true
  schedulePost()
}
function toggle(e) {
  turning.value = !turning.value
  touched = true
  schedulePost()
  if (e?.detail) e.currentTarget.blur()
}

// ---- presenter ↔ audience ------------------------------------------------------------------------
const instance = Math.random().toString(36).slice(2)
const syncKey = () => `TurningScatter:${$page.value}:${props.syncId}`
let chan = null
let shared = ''
let pending = 0
const stateJSON = () => JSON.stringify({ a: Math.round(azim.value * 100) / 100, e: Math.round(elev.value * 100) / 100, t: turning.value, g: dragged.value })
function post(msg) { chan?.postMessage({ key: syncKey(), from: instance, ...msg }) }
// Posted on a drag, a reset and play/pause only: while it turns by itself,
// each window turns on its own clock from the same angle.
function schedulePost() {
  if (!chan || pending) return
  pending = requestAnimationFrame(() => {
    pending = 0
    const s = stateJSON()
    if (s === shared) return
    shared = s
    post({ type: 'state', state: s })
  })
}
function openSync() {
  if (chan || typeof BroadcastChannel === 'undefined' || !live.value) return
  shared = stateJSON()
  chan = new BroadcastChannel('course-interactive-figures')
  chan.onmessage = ({ data: m }) => {
    if (!m || m.key !== syncKey() || m.from === instance) return
    if (m.type === 'state') {
      shared = m.state
      touched = true
      const s = JSON.parse(m.state)
      azim.value = s.a
      elev.value = s.e
      dragged.value = s.g
      turning.value = s.t
    } else if (m.type === 'hello' && touched) {
      post({ type: 'state', state: stateJSON() })
    }
  }
  post({ type: 'hello' })
}
watch(ready, (r) => { if (r) nextTick(openSync) }, { immediate: true })

onBeforeUnmount(() => {
  ro?.disconnect()
  stopTurning()
  if (pending) cancelAnimationFrame(pending)
  chan?.close()
  chan = null
})
</script>

<template>
  <section ref="root" class="tsc" :class="{ 'tsc-grab': grabbing }">
    <svg
      v-if="W > 0 && H > 0"
      class="tsc-svg ixf"
      :width="W"
      :height="H"
      :viewBox="`0 0 ${W} ${H}`"
      role="img"
      aria-label="The days of the log: mean temperature, humidity and wind in three dimensions, the month as colour; drag to turn"
      :data-azim="azim.toFixed(2)"
      :data-elev="elev.toFixed(2)"
      :data-turning="turning"
      @pointerdown="onDown"
    >
      <title>Drag to turn; double-click or double-tap: back to the start</title>
      <template v-if="ready && box">
        <!-- box edges behind the points -->
        <g class="tsc-edges">
          <line v-for="(e, i) in box.edges" :key="'e' + i" :x1="e.x1" :y1="e.y1" :x2="e.x2" :y2="e.y2" />
        </g>
        <g class="tsc-pts">
          <path v-for="l in layers" :key="l.key" :d="l.d" :fill="l.fill" :fill-opacity="l.op" />
        </g>
        <g v-for="ax in box.axes" :key="'a' + ax.k" class="tsc-axis">
          <g v-for="t in ax.ticks" :key="t.t">
            <line class="tsc-tick" :x1="t.x" :y1="t.y" :x2="t.x + ax.ox * 5" :y2="t.y + ax.oy * 5" />
            <text class="ixf-tl" :x="t.lx" :y="t.ly" :text-anchor="ax.anchor" dominant-baseline="central">{{ fmt(t.t, 0) }}</text>
          </g>
          <text class="tsc-name ixf-label" :x="ax.name.x" :y="ax.name.y" :text-anchor="ax.name.anchor" dominant-baseline="central">{{ D.labels[ax.k] }}</text>
        </g>
        <g v-if="legend" class="tsc-legend">
          <text class="tsc-legtitle ixf-text" :x="legend.x" :y="legend.titleY" dominant-baseline="central">month</text>
          <g v-for="it in legend.items" :key="it.name">
            <rect :x="legend.x" :y="it.y + 1" width="11" :height="Math.max(1, it.h - 2)" rx="1.5" :fill="it.color" />
            <text class="ixf-text" :x="legend.x + 18" :y="it.y + it.h / 2" dominant-baseline="central">{{ it.name }}</text>
          </g>
        </g>
      </template>
      <text v-else-if="loadError" class="tsc-msg ixf-text" :x="W / 2" :y="H / 2" text-anchor="middle">{{ loadError }}</text>
    </svg>
    <footer class="tsc-bar">
      <button
        type="button"
        class="tsc-btn"
        :title="turning ? 'Pause' : 'Turn by itself'"
        :aria-label="turning ? 'pause the turning' : 'turn by itself'"
        @mousedown.prevent
        @pointerdown.stop
        @click="toggle"
      >
        <svg viewBox="0 0 16 16" aria-hidden="true">
          <path v-if="turning" d="M5 3.5v9M11 3.5v9" />
          <path v-else class="tsc-play" d="M5.5 3.2v9.6L12.8 8z" />
        </svg>
      </button>
    </footer>
  </section>
</template>

<style scoped>
/* The plot's type: ./figure-look/figure-look.css (STIX, 13.75 px tick
   labels and legend, 15.625 px axis names), the button keeps the slides'.
   A <section>: the theme's FILL rule turns a .fig-fill's direct <div>
   children into shrinking flex columns. In a grid-side row it stretches to
   the row's height; anywhere else it keeps 20rem. */
.tsc {
  position: relative;
  align-self: stretch;
  min-width: 0;
  min-height: 20rem;
  border: 1px solid var(--hair);
  border-radius: 6px;
  background: rgba(255, 255, 255, 0.015);
  overflow: hidden;
  user-select: none;
  -webkit-user-select: none;
  font-family: var(--font-sans);
}
.tsc-svg {
  position: absolute;
  inset: 0;
  display: block;
  cursor: grab;
  touch-action: none;
  -webkit-tap-highlight-color: transparent;
}
.tsc-grab .tsc-svg { cursor: grabbing; }
.tsc-edges line { stroke: var(--hair-strong); stroke-width: 1; }
.tsc-tick { stroke: var(--fg); stroke-width: 1; }
.tsc-axis text { fill: var(--fg); }
.tsc-legend text { fill: var(--fg); }
.tsc-msg { fill: var(--warn); }

.tsc-bar {
  position: absolute;
  right: calc(74px - 8px - 30px);
  bottom: 0.5rem;
  display: flex;
  align-items: center;
  gap: 0.6rem;
  pointer-events: none;
}
.tsc-btn {
  pointer-events: auto;
  display: grid;
  place-items: center;
  width: 30px;
  height: 30px;
  padding: 0;
  border: 1px solid var(--hair-strong);
  border-radius: 50%;
  background: rgba(5, 5, 7, 0.6);
  color: var(--fg-2);
  cursor: pointer;
  transition: color 0.3s var(--ease), border-color 0.3s var(--ease);
}
.tsc-btn:hover,
.tsc-btn:focus-visible { color: var(--accent); border-color: var(--accent); outline: none; }
.tsc-btn svg { width: 14px; height: 14px; fill: none; stroke: currentColor; stroke-width: 1.8; stroke-linecap: round; stroke-linejoin: round; }
.tsc-btn .tsc-play { fill: currentColor; stroke: none; }

@media (prefers-reduced-motion: reduce) {
  .tsc-btn { transition: none; }
}
</style>
