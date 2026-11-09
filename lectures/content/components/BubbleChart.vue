<!--
  BubbleChart — Hans Rosling's Gapminder chart: five variables in one picture.

    <BubbleChart class="fig-fill mt-sm" />     on a `class: fill` slide: takes the rest of it
    <BubbleChart :year="2007" :autoplay="false" />   start at 2007, still

  x = GDP per person (US$, inflation-adjusted, log scale), y = life
  expectancy at birth, bubble area ∝ population, colour = continent, and
  time, 1952 to 2007: it plays by itself once the slide is shown (one
  5-year step per `step-seconds`, the values between two data years drawn
  on straight lines, GDP on the log scale), or is dragged on the scrubber.
  A still chart rests on a data year: the scrubber lets go on the nearest
  one, and only there does a named country show its numbers under its
  name. Hover a bubble to name it, tap it to keep it with its trail; tap
  a continent to highlight it. Bubbles are drawn big to small, so the small ones stay
  on top.

  Data: public/data/l07_gapminder.json (figures/src/interactive_l07_gallery_data.py
  from figures/data/gallery/gapminder.csv): Gapminder Foundation, CC BY 4.0.
  In presenter mode the audience window follows the presenter's buttons,
  scrubber and taps (BroadcastChannel, same browser).
-->
<script>
// Module scope (runs once per page): every BubbleChart shares one fetch.
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
// Names too long for a label.
const SHORT = {
  'Korea, Rep.': 'South Korea',
  'Korea, Dem. Rep.': 'North Korea',
  'Congo, Dem. Rep.': 'DR Congo',
  'Congo, Rep.': 'Congo',
  'Yemen, Rep.': 'Yemen',
  'Hong Kong, China': 'Hong Kong',
  'Slovak Republic': 'Slovakia',
}
// Where a country's own label sits, so the always-named ones do not collide.
const PLACE = { 'China': 'above', 'India': 'below', 'United States': 'above', 'Rwanda': 'left', 'Korea, Rep.': 'left' }
// 1 234 567 with a thin space, as the course writes numbers.
const thin = (n) => String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g, ' ')
function people(p) {
  if (p >= 1e9) return `${(p / 1e9).toFixed(2)} billion`
  if (p >= 1e6) return `${(p / 1e6).toFixed(p >= 1e8 ? 0 : 1)} million`
  return `${thin(p / 1e3)} thousand`
}
</script>

<script setup>
import { computed, nextTick, onBeforeUnmount, onMounted, ref, shallowRef, watch } from 'vue'
import { useIsSlideActive, useSlideContext } from '@slidev/client'

const props = defineProps({
  src: { type: String, default: 'data/l07_gapminder.json' },
  // The year shown first (a data year, 1952 to 2007).
  year: { type: Number, default: 1952 },
  // Seconds per 5 years while it plays: 1.8 s → 1952 to 2007 in about 20 s.
  stepSeconds: { type: Number, default: 1.8 },
  // Countries always named (names as in the data).
  labels: { type: Array, default: () => ['China', 'India', 'United States', 'Rwanda', 'Korea, Rep.'] },
  // Play once by itself when the slide is shown (never with reduced motion).
  autoplay: { type: Boolean, default: true },
  // Two BubbleCharts on one slide need different ids (presenter ↔ audience sync).
  syncId: { type: String, default: '' },
})

const Y_FIRST = 1952
const Y_LAST = 2007
const COLORS = ['var(--accent)', '#66d9ab', '#e88bc4', '#f5b95f', '#8f9dfb'] // Africa, Americas, Asia, Europe, Oceania
const X_DOMAIN = [Math.log10(200), Math.log10(130000)]
const Y_DOMAIN = [20, 85]
const X_TICKS = [500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]
const Y_TICKS = [20, 30, 40, 50, 60, 70, 80]
const POP_MAX = 1.32e9 // China 2007, the largest bubble
const reduceMotion = typeof window !== 'undefined'
  && window.matchMedia?.('(prefers-reduced-motion: reduce)').matches
const clamp = (v, lo, hi) => Math.min(hi, Math.max(lo, v))
const snapYear = (t) => clamp(Y_FIRST + 5 * Math.round((t - Y_FIRST) / 5), Y_FIRST, Y_LAST)

