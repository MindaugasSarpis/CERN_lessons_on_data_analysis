<!--
  PerceptronPlayground — one neuron on the frost question, weights by hand.

    <PerceptronPlayground />                                  w = (−1, 0), b = 3.8: "below 3.8 °C"
    <PerceptronPlayground :w1="0" :w2="0" :b="-1" />          start from "never frost"
    <PerceptronPlayground :w1="-1" :w2="4" :b="0.6" />        Lecture 10's tilted neuron
    <PerceptronPlayground evening="2025-12-06" />             the evening pushed through z at the start
    <PerceptronPlayground class="fig-fill" />                 on a `class: fill` slide

  As in Lecture 10: each evening is a point, x₁ the temperature at 18:00
  (°C) and x₂ the humidity at 18:00 as a fraction (85 % → 0.85), coloured by
  frost at 06:00 the next morning. z = w₁x₁ + w₂x₂ + b; the neuron says
  "frost" when z > 0 (z = 0 is "no frost"), so its boundary is the line
  z = 0 and the tinted side is "frost". Right and wrong are counted over all
  3646 evenings, as the lecture counts them (66.3 % never frost, 91.6 % below
  2 °C, 95.7 % below 3.8 °C); about 300 are drawn, among them every evening
  the lecture names (6–9 Dec 2025, 1, 10 and 11 Jan 2016). Tap an evening
  to push its numbers through z. w₁, w₂ and b move in steps of 0.01, 0.01
  and 0.1, and z is computed exactly (to four decimals), so every number
  shown is the number used and an evening at z = 0 is never frost.

  Data: public/data/frost_evenings.json (figures/src/interactive_data.py).
  In presenter mode the audience window follows (BroadcastChannel).
-->
<script>
const files = new Map()
function fetchJSON(url) {
  if (!files.has(url)) {
    files.set(url, fetch(url).then((r) => {
      if (!r.ok) throw new Error(`${url}: HTTP ${r.status}`)
      return r.json()
    }))
  }
  return files.get(url)
}
function fmt(v, d) {
  const s = Number(v).toFixed(d)
  return (/^-0\.?0*$/.test(s) ? s.slice(1) : s).replace('-', '−')
}
const MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
function niceDate(iso) {
  const [y, m, d] = iso.split('-').map(Number)
  return `${d} ${MONTHS[m - 1]} ${y}`
}
</script>

<script setup>
import { computed, nextTick, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useSlideContext } from '@slidev/client'

const props = defineProps({
  // The starting neuron: Lecture 10's "below 3.8 °C".
  w1: { type: Number, default: -1 },
  w2: { type: Number, default: 0 },
  b: { type: Number, default: 3.8 },
  // The evening (its date) pushed through z at the start: one of the drawn
  // evenings, else the first drawn one after it.
  evening: { type: String, default: '2025-12-08' },
  src: { type: String, default: 'data/frost_evenings.json' },
  syncId: { type: String, default: '' },
})

const RANGE = { w1: [-2, 2, 0.01], w2: [-10, 10, 0.01], b: [-10, 10, 0.1] }
const q1 = (v) => Math.round(v * 100) / 100
const q2 = (v) => Math.round(v * 100) / 100
const q3 = (v) => Math.round(v * 10) / 10
// An exact number as the slides write a sum: no trailing zeros (−2.6, 0, 3.4).
function tidy(v, d) {
  const t = fmt(v, d)
  return t.includes('.') ? t.replace(/0+$/, '').replace(/\.$/, '') : t
}
const clamp = (v, lo, hi) => Math.min(hi, Math.max(lo, v))

// ---- data -------------------------------------------------------------------------
const D = ref(null)
const loadError = ref('')
fetchJSON(import.meta.env.BASE_URL + props.src)
  .then((d) => { D.value = d; if (!touched) start() })
  .catch((e) => { loadError.value = String(e.message || e) })
const ready = computed(() => !!D.value)

// ---- the weights and the chosen evening ------------------------------------------------
const w1 = ref(q1(props.w1))
const w2 = ref(q2(props.w2))
const b = ref(q3(props.b))
const sel = ref(0)                       // position in D.shown
let touched = false

