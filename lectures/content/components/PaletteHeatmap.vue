<script>
// Module scope (runs once): each data file is fetched once per page and
// shared by every instance (the overview mounts every slide a second time).
const files = new Map()
function loadJson(url) {
  if (!files.has(url)) {
    const p = fetch(url).then((r) => {
      if (!r.ok) throw new Error(`HTTP ${r.status}`)
      return r.json()
    })
    p.catch(() => files.delete(url)) // a failed load is retried by the next mount
    files.set(url, p)
  }
  return files.get(url)
}
</script>

<script setup>
// The ten-year mean temperature of each hour (up) of each day of the year
// (across), 24 x 366 cells as in the slide "Day, Hour and Temperature as a
// Heatmap" (figures/src/beyond.py, day_hour_grid), in one of four palettes
// sampled from Matplotlib: viridis, jet, RdBu_r centred on 0 °C, gray. A tap
// (or the mouse) on a cell reads its value. The cells are drawn one pixel each
// on a 366 x 24 canvas and scaled up without smoothing, as Matplotlib's
// imshow(interpolation="none") does; the colour of a value is
// palette[floor((value - lo) / (hi - lo) * 256)], clipped, as in Matplotlib.
import { ref, computed, watch, onMounted, onBeforeUnmount } from 'vue'

const props = defineProps({
  // The palette shown first: 'viridis', 'jet', 'diverging' or 'greys'.
  palette: { type: String, default: 'jet' },
  src: { type: String, default: 'data/l07_heatmap.json' },
})

const PALETTES = [
  { key: 'viridis', label: 'viridis' },
  { key: 'jet', label: 'rainbow (jet)' },
  { key: 'diverging', label: 'diverging at 0 °C' },
  { key: 'greys', label: 'greys' },
]
const MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
const NDAYS = 366
const NHOURS = 24

const pal = ref(PALETTES.some((p) => p.key === props.palette) ? props.palette : 'jet')
const sel = ref(null) // { d, h }: the cell read last
const data = ref(null)
const failed = ref(false)

const base = import.meta.env.BASE_URL || '/'

function fmt(x, nd) {
  let s = x.toFixed(nd)
  if (Number(s) === 0) s = s.replace('-', '')
  return s.replace('-', '\u2212')
}

// 256 colours per palette, [r, g, b, r, g, b, ...]
const luts = computed(() => {
  const d = data.value
  if (!d) return null
  const out = {}
  for (const [key, hex] of Object.entries(d.palettes)) {
    const lut = new Uint8ClampedArray(256 * 3)
    for (let i = 0; i < 256 * 3; i++) lut[i] = parseInt(hex.substr(i * 2, 2), 16)
    out[key] = lut
  }
  return out
})
const range = computed(() => {
  const d = data.value
  if (!d) return [0, 1]
  return pal.value === 'diverging' ? d.div : d.seq
})
function indexOf(v) {
  const [lo, hi] = range.value
  const i = Math.floor(((v - lo) / (hi - lo)) * 256)
  return i < 0 ? 0 : i > 255 ? 255 : i
}
function swatch(key) {
  const d = data.value
  if (!d) return 'none'
  const hex = d.palettes[key]
  const stops = []
  for (let k = 0; k <= 8; k++) {
    const i = Math.min(255, Math.round((k / 8) * 255))
    stops.push(`#${hex.substr(i * 6, 6)} ${(k / 8) * 100}%`)
  }
  return `linear-gradient(90deg, ${stops.join(', ')})`
}

// ---- drawing ------------------------------------------------------------------
const canvas = ref(null)
const bar = ref(null)