// ---- data -------------------------------------------------------------------------
const D = shallowRef(null)
const loadError = ref('')
fetchJSON(import.meta.env.BASE_URL + props.src)
  .then((d) => {
    D.value = {
      ...d,
      logGdp: d.gdp.map((row) => row.map(Math.log)),
      shown: new Set(props.labels.map((n) => d.name.indexOf(n)).filter((i) => i >= 0)),
    }
  })
  .catch((e) => { loadError.value = String(e.message || e) })
const ready = computed(() => !!D.value)

// ---- the time shown -------------------------------------------------------------------
const { $page, $renderContext } = useSlideContext()
const isActive = useIsSlideActive()
const live = computed(() => $renderContext?.value === 'slide' || $renderContext?.value === 'presenter')
const t = ref(snapYear(props.year))
const playing = ref(false)
let touched = false
// Outside the live slide (overview, print, export) the chart shows 2007.
watch(live, (l) => { if (!l && !touched) t.value = Y_LAST }, { immediate: true })
const yearLabel = computed(() => Math.floor(t.value + 1e-6))
const atDataYear = computed(() => Math.abs(t.value - snapYear(t.value)) < 1e-6)

// ---- geometry ---------------------------------------------------------------------------
const box = ref(null)
const svgRef = ref(null)
const W = ref(0)
const H = ref(0)
const M = { l: 54, r: 16, t: 12, b: 46 }
const pw = computed(() => Math.max(1, W.value - M.l - M.r))
const ph = computed(() => Math.max(1, H.value - M.t - M.b))
const sx = (g) => M.l + ((Math.log10(g) - X_DOMAIN[0]) / (X_DOMAIN[1] - X_DOMAIN[0])) * pw.value
const sxl = (lg) => M.l + ((lg / Math.LN10 - X_DOMAIN[0]) / (X_DOMAIN[1] - X_DOMAIN[0])) * pw.value
const sy = (v) => M.t + (1 - (v - Y_DOMAIN[0]) / (Y_DOMAIN[1] - Y_DOMAIN[0])) * ph.value
const rMax = computed(() => Math.max(12, Math.min(ph.value * 0.1, pw.value * 0.055)))
const rOf = (pop) => Math.max(1.6, rMax.value * Math.sqrt(pop / POP_MAX))
const xTicks = computed(() => X_TICKS.map((g) => ({ x: sx(g), label: `$${thin(g)}` })))
const yTicks = computed(() => Y_TICKS.map((v) => ({ y: sy(v), label: String(v) })))

// Each country at time t: straight lines between data years (GDP on the log scale).
function seg(time) {
  const f = clamp((time - Y_FIRST) / 5, 0, 11)
  const k = Math.min(10, Math.floor(f))
  return { k, u: f - k }
}
const bubbles = computed(() => {
  const d = D.value
  if (!d || !W.value) return []
  const { k, u } = seg(t.value)
  const out = d.name.map((_, i) => {
    const life = d.life[i][k] + (d.life[i][k + 1] - d.life[i][k]) * u
    const lg = d.logGdp[i][k] + (d.logGdp[i][k + 1] - d.logGdp[i][k]) * u
    const pop = d.pop[i][k] + (d.pop[i][k + 1] - d.pop[i][k]) * u
    return { i, c: d.continent[i], cx: sxl(lg), cy: sy(life), r: rOf(pop) }
  })
  return out.sort((a, b) => b.r - a.r || a.i - b.i) // big first: the small ones stay on top
})

// ---- hover, tap, highlight ------------------------------------------------------------------
const hover = ref(-1)
const sel = ref(-1)
const hi = ref(-1) // a highlighted continent
const focusIdx = computed(() => (sel.value >= 0 ? sel.value : hover.value))
const dimmed = (b) => (hi.value >= 0 && b.c !== hi.value) || (sel.value >= 0 && b.i !== sel.value && hi.value < 0)

