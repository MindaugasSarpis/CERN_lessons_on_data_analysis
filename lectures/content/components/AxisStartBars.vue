<script setup>
// Five bars and the start of their value axis, chosen with a slider: from 0,
// where each bar is as long as its value, up to 48, where the first bar is
// nine times the last although the values differ by a fifth. The default
// values are figures/src/amounts.py's PASS_RATES (the figures of the slides
// "Bars That Do Not Start at Zero" / "The Same Bars from Zero");
// figures/src/interactive_l07_data.py checks them and prints the ratios.
// Lengths are computed in tenths, so 58.2 - 48 is 10.2, not 10.200000000000003.
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'

const props = defineProps({
  values: { type: Array, default: () => [58.2, 54.7, 51.9, 50.3, 49.1] },
  labels: { type: Array, default: () => ['School A', 'School B', 'School C', 'School D', 'School E'] },
  // Where the axis starts at first.
  start: { type: Number, default: 0 },
  // The highest start on the slider; keep it below the smallest value.
  max: { type: Number, default: 48 },
  // The top of the axis.
  top: { type: Number, default: 60 },
  ylabel: { type: String, default: 'exam pass rate (%)' },
})

const axis = ref(Math.min(Math.max(Math.round(props.start), 0), props.max))

// ---- numbers as the slides write them -------------------------------------
function fmt(x, nd) {
  let s = x.toFixed(nd)
  if (Number(s) === 0) s = s.replace('-', '')
  return s.replace('-', '\u2212')
}
const tenths = (x) => Math.round(x * 10)

const ratio = computed(() => {
  const v = props.values.map(tenths)
  const first = v[0]
  const last = v[v.length - 1]
  const a = first - 10 * axis.value
  const e = last - 10 * axis.value
  return {
    barFirst: fmt(a / 10, 1),
    barLast: fmt(e / 10, 1),
    bars: fmt(a / e, 2),
    valFirst: fmt(first / 10, 1),
    valLast: fmt(last / 10, 1),
    vals: fmt(first / last, 2),
  }
})

// Stops under the slider: every 10, and the end.
const stops = computed(() => {
  const s = []
  for (let v = 0; v < props.max; v += 10) if (props.max - v >= 5) s.push(v)
  s.push(props.max)
  return s
})

// ---- geometry ---------------------------------------------------------------
const plot = ref(null)
const size = ref({ w: 0, h: 0 })
const M = { l: 58, r: 8, t: 26, b: 34 }

const geo = computed(() => {
  const { w, h } = size.value
  if (w < 120 || h < 90) return null
  const pw = w - M.l - M.r
  const ph = h - M.t - M.b
  const lo = axis.value
  const span = props.top - lo
  const y = (v) => M.t + (1 - (v - lo) / span) * ph
  const rough = span / 6
  const mag = 10 ** Math.floor(Math.log10(rough))
  const n = rough / mag
  const step = (n <= 1 ? 1 : n <= 2 ? 2 : n <= 5 ? 5 : 10) * mag
  const ticks = [{ v: lo, y: y(lo), label: fmt(lo, 0), start: true }]
  for (let v = Math.ceil(lo / step) * step; v <= props.top + 1e-9; v += step) {
    if (v - lo >= step / 2) ticks.push({ v, y: y(v), label: fmt(v, 0) })
  }
  const slot = pw / props.values.length
  const bw = Math.min(slot * 0.56, 90)
  const bars = props.values.map((v, i) => {
    const cx = M.l + slot * (i + 0.5)
    const yt = y(v)
    return { cx, x: cx - bw / 2, w: bw, y: yt, h: y(lo) - yt, value: fmt(v, 1), label: props.labels[i] ?? '' }
  })
  return { w, h, pw, ph, ticks, bars, base: y(lo) }
})

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
function pick(v) { axis.value = v }

