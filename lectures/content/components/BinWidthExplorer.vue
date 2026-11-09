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
// The 87 552 hours of weather.csv as a histogram whose bin width is chosen
// with a slider: 0.05 to 10 °C over -17 to 33 °C. The data file holds the
// hours at each tenth of a degree (the station writes tenths); the bins are
// added up here in fortieths of a degree, the unit in which every edge is a
// whole number (figures/src/interactive_l07_data.py prints the same numbers).
// Bins of 0.05 and 0.1 °C are centred on the tenths, so between two tenths a
// bin of 0.05 °C stays empty; wider bins start at -17 °C and a tenth on an
// edge belongs to the bin on its right, as in np.histogram.
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'

const props = defineProps({
  // The bin width shown first, °C: 0.05, 0.1, 0.5, 1, 2, 5 or 10.
  bin: { type: Number, default: 1 },
  // Start on 0 to 2 °C instead of the whole range.
  zoom: { type: Boolean, default: false },
  src: { type: String, default: 'data/l07_hist.json' },
})

const WIDTHS = [0.05, 0.1, 0.5, 1, 2, 5, 10]
const FULL = [-680, 1320] // fortieths of a degree: -17 to 33 °C
const ZOOM = [0, 80] //      0 to 2 °C

const start = WIDTHS.indexOf(props.bin)
const idx = ref(start < 0 ? 3 : start)
const zoomed = ref(props.zoom)
const data = ref(null)
const failed = ref(false)

const base = import.meta.env.BASE_URL || '/'

// ---- numbers as the slides write them -------------------------------------
// toFixed (halves away from zero), a minus sign, never "-0.0"; digit groups
// from five digits on (3848, 29 993).
function fmt(x, nd) {
  let s = x.toFixed(nd)
  if (Number(s) === 0) s = s.replace('-', '')
  return s.replace('-', '\u2212')
}
function count(n) {
  return n >= 10000 ? String(n).replace(/\B(?=(\d{3})+$)/g, '\u00a0') : String(n)
}
// A position in fortieths of a degree, with as many decimals as it needs.
function deg(e) {
  const nd = e % 40 === 0 ? 0 : e % 4 === 0 ? 1 : e % 2 === 0 ? 2 : 3
  return fmt(e / 40, nd)
}

// ---- the bins ---------------------------------------------------------------
const width = computed(() => WIDTHS[idx.value])
const w40 = computed(() => Math.round(width.value * 40))
const off = computed(() => (width.value <= 0.1 ? w40.value / 2 : 0))

const bins = computed(() => {
  const d = data.value
  if (!d) return []
  const w = w40.value
  const o = off.value
  const n = (FULL[1] - FULL[0]) / w
  const counts = new Array(n).fill(0)
  for (let i = 0; i < d.counts.length; i++) {
    const c = d.counts[i]
    if (!c) continue
    const j = Math.floor((4 * (d.k0 + i) - FULL[0] + o) / w)
    if (j >= 0 && j < n) counts[j] += c
  }
  const out = new Array(n)
  for (let j = 0; j < n; j++) out[j] = [FULL[0] - o + j * w, FULL[0] - o + (j + 1) * w, counts[j]]
  return out
})

// The x range shown; zoomed, the centred bins of 0 and 2 °C stay whole.
const win = computed(() => (zoomed.value ? [ZOOM[0] - off.value, ZOOM[1] + off.value] : FULL))
const view = computed(() => bins.value.filter((b) => b[1] > win.value[0] && b[0] < win.value[1]))

const stats = computed(() => {
  const v = view.value
  if (!v.length) return null
  let full = v[0]
  let empty = 0
  for (const b of v) {
    if (b[2] === 0) empty++
    if (b[2] > full[2]) full = b // the first of the fullest, left to right
  }
  const where = width.value <= 0.1
    ? `${fmt((full[0] + full[1]) / 2 / 40, 1)} °C`
    : `${deg(full[0])} to ${deg(full[1])} °C`
  return { n: v.length, empty, full, where }
})

