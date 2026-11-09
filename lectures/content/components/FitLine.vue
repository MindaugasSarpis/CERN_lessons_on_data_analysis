<!--
  FitLine — a straight line through points, and its χ² recomputed live.

    <FitLine />                                   the ten yearly means, σ = 0.70
    <FitLine :a="7.16" :b="0" :year="2023" />     the starting line and year
    <FitLine class="fig-fill" />                  on a `class: fill` slide: takes the rest of it
    <FitLine slope-first />                       the line written a·x + b (a the slope,
                                                  b the line in x0), Lecture 9's letters

  χ² = Σ (yᵢ − a − b·xᵢ)² / σ², with x = year − x0 (x0 = 2016, so a is the
  line in 2016 and b its change per year). Drag the line or its two end
  handles, or the sliders; tap a point to push its numbers through the
  expression; "best fit" snaps to the least-squares line. a and b move in
  steps of 0.01 °C and 0.001 °C a year, so every number shown is the number
  used, and the arithmetic can be redone by hand.

  Data: public/data/yearly_means.json (figures/src/interactive_data.py), or
  the `years` / `means` props. In presenter mode the audience window follows
  the presenter's line (BroadcastChannel, same browser).
-->
<script>
// Module scope (runs once per page): every FitLine shares one fetch of a file.
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
// toFixed with a real minus sign and never "−0.00".
function fmt(v, d) {
  const s = Number(v).toFixed(d)
  return (/^-0\.?0*$/.test(s) ? s.slice(1) : s).replace('-', '−')
}
</script>

<script setup>
import { computed, nextTick, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useSlideContext } from '@slidev/client'

const props = defineProps({
  // The points: by default the ten yearly means of the weather log.
  years: { type: Array, default: null },
  means: { type: Array, default: null },
  src: { type: String, default: 'data/yearly_means.json' },
  // σ of every point, °C (the scatter of the ten yearly means).
  sigma: { type: Number, default: 0.7 },
  // x = year − x0, so a is the line in the year x0.
  x0: { type: Number, default: 2016 },
  // The starting line: a in °C (null = the mean of the points), b in °C a year.
  a: { type: Number, default: null },
  b: { type: Number, default: 0 },
  // The year pushed through the expression at the start.
  year: { type: Number, default: 2023 },
  // Two FitLines on one slide need different ids (presenter ↔ audience sync).
  syncId: { type: String, default: '' },
  // Display only: write the line as a·x + b (a the slope, b the line in x0),
  // as Lecture 9 does, instead of a + b·x. The numbers do not change.
  slopeFirst: { type: Boolean, default: false },
})

const B_MAX = 0.4                       // the b slider runs from −0.4 to 0.4 °C a year
const qa = (v) => Math.round(v * 100) / 100
const qb = (v) => Math.round(v * 1000) / 1000
const clamp = (v, lo, hi) => Math.min(hi, Math.max(lo, v))
const reduceMotion = typeof window !== 'undefined'
  && window.matchMedia?.('(prefers-reduced-motion: reduce)').matches

// ---- data --------------------------------------------------------------------
const years = ref([])
const ys = ref([])
const loadError = ref('')
const ready = computed(() => ys.value.length > 1 && years.value.length === ys.value.length)
const X = computed(() => years.value.map((y) => y - props.x0))

// ---- the line and the chosen year ---------------------------------------------
const a = ref(0)
const b = ref(0)
const sel = ref(0)
let touched = false          // changed by a person here or in a synced window

function startLine() {
  const n = ys.value.length
  const mean = ys.value.reduce((s, v) => s + v, 0) / n
  a.value = qa(props.a ?? mean)
  b.value = qb(clamp(props.b, -B_MAX, B_MAX))
  const i = years.value.indexOf(props.year)
  sel.value = i >= 0 ? i : n - 1
}

function useData(yrs, means) {
  ys.value = means.map(Number)
  years.value = yrs ? yrs.map(Number) : means.map((_, i) => props.x0 + i)
  if (!touched) startLine()
}