const labels = computed(() => {
  const d = D.value
  if (!d) return []
  const byI = new Map(bubbles.value.map((b) => [b.i, b]))
  const want = new Set(d.shown)
  if (hover.value >= 0) want.add(hover.value)
  if (sel.value >= 0) want.add(sel.value)
  const out = []
  for (const i of want) {
    const b = byI.get(i)
    if (!b) continue
    const name = d.name[i]
    const place = (i === hover.value || i === sel.value) && !d.shown.has(i) ? 'above' : (PLACE[name] || 'above')
    // the focused country also gets its numbers, on a second line
    const sub = i === focusIdx.value && atDataYear.value ? values(i) : ''
    const two = sub ? 18 : 0
    let x = b.cx
    let y = b.cy
    let anchor = 'middle'
    if (place === 'above') y = b.cy - b.r - 6 - two
    else if (place === 'below') y = b.cy + b.r + 16
    else if (place === 'right') { x = b.cx + b.r + 6; y = b.cy + 5 - two / 2; anchor = 'start' }
    else { x = b.cx - b.r - 6; y = b.cy + 5 - two / 2; anchor = 'end' }
    if (y < M.t + 14) y = b.cy + b.r + 16
    if (y + two > M.t + ph.value - 4) y = b.cy - b.r - 6 - two
    const text = SHORT[name] || name
    const half = Math.max(text.length * 4.4, sub.length * 3.6)
    if (anchor === 'middle') x = clamp(x, M.l + half, W.value - M.r - half)
    if (anchor === 'start' && x + 2 * half > W.value - M.r) { x = b.cx - b.r - 6; anchor = 'end' }
    if (anchor === 'end' && x - 2 * half < M.l) { x = b.cx + b.r + 6; anchor = 'start' }
    out.push({ i, x, y, anchor, text, sub, dim: dimmed(b), on: i === focusIdx.value })
  }
  return out
})

// The selected country's path so far: its data years, then where it is now.
const trail = computed(() => {
  const d = D.value
  const i = sel.value
  if (!d || i < 0 || !W.value) return null
  const pts = []
  for (let k = 0; k < d.years.length && d.years[k] <= t.value + 1e-6; k++) {
    pts.push({ x: sxl(d.logGdp[i][k]), y: sy(d.life[i][k]) })
  }
  const now = bubbles.value.find((b) => b.i === i)
  const path = [...pts, now ? { x: now.cx, y: now.cy } : null].filter(Boolean)
  return {
    c: d.continent[i],
    dots: pts,
    d: path.map((p, k) => `${k ? 'L' : 'M'}${p.x.toFixed(1)} ${p.y.toFixed(1)}`).join(''),
  }
})

// A country's numbers: only on a data year, where they are data.
function values(i) {
  const d = D.value
  const k = d.years.indexOf(snapYear(t.value))
  return `${d.life[i][k].toFixed(1)} years · $${thin(d.gdp[i][k])} · ${people(d.pop[i][k])}`
}

// ---- size key: two circles at their true areas ---------------------------------------------
const sizeKey = computed(() => {
  if (!W.value) return null
  const r1 = rOf(1e9)
  const r2 = rOf(1e8)
  const cx = M.l + pw.value - 118 - r1
  const base = M.t + ph.value - 10
  return { cx, base, r1, r2 }
})

// ---- pointer on the plot: hover names a bubble, a tap keeps it -------------------------------
function toSvg(e) {
  const m = svgRef.value?.getScreenCTM()
  if (!m) return null
  const p = new DOMPoint(e.clientX, e.clientY).matrixTransform(m.inverse())
  return { x: p.x, y: p.y, k: m.a || 1 }
}
function hit(p, touch) {
  const pad = (touch ? 10 : 3) / p.k
  const list = bubbles.value
  for (let n = list.length - 1; n >= 0; n--) {
    const b = list[n]
    if (Math.hypot(p.x - b.cx, p.y - b.cy) <= b.r + pad) return b.i
  }
  return -1
}
let down = null
function onDown(e) {
  if (!ready.value || (e.pointerType === 'mouse' && e.button !== 0)) return
  e.stopPropagation() // no Slidev swipe from the plot
  const p = toSvg(e)
  if (p) down = { x: p.x, y: p.y, id: e.pointerId, i: hit(p, e.pointerType !== 'mouse') }
}
function onUp(e) {
  if (!down || e.pointerId !== down.id) return
  const p = toSvg(e)
  const { x, y, i } = down
  down = null
  if (!p || Math.hypot(p.x - x, p.y - y) > 12 / p.k) return // a drag, not a tap
  sel.value = i >= 0 && i !== sel.value ? i : -1
  if (i < 0) hi.value = -1
  touched = true
  schedulePost()
}
function onMove(e) {
  if (e.pointerType !== 'mouse' || !ready.value) return
  const p = toSvg(e)
  if (p) hover.value = hit(p, false)
}
function onLeave() { hover.value = -1 }
function pickContinent(c) {
  hi.value = hi.value === c ? -1 : c
  sel.value = -1
  touched = true
  schedulePost()
}