function draw() {
  const d = data.value
  const lut = luts.value?.[pal.value]
  if (!d || !lut) return
  const c = canvas.value
  if (c) {
    const ctx = c.getContext('2d')
    const img = ctx.createImageData(NDAYS, NHOURS)
    for (let h = 0; h < NHOURS; h++) {
      const row = NHOURS - 1 - h // hour 0 at the bottom
      for (let x = 0; x < NDAYS; x++) {
        const i = indexOf(d.cells[h * NDAYS + x] / 10) * 3
        const p = (row * NDAYS + x) * 4
        img.data[p] = lut[i]
        img.data[p + 1] = lut[i + 1]
        img.data[p + 2] = lut[i + 2]
        img.data[p + 3] = 255
      }
    }
    ctx.putImageData(img, 0, 0)
  }
  const b = bar.value
  if (b) {
    const ctx = b.getContext('2d')
    const img = ctx.createImageData(1, 256)
    for (let r = 0; r < 256; r++) {
      const i = (255 - r) * 3 // the highest value at the top
      img.data[r * 4] = lut[i]
      img.data[r * 4 + 1] = lut[i + 1]
      img.data[r * 4 + 2] = lut[i + 2]
      img.data[r * 4 + 3] = 255
    }
    ctx.putImageData(img, 0, 0)
  }
}
watch([data, pal], draw, { flush: 'post' })

// ---- geometry ---------------------------------------------------------------
const plot = ref(null)
const size = ref({ w: 0, h: 0 })
const M = { l: 70, r: 86, t: 8, b: 46 }
const BAR = { gap: 14, w: 14 }

const geo = computed(() => {
  const { w, h } = size.value
  const d = data.value
  if (w < 160 || h < 90 || !d) return null
  const pw = w - M.l - M.r
  const ph = h - M.t - M.b
  const cw = pw / NDAYS
  const chh = ph / NHOURS
  const xTicks = MONTHS.map((m, k) => {
    const day = d.days.indexOf(`${String(k + 1).padStart(2, '0')}-01`)
    return { x: M.l + (day + 0.5) * cw, label: m }
  })
  const yTicks = [0, 6, 12, 18].map((hr) => ({
    y: M.t + (NHOURS - 1 - hr + 0.5) * chh,
    label: `${String(hr).padStart(2, '0')}:00`,
  }))
  const [lo, hi] = range.value
  const bx = w - M.r + BAR.gap
  const vy = (v) => M.t + (1 - (v - lo) / (hi - lo)) * ph
  const barTicks = []
  for (let v = lo; v <= hi; v += 10) barTicks.push({ y: vy(v), label: fmt(v, 0) })
  return { w, h, pw, ph, cw, chh, xTicks, yTicks, bx, barTicks, vy }
})

const marker = computed(() => {
  const g = geo.value
  const d = data.value
  const s = sel.value
  if (!g || !d || !s) return null
  const v = d.cells[s.h * NDAYS + s.d] / 10
  return {
    x: M.l + s.d * g.cw,
    y: M.t + (NHOURS - 1 - s.h) * g.chh,
    vy: g.vy(Math.min(Math.max(v, range.value[0]), range.value[1])),
  }
})

const readout = computed(() => {
  const d = data.value
  const s = sel.value
  if (!d || !s) return null
  const [mm, dd] = d.days[s.d].split('-')
  const v = d.cells[s.h * NDAYS + s.d] / 10
  return { when: `${Number(dd)} ${MONTHS[Number(mm) - 1]}, ${String(s.h).padStart(2, '0')}:00`, value: `${fmt(v, 1)} °C` }
})

// ---- interaction --------------------------------------------------------------
// The pointerdown stays inside the component, so a drag over the cells on a
// touch screen reads them instead of swiping to the next slide. A palette
// button clicked with the pointer gives the focus back (Slidev's keys are off
// while a button has it).
function cellAt(e) {
  const r = canvas.value.getBoundingClientRect()
  const fx = (e.clientX - r.left) / r.width
  const fy = (e.clientY - r.top) / r.height
  if (!(fx >= 0 && fx < 1 && fy >= 0 && fy < 1)) return null
  return { d: Math.floor(fx * NDAYS), h: NHOURS - 1 - Math.floor(fy * NHOURS) }
}
function onDown(e) {
  const c = cellAt(e)
  if (c) sel.value = c
}
function onMove(e) {
  if (e.pointerType !== 'mouse' && !e.buttons) return
  const c = cellAt(e)
  if (c) sel.value = c
}
function choose(key, e) {
  pal.value = key
  if (e && e.detail) e.currentTarget.blur() // a click, not the keyboard
}