if (props.means) useData(props.years, props.means)
else {
  fetchJSON(import.meta.env.BASE_URL + props.src)
    .then((d) => useData(props.years ?? d.years, d.means))
    .catch((e) => { loadError.value = String(e.message || e) })
}

const lineAt = (x) => a.value + b.value * x
const s2 = computed(() => props.sigma * props.sigma)
const terms = computed(() => ys.value.map((y, i) => {
  const r = y - a.value - b.value * X.value[i]
  return (r * r) / s2.value
}))
const chi2 = computed(() => terms.value.reduce((s, v) => s + v, 0))

// Least squares, every point with the same σ: the five sums.
const best = computed(() => {
  const x = X.value
  const y = ys.value
  const n = y.length
  let Sx = 0, Sy = 0, Sxx = 0, Sxy = 0
  for (let i = 0; i < n; i++) { Sx += x[i]; Sy += y[i]; Sxx += x[i] * x[i]; Sxy += x[i] * y[i] }
  const bb = (n * Sxy - Sx * Sy) / (n * Sxx - Sx * Sx)
  const aa = (Sy - bb * Sx) / n
  let c = 0
  for (let i = 0; i < n; i++) c += (y[i] - aa - bb * x[i]) ** 2
  return { a: aa, b: bb, chi2: c / s2.value }
})

// ---- the selected year pushed through the expression ---------------------------
const push = computed(() => {
  if (!ready.value) return null
  const i = sel.value
  const y = ys.value[i]
  const x = X.value[i]
  const r = y - a.value - b.value * x
  return {
    year: years.value[i],
    x,
    y: fmt(y, 2),
    a: fmt(a.value, 2),
    b: fmt(b.value, 3),
    bNeg: b.value < 0,
    r: fmt(r, 3),
    rNeg: r < 0,
    s: fmt(props.sigma, 2),
    s2: String(Number(s2.value.toFixed(4))),
    term: fmt(terms.value[i], 2),
  }
})

// ---- plot geometry --------------------------------------------------------------
const boxRef = ref(null)
const svgRef = ref(null)
const W = ref(0)
const H = ref(0)
const M = { l: 46, r: 16, t: 26, b: 30 }
let ro = null
onMounted(() => {
  ro = new ResizeObserver(([e]) => {
    W.value = Math.round(e.contentRect.width)
    H.value = Math.round(e.contentRect.height)
  })
  if (boxRef.value) ro.observe(boxRef.value)
})

const xd = computed(() => [X.value[0] - 0.6, X.value[X.value.length - 1] + 0.6])
const yd = computed(() => {
  if (!ready.value) return [0, 1]
  const lo = Math.min(...ys.value) - props.sigma - 0.3
  const hi = Math.max(...ys.value) + props.sigma + 0.3
  return [Math.floor(lo * 2) / 2, Math.ceil(hi * 2) / 2]
})
const sx = (x) => M.l + ((x - xd.value[0]) / (xd.value[1] - xd.value[0])) * (W.value - M.l - M.r)
const sy = (v) => H.value - M.b - ((v - yd.value[0]) / (yd.value[1] - yd.value[0])) * (H.value - M.t - M.b)
const syInv = (py) => yd.value[0] + ((H.value - M.b - py) / (H.value - M.t - M.b)) * (yd.value[1] - yd.value[0])

const yTicks = computed(() => {
  const out = []
  for (let t = Math.ceil(yd.value[0]); t <= yd.value[1] + 1e-9; t++) out.push(t)
  return out
})
const labelEvery = computed(() => {
  const step = (W.value - M.l - M.r) / (xd.value[1] - xd.value[0])
  return step >= 40 ? 1 : step >= 22 ? 2 : 3
})
const xL = computed(() => X.value[0])
const xR = computed(() => X.value[X.value.length - 1])
const lineEnds = computed(() => ({
  x1: sx(xd.value[0] + 0.25), y1: sy(lineAt(xd.value[0] + 0.25)),
  x2: sx(xd.value[1] - 0.25), y2: sy(lineAt(xd.value[1] - 0.25)),
}))
const perDecade = computed(() => `${b.value > 0 ? '+' : ''}${fmt(b.value * 10, 2)} °C per decade`)