const widthLabel = computed(() => String(width.value))

// ---- geometry ---------------------------------------------------------------
const plot = ref(null)
const size = ref({ w: 0, h: 0 })
// The left margin holds the widest tick label ("30 000") whatever the width,
// so the bars do not shift while the slider moves; the top margin holds the
// label of the mean, above the bars.
const M = { l: 84, r: 14, t: 30, b: 50 }

function niceStep(max, target) {
  const rough = max / target
  const mag = 10 ** Math.floor(Math.log10(rough))
  const n = rough / mag
  return (n <= 1 ? 1 : n <= 2 ? 2 : n <= 5 ? 5 : 10) * mag
}

const geo = computed(() => {
  const { w, h } = size.value
  const s = stats.value
  if (w < 120 || h < 90 || !s) return null
  const [lo, hi] = win.value
  const pw = w - M.l - M.r
  const ph = h - M.t - M.b
  const step = niceStep(Math.max(s.full[2], 1), 5)
  const top = Math.ceil(Math.max(s.full[2], 1) / step) * step
  const x = (e) => M.l + ((e - lo) / (hi - lo)) * pw
  const y = (c) => M.t + (1 - c / top) * ph
  const yTicks = []
  for (let c = 0; c <= top + step / 2; c += step) yTicks.push({ y: y(c), label: count(c) })
  const xTicks = []
  const [t0, t1, dt] = zoomed.value ? [0, 80, 20] : [-600, 1200, 200] // fortieths
  for (let t = t0; t <= t1; t += dt) xTicks.push({ x: x(t), label: deg(t) })
  return { w, h, pw, ph, x, y, yTicks, xTicks, lo, hi, bottom: y(0) }
})

const barsPath = computed(() => {
  const g = geo.value
  if (!g) return ''
  const parts = []
  for (const [a, b, c] of view.value) {
    if (!c) continue
    let xa = g.x(Math.max(a, g.lo))
    let xb = g.x(Math.min(b, g.hi))
    if (xb - xa > 4) { xa += 0.6; xb -= 0.6 } // a dark seam between wide bars
    parts.push(`M${xa.toFixed(2)} ${g.y(c).toFixed(2)}H${xb.toFixed(2)}V${g.bottom.toFixed(2)}H${xa.toFixed(2)}Z`)
  }
  return parts.join('')
})

const mean = computed(() => {
  const g = geo.value
  const d = data.value
  if (!g || !d) return null
  const e = d.mean * 40
  if (e <= g.lo || e >= g.hi) return null
  return { x: g.x(e), label: `mean ${fmt(d.mean, 2)} °C` }
})