// The evening asked for, or the first drawn one on or after its date.
function start() {
  const dates = D.value.date
  const k = dates.findIndex((d) => d >= props.evening)
  sel.value = k >= 0 ? k : dates.length - 1
}

// z of one evening. w₁x₁ has three decimals, w₂x₂ four, b one, so z rounded
// to four decimals is z exactly: the verdict shown and the one counted agree,
// and an evening at z = 0 is "no frost", as the lecture's rule says.
const zOf = (x1, x2) => Math.round((w1.value * x1 + w2.value * x2 + b.value) * 1e4) / 1e4

// Every evening counts: right and wrong over all of them.
const score = computed(() => {
  const d = D.value
  if (!d) return null
  let right = 0, frost = 0
  const n = d.x1.length
  for (let i = 0; i < n; i++) {
    const p = zOf(d.x1[i], d.x2[i]) > 0
    if (p === (d.y[i] === 1)) right++
    frost += d.y[i]
  }
  return { n, right, acc: right / n, base: (n - frost) / n, baseRight: n - frost }
})

// The drawn evenings.
const pts = computed(() => {
  const d = D.value
  if (!d) return []
  return d.shown.map((i, k) => {
    const z = zOf(d.x1[i], d.x2[i])
    const y = d.y[i] === 1
    return { k, t: d.x1[i], h: d.x2[i], y, right: (z > 0) === y }
  })
})

// The chosen evening pushed through z.
const push = computed(() => {
  const d = D.value
  if (!d) return null
  const k = sel.value
  const i = d.shown[k]
  const x1 = d.x1[i]
  const x2 = d.x2[i]
  const p1 = Math.round(w1.value * x1 * 1e3) / 1e3
  const p2 = Math.round(w2.value * x2 * 1e4) / 1e4
  const z = zOf(x1, x2)
  const frost = z > 0
  const truth = d.y[i] === 1
  // As Lecture 10 writes it: z = (−1)(2.6) + (0)(0.85) + 3.8 = −2.6 + 0 + 3.8 = 1.2
  const term = (v, dd) => (v < 0 ? `(${tidy(v, dd)})` : tidy(v, dd))
  return {
    date: niceDate(d.date[k]),
    x1: tidy(x1, 1), x2: tidy(x2, 2), m: fmt(d.m[k], 1),
    w1: tidy(w1.value, 2), w2: tidy(w2.value, 2),
    bSign: b.value < 0 ? '−' : '+',
    bAbs: tidy(Math.abs(b.value), 1),
    p1: tidy(p1, 3), p2: term(p2, 4),
    z: tidy(z, 4), frost, truth, right: frost === truth,
  }
})

// ---- plot geometry ------------------------------------------------------------------------
const boxRef = ref(null)
const svgRef = ref(null)
const W = ref(0)
const H = ref(0)
const M = { l: 48, r: 14, t: 24, b: 46 }
const TD = [-12, 30]                      // x₁, °C
const HD = [0.4, 1]                       // x₂, a fraction
let ro = null
onMounted(() => {
  ro = new ResizeObserver(([e]) => {
    W.value = Math.round(e.contentRect.width)
    H.value = Math.round(e.contentRect.height)
  })
  if (boxRef.value) ro.observe(boxRef.value)
})
const sx = (t) => M.l + ((t - TD[0]) / (TD[1] - TD[0])) * (W.value - M.l - M.r)
const sy = (h) => H.value - M.b - ((h - HD[0]) / (HD[1] - HD[0])) * (H.value - M.t - M.b)
const tTicks = [-10, 0, 10, 20, 30]
const hTicks = [0.4, 0.6, 0.8, 1]