// ---- pointer: drag the line or a handle, tap a point ------------------------------
const cursor = ref('default')
let drag = null

function toSvg(e) {
  const m = svgRef.value?.getScreenCTM()
  if (!m) return null
  const p = new DOMPoint(e.clientX, e.clientY).matrixTransform(m.inverse())
  return { x: p.x, y: p.y, k: m.a || 1 }   // k: screen px per slide px
}
// What sits under the pointer: a handle, a point, the line, or nothing.
function hitTest(p, touch) {
  const r = (touch ? 22 : 12) / p.k
  const hL = { x: sx(xL.value), y: sy(lineAt(xL.value)) }
  const hR = { x: sx(xR.value), y: sy(lineAt(xR.value)) }
  const dL = Math.hypot(p.x - hL.x, p.y - hL.y)
  const dR = Math.hypot(p.x - hR.x, p.y - hR.y)
  if (Math.min(dL, dR) < Math.max(r, 14)) return { kind: dL <= dR ? 'left' : 'right' }
  let best = -1, bd = Infinity
  ys.value.forEach((y, i) => {
    const d = Math.hypot(p.x - sx(X.value[i]), p.y - sy(y))
    if (d < bd) { bd = d; best = i }
  })
  if (bd < Math.max(r, 12)) return { kind: 'point', i: best }
  const xv = xd.value[0] + ((p.x - M.l) / (W.value - M.l - M.r)) * (xd.value[1] - xd.value[0])
  if (Math.abs(p.y - sy(lineAt(xv))) < Math.max(r, 10)) return { kind: 'line' }
  // Anywhere else in the plot: the year of that column.
  let ci = 0, cd = Infinity
  X.value.forEach((x, i) => { const d = Math.abs(p.x - sx(x)); if (d < cd) { cd = d; ci = i } })
  return { kind: 'column', i: ci }
}

function onDown(e) {
  if (!ready.value || (e.pointerType === 'mouse' && e.button !== 0)) return
  e.stopPropagation()                       // no Slidev swipe while dragging
  const p = toSvg(e)
  if (!p) return
  const hit = hitTest(p, e.pointerType === 'touch')
  stopTween()
  if (hit.kind === 'point' || hit.kind === 'column') { sel.value = hit.i; touched = true; return }
  drag = { kind: hit.kind, id: e.pointerId, v0: syInv(p.y), a0: a.value }
  e.currentTarget.setPointerCapture(e.pointerId)
  cursor.value = 'grabbing'
  e.preventDefault()
}
function onMove(e) {
  const p = toSvg(e)
  if (!p) return
  if (!drag) {
    if (e.pointerType !== 'mouse' || !ready.value) return
    const k = hitTest(p, false).kind
    cursor.value = k === 'left' || k === 'right' || k === 'line' ? 'grab' : k === 'point' ? 'pointer' : 'default'
    return
  }
  if (e.pointerId !== drag.id) return
  const v = clamp(syInv(p.y), yd.value[0], yd.value[1])
  const span = xR.value - xL.value
  if (drag.kind === 'line') {
    a.value = qa(clamp(drag.a0 + v - drag.v0, yd.value[0], yd.value[1]))
  } else if (drag.kind === 'left') {
    const vR = lineAt(xR.value)
    const nb = qb(clamp((vR - v) / span, -B_MAX, B_MAX))
    b.value = nb
    a.value = qa(clamp(v - nb * xL.value, yd.value[0], yd.value[1]))
  } else {
    const vL = lineAt(xL.value)
    const nb = qb(clamp((v - vL) / span, -B_MAX, B_MAX))
    b.value = nb
    a.value = qa(clamp(vL - nb * xL.value, yd.value[0], yd.value[1]))
  }
  touched = true
}
function onUp(e) {
  if (drag && e.pointerId === drag.id) {
    drag = null
    cursor.value = e.pointerType === 'mouse' ? 'grab' : 'default'
  }
}
function onLeave() { if (!drag) cursor.value = 'default' }