let ro = null
onMounted(() => {
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
    <section class="ix asb">
      <div ref="plot" class="ix-plot">
        <svg v-if="geo" class="ix-svg" :viewBox="`0 0 ${geo.w} ${geo.h}`" role="img"
          :aria-label="`Bar chart, value axis from ${axis} to ${top}`">
          <g class="ix-grid">
            <line v-for="t in geo.ticks" :key="`g${t.v}`" :x1="M.l" :x2="geo.w - M.r" :y1="t.y" :y2="t.y" />
          </g>
          <g class="ix-ticks ix-yticks">
            <text v-for="t in geo.ticks" :key="`y${t.v}`" :x="M.l - 8" :y="t.y" dy="0.35em"
              :class="{ 'asb-start': t.start && axis > 0 }">{{ t.label }}</text>
          </g>
          <g class="asb-bars">
            <rect v-for="b in geo.bars" :key="b.label" :x="b.x" :y="b.y" :width="b.w" :height="Math.max(b.h, 0)" />
          </g>
          <g class="asb-values">
            <text v-for="b in geo.bars" :key="`v${b.label}`" :x="b.cx" :y="b.y - 8">{{ b.value }}</text>
          </g>
          <line class="ix-axis" :class="{ 'asb-cut': axis > 0 }" :x1="M.l" :x2="geo.w - M.r" :y1="geo.base" :y2="geo.base" />
          <g class="ix-ticks ix-xticks">
            <text v-for="b in geo.bars" :key="`x${b.label}`" :x="b.cx" :y="geo.base + 22">{{ b.label }}</text>
          </g>
          <text class="ix-axis-label" :transform="`translate(15 ${M.t + geo.ph / 2}) rotate(-90)`">{{ ylabel }}</text>
        </svg>
      </div>

      <div class="asb-panel">
        <div class="ix-control">
          <div class="ix-label">Axis starts at <span class="ix-value">{{ axis }}</span></div>
          <div class="ix-slider">
            <input
              v-model.number="axis"
              class="ix-range"
              type="range"
              min="0"
              :max="max"
              step="1"
              aria-label="Where the value axis starts"
              @pointerdown.stop="releaseOnPointerUp"
              @keydown.esc="$event.target.blur()"
            >
            <div class="ix-stops" aria-hidden="true">
              <span
                v-for="v in stops"
                :key="v"
                class="ix-stop"
                :class="{ on: v === axis }"
                :style="{ left: `calc(11px + (100% - 22px) * ${v / max})` }"
                @pointerdown.stop.prevent="pick(v)"
              >{{ v }}</span>
            </div>
          </div>
        </div>

        <div class="asb-stat" aria-live="polite">
          <div class="ix-label">First bar ÷ last bar</div>
          <div class="asb-big" :class="axis > 0 ? 'asb-warn' : 'asb-ok'">{{ ratio.bars }} times</div>
          <div class="asb-sum">{{ ratio.barFirst }} ÷ {{ ratio.barLast }}</div>
        </div>
        <div class="asb-stat">
          <div class="ix-label">First value ÷ last value</div>
          <div class="asb-big">{{ ratio.vals }} times</div>
          <div class="asb-sum">{{ ratio.valFirst }} ÷ {{ ratio.valLast }}</div>
        </div>
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
  min-height: 0;
  font-family: var(--font-sans);
  color: var(--fg);
}
.asb {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 15.5rem;
  grid-template-rows: minmax(0, 1fr);
  gap: 1.5rem;
}
.ix-plot { position: relative; min-height: 0; }
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
.ix-axis.asb-cut { stroke: var(--warn); stroke-width: 1.5; }
.ix-ticks text { fill: var(--dim); font-size: 13px; font-variant-numeric: tabular-nums; }
.ix-yticks text { text-anchor: end; }
.ix-yticks text.asb-start { fill: var(--warn); }
.ix-xticks text { text-anchor: middle; fill: var(--fg-2); }
.ix-axis-label { fill: var(--fg-2); font-size: 14px; text-anchor: middle; }
.asb-bars rect { fill: var(--accent); }
.asb-values text {
  fill: var(--fg);
  font-size: 14px;
  text-anchor: middle;
  font-variant-numeric: tabular-nums;
}

.asb-panel {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  min-height: 0;
  padding-top: 0.2rem;
}
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

.asb-stat {
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
  padding-top: 0.7rem;
  border-top: 1px solid var(--hair);
}
.asb-big {
  font-size: 1.6rem;
  font-weight: 500;
  line-height: 1.2;
  letter-spacing: -0.01em;
  font-variant-numeric: tabular-nums;
  color: var(--fg);
}
.asb-big.asb-warn { color: var(--warn); }
.asb-big.asb-ok { color: var(--ok); }
.asb-sum {
  font-size: 0.95rem;
  color: var(--fg-2);
  font-variant-numeric: tabular-nums;
}
</style>