let ro = null
onMounted(() => {
  loadJson(base + props.src)
    .then((d) => { data.value = d })
    .catch(() => { failed.value = true })
  ro = new ResizeObserver(([entry]) => {
    const { width: w, height: h } = entry.contentRect
    if (w > 0 && h > 0) size.value = { w: Math.round(w), h: Math.round(h) }
  })
  if (plot.value) ro.observe(plot.value)
})
onBeforeUnmount(() => ro?.disconnect())
</script>

<template>
  <div class="ix-wrap">
    <section class="ix phm">
      <div class="ix-row">
        <div class="phm-palettes" role="group" aria-label="Palette">
          <button
            v-for="p in PALETTES"
            :key="p.key"
            type="button"
            :class="{ on: pal === p.key }"
            :aria-pressed="pal === p.key"
            @pointerdown.stop
            @click="choose(p.key, $event)"
          >
            <span class="phm-swatch" :style="{ background: swatch(p.key) }" aria-hidden="true" />{{ p.label }}
          </button>
        </div>
        <div class="ix-readout" aria-live="polite">
          <template v-if="readout">{{ readout.when }}: <span class="ix-num">{{ readout.value }}</span></template>
          <span v-else-if="failed" class="ix-error">Data not available: {{ src }}</span>
          <span v-else class="ix-dim">Tap a cell to read it</span>
        </div>
      </div>

      <div ref="plot" class="ix-plot">
        <canvas
          ref="canvas"
          class="phm-cells"
          :width="NDAYS"
          :height="NHOURS"
          :style="geo ? { left: `${M.l}px`, top: `${M.t}px`, width: `${geo.pw}px`, height: `${geo.ph}px` } : { display: 'none' }"
          role="img"
          aria-label="Mean temperature of each hour of each day of the year"
          @pointerdown.stop="onDown"
          @pointermove="onMove"
        />
        <canvas
          ref="bar"
          class="phm-bar"
          width="1"
          height="256"
          :style="geo ? { left: `${geo.bx}px`, top: `${M.t}px`, width: `${BAR.w}px`, height: `${geo.ph}px` } : { display: 'none' }"
          aria-hidden="true"
        />
        <svg v-if="geo" class="ix-svg" :viewBox="`0 0 ${geo.w} ${geo.h}`" aria-hidden="true">
          <rect class="phm-frame" :x="M.l - 0.5" :y="M.t - 0.5" :width="geo.pw + 1" :height="geo.ph + 1" />
          <g class="ix-ticks ix-xticks">
            <text v-for="t in geo.xTicks" :key="t.label" :x="t.x" :y="M.t + geo.ph + 18">{{ t.label }}</text>
          </g>
          <g class="ix-ticks ix-yticks">
            <text v-for="t in geo.yTicks" :key="t.label" :x="M.l - 8" :y="t.y" dy="0.35em">{{ t.label }}</text>
          </g>
          <g class="ix-ticks phm-barticks">
            <line v-for="t in geo.barTicks" :key="`l${t.label}`" :x1="geo.bx + BAR.w" :x2="geo.bx + BAR.w + 4" :y1="t.y" :y2="t.y" />
            <text v-for="t in geo.barTicks" :key="`t${t.label}`" :x="geo.bx + BAR.w + 7" :y="t.y" dy="0.35em">{{ t.label }}</text>
          </g>
          <text class="ix-axis-label" :x="M.l + geo.pw / 2" :y="geo.h - 6">day of the year</text>
          <text class="ix-axis-label" :transform="`translate(16 ${M.t + geo.ph / 2}) rotate(-90)`">hour of the day</text>
          <text class="ix-axis-label" :transform="`translate(${geo.w - 8} ${M.t + geo.ph / 2}) rotate(90)`">mean temperature (°C)</text>
          <g v-if="marker" class="phm-marker">
            <rect :x="marker.x - 1" :y="marker.y - 1" :width="geo.cw + 2" :height="geo.chh + 2" />
            <line :x1="geo.bx - 5" :x2="geo.bx + BAR.w + 1" :y1="marker.vy" :y2="marker.vy" />
            <path :d="`M${geo.bx - 5} ${marker.vy - 5}L${geo.bx} ${marker.vy}L${geo.bx - 5} ${marker.vy + 5}Z`" />
          </g>
        </svg>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* The course look (theme/styles/tokens.css); nothing moves on its own. */