// ---- sliders (pointer anywhere on the row; keys when focused with Tab) --------------
const sliders = computed(() => {
  const level = {
    key: 'a', label: props.slopeFirst ? 'b' : 'a', unit: '°C', hint: `the line in ${props.x0}`,
    min: yd.value[0], max: yd.value[1], step: 0.01,
    value: a.value, text: fmt(a.value, 2),
    set: (v) => { a.value = qa(clamp(v, yd.value[0], yd.value[1])) },
  }
  const slope = {
    key: 'b', label: props.slopeFirst ? 'a' : 'b', unit: '°C a year', hint: 'change per year',
    min: -B_MAX, max: B_MAX, step: 0.001,
    value: b.value, text: fmt(b.value, 3),
    set: (v) => { b.value = qb(clamp(v, -B_MAX, B_MAX)) },
  }
  return props.slopeFirst ? [slope, level] : [level, slope]
})
const frac = (s) => (s.value - s.min) / (s.max - s.min)

function sliderDown(e, s) {
  if (e.pointerType === 'mouse' && e.button !== 0) return
  e.stopPropagation()
  e.preventDefault()
  stopTween()
  const track = e.currentTarget.querySelector('.ifl-track')
  const setFrom = (ev) => {
    const r = track.getBoundingClientRect()
    const u = clamp((ev.clientX - r.left) / r.width, 0, 1)
    s.set(s.min + u * (s.max - s.min))
    touched = true
  }
  const row = e.currentTarget
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
  const big = (s.max - s.min) / 20
  const map = {
    ArrowRight: s.step, ArrowUp: s.step, ArrowLeft: -s.step, ArrowDown: -s.step,
    PageUp: big, PageDown: -big,
  }
  if (e.key === 'Escape') { e.currentTarget.blur(); return }
  let v
  if (e.key in map) v = s.value + map[e.key]
  else if (e.key === 'Home') v = s.min
  else if (e.key === 'End') v = s.max
  else return
  e.preventDefault()
  e.stopPropagation()                      // arrows move the slider, not the deck
  stopTween()
  s.set(v)
  touched = true
}

// ---- best fit: a short glide to the least-squares line -------------------------------
let tween = 0
function stopTween() { if (tween) cancelAnimationFrame(tween); tween = 0 }
function glideTo(ta, tb) {
  stopTween()
  touched = true
  if (reduceMotion) { a.value = ta; b.value = tb; return }
  const a0 = a.value, b0 = b.value, t0 = performance.now(), T = 650
  const step = (now) => {
    const u = Math.min(1, (now - t0) / T)
    const e = 1 - (1 - u) ** 4
    a.value = u < 1 ? a0 + (ta - a0) * e : ta
    b.value = u < 1 ? b0 + (tb - b0) * e : tb
    tween = u < 1 ? requestAnimationFrame(step) : 0
  }
  tween = requestAnimationFrame(step)
}
function bestFit(e) {
  if (!ready.value) return
  const tb = qb(best.value.b)
  const ta = qa(best.value.a + (best.value.b - tb) * (X.value.reduce((s, x) => s + x, 0) / X.value.length))
  glideTo(ta, tb)
  if (e?.detail) e.currentTarget.blur()
}
function reset(e) {
  if (!ready.value) return
  const n = ys.value.length
  const ta = qa(props.a ?? ys.value.reduce((s, v) => s + v, 0) / n)
  glideTo(ta, qb(clamp(props.b, -B_MAX, B_MAX)))
  if (e?.detail) e.currentTarget.blur()
}

// ---- the χ² bar: one segment per year ----------------------------------------------------
const barMax = computed(() => {
  const c = chi2.value
  return c <= 12 ? 12 : Math.ceil((c * 1.08) / 4) * 4
})
const segments = computed(() => {
  let acc = 0
  return terms.value.map((t, i) => {
    const s = { i, x: acc / barMax.value, w: t / barMax.value }
    acc += t
    return s
  })
})