// ---- playing --------------------------------------------------------------------------------
let raf = 0
let last = 0
function loop(now) {
  raf = 0
  if (!playing.value) return
  const dt = last ? Math.min(0.1, (now - last) / 1000) : 0
  last = now
  t.value = Math.min(Y_LAST, t.value + (dt * 5) / props.stepSeconds)
  if (t.value >= Y_LAST) { playing.value = false; schedulePost(); return }
  raf = requestAnimationFrame(loop)
}
watch(playing, (p) => {
  if (p && !raf) { last = 0; raf = requestAnimationFrame(loop) }
  if (!p && raf) { cancelAnimationFrame(raf); raf = 0 }
})
let glide = 0
function stopGlide() { if (glide) cancelAnimationFrame(glide); glide = 0 }
function glideTo(target) {
  stopGlide()
  if (reduceMotion) { t.value = target; return }
  const t0 = performance.now()
  const from = t.value
  const T = 160 + 120 * Math.abs(target - from)
  const step = (now) => {
    const u = Math.min(1, (now - t0) / T)
    t.value = from + (target - from) * (1 - (1 - u) ** 3)
    glide = u < 1 ? requestAnimationFrame(step) : 0
    if (u >= 1) schedulePost()
  }
  glide = requestAnimationFrame(step)
}
function toggle(e) {
  stopGlide()
  if (!playing.value && t.value >= Y_LAST - 1e-6) t.value = Y_FIRST
  playing.value = !playing.value
  if (!playing.value) glideTo(snapYear(t.value))
  touched = true
  schedulePost()
  if (e?.detail) e.currentTarget.blur()
}

// Play once by itself when the slide is shown, from the first year.
let autoTimer = 0
watch([isActive, ready, live], ([a, r, l]) => {
  clearTimeout(autoTimer)
  if (!a) { playing.value = false; return }
  if (!r || !l || touched || reduceMotion || !props.autoplay) return
  t.value = snapYear(props.year)
  autoTimer = setTimeout(() => { if (isActive.value && !touched) playing.value = true }, 900)
}, { immediate: true })

// ---- the scrubber: tap or drag along it --------------------------------------------------------
const frac = computed(() => (t.value - Y_FIRST) / (Y_LAST - Y_FIRST))
const yearsAll = Array.from({ length: 12 }, (_, k) => Y_FIRST + 5 * k)
function scrubDown(e) {
  if (!ready.value || (e.pointerType === 'mouse' && e.button !== 0)) return
  e.stopPropagation()
  e.preventDefault()
  const el = e.currentTarget
  const track = el.querySelector('.bub-track')
  const setFrom = (ev) => {
    const r = track.getBoundingClientRect()
    t.value = Y_FIRST + clamp((ev.clientX - r.left) / r.width, 0, 1) * (Y_LAST - Y_FIRST)
    schedulePost()
  }
  playing.value = false
  stopGlide()
  touched = true
  el.setPointerCapture(e.pointerId)
  const move = (ev) => { if (ev.pointerId === e.pointerId) setFrom(ev) }
  const up = (ev) => {
    if (ev.pointerId !== e.pointerId) return
    el.removeEventListener('pointermove', move)
    el.removeEventListener('pointerup', up)
    el.removeEventListener('pointercancel', up)
    glideTo(snapYear(t.value))
  }
  el.addEventListener('pointermove', move)
  el.addEventListener('pointerup', up)
  el.addEventListener('pointercancel', up)
  setFrom(e)
}