/* The root takes `fig-fill` (the rest of a `class: fill` slide). The theme
   makes every direct div child of a .fig-fill a flex column, so the layout
   lives in one <section> inside the root, out of reach of that rule. */
.ix-wrap {
  display: flex;
  flex-direction: column;
  min-height: 0;
  height: 20rem; /* off a `class: fill` slide */
}
.ix {
  flex: 1 1 0;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  min-height: 0;
  font-family: var(--font-sans);
  color: var(--fg);
}
.ix-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}
.phm-palettes {
  display: flex;
  border: 1px solid var(--hair);
  border-radius: 4px;
}
.phm-palettes button {
  display: flex;
  align-items: center;
  gap: 0.45rem;
  font-family: var(--font-sans);
  font-size: 0.8rem;
  padding: 0.35rem 0.7rem;
  min-height: 34px;
  margin: 0;
  background: none;
  color: var(--dim);
  border: none;
  border-radius: 0;
  cursor: pointer;
  white-space: nowrap;
}
.phm-palettes button + button { border-left: 1px solid var(--hair); }
.phm-palettes button.on { color: var(--fg); box-shadow: inset 0 -2px 0 var(--accent); }
.phm-palettes button:focus { outline: none; }
.phm-palettes button:focus-visible { outline: 1px solid var(--fg); outline-offset: 2px; }
.phm-swatch {
  display: inline-block;
  width: 1.8rem;
  height: 0.55rem;
  border-radius: 1px;
}
.ix-readout {
  font-size: 0.95em;
  line-height: 1.3;
  font-variant-numeric: tabular-nums;
  white-space: nowrap;
}
.ix-num { color: var(--accent); }
.ix-dim { color: var(--dim); }
.ix-error { color: var(--warn); }
.ix-plot { position: relative; flex: 1 1 0; min-height: 0; }
.phm-cells,
.phm-bar {
  position: absolute;
  display: block;
}
.phm-cells {
  image-rendering: pixelated;
  image-rendering: crisp-edges;
  touch-action: none;
  cursor: crosshair;
}
@supports (image-rendering: pixelated) {
  .phm-cells { image-rendering: pixelated; }
}
.ix-svg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  overflow: visible;
  font-family: var(--font-sans);
  pointer-events: none;
}
.phm-frame { fill: none; stroke: var(--hair); stroke-width: 1; }
.ix-ticks text { fill: var(--dim); font-size: 13px; font-variant-numeric: tabular-nums; }
.ix-yticks text { text-anchor: end; }
.ix-xticks text { text-anchor: middle; }
.phm-barticks line { stroke: var(--dim); stroke-width: 1; }
.phm-barticks text { text-anchor: start; }
.ix-axis-label { fill: var(--fg-2); font-size: 14px; text-anchor: middle; }
.phm-marker rect { fill: none; stroke: var(--fg); stroke-width: 1.5; }
.phm-marker line { stroke: var(--fg); stroke-width: 1.5; }
.phm-marker path { fill: var(--fg); }
</style>