// The side z > 0 of the plot: the rectangle clipped by the half-plane.
const f = (T, Hh) => w1.value * T + w2.value * Hh + b.value
const region = computed(() => {
  const rect = [[TD[0], HD[0]], [TD[1], HD[0]], [TD[1], HD[1]], [TD[0], HD[1]]]
  const out = []
  for (let i = 0; i < 4; i++) {
    const P = rect[i]
    const Q = rect[(i + 1) % 4]
    const fp = f(...P)
    const fq = f(...Q)
    if (fp > 0) out.push(P)
    if ((fp > 0) !== (fq > 0)) {
      const u = fp / (fp - fq)
      out.push([P[0] + u * (Q[0] - P[0]), P[1] + u * (Q[1] - P[1])])
    }
  }
  return out
})
const regionPath = computed(() => {
  if (!W.value || region.value.length < 3) return ''
  return `M${region.value.map(([T, Hh]) => `${sx(T).toFixed(1)},${sy(Hh).toFixed(1)}`).join('L')}Z`
})
// The boundary z = 0 inside the plot.
const boundary = computed(() => {
  if (w1.value === 0 && w2.value === 0) return null
  const pts2 = []
  const edges = [
    [TD[0], null], [TD[1], null], [null, HD[0]], [null, HD[1]],
  ]
  for (const [T, Hh] of edges) {
    if (T !== null && w2.value !== 0) {
      const hh = -(w1.value * T + b.value) / w2.value
      if (hh >= HD[0] - 1e-9 && hh <= HD[1] + 1e-9) pts2.push([T, hh])
    }
    if (Hh !== null && w1.value !== 0) {
      const tt = -(w2.value * Hh + b.value) / w1.value
      if (tt >= TD[0] - 1e-9 && tt <= TD[1] + 1e-9) pts2.push([tt, Hh])
    }
  }
  if (pts2.length < 2) return null
  // the two points farthest apart (corners can repeat)
  let best = null, bd = -1
  for (let i = 0; i < pts2.length; i++) {
    for (let j = i + 1; j < pts2.length; j++) {
      const d = Math.hypot(sx(pts2[i][0]) - sx(pts2[j][0]), sy(pts2[i][1]) - sy(pts2[j][1]))
      if (d > bd) { bd = d; best = [pts2[i], pts2[j]] }
    }
  }
  if (bd <= 1e-6) return null
  return { x1: sx(best[0][0]), y1: sy(best[0][1]), x2: sx(best[1][0]), y2: sy(best[1][1]) }
})
// "frost" / "no frost" are written in the band of 40-50 % humidity, where no
// evening lies, in the middle of each side's stretch of that band.
const LAB_H = 0.45
const labels = computed(() => {
  if (!W.value) return []
  const y = sy(LAB_H)
  const c = w2.value * LAB_H + b.value            // z = w1·T + c along the band
  let yes                                        // the stretch of T where z > 0
  if (w1.value === 0) yes = c > 0 ? [TD[0], TD[1]] : null
  else {
    const t0 = -c / w1.value
    yes = w1.value > 0 ? [Math.max(t0, TD[0]), TD[1]] : [TD[0], Math.min(t0, TD[1])]
    if (yes[1] <= yes[0]) yes = null
  }
  const no = !yes ? [TD[0], TD[1]]
    : yes[0] > TD[0] ? [TD[0], yes[0]]
    : yes[1] < TD[1] ? [yes[1], TD[1]] : null
  const out = []
  for (const [span, text, cls] of [[yes, 'frost', 'ipp-lab-yes'], [no, 'no frost', 'ipp-lab-no']]) {
    if (span && sx(span[1]) - sx(span[0]) > 90) out.push({ text, cls, x: (sx(span[0]) + sx(span[1])) / 2, y })
  }
  return out
})

// ---- pointer: tap an evening ---------------------------------------------------------------
const cursor = ref('default')
function toSvg(e) {
  const m = svgRef.value?.getScreenCTM()
  if (!m) return null
  const p = new DOMPoint(e.clientX, e.clientY).matrixTransform(m.inverse())
  return { x: p.x, y: p.y, k: m.a || 1 }
}
function nearest(p) {
  let best = -1, bd = Infinity
  for (const q of pts.value) {
    const d = Math.hypot(p.x - sx(q.t), p.y - sy(q.h))
    if (d < bd) { bd = d; best = q.k }
  }
  return { k: best, d: bd }
}
function onDown(e) {
  if (!ready.value || (e.pointerType === 'mouse' && e.button !== 0)) return
  e.stopPropagation()
  const p = toSvg(e)
  if (!p) return
  const { k, d } = nearest(p)
  const r = (e.pointerType === 'touch' ? 28 : 16) / p.k
  if (k >= 0 && d < Math.max(r, 12)) { sel.value = k; touched = true }
}
function onMove(e) {
  if (e.pointerType !== 'mouse' || !ready.value) return
  const p = toSvg(e)
  if (!p) return
  cursor.value = nearest(p).d < Math.max(16 / p.k, 12) ? 'pointer' : 'default'
}