// ---- presenter ↔ audience: buttons, scrubber and taps are posted ----------------------------------
// While it plays, each window keeps its own clock from the same year.
const instance = Math.random().toString(36).slice(2)
const syncKey = () => `BubbleChart:${$page.value}:${props.syncId}`
let chan = null
let shared = ''
let pending = 0
const stateJSON = () => JSON.stringify({ t: Math.round(t.value * 1000) / 1000, p: playing.value, s: sel.value, h: hi.value })
function post(msg) { chan?.postMessage({ key: syncKey(), from: instance, ...msg }) }
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
      const s = JSON.parse(m.state)
      shared = m.state
      touched = true
      clearTimeout(autoTimer)
      stopGlide()
      t.value = s.t
      sel.value = s.s
      hi.value = s.h
      playing.value = s.p && isActive.value
    } else if (m.type === 'hello' && touched) {
      post({ type: 'state', state: stateJSON() })
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
})
onBeforeUnmount(() => {
  ro?.disconnect()
  clearTimeout(autoTimer)
  if (raf) cancelAnimationFrame(raf)
  stopGlide()
  if (pending) cancelAnimationFrame(pending)
  chan?.close()
  chan = null
})
</script>

<template>
  <section class="bub" :class="{ 'bub-wait': !ready }">
    <figure ref="box" class="bub-plot">
      <svg
        v-if="W > 0 && H > 0"
        ref="svgRef"
        class="bub-svg"
        :viewBox="`0 0 ${W} ${H}`"
        :width="W"
        :height="H"
        role="img"
        :aria-label="`Life expectancy against GDP per person, ${yearLabel}: 142 countries, bubble area by population, colour by continent`"
        @pointerdown="onDown"
        @pointerup="onUp"
        @pointercancel="down = null"
        @pointermove="onMove"
        @pointerleave="onLeave"
      >
        <text class="bub-year" :x="M.l + pw / 2" :y="M.t + ph / 2" :style="{ fontSize: `${Math.round(Math.min(ph * 0.5, pw * 0.27))}px` }">{{ yearLabel }}</text>
        <g class="bub-grid">
          <line v-for="tk in xTicks" :key="'gx' + tk.label" :x1="tk.x" :x2="tk.x" :y1="M.t" :y2="M.t + ph" />
          <line v-for="tk in yTicks" :key="'gy' + tk.label" :x1="M.l" :x2="M.l + pw" :y1="tk.y" :y2="tk.y" />
        </g>
        <g class="bub-ticks">
          <text v-for="tk in xTicks" :key="'x' + tk.label" :x="tk.x" :y="M.t + ph + 18" text-anchor="middle">{{ tk.label }}</text>
          <text v-for="tk in yTicks" :key="'y' + tk.label" :x="M.l - 9" :y="tk.y" text-anchor="end" dominant-baseline="central">{{ tk.label }}</text>
        </g>
        <text class="bub-axis" :x="M.l + pw / 2" :y="H - 6" text-anchor="middle">GDP per person (US$, inflation-adjusted), log scale</text>
        <text class="bub-axis" :transform="`translate(15 ${M.t + ph / 2}) rotate(-90)`" text-anchor="middle">life expectancy (years)</text>

        <template v-if="ready">
          <!-- size key: 1 billion and 100 million people at their true areas -->
          <g v-if="sizeKey" class="bub-size">
            <circle :cx="sizeKey.cx" :cy="sizeKey.base - sizeKey.r1" :r="sizeKey.r1" />
            <circle :cx="sizeKey.cx" :cy="sizeKey.base - sizeKey.r2" :r="sizeKey.r2" />
            <text :x="sizeKey.cx - sizeKey.r1 - 7" :y="sizeKey.base - 2 * sizeKey.r1 + 5" text-anchor="end">1 billion</text>
            <text :x="sizeKey.cx - sizeKey.r1 - 7" :y="sizeKey.base - 2 * sizeKey.r2 + 5" text-anchor="end">100 million</text>
          </g>
          <!-- colour key: the continents named in their colours; tap one to highlight it -->
          <g class="bub-legend">
            <text
              v-for="(name, c) in D.continents"
              :key="name"
              :x="M.l + pw - 8"
              :y="M.t + ph - 12 - (D.continents.length - 1 - c) * 21"
              text-anchor="end"
              :class="{ off: hi >= 0 && hi !== c }"
              :style="{ fill: COLORS[c] }"
              @pointerdown.stop.prevent="pickContinent(c)"
            >{{ name }}</text>
          </g>

          <g v-if="trail" class="bub-trail" :style="{ stroke: COLORS[trail.c], fill: COLORS[trail.c] }">
            <path :d="trail.d" />
            <circle v-for="(p, k) in trail.dots" :key="k" :cx="p.x" :cy="p.y" r="2.6" />
          </g>

          <g class="bub-dots">
            <circle
              v-for="b in bubbles"
              :key="b.i"
              :data-name="D.name[b.i]"
              :cx="b.cx"
              :cy="b.cy"
              :r="b.r"
              :class="{ dim: dimmed(b), on: b.i === focusIdx }"
              :style="{ fill: COLORS[b.c] }"
            />
          </g>
          <g class="bub-labels">
            <text
              v-for="l in labels"
              :key="'l' + l.i"
              :x="l.x"
              :y="l.y"
              :text-anchor="l.anchor"
              :class="{ dim: l.dim, on: l.on }"
            >{{ l.text }}<tspan v-if="l.sub" class="bub-sub" :x="l.x" dy="18">{{ l.sub }}</tspan></text>
          </g>
        </template>
        <text v-else-if="loadError" class="bub-msg" :x="W / 2" :y="H / 2" text-anchor="middle">{{ loadError }}</text>
      </svg>
    </figure>

    <nav class="bub-controls">
      <button
        type="button"
        class="bub-play"
        tabindex="-1"
        :disabled="!ready"
        :aria-label="playing ? 'Pause' : 'Play from ' + (t >= 2007 ? 1952 : yearLabel)"
        @mousedown.prevent
        @pointerdown.stop
        @click="toggle"
      >
        <svg viewBox="0 0 20 20" aria-hidden="true">
          <g v-if="playing"><rect x="5" y="4" width="3.4" height="12" rx="0.8" /><rect x="11.6" y="4" width="3.4" height="12" rx="0.8" /></g>
          <path v-else-if="t >= 2007" d="M10 4a6 6 0 1 1-5.6 3.9" fill="none" stroke-width="2" stroke-linecap="round" />
          <path v-else d="M6 3.8v12.4a.8.8 0 0 0 1.2.7l10-6.2a.8.8 0 0 0 0-1.4l-10-6.2A.8.8 0 0 0 6 3.8z" />
          <path v-if="!playing && t >= 2007" d="M3.2 4.6l1.3 3.4 3.4-1.3" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
      </button>
      <span
        class="bub-scrub"
        role="slider"
        aria-label="Year"
        :aria-valuemin="1952"
        :aria-valuemax="2007"
        :aria-valuenow="yearLabel"
        @pointerdown="scrubDown"
        @mousedown.prevent
      >
        <span class="bub-track">
          <span class="bub-fill" :style="{ width: `${frac * 100}%` }" />
          <span v-for="y in yearsAll" :key="y" class="bub-tick" :class="{ on: Math.abs(t - y) < 1e-6 }" :style="{ left: `${((y - 1952) / 55) * 100}%` }">
            <span class="bub-ticklab">{{ y }}</span>
          </span>
          <span class="bub-thumb" :style="{ left: `${frac * 100}%` }" />
        </span>
      </span>
    </nav>
  </section>
