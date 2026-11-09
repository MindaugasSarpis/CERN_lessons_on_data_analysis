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
// The daily means of 2024 and 2025 (thin line) and their running mean over a
// window chosen with a slider, 1 to 61 days (thick line), as the figure of
// the slide "Visualising Trends" draws it at 21 days
// (figures/src/associations.py): centred, with the partial windows at the
// two ends, which is pandas' rolling(window, center=True, min_periods=1).
// figures/src/interactive_l07_data.py sums the windows in the same order and
// prints the same lowest and highest values.
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'

const props = defineProps({
  // The window shown first, in days: an odd number from 1 to 61.
  window: { type: Number, default: 21 },
  src: { type: String, default: 'data/l07_daily.json' },
})

const MAX_HALF = 30 // windows of 1, 3, ..., 61 days
const MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
const half = ref(Math.min(Math.max(Math.floor(props.window / 2), 0), MAX_HALF))
const days = computed(() => 2 * half.value + 1)
const data = ref(null)
const failed = ref(false)

const base = import.meta.env.BASE_URL || '/'

function fmt(x, nd) {
  let s = x.toFixed(nd)
  if (Number(s) === 0) s = s.replace('-', '')
  return s.replace('-', '\u2212')
}

const smooth = computed(() => {
  const t = data.value?.temps
  if (!t) return []
  const h = half.value
  const out = new Array(t.length)
  for (let i = 0; i < t.length; i++) {
    const a = Math.max(0, i - h)
    const b = Math.min(t.length - 1, i + h)
    let s = 0
    for (let j = a; j <= b; j++) s += t[j]
    out[i] = s / (b - a + 1)
  }
  return out
})

function extremes(v) {
  let lo = 0
  let hi = 0
  for (let i = 1; i < v.length; i++) {
    if (v[i] < v[lo]) lo = i
    if (v[i] > v[hi]) hi = i
  }
  return { lo: v[lo], hi: v[hi] }
}
const rawRange = computed(() => (data.value ? extremes(data.value.temps) : null))
const smoothRange = computed(() => (smooth.value.length ? extremes(smooth.value) : null))

// Stops under the slider: 1, 11, 21, ..., 61 days.
const stops = [0, 5, 10, 15, 20, 25, 30]

// ---- geometry ---------------------------------------------------------------
const plot = ref(null)
const size = ref({ w: 0, h: 0 })
const M = { l: 58, r: 12, t: 10, b: 30 }

function dayIndex(first, iso) {
  return Math.round((Date.parse(`${iso}T00:00:00Z`) - Date.parse(`${first}T00:00:00Z`)) / 86400000)
}

const geo = computed(() => {
  const { w, h } = size.value
  const d = data.value
  const r = rawRange.value
  if (w < 120 || h < 90 || !d || !r) return null
  const n = d.temps.length
  const pw = w - M.l - M.r
  const ph = h - M.t - M.b
  const lo = Math.floor(r.lo / 5) * 5
  const hi = Math.ceil(r.hi / 5) * 5
  const x = (i) => M.l + (i / (n - 1)) * pw
  const y = (v) => M.t + (1 - (v - lo) / (hi - lo)) * ph
  const yTicks = []
  for (let v = Math.ceil(lo / 10) * 10; v <= hi; v += 10) yTicks.push({ y: y(v), label: fmt(v, 0) })
  const y0 = Number(d.first.slice(0, 4))
  const xTicks = []
  for (let yr = y0; ; yr++) {
    let done = false
    for (const m of [1, 4, 7, 10]) {
      const i = dayIndex(d.first, `${yr}-${String(m).padStart(2, '0')}-01`)
      if (i >= n) { done = true; break }
      if (i >= 0) xTicks.push({ x: x(i), label: m === 1 ? `Jan ${yr}` : MONTHS[m - 1] })
    }
    if (done || yr > y0 + 50) break
  }
  return { w, h, pw, ph, x, y, yTicks, xTicks }
})

function pathOf(values, g) {
  const parts = new Array(values.length)
  for (let i = 0; i < values.length; i++) {
    parts[i] = `${i ? 'L' : 'M'}${g.x(i).toFixed(1)} ${g.y(values[i]).toFixed(1)}`
  }
  return parts.join('')
}
const rawPath = computed(() => (geo.value ? pathOf(data.value.temps, geo.value) : ''))
const smoothPath = computed(() => (geo.value ? pathOf(smooth.value, geo.value) : ''))