// ---- sliders ---------------------------------------------------------------------------------
const sliders = computed(() => [
  { key: 'w1', name: 'w', sub: '1', unit: 'per °C', r: RANGE.w1, value: w1.value, text: fmt(w1.value, 2),
    set: (v) => { w1.value = q1(clamp(v, RANGE.w1[0], RANGE.w1[1])) } },
  { key: 'w2', name: 'w', sub: '2', unit: '', r: RANGE.w2, value: w2.value, text: fmt(w2.value, 2),
    set: (v) => { w2.value = q2(clamp(v, RANGE.w2[0], RANGE.w2[1])) } },
  { key: 'b', name: 'b', sub: '', unit: '', r: RANGE.b, value: b.value, text: fmt(b.value, 1),
    set: (v) => { b.value = q3(clamp(v, RANGE.b[0], RANGE.b[1])) } },
])
const frac = (s) => (s.value - s.r[0]) / (s.r[1] - s.r[0])
function sliderDown(e, s) {
  if (e.pointerType === 'mouse' && e.button !== 0) return
  e.stopPropagation()
  e.preventDefault()
  const row = e.currentTarget
  const track = row.querySelector('.ipp-track')
  const setFrom = (ev) => {
    const r = track.getBoundingClientRect()
    const u = clamp((ev.clientX - r.left) / r.width, 0, 1)
    s.set(s.r[0] + u * (s.r[1] - s.r[0]))
    touched = true
  }
  row.setPointerCapture(e.pointerId)
  const move = (ev) => { if (ev.pointerId === e.pointerId) setFrom(ev) }
  const up = (ev) => {
    if (ev.pointerId !== e.pointerId) return
    row.removeEventListener('pointermove', move)
    row.removeEventListener('pointerup', up)
    row.removeEventListener('pointercancel', up)
  }
  row.addEventListener('pointermove', move)
  row.addEventListener('pointerup', up)
  row.addEventListener('pointercancel', up)
  setFrom(e)
}
function sliderKey(e, s) {
  const step = s.r[2]
  const big = (s.r[1] - s.r[0]) / 20
  const map = { ArrowRight: step, ArrowUp: step, ArrowLeft: -step, ArrowDown: -step, PageUp: big, PageDown: -big }
  if (e.key === 'Escape') { e.currentTarget.blur(); return }
  let v
  if (e.key in map) v = s.value + map[e.key]
  else if (e.key === 'Home') v = s.r[0]
  else if (e.key === 'End') v = s.r[1]
  else return
  e.preventDefault()
  e.stopPropagation()
  s.set(v)
  touched = true
}
function setWeights(a1, a2, bb, e) {
  w1.value = q1(a1)
  w2.value = q2(a2)
  b.value = q3(bb)
  touched = true
  if (e?.detail) e.currentTarget.blur()
}

// ---- presenter ↔ audience ---------------------------------------------------------------------
const { $page, $renderContext } = useSlideContext()
const instance = Math.random().toString(36).slice(2)
const syncKey = () => `PerceptronPlayground:${$page.value}:${props.syncId}`
let chan = null
let shared = ''
let pending = 0
const stateJSON = () => JSON.stringify({ w1: w1.value, w2: w2.value, b: b.value, sel: sel.value })
function post(msg) { chan?.postMessage({ key: syncKey(), from: instance, ...msg }) }
watch([w1, w2, b, sel], () => {
  if (!chan || pending) return
  pending = requestAnimationFrame(() => {
    pending = 0
    const s = stateJSON()
    if (s === shared) return
    shared = s
    post({ type: 'state', state: s })
  })
})
function openSync() {
  const ctx = $renderContext?.value
  if (chan || typeof BroadcastChannel === 'undefined' || (ctx !== 'slide' && ctx !== 'presenter')) return
  shared = stateJSON()
  chan = new BroadcastChannel('course-interactive-figures')
  chan.onmessage = ({ data: m }) => {
    if (!m || m.key !== syncKey() || m.from === instance) return
    if (m.type === 'state') {
      shared = m.state
      touched = true
      const s = JSON.parse(m.state)
      w1.value = s.w1
      w2.value = s.w2
      b.value = s.b
      sel.value = s.sel
    } else if (m.type === 'hello' && touched) {
      post({ type: 'state', state: stateJSON() })
    }
  }
  post({ type: 'hello' })
}
watch(ready, (r) => { if (r) nextTick(openSync) }, { immediate: true })