// ---- interaction ------------------------------------------------------------
// Slidev turns its keys off while an input or a button has the focus, so a
// control used with the pointer gives the focus back on release: the clicker
// and the arrow keys then move the slides again. The pointerdown stays inside
// the component, so a drag on a touch screen is not read as a swipe.
function releaseOnPointerUp(e) {
  const el = e.currentTarget
  const done = () => {
    window.removeEventListener('pointerup', done)
    window.removeEventListener('pointercancel', done)
    requestAnimationFrame(() => el.blur())
  }
  window.addEventListener('pointerup', done)
  window.addEventListener('pointercancel', done)
}
function pick(i, e) {
  idx.value = i
  e?.currentTarget?.blur?.()
}
function setZoom(z, e) {
  zoomed.value = z
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
    <section class="ix bwx">
      <div class="ix-row">
        <div class="ix-control">
          <div class="ix-label">
            Bin width <span class="ix-value">{{ widthLabel }} °C</span>
          </div>
          <div class="ix-slider">
            <input
              v-model.number="idx"
              class="ix-range"
              type="range"
              min="0"
              :max="WIDTHS.length - 1"
              step="1"
              aria-label="Bin width"
              :aria-valuetext="`${widthLabel} °C`"
              @pointerdown.stop="releaseOnPointerUp"
              @keydown.esc="$event.target.blur()"
            >
            <div class="ix-stops" aria-hidden="true">
              <span
                v-for="(w, i) in WIDTHS"
                :key="w"
                class="ix-stop"
                :class="{ on: i === idx }"
                :style="{ left: `calc(11px + (100% - 22px) * ${i / (WIDTHS.length - 1)})` }"
                @pointerdown.stop.prevent="pick(i)"
              >{{ w }}</span>
            </div>
          </div>
        </div>
        <div class="ix-toggle" role="group" aria-label="Range of the x axis">
          <button
            type="button"
            :class="{ on: !zoomed }"
            :aria-pressed="!zoomed"
            @pointerdown.stop
            @click="setZoom(false, $event)"
          >−17 to 33 °C</button>
          <button
            type="button"
            :class="{ on: zoomed }"
            :aria-pressed="zoomed"
            @pointerdown.stop
            @click="setZoom(true, $event)"
          >0 to 2 °C</button>
        </div>
      </div>

      <div class="ix-readout" aria-live="polite">
        <template v-if="stats">
          <span class="ix-num">{{ stats.n }}</span> {{ stats.n === 1 ? 'bin' : 'bins' }}<template v-if="stats.empty">, <span class="ix-num">{{ stats.empty }}</span> empty</template>
          · fullest {{ stats.where }}: <span class="ix-num">{{ count(stats.full[2]) }}</span> hours
        </template>
        <span v-else-if="failed" class="ix-error">Data not available: {{ src }}</span>
        <span v-else class="ix-dim">Loading the hours…</span>
      </div>

      <div ref="plot" class="ix-plot">
        <svg v-if="geo" class="ix-svg" :viewBox="`0 0 ${geo.w} ${geo.h}`" role="img"
          :aria-label="`Histogram of the hours, ${widthLabel} °C per bin`">
          <g class="ix-grid">
            <line v-for="t in geo.yTicks" :key="`g${t.label}`" :x1="M.l" :x2="geo.w - M.r" :y1="t.y" :y2="t.y" />
          </g>
          <g class="ix-ticks ix-yticks">
            <text v-for="t in geo.yTicks" :key="`y${t.label}`" :x="M.l - 8" :y="t.y" dy="0.35em">{{ t.label }}</text>
          </g>
          <g class="ix-ticks ix-xticks">
            <text v-for="t in geo.xTicks" :key="`x${t.label}`" :x="t.x" :y="geo.bottom + 20">{{ t.label }}</text>
          </g>
          <path class="bwx-bars" :d="barsPath" />
          <line class="ix-axis" :x1="M.l" :x2="geo.w - M.r" :y1="geo.bottom" :y2="geo.bottom" />
          <g v-if="mean" class="bwx-mean">
            <line :x1="mean.x" :x2="mean.x" :y1="M.t - 24" :y2="geo.bottom" />
            <text :x="mean.x + 7" :y="M.t - 12">{{ mean.label }}</text>
          </g>
          <text class="ix-axis-label" :x="M.l + geo.pw / 2" :y="geo.h - 6">temperature (°C)</text>
          <text class="ix-axis-label" :transform="`translate(16 ${M.t + geo.ph / 2}) rotate(-90)`">hours per {{ widthLabel }} °C</text>
        </svg>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* The course look (theme/styles/tokens.css): hairlines, Space Grotesk, the
   cyan accent for the data, --warn for the marked mean. No motion. */
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
  gap: 0.45rem;
  min-height: 0;
  font-family: var(--font-sans);
  color: var(--fg);
}
.ix-row {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 1.5rem;
}
.ix-control { flex: 0 1 26rem; min-width: 0; }
.ix-label {
  display: flex;
  align-items: baseline;
  gap: 0.6rem;
  font-size: 0.72rem;
  font-weight: 500;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--dim);
}
.ix-value {
  font-size: 1rem;
  letter-spacing: 0;
  text-transform: none;
  color: var(--accent);
  font-variant-numeric: tabular-nums;
}
.ix-slider { position: relative; padding-bottom: 1.25rem; touch-action: none; }
.ix-range {
  -webkit-appearance: none;
  appearance: none;
  display: block;
  width: 100%;
  height: 30px;
  margin: 0;
  background: transparent;
  cursor: pointer;
  touch-action: none;
}
.ix-range:focus { outline: none; }
.ix-range::-webkit-slider-runnable-track {
  height: 2px;
  background: color-mix(in srgb, var(--dim) 60%, transparent);
  border-radius: 1px;
}
.ix-range::-moz-range-track {
  height: 2px;
  background: color-mix(in srgb, var(--dim) 60%, transparent);
  border-radius: 1px;
}
.ix-range::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 22px;
  height: 22px;
  margin-top: -10px;
  border: none;
  border-radius: 50%;
  background: var(--accent);
}
.ix-range::-moz-range-thumb {
  width: 22px;
  height: 22px;
  border: none;
  border-radius: 50%;
  background: var(--accent);
}
.ix-range:focus-visible::-webkit-slider-thumb { box-shadow: 0 0 0 4px var(--bg), 0 0 0 5px var(--fg); }
.ix-range:focus-visible::-moz-range-thumb { box-shadow: 0 0 0 4px var(--bg), 0 0 0 5px var(--fg); }
.ix-stops { position: absolute; left: 0; right: 0; bottom: 0; height: 1.2rem; }
.ix-stop {
  position: absolute;
  top: 0;
  transform: translateX(-50%);
  padding: 0 0.25rem;
  font-size: 0.8rem;
  font-variant-numeric: tabular-nums;
  color: var(--dim);
  cursor: pointer;
  user-select: none;
}
.ix-stop.on { color: var(--accent); }
/* A hairline group; the chosen button takes the accent and an underline. */
.ix-toggle {
  display: flex;
  flex: none;
  margin-bottom: 1.25rem;
  border: 1px solid var(--hair);
  border-radius: 4px;
}
.ix-toggle button {
  font-family: var(--font-sans);
  font-size: 0.8rem;
  font-variant-numeric: tabular-nums;
  padding: 0.35rem 0.75rem;
  min-height: 32px;
  margin: 0;
  background: none;
  color: var(--dim);
  border: none;
  border-radius: 0;
  cursor: pointer;
}
.ix-toggle button + button { border-left: 1px solid var(--hair); }
.ix-toggle button.on { color: var(--accent); box-shadow: inset 0 -2px 0 var(--accent); }
.ix-toggle button:focus { outline: none; }
.ix-toggle button:focus-visible { outline: 1px solid var(--fg); outline-offset: 2px; }
.ix-readout {
  font-size: 0.95em;
  line-height: 1.3;
  color: var(--fg);
  font-variant-numeric: tabular-nums;
  min-height: 1.3em;
}
.ix-num { color: var(--accent); }
.ix-dim { color: var(--dim); }
.ix-error { color: var(--warn); }
.ix-plot { position: relative; flex: 1 1 0; min-height: 0; }
.ix-svg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  overflow: visible;
  font-family: var(--font-sans);
}
.ix-grid line { stroke: var(--hair); stroke-width: 1; }
.ix-axis { stroke: var(--dim); stroke-width: 1; }
.ix-ticks text { fill: var(--dim); font-size: 13px; font-variant-numeric: tabular-nums; }
.ix-yticks text { text-anchor: end; }
.ix-xticks text { text-anchor: middle; }
.ix-axis-label { fill: var(--fg-2); font-size: 14px; text-anchor: middle; }
.bwx-bars { fill: var(--accent); }
.bwx-mean line { stroke: var(--warn); stroke-width: 1.6; }
.bwx-mean text { fill: var(--warn); font-size: 14px; }
</style>