// ---- interaction (see BinWidthExplorer.vue) ---------------------------------
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
function pick(v) { half.value = v }

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
    <section class="ix smw">
      <div class="ix-row">
        <div class="ix-control">
          <div class="ix-label">Window <span class="ix-value">{{ days }} {{ days === 1 ? 'day' : 'days' }}</span></div>
          <div class="ix-slider">
            <input
              v-model.number="half"
              class="ix-range"
              type="range"
              min="0"
              :max="MAX_HALF"
              step="1"
              aria-label="Window of the running mean"
              :aria-valuetext="`${days} days`"
              @pointerdown.stop="releaseOnPointerUp"
              @keydown.esc="$event.target.blur()"
            >
            <div class="ix-stops" aria-hidden="true">
              <span
                v-for="v in stops"
                :key="v"
                class="ix-stop"
                :class="{ on: v === half }"
                :style="{ left: `calc(11px + (100% - 22px) * ${v / MAX_HALF})` }"
                @pointerdown.stop.prevent="pick(v)"
              >{{ 2 * v + 1 }}</span>
            </div>
          </div>
        </div>
        <div class="ix-readout" aria-live="polite">
          <template v-if="rawRange && smoothRange">
            <div><span class="smw-key smw-key-raw" aria-hidden="true" />every day: <span class="ix-num-2">{{ fmt(rawRange.lo, 1) }}</span> to <span class="ix-num-2">{{ fmt(rawRange.hi, 1) }}</span> °C</div>
            <div><span class="smw-key smw-key-smooth" aria-hidden="true" />mean over {{ days }} {{ days === 1 ? 'day' : 'days' }}: <span class="ix-num">{{ fmt(smoothRange.lo, 1) }}</span> to <span class="ix-num">{{ fmt(smoothRange.hi, 1) }}</span> °C</div>
          </template>
          <span v-else-if="failed" class="ix-error">Data not available: {{ src }}</span>
          <span v-else class="ix-dim">Loading the days…</span>
        </div>
      </div>

      <div ref="plot" class="ix-plot">
        <svg v-if="geo" class="ix-svg" :viewBox="`0 0 ${geo.w} ${geo.h}`" role="img"
          :aria-label="`Daily means of 2024 and 2025 and their mean over ${days} days`">
          <g class="ix-grid">
            <line v-for="t in geo.yTicks" :key="`g${t.label}`" :x1="M.l" :x2="geo.w - M.r" :y1="t.y" :y2="t.y" />
          </g>
          <g class="ix-ticks ix-yticks">
            <text v-for="t in geo.yTicks" :key="`y${t.label}`" :x="M.l - 8" :y="t.y" dy="0.35em">{{ t.label }}</text>
          </g>
          <g class="ix-ticks ix-xticks">
            <line v-for="t in geo.xTicks" :key="`l${t.label}${t.x}`" :x1="t.x" :x2="t.x" :y1="M.t + geo.ph" :y2="M.t + geo.ph + 4" />
            <text v-for="t in geo.xTicks" :key="`x${t.label}${t.x}`" :x="t.x" :y="M.t + geo.ph + 19">{{ t.label }}</text>
          </g>
          <path class="smw-raw" :d="rawPath" />
          <path class="smw-smooth" :d="smoothPath" />
          <text class="ix-axis-label" :transform="`translate(15 ${M.t + geo.ph / 2}) rotate(-90)`">temperature (°C)</text>
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
  align-items: flex-start;
  justify-content: space-between;
  gap: 1.5rem;
}
.ix-control { flex: 0 1 22rem; min-width: 0; }
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
.ix-readout {
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
  padding-top: 0.15rem;
  font-size: 0.95em;
  line-height: 1.3;
  font-variant-numeric: tabular-nums;
  white-space: nowrap;
}
.ix-num { color: var(--accent); }
.ix-num-2 { color: var(--fg); }
.ix-dim { color: var(--dim); }
.ix-error { color: var(--warn); }
.smw-key {
  display: inline-block;
  width: 1.4rem;
  margin-right: 0.5rem;
  vertical-align: middle;
}
.smw-key-raw { border-top: 1px solid var(--dim); }
.smw-key-smooth { border-top: 3px solid var(--accent); }
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
.ix-ticks text { fill: var(--dim); font-size: 13px; font-variant-numeric: tabular-nums; }
.ix-ticks line { stroke: var(--dim); stroke-width: 1; }
.ix-yticks text { text-anchor: end; }
.ix-xticks text { text-anchor: middle; }
.ix-axis-label { fill: var(--fg-2); font-size: 14px; text-anchor: middle; }
.smw-raw { fill: none; stroke: var(--dim); stroke-width: 1; stroke-linejoin: round; }
.smw-smooth { fill: none; stroke: var(--accent); stroke-width: 2.6; stroke-linejoin: round; stroke-linecap: round; }
</style>