onBeforeUnmount(() => {
  ro?.disconnect()
  if (pending) cancelAnimationFrame(pending)
  chan?.close()
  chan = null
})
</script>

<template>
  <section class="ipp" :class="{ 'ipp-wait': !ready }">
    <figure class="ipp-plot">
      <div ref="boxRef" class="ipp-box">
      <svg
        v-if="W > 0 && H > 0"
        ref="svgRef"
        class="ipp-svg"
        :width="W"
        :height="H"
        :style="{ cursor }"
        role="img"
        :aria-label="score ? `Evenings by temperature and humidity; the neuron is right on ${score.right} of ${score.n}` : 'Loading'"
        @pointerdown="onDown"
        @pointermove="onMove"
      >
        <path v-if="regionPath" class="ipp-region" :d="regionPath" />
        <g class="ipp-grid">
          <line v-for="t in tTicks" :key="'gx' + t" :x1="sx(t)" :x2="sx(t)" :y1="M.t" :y2="H - M.b" />
          <line v-for="h in hTicks" :key="'gy' + h" :x1="M.l" :x2="W - M.r" :y1="sy(h)" :y2="sy(h)" />
        </g>
        <g class="ipp-ticks">
          <text v-for="t in tTicks" :key="'tx' + t" :x="sx(t)" :y="H - M.b + 16" text-anchor="middle" dominant-baseline="central">{{ fmt(t, 0) }}</text>
          <text v-for="h in hTicks" :key="'ty' + h" :x="M.l - 8" :y="sy(h)" text-anchor="end" dominant-baseline="central">{{ fmt(h, 1) }}</text>
          <text class="ipp-axis" :x="(M.l + W - M.r) / 2" :y="H - 9" text-anchor="middle"><tspan class="ipp-axvar">x</tspan><tspan class="ipp-axsub" dy="3">1</tspan><tspan dy="-3"> temperature at 18:00 (°C)</tspan></text>
          <text class="ipp-axis" :x="M.l - 8" :y="M.t - 12" text-anchor="start" dominant-baseline="central"><tspan class="ipp-axvar">x</tspan><tspan class="ipp-axsub" dy="3">2</tspan><tspan dy="-3"> humidity at 18:00</tspan></text>
        </g>
        <template v-if="ready">
          <text v-for="l in labels" :key="l.text" class="ipp-lab" :class="l.cls" :x="l.x" :y="l.y" text-anchor="middle" dominant-baseline="central">{{ l.text }}</text>
          <g class="ipp-pts">
            <circle
              v-for="p in pts"
              :key="p.k"
              :class="[p.y ? 'ipp-yes' : 'ipp-no', p.right ? '' : 'ipp-wrong']"
              :cx="sx(p.t)"
              :cy="sy(p.h)"
              r="3.6"
            />
          </g>
          <line v-if="boundary" class="ipp-boundary" v-bind="boundary" />
          <g v-if="push" class="ipp-sel">
            <line class="ipp-guide" :x1="sx(pts[sel].t)" :x2="sx(pts[sel].t)" :y1="sy(pts[sel].h) + 9" :y2="H - M.b" />
            <line class="ipp-guide" :x1="M.l" :x2="sx(pts[sel].t) - 9" :y1="sy(pts[sel].h)" :y2="sy(pts[sel].h)" />
            <circle :cx="sx(pts[sel].t)" :cy="sy(pts[sel].h)" r="8.5" />
          </g>
        </template>
        <text v-else-if="loadError" class="ipp-msg" :x="W / 2" :y="H / 2" text-anchor="middle">{{ loadError }}</text>
      </svg>
      </div>
      <figcaption class="ipp-key">
        <span><i class="ipp-dot ipp-yes" /> frost at 06:00</span>
        <span><i class="ipp-dot ipp-no" /> no frost</span>
        <span><i class="ipp-dot ipp-ring" /> neuron wrong</span>
        <span v-if="score" class="ipp-shown">{{ pts.length }} of {{ score.n }} evenings</span>
      </figcaption>
    </figure>

    <aside class="ipp-side">
      <div class="ipp-expr">
        <span class="ipp-math"><i>z</i> = <i class="ipp-k">w</i><sub>1</sub><i>x</i><sub>1</sub> + <i class="ipp-k">w</i><sub>2</sub><i>x</i><sub>2</sub> + <i class="ipp-k">b</i></span>
        <span class="ipp-rule">frost if <i>z</i> &gt; 0</span>
      </div>

      <div v-if="push" class="ipp-push">
        <div class="ipp-label"><span class="ipp-on">{{ push.date }}</span> · 18:00 · <i class="ipp-var">x</i><sub>1</sub> = {{ push.x1 }} °C · <i class="ipp-var">x</i><sub>2</sub> = {{ push.x2 }}</div>
        <div class="ipp-math ipp-line">
          <i>z</i> = (<span class="ipp-k">{{ push.w1 }}</span>)({{ push.x1 }}) + (<span class="ipp-k">{{ push.w2 }}</span>)({{ push.x2 }}) {{ push.bSign }} <span class="ipp-k">{{ push.bAbs }}</span>
        </div>
        <div class="ipp-math ipp-line">
          = {{ push.p1 }} + {{ push.p2 }} {{ push.bSign }} {{ push.bAbs }} = <b :class="push.frost ? 'ipp-yes-t' : 'ipp-no-t'">{{ push.z }}</b>
          <span class="ipp-verdict" :class="push.frost ? 'ipp-yes-t' : 'ipp-no-t'">{{ push.frost ? '> 0 → frost' : '≤ 0 → no frost' }}</span>
        </div>
        <div class="ipp-label">06:00 next morning {{ push.m }} °C · {{ push.truth ? 'frost' : 'no frost' }} · <b :class="push.right ? 'ipp-ok' : 'ipp-bad'">{{ push.right ? 'right' : 'wrong' }}</b></div>
      </div>

      <div v-if="score" class="ipp-score">
        <b class="ipp-accnum">{{ fmt(score.acc * 100, 1) }} %</b>
        <div class="ipp-accside">
          <div class="ipp-bar">
            <span class="ipp-barfill" :style="{ width: `${score.acc * 100}%` }" />
            <span class="ipp-base" :style="{ left: `${score.base * 100}%` }" />
          </div>
          <div class="ipp-label ipp-acc">right on {{ score.right }} of {{ score.n }} · <span class="ipp-baselab">never frost {{ fmt(score.base * 100, 1) }} %</span></div>
        </div>
      </div>

      <div class="ipp-controls">
        <div
          v-for="s in sliders"
          :key="s.key"
          class="ipp-slider"
          role="slider"
          tabindex="0"
          :aria-label="s.key"
          :aria-valuemin="s.r[0]"
          :aria-valuemax="s.r[1]"
          :aria-valuenow="s.value"
          :aria-valuetext="`${s.text} ${s.unit}`"
          @pointerdown="sliderDown($event, s)"
          @mousedown.prevent
          @keydown="sliderKey($event, s)"
        >
          <span class="ipp-sname"><i class="ipp-k">{{ s.name }}</i><sub v-if="s.sub">{{ s.sub }}</sub></span>
          <span class="ipp-track">
            <span class="ipp-zero" :style="{ left: `${((0 - s.r[0]) / (s.r[1] - s.r[0])) * 100}%` }" />
            <span class="ipp-thumb" :style="{ left: `${frac(s) * 100}%` }" />
          </span>
          <span class="ipp-sval"><b>{{ s.text }}</b> {{ s.unit }}</span>
        </div>
      </div>

      <div class="ipp-buttons">
        <button type="button" class="ipp-btn" :disabled="!ready" @mousedown.prevent @pointerdown.stop @click="setWeights(0, 0, -1, $event)">never frost</button>
        <button type="button" class="ipp-btn" :disabled="!ready" @mousedown.prevent @pointerdown.stop @click="setWeights(props.w1, props.w2, props.b, $event)">reset</button>
      </div>
    </aside>
  </section>
