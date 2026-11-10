<!--
  MeanSpread — how far the mean of N random hours strays: s/√N.

    <MeanSpread />                        N = 1 at the start
    <MeanSpread :n="100" />               another N at the start
    <MeanSpread :n="16" zoom />           start zoomed in on the means
    <MeanSpread class="fig-fill" />       on a `class: fill` slide

  Top: every measured hour (87 552) and the N hours of one draw. Bottom: the
  means of 1000 draws of N hours each, with the Gaussian of width s/√N.
  Readout: the spread of those 1000 means beside s/√N = 8.85/√N.
  Draws are seeded by N and by how often "draw again" was pressed, so every
  view is reproducible; figures/src/interactive_data.py repeats the same
  draws in Python and prints the same spreads.

  Data: public/data/hour_temps.json (every hour as a count per 0.1 °C).
  In presenter mode the audience window follows (BroadcastChannel).

  The two panels have the look of the static figures (figures/src/style.py):
  STIX type, a closed frame each, ticks pointing in at the top and bottom
  with minor ticks (no count axis, so no ticks at the sides), each histogram
  as a light fill under a thin outline (handson.py's _paper_hist)
  (./figure-look/figure-look.css).
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
// Three significant figures for a spread: 8.85, 0.885, 0.0299.
function fmt3(v) {
  const a = Math.abs(v)
  return fmt(v, a >= 10 ? 1 : a >= 1 ? 2 : a >= 0.1 ? 3 : 4)
}
// The generator of figures/src/interactive_data.py, bit for bit.
function mulberry32(seed) {
  let a = seed | 0
  return () => {
    a = (a + 0x6D2B79F5) | 0
    let t = Math.imul(a ^ (a >>> 15), 1 | a)
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296
  }
}
const seedOf = (n, draw) => n * 7919 + draw * 104729 + 1
// 1 2 5 steps for an axis.
function niceStep(span, count) {
  const raw = span / count
  const p = 10 ** Math.floor(Math.log10(raw))
  const m = raw / p
  return (m < 1.5 ? 1 : m < 3.5 ? 2 : m < 7.5 ? 5 : 10) * p
}
</script>

<script setup>
import { computed, nextTick, onBeforeUnmount, onMounted, ref, shallowRef, watch } from 'vue'
import { useSlideContext } from '@slidev/client'
import './figure-look/figure-look.css'

const props = defineProps({
  // Hours in each mean at the start (1 … 1000).
  n: { type: Number, default: 1 },
  // Means in the histogram.
  samples: { type: Number, default: 1000 },
  // Start zoomed in on the means.
  zoom: { type: Boolean, default: false },
  src: { type: String, default: 'data/hour_temps.json' },
  syncId: { type: String, default: '' },
})

const N_MAX = 1000
const CHIPS = [1, 4, 16, 100, 1000]
const FD = [-17, 33]                    // the full temperature axis, °C
const clamp = (v, lo, hi) => Math.min(hi, Math.max(lo, v))
const reduceMotion = typeof window !== 'undefined'
  && window.matchMedia?.('(prefers-reduced-motion: reduce)').matches

// ---- data: every hour, sorted ---------------------------------------------------------
const values = shallowRef(null)        // Float64Array of every measured hour
const pop = shallowRef(null)           // { n, mean, sd, bins: [{x0, count}] }
const loadError = ref('')
fetchJSON(import.meta.env.BASE_URL + props.src)
  .then((d) => {
    const lo = Math.round(d.min * 10)
    const total = d.counts.reduce((s, c) => s + c, 0)
    const v = new Float64Array(total)
    let k = 0
    d.counts.forEach((c, j) => { const x = (lo + j) / 10; for (let r = 0; r < c; r++) v[k++] = x })
    let s = 0
    for (let i = 0; i < total; i++) s += v[i]
    const mean = s / total
    let ss = 0
    for (let i = 0; i < total; i++) ss += (v[i] - mean) ** 2
    const bins = []
    for (let x0 = FD[0]; x0 < FD[1]; x0++) bins.push({ x0, count: 0 })
    for (let i = 0; i < total; i++) {
      const b = Math.floor(v[i]) - FD[0]
      if (b >= 0 && b < bins.length) bins[b].count++
    }
    values.value = v
    pop.value = { n: total, mean, sd: Math.sqrt(ss / (total - 1)), bins }
  })
  .catch((e) => { loadError.value = String(e.message || e) })
const ready = computed(() => !!pop.value)

// ---- state ------------------------------------------------------------------------------------
const N = ref(clamp(Math.round(props.n), 1, N_MAX))
const draws = ref({})                  // N → how often "draw again" was pressed
const draw = computed(() => draws.value[N.value] || 0)
const zoomed = ref(props.zoom)
let touched = false

// One batch: `samples` means of N hours, and the hours of the first draw.
const batch = shallowRef(null)
function computeBatch() {
  const v = values.value
  if (!v) return
  const n = N.value
  const m = props.samples
  const rnd = mulberry32(seedOf(n, draw.value))
  const size = v.length
  const means = new Float64Array(m)
  const first = new Float64Array(n)
  for (let i = 0; i < m; i++) {
    let s = 0
    for (let j = 0; j < n; j++) {
      const x = v[Math.floor(rnd() * size)]
      s += x
      if (i === 0) first[j] = x
    }
    means[i] = s / n
  }
  let s = 0
  for (let i = 0; i < m; i++) s += means[i]
  const mm = s / m
  let ss = 0
  for (let i = 0; i < m; i++) ss += (means[i] - mm) ** 2
  batch.value = { n, draw: draw.value, means, first, mean: mm, spread: Math.sqrt(ss / (m - 1)) }
}

// How many of the batch's means are on show (they stream in after "draw again").
const shown = ref(0)
let streamRaf = 0
function stopStream() { if (streamRaf) cancelAnimationFrame(streamRaf); streamRaf = 0 }
function present(stream) {
  computeBatch()
  stopStream()
  if (!batch.value) return
  const m = props.samples
  if (!stream || reduceMotion) { shown.value = m; return }
  shown.value = 0
  const t0 = performance.now()
  const T = 700
  const tick = (now) => {
    const u = Math.min(1, (now - t0) / T)
    shown.value = Math.round(m * (1 - (1 - u) ** 2))
    streamRaf = u < 1 ? requestAnimationFrame(tick) : 0
  }
  streamRaf = requestAnimationFrame(tick)
}
// N moved on the slider: recompute at most once a frame.
let recalc = 0
function scheduleRecalc() {
  if (recalc) return
  recalc = requestAnimationFrame(() => { recalc = 0; present(false) })
}
watch(ready, (r) => { if (r) present(false) }, { immediate: true })

const sigmaN = computed(() => (pop.value ? pop.value.sd / Math.sqrt(N.value) : 1))

// ---- plot geometry ----------------------------------------------------------------------------
const boxRef = ref(null)
const svgRef = ref(null)
const W = ref(0)
const H = ref(0)
const M = { l: 14, r: 14, t: 8, b: 30 }
const GAP = 34
let ro = null
onMounted(() => {
  ro = new ResizeObserver(([e]) => {
    W.value = Math.round(e.contentRect.width)
    H.value = Math.round(e.contentRect.height)
  })
  if (boxRef.value) ro.observe(boxRef.value)
})
const topH = computed(() => Math.round((H.value - M.t - M.b - GAP) * 0.36))
const top0 = M.t
const bot0 = computed(() => M.t + topH.value + GAP)
const botH = computed(() => H.value - M.b - bot0.value)
const sxTop = (x) => M.l + ((x - FD[0]) / (FD[1] - FD[0])) * (W.value - M.l - M.r)

// The bottom axis: the full one, or ±4 s/√N around the mean (it glides between them).
const target = computed(() => {
  if (!zoomed.value || !pop.value) return FD
  const mu = pop.value.mean
  const h = 4 * sigmaN.value
  return [Math.max(FD[0], mu - h), Math.min(FD[1], mu + h)]
})
const BD = ref([...FD])
let zoomRaf = 0
let zoomChanged = false                // set by the zoom button: glide, do not jump
watch(target, (t, old) => {
  if (zoomRaf) cancelAnimationFrame(zoomRaf)
  const glide = !reduceMotion && old && (old[0] !== t[0] || old[1] !== t[1]) && zoomChanged
  zoomChanged = false
  if (!glide) { BD.value = [...t]; return }
  // glide in log-width so the zoom feels even
  const from = [...BD.value]
  const c0 = (from[0] + from[1]) / 2, w0 = from[1] - from[0]
  const c1 = (t[0] + t[1]) / 2, w1 = t[1] - t[0]
  const t0 = performance.now()
  const step = (now) => {
    const u = Math.min(1, (now - t0) / 550)
    const e = 1 - (1 - u) ** 3
    const c = c0 + (c1 - c0) * e
    const w = Math.exp(Math.log(w0) + (Math.log(w1) - Math.log(w0)) * e)
    BD.value = u < 1 ? [c - w / 2, c + w / 2] : [...t]
    zoomRaf = u < 1 ? requestAnimationFrame(step) : 0
  }
  zoomRaf = requestAnimationFrame(step)
}, { immediate: true })
const sxBot = (x) => M.l + ((x - BD.value[0]) / (BD.value[1] - BD.value[0])) * (W.value - M.l - M.r)
const isZoomed = computed(() => BD.value[1] - BD.value[0] < FD[1] - FD[0] - 1e-6)

const ticksFull = [-10, 0, 10, 20, 30]
const ticksBot = computed(() => {
  const [a, b] = BD.value
  const st = niceStep(b - a, 6)
  const out = []
  for (let t = Math.ceil(a / st) * st; t <= b + 1e-9; t += st) out.push(Math.round(t / st) * st)
  return { list: out, step: st, digits: Math.max(0, -Math.floor(Math.log10(st) + 1e-9)) }
})

// Ticks pointing in at the top and bottom of each panel (style.py), minor
// ticks as Matplotlib's AutoMinorLocator: five steps of a major step, four
// when it is a 2 (every 2 °C on the full axis).
const TL = 6.25
const TM = 3.125
function xTicksPath(list, step, lo, hi, sx, y0, y1) {
  const lead = step / 10 ** Math.floor(Math.log10(step) + 1e-9)
  const ms = step / (Math.abs(lead - 2) < 1e-6 ? 4 : 5)
  let major = ''
  let minor = ''
  for (const t of list) major += `M${sx(t).toFixed(2)} ${y1}v${-TL}M${sx(t).toFixed(2)} ${y0}v${TL}`
  for (let k = Math.ceil(lo / ms - 1e-9); k * ms < hi - 1e-9; k++) {
    const v = k * ms
    if (v <= lo + 1e-9 || Math.abs(v / step - Math.round(v / step)) < 1e-6) continue
    minor += `M${sx(v).toFixed(2)} ${y1}v${-TM}M${sx(v).toFixed(2)} ${y0}v${TM}`
  }
  return { major, minor }
}
const frameTicks = computed(() => {
  if (!W.value) return { major: '', minor: '' }
  const t = xTicksPath(ticksFull, 10, FD[0], FD[1], sxTop, top0, top0 + topH.value)
  const [a, b] = BD.value
  const u = xTicksPath(ticksBot.value.list, ticksBot.value.step, a, b, sxBot, bot0.value, bot0.value + botH.value)
  return { major: t.major + u.major, minor: t.minor + u.minor }
})

// Top: the hours, as Matplotlib's histtype "step" (along the top of each
// bin, down to zero at both ends); closed, it is the light fill.
const popPath = computed(() => {
  const p = pop.value
  if (!p || !W.value) return ''
  const max = Math.max(...p.bins.map((b) => b.count))
  const base = top0 + topH.value
  let d = `M${sxTop(p.bins[0].x0).toFixed(1)},${base}`
  for (const b of p.bins) {
    const h = (b.count / max) * (topH.value - 6)
    d += `V${(base - h).toFixed(1)}H${sxTop(b.x0 + 1).toFixed(1)}`
  }
  return `${d}V${base}`
})
// The hours of the first draw, as a rug (at most 1000 ticks).
const rug = computed(() => {
  const B = batch.value
  if (!B || !W.value) return ''
  const y1 = top0 + topH.value + 3
  const y2 = y1 + 9
  let d = ''
  for (let j = 0; j < B.first.length; j++) d += `M${sxTop(B.first[j]).toFixed(1)},${y1}V${y2}`
  return d
})

// Bottom: the means, as a density, with the Gaussian of width s/√N.
const meanBars = computed(() => {
  const B = batch.value
  const p = pop.value
  if (!B || !p || !W.value) return { step: '', curve: '', peak: 1 }
  const sN = sigmaN.value
  const [a, b] = BD.value
  const pxPerDeg = (W.value - M.l - M.r) / (b - a)
  // a third of s/√N, at most the 1 °C of the top panel, never thinner than 3 px
  const bw = Math.max(Math.min(sN / 3, 1), 3 / pxPerDeg)
  const mu = p.mean
  const k0 = Math.floor((a - mu) / bw - 0.5)
  const k1 = Math.ceil((b - mu) / bw + 0.5)
  const nb = k1 - k0 + 1
  const counts = new Uint32Array(nb)
  const m = shown.value
  for (let i = 0; i < m; i++) {
    const k = Math.round((B.means[i] - mu) / bw) - k0
    if (k >= 0 && k < nb) counts[k]++
  }
  const total = props.samples
  const gPeak = 1 / (sN * Math.sqrt(2 * Math.PI))
  let dMax = 0
  for (let k = 0; k < nb; k++) dMax = Math.max(dMax, counts[k] / (total * bw))
  const peak = Math.max(gPeak, dMax) * 1.3
  const sy = (dens) => bot0.value + botH.value - (dens / peak) * (botH.value - 4)
  // The means as a step outline over every bin in view, empty ones included,
  // down to zero at both ends (as the top panel).
  const base = (bot0.value + botH.value).toFixed(1)
  let step = ''
  for (let k = 0; k < nb; k++) {
    const c = mu + (k + k0) * bw
    const x1 = Math.max(sxBot(c - bw / 2), M.l)
    const x2 = Math.min(sxBot(c + bw / 2), W.value - M.r)
    if (x2 <= x1) continue
    if (!step) step = `M${x1.toFixed(1)},${base}`
    step += `V${sy(counts[k] / (total * bw)).toFixed(1)}H${x2.toFixed(1)}`
  }
  if (step) step += `V${base}`
  // the Gaussian, sampled densely around the mean
  const pts = []
  const lo = Math.max(a, mu - 5 * sN)
  const hi = Math.min(b, mu + 5 * sN)
  for (let i = 0; i <= 160; i++) {
    const x = lo + ((hi - lo) * i) / 160
    const g = gPeak * Math.exp(-0.5 * ((x - mu) / sN) ** 2)
    pts.push(`${sxBot(x).toFixed(1)},${sy(g).toFixed(1)}`)
  }
  return { step, curve: `M${pts.join('L')}`, peak }
})
// ±1 spread of the means, measured, as a bracket above the bars.
const bracket = computed(() => {
  const B = batch.value
  if (!B || !W.value || shown.value < props.samples) return null
  const y = bot0.value + 32
  return { x1: sxBot(B.mean - B.spread), x2: sxBot(B.mean + B.spread), y }
})

// ---- controls ----------------------------------------------------------------------------------
const uOf = (n) => Math.log10(n) / 3
const nOf = (u) => clamp(Math.round(10 ** (3 * u)), 1, N_MAX)
function setN(n, stream) {
  n = clamp(Math.round(n), 1, N_MAX)
  if (n === N.value) return
  N.value = n
  touched = true
  action = stream ? 'stream' : 'jump'
  if (stream) present(true)
  else scheduleRecalc()
}
function sliderDown(e) {
  if (!ready.value || (e.pointerType === 'mouse' && e.button !== 0)) return
  e.stopPropagation()
  e.preventDefault()
  const row = e.currentTarget
  const track = row.querySelector('.ims-track')
  const setFrom = (ev) => {
    const r = track.getBoundingClientRect()
    setN(nOf(clamp((ev.clientX - r.left) / r.width, 0, 1)), false)
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
function sliderKey(e) {
  if (!ready.value) return
  let n = N.value
  if (e.key === 'ArrowRight' || e.key === 'ArrowUp') n += 1
  else if (e.key === 'ArrowLeft' || e.key === 'ArrowDown') n -= 1
  else if (e.key === 'PageUp') n = nOf(uOf(n) + 0.1)
  else if (e.key === 'PageDown') n = nOf(uOf(n) - 0.1)
  else if (e.key === 'Home') n = 1
  else if (e.key === 'End') n = N_MAX
  else if (e.key === 'Escape') { e.currentTarget.blur(); return }
  else return
  e.preventDefault()
  e.stopPropagation()
  setN(n, false)
}
function chip(n, e) {
  if (!ready.value) return
  setN(n, true)
  if (e?.detail) e.currentTarget.blur()
}
function drawAgain(e) {
  if (!ready.value) return
  draws.value = { ...draws.value, [N.value]: draw.value + 1 }
  touched = true
  action = 'stream'
  present(true)
  if (e?.detail) e.currentTarget.blur()
}
function toggleZoom(e) {
  zoomChanged = true
  zoomed.value = !zoomed.value
  touched = true
  action = 'jump'
  if (e?.detail) e.currentTarget.blur()
}

const readout = computed(() => {
  const B = batch.value
  const p = pop.value
  if (!B || !p) return null
  return {
    spread: fmt3(B.spread),
    mean: fmt(B.mean, 2),
    s: fmt(p.sd, 2),
    pred: fmt3(p.sd / Math.sqrt(N.value)),
    hours: String(p.n).replace(/\B(?=(\d{3})+(?!\d))/g, ' '),
    mu: fmt(p.mean, 2),
  }
})

// ---- presenter ↔ audience -----------------------------------------------------------------------
const { $page, $renderContext } = useSlideContext()
const instance = Math.random().toString(36).slice(2)
const syncKey = () => `MeanSpread:${$page.value}:${props.syncId}`
let chan = null
let shared = ''
let pending = 0
let action = 'jump'
const stateJSON = () => JSON.stringify({ n: N.value, draw: draw.value, zoom: zoomed.value })
function post(msg) { chan?.postMessage({ key: syncKey(), from: instance, ...msg }) }
watch([N, draw, zoomed], () => {
  if (!chan || pending) return
  pending = requestAnimationFrame(() => {
    pending = 0
    const s = stateJSON()
    if (s === shared) return
    shared = s
    post({ type: 'state', state: s, action })
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
      if (s.zoom !== zoomed.value) { zoomChanged = true; zoomed.value = s.zoom }
      const changed = s.n !== N.value || s.draw !== draw.value
      N.value = s.n
      draws.value = { ...draws.value, [s.n]: s.draw }
      if (changed) present(m.action === 'stream')
    } else if (m.type === 'hello' && touched) {
      post({ type: 'state', state: stateJSON(), action: 'jump' })
    }
  }
  post({ type: 'hello' })
}
watch(ready, (r) => { if (r) nextTick(openSync) }, { immediate: true })

onBeforeUnmount(() => {
  ro?.disconnect()
  stopStream()
  if (recalc) cancelAnimationFrame(recalc)
  if (zoomRaf) cancelAnimationFrame(zoomRaf)
  if (pending) cancelAnimationFrame(pending)
  chan?.close()
  chan = null
})
</script>

<template>
  <section class="ims" :class="{ 'ims-wait': !ready }">
    <figure ref="boxRef" class="ims-plot">
      <svg
        v-if="W > 0 && H > 0"
        ref="svgRef"
        class="ims-svg ixf"
        :width="W"
        :height="H"
        role="img"
        :aria-label="readout ? `Means of ${N} random hours: spread ${readout.spread}, s over root N ${readout.pred}` : 'Loading'"
      >
        <template v-if="ready">
          <!-- top: every hour, on the full axis -->
          <path class="ims-pop-fill" :d="popPath" />
          <path class="ims-pop-step" :d="popPath" />
          <path class="ims-rug" :d="rug" />
          <line class="ims-mu" :x1="sxTop(pop.mean)" :x2="sxTop(pop.mean)" :y1="top0" :y2="top0 + topH" />
          <rect class="ixf-frame" :x="M.l" :y="top0" :width="W - M.l - M.r" :height="topH" />
          <text class="ims-panel ixf-text" :x="M.l + 6" :y="top0 + 12" dominant-baseline="central">every hour · {{ readout?.hours }}</text>
          <text class="ims-panel ims-mulab ixf-text" :x="sxTop(pop.mean) + 6" :y="top0 + 12" dominant-baseline="central">mean {{ readout?.mu }}</text>
          <text class="ims-panel ims-acc ixf-text" :x="M.l + 6" :y="top0 + 30" dominant-baseline="central">{{ N }} drawn</text>

          <!-- the zoom funnel: from the window on the top axis to the bottom panel -->
          <path
            v-if="isZoomed"
            class="ims-funnel"
            :d="`M${sxTop(BD[0])},${top0 + topH + 14}L${M.l},${bot0}M${sxTop(BD[1])},${top0 + topH + 14}L${W - M.r},${bot0}`"
          />
          <rect v-if="isZoomed" class="ims-window" :x="sxTop(BD[0])" :y="top0 + topH + 13" :width="Math.max(2, sxTop(BD[1]) - sxTop(BD[0]))" height="2" />

          <!-- bottom: the means -->
          <path class="ims-means-fill" :d="meanBars.step" />
          <path class="ims-means-step" :d="meanBars.step" />
          <path class="ims-gauss" :d="meanBars.curve" />
          <line class="ims-mu" :x1="sxBot(pop.mean)" :x2="sxBot(pop.mean)" :y1="bot0" :y2="bot0 + botH" />
          <rect class="ixf-frame" :x="M.l" :y="bot0" :width="W - M.l - M.r" :height="botH" />
          <path class="ixf-minor" :d="frameTicks.minor" />
          <path class="ixf-ticks" :d="frameTicks.major" />
          <g v-if="bracket" class="ims-bracket">
            <path :d="`M${bracket.x1},${bracket.y - 5}V${bracket.y + 5}M${bracket.x1},${bracket.y}H${bracket.x2}M${bracket.x2},${bracket.y - 5}V${bracket.y + 5}`" />
            <text class="ixf-text" :x="bracket.x2 + 7" :y="bracket.y" dominant-baseline="central">±{{ readout?.spread }}</text>
          </g>
          <text class="ims-panel ixf-text" :x="M.l + 6" :y="bot0 + 12" dominant-baseline="central">{{ samples }} means of {{ N }} {{ N === 1 ? 'hour' : 'hours' }}</text>

          <g class="ims-ticks">
            <text v-for="t in ticksBot.list" :key="'tb' + t" class="ixf-tl" :x="sxBot(t)" :y="H - M.b + 16" text-anchor="middle">{{ fmt(t, ticksBot.digits) }}</text>
            <text :x="W - M.r" :y="H - M.b + 16" text-anchor="end" class="ixf-tl ims-unit">°C</text>
          </g>
        </template>
        <text v-else-if="loadError" class="ims-msg" :x="W / 2" :y="H / 2" text-anchor="middle">{{ loadError }}</text>
      </svg>
    </figure>

    <aside class="ims-side">
      <div class="ims-n">
        <span class="ims-math"><i>N</i> =</span> <b>{{ N }}</b>
        <span class="ims-label">{{ N === 1 ? 'hour' : 'hours' }} in each mean</span>
      </div>
      <div
        class="ims-slider"
        role="slider"
        tabindex="0"
        aria-label="N, hours in each mean"
        :aria-valuemin="1"
        :aria-valuemax="1000"
        :aria-valuenow="N"
        @pointerdown="sliderDown"
        @mousedown.prevent
        @keydown="sliderKey"
      >
        <span class="ims-track">
          <span class="ims-fill" :style="{ width: `${uOf(N) * 100}%` }" />
          <span v-for="c in CHIPS" :key="'d' + c" class="ims-dec" :style="{ left: `${uOf(c) * 100}%` }" />
          <span class="ims-thumb" :style="{ left: `${uOf(N) * 100}%` }" />
        </span>
      </div>
      <div class="ims-chips">
        <button
          v-for="c in CHIPS"
          :key="c"
          type="button"
          class="ims-chip"
          :class="{ 'ims-chip-on': c === N }"
          :disabled="!ready"
          @mousedown.prevent
          @pointerdown.stop
          @click="chip(c, $event)"
        >{{ c }}</button>
      </div>

      <div v-if="readout" class="ims-nums">
        <div class="ims-row">
          <span class="ims-label">spread of the {{ samples }} means</span>
          <span class="ims-val ims-acc"><b>{{ shown < samples ? '…' : readout.spread }}</b> °C</span>
        </div>
        <div class="ims-row">
          <span class="ims-math"><i>s</i>/√<i>N</i> = {{ readout.s }}/√{{ N }}</span>
          <span class="ims-val"><b>{{ readout.pred }}</b> °C</span>
        </div>
        <div class="ims-row ims-small">
          <span class="ims-label">mean of the means</span>
          <span class="ims-val">{{ shown < samples ? '…' : readout.mean }} °C</span>
        </div>
      </div>

      <div class="ims-buttons">
        <button type="button" class="ims-btn ims-btn-main" :disabled="!ready" @mousedown.prevent @pointerdown.stop @click="drawAgain">draw again</button>
        <button type="button" class="ims-btn" :class="{ 'ims-btn-on': zoomed }" :disabled="!ready" @mousedown.prevent @pointerdown.stop @click="toggleZoom">{{ zoomed ? 'full axis' : 'zoom in' }}</button>
        <span class="ims-label ims-drawno">draw {{ draw + 1 }}</span>
      </div>
    </aside>
  </section>
</template>

<style scoped>
.ims {
  display: grid;
  grid-template-columns: minmax(0, 1.55fr) minmax(0, 1fr);
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
.ims-plot {
  margin: 0;
  min-width: 0;
  min-height: 0;
  position: relative;
  border: 1px solid var(--hair);
  border-radius: 6px;
  background: rgba(255, 255, 255, 0.015);
  overflow: hidden;
}
.ims-svg { position: absolute; inset: 0; display: block; }

/* The plot's type, frames and ticks: ./figure-look/figure-look.css. Each
   histogram as a light fill under a thin outline, as the static ones. */
.ims-pop-fill { fill: var(--fg-2); fill-opacity: 0.3; stroke: none; }
.ims-pop-step { fill: none; stroke: var(--dim); stroke-width: 1.5; }
.ims-rug { stroke: var(--accent); stroke-width: 1; opacity: 0.55; }
.ims-mu { stroke: var(--fg); stroke-width: 1; stroke-dasharray: 2 3; opacity: 0.55; }
.ims-means-fill { fill: var(--accent); fill-opacity: 0.3; stroke: none; }
.ims-means-step { fill: none; stroke: var(--accent); stroke-width: 1.5; }
.ims-gauss { fill: none; stroke: var(--fg); stroke-width: 1.6; opacity: 0.75; }
.ims-bracket path { fill: none; stroke: var(--ok); stroke-width: 1.6; }
.ims-bracket text { fill: var(--ok); }
.ims-funnel { fill: none; stroke: var(--hair-strong); stroke-width: 1; stroke-dasharray: 3 3; }
.ims-window { fill: var(--accent); }
.ims-panel { fill: var(--dim); }
.ims-panel.ims-acc { fill: var(--accent); }
.ims-panel.ims-mulab { fill: var(--fg-2); }
.ims-msg { fill: var(--warn); font-size: 13px; }

.ims-side {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 0.45rem;
  min-width: 0;
  min-height: 0;
}
.ims-math {
  font-family: KaTeX_Main, 'Times New Roman', serif;
  font-size: 1.21em;
  white-space: nowrap;
}
.ims-math i {
  font-family: KaTeX_Math, 'Times New Roman', serif;
  font-style: italic;
}
.ims-n { display: flex; align-items: baseline; gap: 0.5rem; white-space: nowrap; }
.ims-n .ims-math { font-size: 1.5rem; }
.ims-n b { font-size: 1.875rem; font-weight: 500; color: var(--accent); letter-spacing: -0.01em; min-width: 2.6ch; }
.ims-label { font-size: 0.875rem; letter-spacing: 0.05em; color: var(--dim); white-space: nowrap; }

.ims-slider {
  display: flex;
  align-items: center;
  height: 2rem;
  padding: 0 7px;
  cursor: pointer;
  touch-action: none;
  outline: none;
  border-radius: 4px;
}
.ims-slider:focus-visible { box-shadow: 0 0 0 1px var(--hair-strong); }
.ims-track { position: relative; flex: 1; height: 2px; background: var(--hair-strong); border-radius: 1px; }
.ims-fill { position: absolute; left: 0; top: 0; bottom: 0; background: var(--accent); opacity: 0.55; }
.ims-dec { position: absolute; top: -4px; bottom: -4px; width: 0; border-left: 1px solid var(--dim); opacity: 0.7; }
.ims-thumb {
  position: absolute;
  top: 50%;
  width: 18px;
  height: 18px;
  margin: -9px 0 0 -9px;
  border-radius: 50%;
  background: var(--accent);
  transition: transform 0.25s var(--ease);
}
.ims-slider:hover .ims-thumb,
.ims-slider:focus-visible .ims-thumb { transform: scale(1.2); }

.ims-chips { display: flex; gap: 0.4rem; }
.ims-chip {
  flex: 1;
  font-family: var(--font-sans);
  font-size: 0.95rem;
  font-variant-numeric: tabular-nums;
  color: var(--fg-2);
  background: none;
  border: 1px solid var(--hair-strong);
  border-radius: 4px;
  padding: 0.28rem 0;
  cursor: pointer;
  transition: color 0.3s var(--ease), border-color 0.3s var(--ease);
}
.ims-chip:hover:not(:disabled),
.ims-chip:focus-visible { color: var(--accent); border-color: var(--accent); outline: none; }
.ims-chip-on { color: var(--accent); border-color: var(--accent); }

.ims-nums { display: flex; flex-direction: column; gap: 0.3rem; border-top: 1px solid var(--hair); padding-top: 0.5rem; }
.ims-row { display: flex; justify-content: space-between; align-items: baseline; gap: 0.6rem; }
.ims-val { white-space: nowrap; color: var(--dim); font-size: 0.95rem; }
.ims-val b { font-size: 1.25rem; font-weight: 500; color: var(--fg); }
.ims-val.ims-acc b { color: var(--ok); }
.ims-small .ims-val { font-size: 0.875rem; }

.ims-buttons { display: flex; align-items: center; gap: 0.6rem; }
.ims-drawno { margin-left: auto; }
.ims-btn {
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
.ims-btn:hover:not(:disabled),
.ims-btn:focus-visible { color: var(--accent); border-color: var(--accent); outline: none; }
.ims-btn-main { color: var(--accent); border-color: color-mix(in srgb, var(--accent) 55%, transparent); }
.ims-btn-on { color: var(--accent); }
.ims-btn:disabled,
.ims-chip:disabled { opacity: 0.4; cursor: default; }

.ims-wait .ims-side { opacity: 0.35; }

@media (prefers-reduced-motion: reduce) {
  .ims-thumb,
  .ims-chip,
  .ims-btn { transition: none; }
}
</style>