// ---- presenter ↔ audience: the same slide in another window follows ------------------------
const { $page, $renderContext } = useSlideContext()
const instance = Math.random().toString(36).slice(2)
const syncKey = () => `FitLine:${$page.value}:${props.syncId}`
let chan = null
let shared = ''
let pending = 0
const stateJSON = () => JSON.stringify({ a: a.value, b: b.value, sel: sel.value })
function post(msg) { chan?.postMessage({ key: syncKey(), from: instance, ...msg }) }
watch([a, b, sel], () => {
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
      stopTween()
      shared = m.state
      touched = true
      const s = JSON.parse(m.state)
      a.value = s.a
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
  stopTween()
  if (pending) cancelAnimationFrame(pending)
  chan?.close()
  chan = null
})
</script>

<template>
  <section class="ifl" :class="{ 'ifl-wait': !ready }">
    <figure ref="boxRef" class="ifl-plot">
      <svg
        v-if="W > 0 && H > 0"
        ref="svgRef"
        class="ifl-svg"
        :width="W"
        :height="H"
        :style="{ cursor }"
        role="img"
        :aria-label="ready ? `The ${ys.length} points and the line ${slopeFirst ? `a = ${fmt(b, 3)} a year, b = ${fmt(a, 2)}` : `a = ${fmt(a, 2)}, b = ${fmt(b, 3)}`}; chi-square ${fmt(chi2, 2)}` : 'Loading'"
        @pointerdown="onDown"
        @pointermove="onMove"
        @pointerup="onUp"
        @pointercancel="onUp"
        @pointerleave="onLeave"
      >
        <template v-if="ready">
          <g class="ifl-grid">
            <line v-for="t in yTicks" :key="'g' + t" :x1="M.l" :x2="W - M.r" :y1="sy(t)" :y2="sy(t)" />
          </g>
          <g class="ifl-ticks">
            <text v-for="t in yTicks" :key="'y' + t" :x="M.l - 9" :y="sy(t)" text-anchor="end" dominant-baseline="central">{{ t }}</text>
            <text :x="M.l - 9" :y="M.t - 12" text-anchor="end" dominant-baseline="central" class="ifl-unit">°C</text>
            <template v-for="(yr, i) in years" :key="'x' + yr">
              <line class="ifl-tickmark" :x1="sx(X[i])" :x2="sx(X[i])" :y1="H - M.b" :y2="H - M.b + 4" />
              <text
                v-if="i === sel || i % labelEvery === 0"
                :x="sx(X[i])"
                :y="H - M.b + 17"
                text-anchor="middle"
                dominant-baseline="central"
                :class="{ 'ifl-on': i === sel }"
              >{{ yr }}</text>
            </template>
          </g>
          <!-- ±σ of each point -->
          <g class="ifl-err">
            <line v-for="(y, i) in ys" :key="'e' + i" :x1="sx(X[i])" :x2="sx(X[i])" :y1="sy(y - sigma)" :y2="sy(y + sigma)" />
          </g>
          <!-- residuals: the gap between each point and the line -->
          <g class="ifl-res">
            <line
              v-for="(y, i) in ys"
              :key="'r' + i"
              :class="{ 'ifl-on': i === sel }"
              :x1="sx(X[i])"
              :x2="sx(X[i])"
              :y1="sy(y)"
              :y2="sy(lineAt(X[i]))"
            />
          </g>
          <!-- the chosen residual, with the number the expression squares -->
          <text
            v-if="push"
            class="ifl-rlab"
            :x="sx(X[sel]) + (sel === ys.length - 1 ? -10 : 10)"
            :y="(sy(ys[sel]) + sy(lineAt(X[sel]))) / 2"
            :text-anchor="sel === ys.length - 1 ? 'end' : 'start'"
            dominant-baseline="central"
          >{{ push.r }}</text>
          <line class="ifl-line" :x1="lineEnds.x1" :y1="lineEnds.y1" :x2="lineEnds.x2" :y2="lineEnds.y2" />
          <text class="ifl-trend" :x="W - M.r" :y="M.t - 12" text-anchor="end" dominant-baseline="central">{{ perDecade }}</text>
          <g class="ifl-pts">
            <circle
              v-for="(y, i) in ys"
              :key="'p' + i"
              :class="{ 'ifl-on': i === sel }"
              :cx="sx(X[i])"
              :cy="sy(y)"
              :r="i === sel ? 6.5 : 5"
            />
          </g>
          <g class="ifl-handles">
            <circle :cx="sx(xL)" :cy="sy(lineAt(xL))" r="7" />
            <circle :cx="sx(xR)" :cy="sy(lineAt(xR))" r="7" />
          </g>
        </template>
        <text v-else-if="loadError" class="ifl-msg" :x="W / 2" :y="H / 2" text-anchor="middle">{{ loadError }}</text>
      </svg>
    </figure>

    <aside class="ifl-side">
      <div class="ifl-math ifl-expr">
        <i>χ</i><sup>2</sup> = <span class="ifl-sum">Σ</span><span class="ifl-frac"><span v-if="slopeFirst">(<i>y</i><sub><i>i</i></sub> − <i class="ifl-k">a</i>·<i>x</i><sub><i>i</i></sub> − <i class="ifl-k">b</i>)<sup>2</sup></span><span v-else>(<i>y</i><sub><i>i</i></sub> − <i class="ifl-k">a</i> − <i class="ifl-k">b</i>·<i>x</i><sub><i>i</i></sub>)<sup>2</sup></span><span><i>σ</i><sup>2</sup></span></span>
      </div>

      <div v-if="push" class="ifl-push">
        <div class="ifl-label"><span class="ifl-on">{{ push.year }}</span> · <i class="ifl-var">x</i> = {{ push.year }} − {{ x0 }} = {{ push.x }}</div>
        <div class="ifl-math ifl-line1">
          <span class="ifl-frac"><span v-if="slopeFirst">({{ push.y }} − <span class="ifl-k">{{ push.bNeg ? `(${push.b})` : push.b }}</span>·{{ push.x }} − <span class="ifl-k">{{ push.a }}</span>)<sup>2</sup></span><span v-else>({{ push.y }} − <span class="ifl-k">{{ push.a }}</span> − <span class="ifl-k">{{ push.bNeg ? `(${push.b})` : push.b }}</span>·{{ push.x }})<sup>2</sup></span><span>{{ push.s }}<sup>2</sup></span></span>
          = <span class="ifl-frac"><span>{{ push.rNeg ? `(${push.r})` : push.r }}<sup>2</sup></span><span>{{ push.s2 }}</span></span>
          = <b class="ifl-on">{{ push.term }}</b>
        </div>
      </div>

      <div v-if="ready" class="ifl-total">
        <div class="ifl-bar" role="img" :aria-label="`Ten terms adding up to ${fmt(chi2, 2)}`">
          <span
            v-for="s in segments"
            :key="s.i"
            class="ifl-seg"
            :class="{ 'ifl-on': s.i === sel }"
            :style="{ left: `${s.x * 100}%`, width: `${s.w * 100}%` }"
          />
          <span class="ifl-min" :style="{ left: `${(best.chi2 / barMax) * 100}%` }" />
        </div>
        <div class="ifl-sumrow">
          <span class="ifl-math"><i>χ</i><sup>2</sup> = <b>{{ fmt(chi2, 2) }}</b></span>
          <span class="ifl-label">least squares {{ fmt(best.chi2, 2) }}</span>
        </div>
      </div>

      <div class="ifl-controls">
        <div
          v-for="s in sliders"
          :key="s.key"
          class="ifl-slider"
          role="slider"
          tabindex="0"
          :aria-label="`${s.label}, ${s.hint}`"
          :aria-valuemin="s.min"
          :aria-valuemax="s.max"
          :aria-valuenow="s.value"
          :aria-valuetext="`${s.text} ${s.unit}`"
          @pointerdown="sliderDown($event, s)"
          @mousedown.prevent
          @keydown="sliderKey($event, s)"
        >
          <span class="ifl-sname"><i class="ifl-k">{{ s.label }}</i></span>
          <span class="ifl-track">
            <span class="ifl-fill" :style="{ width: `${frac(s) * 100}%` }" />
            <span class="ifl-thumb" :style="{ left: `${frac(s) * 100}%` }" />
          </span>
          <span class="ifl-sval"><b>{{ s.text }}</b> {{ s.unit }}</span>
        </div>
      </div>

      <div class="ifl-buttons">
        <button type="button" class="ifl-btn ifl-btn-main" :disabled="!ready" @mousedown.prevent @pointerdown.stop @click="bestFit">best fit</button>
        <button type="button" class="ifl-btn" :disabled="!ready" @mousedown.prevent @pointerdown.stop @click="reset">reset</button>
      </div>
    </aside>
  </section>
