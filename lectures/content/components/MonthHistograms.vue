<!--
  MonthHistograms — each month's hours over the outline of all hours ÷ 12.

    <MonthHistograms />                     steps by itself, a month every 1.8 s
    <MonthHistograms :month="6" />          start at July (0 = January)
    <MonthHistograms class="fig-fill" />    on a `class: fill` slide: takes the rest of it

  The hours of one month in 1 °C bins from −17 to 33 °C, over the outline of
  all hours ÷ 12, on one fixed scale (beyond.py's old animation, as vectors).
  It steps through the months by itself; the button pauses and plays, the
  month bar picks a month (tap or drag along it; it pauses). Reduced motion:
  it starts paused and the bars change without a glide. No control takes the
  keyboard focus and a drag never moves the slide. In presenter mode the
  audience window follows (BroadcastChannel).

  The plot has the look of the static figures (figures/src/style.py): STIX
  type, a closed frame, ticks pointing in on all four sides with minor ticks,
  the month as a light fill under a thin outline (handson.py's _paper_hist)
  (./figure-look/figure-look.css).

  Data: public/data/l07_month_hist.json (figures/src/interactive_l07_data.py).
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
</script>

<script setup>
import { computed, nextTick, onBeforeUnmount, onMounted, ref, shallowRef, watch } from 'vue'
import { useIsSlideActive, useSlideContext } from '@slidev/client'
import './figure-look/figure-look.css'

const props = defineProps({
  // The month at the start, 0 = January.
  month: { type: Number, default: 0 },
  // Seconds on each month while it steps by itself.
  interval: { type: Number, default: 1.8 },
  src: { type: String, default: 'data/l07_month_hist.json' },
  syncId: { type: String, default: '' },
})

const reduceMotion = typeof window !== 'undefined'
  && window.matchMedia?.('(prefers-reduced-motion: reduce)').matches
const clamp = (v, lo, hi) => Math.min(hi, Math.max(lo, v))

const D = shallowRef(null)
const loadError = ref('')
fetchJSON(import.meta.env.BASE_URL + props.src)
  .then((d) => { D.value = d; heights.value = Float64Array.from(d.counts[m.value]) })
  .catch((e) => { loadError.value = String(e.message || e) })
const ready = computed(() => !!D.value)

const m = ref(clamp(Math.round(props.month), 0, 11))
const playing = ref(!reduceMotion)
let touched = false

// ---- the bars glide from one month to the next ---------------------------------------
const heights = shallowRef(new Float64Array(0))
let glide = 0
watch(m, (k) => {
  const d = D.value
  if (!d) return
  const to = d.counts[k]
  if (glide) cancelAnimationFrame(glide)
  if (reduceMotion || heights.value.length !== to.length) { heights.value = Float64Array.from(to); return }
  const from = Float64Array.from(heights.value)
  const t0 = performance.now()
  const T = Math.min(520, props.interval * 400)
  const step = (now) => {
    const u = Math.min(1, (now - t0) / T)
    const e = 1 - (1 - u) ** 3
    heights.value = from.map((f, i) => f + (to[i] - f) * e)
    glide = u < 1 ? requestAnimationFrame(step) : 0
  }
  glide = requestAnimationFrame(step)
})

// ---- geometry ----------------------------------------------------------------------------
const box = ref(null)
const W = ref(0)
const H = ref(0)
const M = { l: 56, r: 14, t: 16, b: 40 }
let ro = null
onMounted(() => {
  ro = new ResizeObserver(([e]) => {
    W.value = Math.round(e.contentRect.width)
    H.value = Math.round(e.contentRect.height)
  })
  if (box.value) ro.observe(box.value)
})
const ymax = computed(() => (D.value ? 1.08 * Math.max(...D.value.counts.map((r) => Math.max(...r))) : 1))
const sx = (t) => M.l + ((t - D.value.range[0]) / (D.value.range[1] - D.value.range[0])) * (W.value - M.l - M.r)
const sy = (c) => H.value - M.b - (c / ymax.value) * (H.value - M.t - M.b)
const xticks = [-10, 0, 10, 20, 30]
const yticks = computed(() => {
  const out = []
  for (let c = 0; c <= ymax.value; c += 250) out.push(c)
  return out
})
// The month as Matplotlib's histtype "step": along the top of each bin, down
// to zero at both ends. Closed, it is the light fill ("stepfilled").
const monthPath = computed(() => {
  const d = D.value
  if (!d || !W.value || !heights.value.length) return ''
  const w = (d.range[1] - d.range[0]) / d.bins
  let path = `M${sx(d.range[0]).toFixed(1)},${sy(0).toFixed(1)}`
  heights.value.forEach((c, i) => {
    path += `V${sy(c).toFixed(1)}H${sx(d.range[0] + (i + 1) * w).toFixed(1)}`
  })
  return `${path}V${sy(0).toFixed(1)}`
})
// Ticks pointing in on all four sides (style.py), minor ticks as Matplotlib's
// AutoMinorLocator: every 2 °C (five steps of 10), every 50 hours (five
// steps of 250).
const TL = 6.25
const TM = 3.125
const frameTicks = computed(() => {
  const d = D.value
  if (!d || !W.value) return { major: '', minor: '' }
  const [lo, hi] = d.range
  const left = M.l
  const right = W.value - M.r
  const top = M.t
  const bottom = H.value - M.b
  let major = ''
  let minor = ''
  for (const t of xticks) major += `M${sx(t)} ${bottom}v${-TL}M${sx(t)} ${top}v${TL}`
  for (const c of yticks.value) major += `M${left} ${sy(c)}h${TL}M${right} ${sy(c)}h${-TL}`
  for (let t = Math.ceil(lo / 2) * 2; t < hi; t += 2) {
    if (t <= lo || t % 10 === 0) continue
    minor += `M${sx(t)} ${bottom}v${-TM}M${sx(t)} ${top}v${TM}`
  }
  for (let c = 50; c < ymax.value; c += 50) {
    if (c % 250 === 0) continue
    minor += `M${left} ${sy(c)}h${TM}M${right} ${sy(c)}h${-TM}`
  }
  return { major, minor }
})
const outline = computed(() => {
  const d = D.value
  if (!d || !W.value) return ''
  const w = (d.range[1] - d.range[0]) / d.bins
  let path = `M${sx(d.range[0]).toFixed(1)},${sy(0).toFixed(1)}`
  d.all.forEach((c, i) => {
    const y = sy(c / 12).toFixed(1)
    path += `V${y}H${sx(d.range[0] + (i + 1) * w).toFixed(1)}`
  })
  return `${path}V${sy(0).toFixed(1)}`
})

// ---- stepping by itself ---------------------------------------------------------------------
const { $page, $renderContext } = useSlideContext()
const isActive = useIsSlideActive()
const live = computed(() => $renderContext?.value === 'slide' || $renderContext?.value === 'presenter')
let timer = 0
function stopTimer() { if (timer) clearInterval(timer); timer = 0 }
function startTimer() {
  stopTimer()
  if (!playing.value || !isActive.value || !live.value || !ready.value) return
  timer = setInterval(() => { m.value = (m.value + 1) % 12 }, props.interval * 1000)
}
watch([playing, isActive, ready], startTimer, { immediate: true })

function toggle(e) {
  playing.value = !playing.value
  touched = true
  schedulePost()
  if (e?.detail) e.currentTarget.blur()
}

// ---- the month bar: tap or drag along it ----------------------------------------------------
function scrubDown(e) {
  if (!ready.value || (e.pointerType === 'mouse' && e.button !== 0)) return
  e.stopPropagation()
  e.preventDefault()
  const el = e.currentTarget
  const pick = (ev) => {
    const r = el.getBoundingClientRect()
    const k = clamp(Math.floor(((ev.clientX - r.left) / r.width) * 12), 0, 11)
    if (k !== m.value) { m.value = k; schedulePost() }
  }
  playing.value = false
  touched = true
  el.setPointerCapture(e.pointerId)
  const move = (ev) => { if (ev.pointerId === e.pointerId) pick(ev) }
  const up = (ev) => {
    if (ev.pointerId !== e.pointerId) return
    el.removeEventListener('pointermove', move)
    el.removeEventListener('pointerup', up)
    el.removeEventListener('pointercancel', up)
  }
  el.addEventListener('pointermove', move)
  el.addEventListener('pointerup', up)
  el.addEventListener('pointercancel', up)
  pick(e)
  schedulePost()
}

// ---- presenter ↔ audience ---------------------------------------------------------------------
// Posted on the button and the month bar only: while it steps by itself each
// window keeps its own clock from the same month.
const instance = Math.random().toString(36).slice(2)
const syncKey = () => `MonthHistograms:${$page.value}:${props.syncId}`
let chan = null
let shared = ''
let pending = 0
const stateJSON = () => JSON.stringify({ m: m.value, p: playing.value })
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
  chan.onmessage = ({ data: msg }) => {
    if (!msg || msg.key !== syncKey() || msg.from === instance) return
    if (msg.type === 'state') {
      shared = msg.state
      touched = true
      const s = JSON.parse(msg.state)
      m.value = s.m
      playing.value = s.p
      startTimer()
    } else if (msg.type === 'hello' && touched) {
      post({ type: 'state', state: stateJSON() })
    }
  }
  post({ type: 'hello' })
}
watch(ready, (r) => { if (r) nextTick(openSync) }, { immediate: true })

onBeforeUnmount(() => {
  ro?.disconnect()
  stopTimer()
  if (glide) cancelAnimationFrame(glide)
  if (pending) cancelAnimationFrame(pending)
  chan?.close()
  chan = null
})
</script>

<template>
  <section class="imh" :data-month="m" :data-playing="playing">
    <header class="imh-head">
      <span v-if="D" class="imh-title"><b>{{ D.names[m] }}</b>: mean {{ fmt(D.means[m], 1) }} °C</span>
      <span v-else class="imh-title imh-dim">{{ loadError || '…' }}</span>
      <span class="imh-controls">
        <button
          type="button"
          class="imh-btn"
          :title="playing ? 'Pause' : 'Play'"
          :aria-label="playing ? 'pause' : 'play'"
          @mousedown.prevent
          @pointerdown.stop
          @click="toggle"
        >
          <svg viewBox="0 0 16 16" aria-hidden="true">
            <path v-if="playing" d="M5 3.5v9M11 3.5v9" />
            <path v-else class="imh-play" d="M5.5 3.2v9.6L12.8 8z" />
          </svg>
        </button>
        <span
          class="imh-scrub"
          role="slider"
          aria-label="month"
          :aria-valuemin="1"
          :aria-valuemax="12"
          :aria-valuenow="m + 1"
          :aria-valuetext="D ? D.names[m] : ''"
          @pointerdown="scrubDown"
          @mousedown.prevent
        >
          <span
            v-for="(name, k) in (D ? D.names : [])"
            :key="name"
            class="imh-stop"
            :class="{ 'imh-on': k === m }"
          >{{ name.slice(0, 3) }}</span>
        </span>
      </span>
    </header>
    <figure ref="box" class="imh-plot">
      <svg v-if="W > 0 && H > 0 && D" class="imh-svg ixf" :width="W" :height="H" :viewBox="`0 0 ${W} ${H}`" role="img" :aria-label="`${D.names[m]}: the hours in 1 °C bins over all hours divided by 12`">
        <path class="imh-fill" :d="monthPath" />
        <path class="imh-step" :d="monthPath" />
        <path class="imh-outline" :d="outline" />
        <rect class="ixf-frame" :x="M.l" :y="M.t" :width="W - M.l - M.r" :height="H - M.t - M.b" />
        <path class="ixf-minor" :d="frameTicks.minor" />
        <path class="ixf-ticks" :d="frameTicks.major" />
        <g class="imh-ticks">
          <text v-for="t in xticks" :key="'x' + t" class="ixf-tl" :x="sx(t)" :y="H - M.b + 16" text-anchor="middle">{{ fmt(t, 0) }}</text>
          <text v-for="c in yticks" :key="'y' + c" class="ixf-tl" :x="M.l - 6.25" :y="sy(c)" dy="0.33em" text-anchor="end">{{ c }}</text>
          <text class="ixf-label" :x="M.l + (W - M.l - M.r) / 2" :y="H - 6" text-anchor="middle">temperature (°C)</text>
          <text class="ixf-label" text-anchor="middle" :transform="`translate(14 ${M.t + (H - M.t - M.b) / 2}) rotate(-90)`">hours per 1 °C</text>
        </g>
        <g class="imh-legend" :transform="`translate(${M.l + 14} ${M.t + 8})`">
          <rect x="0.75" y="0.75" width="14" height="10" class="imh-legbar" />
          <text class="ixf-text" x="22" y="5.75" dy="0.33em">this month</text>
          <line x1="0" x2="15.5" y1="25" y2="25" class="imh-outline" />
          <text class="ixf-text" x="22" y="25" dy="0.33em">all hours ÷ 12</text>
        </g>
      </svg>
    </figure>
  </section>
</template>

<style scoped>
/* A <section> with no <div> children: the theme's FILL rule turns a
   .fig-fill's direct <div> children into shrinking flex columns. */
.imh {
  display: flex;
  flex-direction: column;
  gap: 0.45rem;
  height: 20rem;
  min-height: 0;
  user-select: none;
  -webkit-user-select: none;
  font-family: var(--font-sans);
  color: var(--fg);
}
.imh-head { display: flex; align-items: center; justify-content: space-between; gap: 1rem; }
.imh-title { font-size: 1.1rem; color: var(--fg-2); font-variant-numeric: tabular-nums; white-space: nowrap; }
.imh-title b { color: var(--accent); font-weight: 600; }
.imh-dim { color: var(--dim); }
.imh-controls { display: flex; align-items: center; gap: 0.7rem; }
.imh-btn {
  display: grid;
  place-items: center;
  width: 30px;
  height: 30px;
  padding: 0;
  border: 1px solid var(--hair-strong);
  border-radius: 50%;
  background: none;
  color: var(--fg-2);
  cursor: pointer;
  transition: color 0.3s var(--ease), border-color 0.3s var(--ease);
}
.imh-btn:hover,
.imh-btn:focus-visible { color: var(--accent); border-color: var(--accent); outline: none; }
.imh-btn svg { width: 14px; height: 14px; fill: none; stroke: currentColor; stroke-width: 1.8; stroke-linecap: round; }
.imh-btn .imh-play { fill: currentColor; stroke: none; }
.imh-scrub {
  display: grid;
  grid-template-columns: repeat(12, minmax(0, 1fr));
  border: 1px solid var(--hair);
  border-radius: 4px;
  cursor: pointer;
  touch-action: none;
}
.imh-stop {
  padding: 0.3rem 0.35rem;
  font-size: 0.8rem;
  text-align: center;
  color: var(--dim);
  transition: color 0.3s var(--ease), box-shadow 0.3s var(--ease);
}
.imh-stop + .imh-stop { border-left: 1px solid var(--hair); }
.imh-stop.imh-on { color: var(--accent); box-shadow: inset 0 -2px 0 var(--accent); }
.imh-plot {
  position: relative;
  flex: 1 1 0;
  min-height: 0;
  margin: 0;
  border: 1px solid var(--hair);
  border-radius: 6px;
  background: rgba(255, 255, 255, 0.015);
  overflow: hidden;
}
.imh-svg { position: absolute; inset: 0; display: block; }
/* The plot's type, frame and ticks: ./figure-look/figure-look.css. The month
   as a light fill under a thin outline, as the static histograms. */
.imh-fill { fill: var(--accent); fill-opacity: 0.3; stroke: none; }
.imh-step { fill: none; stroke: var(--accent); stroke-width: 1.5; }
.imh-outline { fill: none; stroke: var(--dim); stroke-width: 1.5; }
.imh-legend text { fill: var(--fg); }
.imh-legbar { fill: color-mix(in srgb, var(--accent) 30%, transparent); stroke: var(--accent); stroke-width: 1.5; }

@media (prefers-reduced-motion: reduce) {
  .imh-btn,
  .imh-stop { transition: none; }
}
</style>