</template>

<style scoped>
/* The root takes `fig-fill` on a `class: fill` slide. The theme turns every
   direct div child of a .fig-fill into a flex column, so the parts are a
   <figure> and a <nav>, out of reach of that rule. */
.bub {
  display: grid;
  grid-template-rows: minmax(0, 1fr) auto;
  gap: 0.35rem;
  height: 22rem; /* off a `class: fill` slide */
  min-height: 0;
  user-select: none;
  -webkit-user-select: none;
  color: var(--fg);
  font-family: var(--font-sans);
  font-variant-numeric: tabular-nums;
}
.bub-plot {
  position: relative;
  margin: 0;
  min-width: 0;
  min-height: 0;
}
.bub-svg {
  position: absolute;
  inset: 0;
  display: block;
  overflow: visible;
  touch-action: none;
  -webkit-tap-highlight-color: transparent;
  font-family: var(--font-sans);
}
.bub-year {
  fill: var(--fg);
  opacity: 0.09;
  font-weight: 600;
  letter-spacing: -0.02em;
  text-anchor: middle;
  dominant-baseline: central;
  pointer-events: none;
}
.bub-grid line { stroke: var(--hair); stroke-width: 1; }
.bub-ticks text { fill: var(--dim); font-size: 14px; }
.bub-axis { fill: var(--fg-2); font-size: 14px; }
.bub-dots circle {
  fill-opacity: 0.9;
  stroke: var(--bg);
  stroke-width: 1;
  transition: opacity 0.3s var(--ease);
}
.bub-dots circle.dim { opacity: 0.22; }
.bub-dots circle.on { stroke: var(--fg); stroke-width: 2; fill-opacity: 1; }
.bub-labels text {
  fill: var(--fg);
  font-size: 15px;
  font-weight: 500;
  paint-order: stroke;
  stroke: var(--bg);
  stroke-width: 3.5px;
  stroke-linejoin: round;
  pointer-events: none;
  transition: opacity 0.3s var(--ease);
}
.bub-labels text.dim { opacity: 0.3; }
.bub-labels text.on { fill: var(--accent); }
.bub-trail path { fill: none; stroke-width: 1.6; stroke-opacity: 0.75; stroke-linejoin: round; }
.bub-trail circle { stroke: none; fill-opacity: 0.85; }
.bub-legend text {
  font-size: 15px;
  font-weight: 500;
  cursor: pointer;
  transition: opacity 0.3s var(--ease);
}
.bub-legend text.off { opacity: 0.35; }
.bub-size circle { fill: none; stroke: var(--dim); stroke-width: 1; }
.bub-size text { fill: var(--dim); font-size: 13px; }
.bub-labels .bub-sub { fill: var(--fg); font-size: 14px; font-weight: 400; }
.bub-msg { fill: var(--warn); font-size: 13px; }