</template>

<style scoped>
.ifl {
  display: grid;
  grid-template-columns: minmax(0, 1.15fr) minmax(0, 1fr);
  grid-template-rows: minmax(0, 1fr);
  gap: 1.4rem;
  height: 21rem;
  min-height: 0;
  user-select: none;
  -webkit-user-select: none;
  color: var(--fg);
  font-family: var(--font-sans);
  font-variant-numeric: tabular-nums;
}
.ifl-plot {
  margin: 0;
  min-width: 0;
  min-height: 0;
  position: relative;
  border: 1px solid var(--hair);
  border-radius: 6px;
  background: rgba(255, 255, 255, 0.015);
  overflow: hidden;
}
.ifl-svg {
  position: absolute;
  inset: 0;
  display: block;
  touch-action: none;
  -webkit-tap-highlight-color: transparent;
}

/* ---- plot ---- */
.ifl-grid line { stroke: var(--hair); stroke-width: 1; }
.ifl-ticks text { fill: var(--dim); font-size: 14px; }
.ifl-ticks text.ifl-on { fill: var(--accent); font-weight: 600; }
.ifl-ticks .ifl-tickmark { stroke: var(--hair-strong); }
.ifl-unit { letter-spacing: 0.04em; }
.ifl-err line { stroke: var(--dim); stroke-width: 1.2; opacity: 0.55; }
.ifl-res line {
  stroke: var(--fg-2);
  stroke-width: 1.6;
  stroke-dasharray: 3 3;
  opacity: 0.75;
}
.ifl-res line.ifl-on {
  stroke: var(--accent);
  stroke-width: 2.6;
  stroke-dasharray: none;
  opacity: 1;
}
.ifl-line { stroke: var(--accent); stroke-width: 2.6; stroke-linecap: round; }
.ifl-rlab { fill: var(--accent); font-size: 13px; font-weight: 500; }
.ifl-trend { fill: var(--accent); font-size: 14px; font-weight: 500; }
.ifl-pts circle { fill: var(--fg); stroke: var(--bg); stroke-width: 1.5; }
.ifl-pts circle.ifl-on { fill: var(--accent); stroke: var(--fg); stroke-width: 1.5; }
.ifl-handles circle {
  fill: var(--bg);
  stroke: var(--accent);
  stroke-width: 2;
  transition: r 0.25s var(--ease);
}
.ifl-plot:hover .ifl-handles circle { r: 8.5; }
.ifl-msg { fill: var(--warn); font-size: 13px; }