</template>

<style scoped>
.ipp {
  display: grid;
  grid-template-columns: minmax(0, 1.08fr) minmax(0, 1fr);
  grid-template-rows: minmax(0, 1fr);
  gap: 1.3rem;
  height: 21rem;
  min-height: 0;
  user-select: none;
  -webkit-user-select: none;
  color: var(--fg);
  font-family: var(--font-sans);
  font-variant-numeric: tabular-nums;
}
.ipp-plot {
  margin: 0;
  min-width: 0;
  min-height: 0;
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}
.ipp-box {
  position: relative;
  flex: 1 1 0;
  min-height: 0;
  border: 1px solid var(--hair);
  border-radius: 6px;
  background: rgba(255, 255, 255, 0.015);
  overflow: hidden;
}
.ipp-svg {
  position: absolute;
  inset: 0;
  display: block;
  touch-action: none;
  -webkit-tap-highlight-color: transparent;
}

/* ---- plot ---- */
.ipp-region { fill: var(--accent); opacity: 0.075; }
.ipp-grid line { stroke: var(--hair); stroke-width: 1; }
.ipp-ticks text { fill: var(--dim); font-size: 14px; }
.ipp-ticks .ipp-axis { font-size: 13px; letter-spacing: 0.04em; }
.ipp-ticks .ipp-axvar { font-family: KaTeX_Math, 'Times New Roman', serif; font-style: italic; font-size: 15px; letter-spacing: 0; }
.ipp-ticks .ipp-axsub { font-size: 10px; letter-spacing: 0; }
.ipp-label sub { font-size: 0.75em; line-height: 0; }
.ipp-lab {
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  opacity: 0.8;
  pointer-events: none;
}
.ipp-lab-yes { fill: var(--accent); }
.ipp-lab-no { fill: var(--warn); }
.ipp-pts circle { stroke: none; opacity: 0.62; }
.ipp-pts circle.ipp-yes { fill: var(--accent); }
.ipp-pts circle.ipp-no { fill: var(--warn); }
.ipp-pts circle.ipp-wrong { opacity: 1; stroke: var(--fg); stroke-width: 1.3; }
.ipp-boundary { stroke: var(--fg); stroke-width: 2.2; stroke-linecap: round; }
.ipp-sel circle { fill: none; stroke: var(--fg); stroke-width: 1.6; }
.ipp-guide { stroke: var(--fg-2); stroke-width: 1; stroke-dasharray: 3 4; opacity: 0.7; }
.ipp-msg { fill: var(--warn); font-size: 13px; }