/* ---- controls ---- */
.bub-controls {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  align-items: center;
  gap: 1rem;
  padding: 0 0.6rem 0 0.2rem;
}
.bub-play {
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
  transition: border-color 0.3s var(--ease), background-color 0.3s var(--ease);
}
.bub-play:hover:not(:disabled) { border-color: var(--accent); background: color-mix(in srgb, var(--accent) 12%, transparent); }
.bub-play:focus { outline: none; }
.bub-play:disabled { opacity: 0.4; cursor: default; }
.bub-play svg { width: 18px; height: 18px; fill: currentColor; stroke: currentColor; }
.bub-play svg rect, .bub-play svg path:not([fill='none']) { stroke: none; }
.bub-scrub {
  display: block;
  position: relative;
  height: 2.4rem;
  padding-top: 0.55rem;
  cursor: pointer;
  touch-action: none;
}
.bub-track {
  position: relative;
  display: block;
  height: 2px;
  margin: 0 9px;
  background: var(--hair-strong);
  border-radius: 1px;
}
.bub-fill { position: absolute; left: 0; top: 0; bottom: 0; background: var(--accent); opacity: 0.55; }
.bub-tick {
  position: absolute;
  top: -4px;
  width: 1px;
  height: 10px;
  background: var(--hair-strong);
}
.bub-ticklab {
  position: absolute;
  top: 13px;
  left: 0;
  transform: translateX(-50%);
  font-size: 13px;
  color: var(--dim);
  white-space: nowrap;
}
.bub-tick.on .bub-ticklab { color: var(--accent); font-weight: 600; }
.bub-thumb {
  position: absolute;
  top: 50%;
  width: 18px;
  height: 18px;
  margin: -9px 0 0 -9px;
  border-radius: 50%;
  background: var(--accent);
  transition: transform 0.25s var(--ease);
}
.bub-scrub:hover .bub-thumb { transform: scale(1.2); }
.bub-wait .bub-controls { opacity: 0.35; }

@media (prefers-reduced-motion: reduce) {
  .bub-dots circle,
  .bub-labels text,
  .bub-legend text,
  .bub-thumb,
  .bub-play { transition: none; }
}
</style>