/* ---- side panel ---- */
.ifl-side {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 0.55rem;
  min-width: 0;
  min-height: 0;
}
/* Math set like the slides' KaTeX: the KaTeX fonts (loaded by any deck with
   formulas), a serif when a deck has none. */
.ifl-math {
  font-family: KaTeX_Main, 'Times New Roman', serif;
  font-size: 1.21em;
  line-height: 1.25;
  white-space: nowrap;
}
.ifl-math i,
.ifl-var {
  font-family: KaTeX_Math, 'Times New Roman', serif;
  font-style: italic;
}
.ifl-math sup,
.ifl-math sub { font-size: 0.7em; line-height: 0; }
.ifl-math b { font-weight: 400; }
.ifl-sum {
  font-family: KaTeX_Size1, KaTeX_Main, 'Times New Roman', serif;
  font-size: 1.25em;
  margin: 0 0.12em 0 0.1em;
  vertical-align: -0.12em;
}
.ifl-frac {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  vertical-align: middle;
  margin: 0 0.12em;
}
.ifl-frac > span { padding: 0 0.15em; line-height: 1.2; }
.ifl-frac > span:first-child { border-bottom: 1px solid currentColor; padding-bottom: 0.08em; }
.ifl-frac > span:last-child { padding-top: 0.06em; }
.ifl-k { color: var(--accent); }
.ifl-on { color: var(--accent); }
.ifl-expr { font-size: 1.32em; }