.ipp-key {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.35rem 1rem;
  font-size: 0.8rem;
  letter-spacing: 0.04em;
  color: var(--dim);
}
.ipp-key .ipp-shown { margin-left: auto; }
.ipp-dot {
  display: inline-block;
  width: 9px;
  height: 9px;
  margin-right: 0.3rem;
  border-radius: 50%;
  vertical-align: 0;
}
.ipp-dot.ipp-yes { background: var(--accent); }
.ipp-dot.ipp-no { background: var(--warn); }
.ipp-dot.ipp-ring { border: 1.5px solid var(--fg); background: none; }

/* ---- side panel ---- */
.ipp-side {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 0.4rem;
  min-width: 0;
  min-height: 0;
}
.ipp-math {
  font-family: KaTeX_Main, 'Times New Roman', serif;
  font-size: 1.21em;
  line-height: 1.25;
  white-space: nowrap;
}
.ipp-math i,
.ipp-var,
.ipp-sname {
  font-family: KaTeX_Math, 'Times New Roman', serif;
  font-style: italic;
}
.ipp-math sub,
.ipp-sname sub { font-size: 0.7em; line-height: 0; font-style: normal; font-family: KaTeX_Main, 'Times New Roman', serif; }
.ipp-math b { font-weight: 400; }
.ipp-k { color: var(--accent); }
.ipp-on { color: var(--accent); }
.ipp-expr { display: flex; align-items: baseline; gap: 0.9rem; }
.ipp-expr .ipp-math { font-size: 1.45em; }
.ipp-rule {
  font-size: 0.875rem;
  letter-spacing: 0.06em;
  color: var(--dim);
  white-space: nowrap;
}
.ipp-rule i { font-family: KaTeX_Math, 'Times New Roman', serif; font-style: italic; font-size: 1.15em; letter-spacing: 0; }
.ipp-label {
  font-size: 0.875rem;
  letter-spacing: 0.05em;
  color: var(--dim);
  white-space: nowrap;
}
.ipp-label .ipp-on { font-weight: 600; }
.ipp-var { font-size: 1.1em; letter-spacing: 0; }
.ipp-push { display: flex; flex-direction: column; gap: 0.22rem; }
.ipp-line { font-size: 1.08em; }
.ipp-verdict { font-family: var(--font-sans); font-size: 0.78em; margin-left: 0.4em; }
.ipp-yes-t { color: var(--accent); }
.ipp-no-t { color: var(--warn); }
.ipp-ok { color: var(--ok); font-weight: 600; }
.ipp-bad { color: var(--warn); font-weight: 600; }