.ifl-label {
  font-size: 0.875rem;
  letter-spacing: 0.06em;
  color: var(--dim);
}
.ifl-label .ifl-on { font-weight: 600; letter-spacing: 0.08em; }
.ifl-var { font-size: 1.1em; letter-spacing: 0; }
.ifl-push { display: flex; flex-direction: column; gap: 0.3rem; }
.ifl-line1 { font-size: 1.12em; }
.ifl-line1 b { color: var(--accent); }

.ifl-total { display: flex; flex-direction: column; gap: 0.35rem; }
.ifl-bar {
  position: relative;
  height: 14px;
  border-radius: 2px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid var(--hair);
}
.ifl-seg {
  position: absolute;
  top: 1px;
  bottom: 1px;
  background: var(--fg-2);
  opacity: 0.45;
  box-shadow: inset -1px 0 0 var(--bg);
}
.ifl-seg.ifl-on { background: var(--accent); opacity: 1; }
.ifl-min {
  position: absolute;
  top: -4px;
  bottom: -4px;
  width: 0;
  border-left: 1.5px solid var(--ok);
}
.ifl-sumrow { display: flex; justify-content: space-between; align-items: baseline; gap: 0.6rem; }
.ifl-sumrow .ifl-label::before {
  content: '';
  display: inline-block;
  width: 0;
  height: 0.8em;
  margin-right: 0.45em;
  vertical-align: -0.1em;
  border-left: 1.5px solid var(--ok);
}

.ifl-controls { display: flex; flex-direction: column; gap: 0.1rem; }
.ifl-slider {
  display: grid;
  grid-template-columns: 1.4rem minmax(0, 1fr) 7.6rem;
  align-items: center;
  gap: 0.7rem;
  height: 2.1rem;
  cursor: pointer;
  touch-action: none;
  outline: none;
  border-radius: 4px;
}
.ifl-slider:focus-visible { box-shadow: 0 0 0 1px var(--hair-strong); }
.ifl-sname { font-family: KaTeX_Math, 'Times New Roman', serif; font-style: italic; font-size: 1.3em; text-align: center; }
.ifl-track {
  position: relative;
  height: 2px;
  background: var(--hair-strong);
  border-radius: 1px;
}
.ifl-fill { position: absolute; left: 0; top: 0; bottom: 0; background: var(--accent); opacity: 0.55; }
.ifl-thumb {
  position: absolute;
  top: 50%;
  width: 18px;
  height: 18px;
  margin: -9px 0 0 -9px;
  border-radius: 50%;
  background: var(--accent);
  transition: transform 0.25s var(--ease);
}
.ifl-slider:hover .ifl-thumb,
.ifl-slider:focus-visible .ifl-thumb { transform: scale(1.2); }
.ifl-sval { font-size: 0.95rem; color: var(--dim); white-space: nowrap; text-align: right; }
.ifl-sval b { color: var(--fg); font-weight: 500; font-size: 1.05rem; }

.ifl-buttons { display: flex; gap: 0.6rem; }
.ifl-btn {
  font-family: var(--font-sans);
  font-size: 0.875rem;
  font-weight: 500;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--fg-2);
  background: none;
  border: 1px solid var(--hair-strong);
  border-radius: 4px;
  padding: 0.38rem 0.85rem;
  cursor: pointer;
  transition: color 0.3s var(--ease), border-color 0.3s var(--ease);
}
.ifl-btn:hover:not(:disabled),
.ifl-btn:focus-visible { color: var(--accent); border-color: var(--accent); outline: none; }
.ifl-btn-main { color: var(--accent); border-color: color-mix(in srgb, var(--accent) 55%, transparent); }
.ifl-btn:disabled { opacity: 0.4; cursor: default; }

.ifl-wait .ifl-side { opacity: 0.35; }

@media (prefers-reduced-motion: reduce) {
  .ifl-handles circle,
  .ifl-thumb,
  .ifl-btn { transition: none; }
}
</style>