.ipp-score { display: grid; grid-template-columns: auto minmax(0, 1fr); align-items: center; gap: 0.9rem; }
.ipp-accnum { font-size: 1.5rem; font-weight: 500; letter-spacing: -0.01em; color: var(--fg); white-space: nowrap; }
.ipp-accside { display: flex; flex-direction: column; gap: 0.3rem; min-width: 0; }
.ipp-acc { font-size: 0.8rem; }
.ipp-bar {
  position: relative;
  height: 8px;
  border-radius: 2px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--hair);
}
.ipp-barfill {
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  background: var(--accent);
  opacity: 0.8;
  transition: width 0.25s var(--ease);
}
.ipp-base {
  position: absolute;
  top: -5px;
  bottom: -5px;
  width: 0;
  border-left: 1.5px solid var(--warn);
}
.ipp-baselab { color: var(--warn); }

.ipp-controls { display: flex; flex-direction: column; }
.ipp-slider {
  display: grid;
  grid-template-columns: 1.6rem minmax(0, 1fr) 7.2rem;
  align-items: center;
  gap: 0.7rem;
  height: 1.8rem;
  cursor: pointer;
  touch-action: none;
  outline: none;
  border-radius: 4px;
}
.ipp-slider:focus-visible { box-shadow: 0 0 0 1px var(--hair-strong); }
.ipp-sname { font-size: 1.25em; text-align: center; }
.ipp-track {
  position: relative;
  height: 2px;
  background: var(--hair-strong);
  border-radius: 1px;
}
.ipp-zero {
  position: absolute;
  top: -4px;
  bottom: -4px;
  width: 0;
  border-left: 1px solid var(--dim);
}
.ipp-thumb {
  position: absolute;
  top: 50%;
  width: 18px;
  height: 18px;
  margin: -9px 0 0 -9px;
  border-radius: 50%;
  background: var(--accent);
  transition: transform 0.25s var(--ease);
}
.ipp-slider:hover .ipp-thumb,
.ipp-slider:focus-visible .ipp-thumb { transform: scale(1.2); }
.ipp-sval { font-size: 0.9rem; color: var(--dim); white-space: nowrap; text-align: right; }
.ipp-sval b { color: var(--fg); font-weight: 500; font-size: 1.05rem; }

.ipp-buttons { display: flex; gap: 0.6rem; }
.ipp-btn {
  font-family: var(--font-sans);
  font-size: 0.875rem;
  font-weight: 500;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--fg-2);
  background: none;
  border: 1px solid var(--hair-strong);
  border-radius: 4px;
  padding: 0.36rem 0.8rem;
  cursor: pointer;
  transition: color 0.3s var(--ease), border-color 0.3s var(--ease);
}
.ipp-btn:hover:not(:disabled),
.ipp-btn:focus-visible { color: var(--accent); border-color: var(--accent); outline: none; }
.ipp-btn:disabled { opacity: 0.4; cursor: default; }

.ipp-wait .ipp-side { opacity: 0.35; }

@media (prefers-reduced-motion: reduce) {
  .ipp-barfill,
  .ipp-thumb,
  .ipp-btn { transition: none; }
}
</style>
