<!--
  SoftmaxTemperature — scores of the next word into probabilities.

    <SoftmaxTemperature />                                         cold / frosty / warm, scores 2.0 1.0 0.1, T = 1
    <SoftmaxTemperature :t="0.5" />                                another temperature at the start
    <SoftmaxTemperature prompt="Tomorrow will be" :words="['cold', 'windy', 'warm']" :scores="[1.5, 1.2, -0.3]" />

  pᵢ = e^(sᵢ/T) / Σⱼ e^(sⱼ/T), every step on show: s, s/T, e^(s/T), their
  sum, p. Drag a score sideways (or Tab to it and use the arrows) to change
  it; the temperature slider runs from 0.1 to 3. Tap a row to push that
  word through the expression. "draw" picks the next word with these
  probabilities (seeded, so a replay draws the same words); the tally starts
  again whenever the probabilities change.

  In presenter mode the audience window follows (BroadcastChannel).
-->
<script>
function fmt(v, d) {
  const s = Number(v).toFixed(d)
  return (/^-0\.?0*$/.test(s) ? s.slice(1) : s).replace('-', '−')
}
// Four significant figures, as HTML (numbers only): a power of ten is
// written out, 4.852·10<sup>8</sup>, when the number is large or small.
function sig4(v) {
  if (v === 0) return '0'
  let e = Math.floor(Math.log10(Math.abs(v)))
  if (e >= 5 || e <= -4) {
    let ms = (v / 10 ** e).toFixed(3)
    if (/^-?10/.test(ms)) { e += 1; ms = (v / 10 ** e).toFixed(3) }
    return `${fmt(Number(ms), 3)}·10<sup>${fmt(e, 0)}</sup>`
  }
  return fmt(v, Math.max(0, 3 - e))
}
function mulberry32(seed) {
  let a = seed | 0
  return () => {
    a = (a + 0x6D2B79F5) | 0
    let t = Math.imul(a ^ (a >>> 15), 1 | a)
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296
  }
}
</script>

<script setup>
import { computed, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useSlideContext } from '@slidev/client'

const props = defineProps({
  prompt: { type: String, default: 'After a clear night, the morning is' },
  words: { type: Array, default: () => ['cold', 'frosty', 'warm'] },
  scores: { type: Array, default: () => [2.0, 1.0, 0.1] },
  // The temperature at the start (0.1 … 3).
  t: { type: Number, default: 1 },
  // The word pushed through the expression at the start (its index).
  select: { type: Number, default: 0 },
  syncId: { type: String, default: '' },
})

const T_MIN = 0.1
const T_MAX = 3
const S_MAX = 5
const T_CHIPS = [0.1, 0.5, 1, 2, 3]
const clamp = (v, lo, hi) => Math.min(hi, Math.max(lo, v))
const qT = (v) => Math.round(clamp(v, T_MIN, T_MAX) * 100) / 100
const qS = (v) => Math.round(clamp(v, -S_MAX, S_MAX) * 10) / 10
const reduceMotion = typeof window !== 'undefined'
  && window.matchMedia?.('(prefers-reduced-motion: reduce)').matches

// ---- state ----------------------------------------------------------------------------
const T = ref(qT(props.t))
const s = ref(props.scores.map((v) => qS(Number(v))))
const sel = ref(clamp(props.select, 0, props.words.length - 1))
const counts = ref(props.words.map(() => 0))
const last = ref(-1)
const seq = ref(0)                     // draws so far: seeds the next one
let touched = false

const rows = computed(() => {
  const z = s.value.map((v) => v / T.value)
  const top = Math.max(...z)
  // e^(s/T) as shown; p from the shifted exponentials (same ratio, no overflow)
  const e = z.map((v) => Math.exp(v))
  const sh = z.map((v) => Math.exp(v - top))
  const sum = sh.reduce((a, b) => a + b, 0)
  return props.words.map((w, i) => ({
    i, w, s: s.value[i], z: z[i], e: e[i], p: sh[i] / sum,
  }))
})
const total = computed(() => rows.value.reduce((a, r) => a + r.e, 0))
const drawn = computed(() => counts.value.reduce((a, b) => a + b, 0))

// ---- temperature slider (log scale) --------------------------------------------------------
const uOf = (t) => Math.log(t / T_MIN) / Math.log(T_MAX / T_MIN)
const tOf = (u) => T_MIN * (T_MAX / T_MIN) ** u
function setT(v) {
  const nt = qT(v)
  if (nt === T.value) return
  T.value = nt
  touched = true
}
function sliderDown(e) {
  if (e.pointerType === 'mouse' && e.button !== 0) return
  e.stopPropagation()
  e.preventDefault()
  const row = e.currentTarget
  const track = row.querySelector('.ism-track')
  const setFrom = (ev) => {
    const r = track.getBoundingClientRect()
    setT(tOf(clamp((ev.clientX - r.left) / r.width, 0, 1)))
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
  let v = T.value
  if (e.key === 'ArrowRight' || e.key === 'ArrowUp') v += 0.01
  else if (e.key === 'ArrowLeft' || e.key === 'ArrowDown') v -= 0.01
  else if (e.key === 'PageUp') v = tOf(uOf(v) + 0.05)
  else if (e.key === 'PageDown') v = tOf(uOf(v) - 0.05)
  else if (e.key === 'Home') v = T_MIN
  else if (e.key === 'End') v = T_MAX
  else if (e.key === 'Escape') { e.currentTarget.blur(); return }
  else return
  e.preventDefault()
  e.stopPropagation()
  setT(v)
}
function chipT(v, e) {
  setT(v)
  if (e?.detail) e.currentTarget.blur()
}

// ---- scores: drag sideways (0.1 per 10 slide px) ------------------------------------------------
const scrubbing = ref(-1)
function scoreDown(e, i) {
  if (e.pointerType === 'mouse' && e.button !== 0) return
  e.stopPropagation()
  e.preventDefault()
  const el = e.currentTarget
  const k = el.getBoundingClientRect().width / el.offsetWidth || 1   // screen px per slide px
  const x0 = e.clientX
  const s0 = s.value[i]
  let moved = false
  scrubbing.value = i
  el.setPointerCapture(e.pointerId)
  const move = (ev) => {
    if (ev.pointerId !== e.pointerId) return
    const dx = (ev.clientX - x0) / k
    if (Math.abs(dx) > 3) moved = true
    const ns = qS(s0 + Math.round(dx / 10) / 10)
    if (ns !== s.value[i]) {
      s.value = s.value.map((v, j) => (j === i ? ns : v))
      touched = true
    }
  }
  const up = (ev) => {
    if (ev.pointerId !== e.pointerId) return
    el.removeEventListener('pointermove', move)
    el.removeEventListener('pointerup', up)
    el.removeEventListener('pointercancel', up)
    scrubbing.value = -1
    if (!moved) { sel.value = i; touched = true }
  }
  el.addEventListener('pointermove', move)
  el.addEventListener('pointerup', up)
  el.addEventListener('pointercancel', up)
}
function scoreKey(e, i) {
  let d = 0
  if (e.key === 'ArrowRight' || e.key === 'ArrowUp') d = 0.1
  else if (e.key === 'ArrowLeft' || e.key === 'ArrowDown') d = -0.1
  else if (e.key === 'PageUp') d = 1
  else if (e.key === 'PageDown') d = -1
  else if (e.key === 'Escape') { e.currentTarget.blur(); return }
  else return
  e.preventDefault()
  e.stopPropagation()
  s.value = s.value.map((v, j) => (j === i ? qS(v + d) : v))
  touched = true
}
function pick(i, e) {
  e?.stopPropagation()
  sel.value = i
  touched = true
}

// ---- drawing words -----------------------------------------------------------------------------------
function drawOne() {
  const r = mulberry32(seq.value * 7919 + 4111)()
  seq.value += 1
  let acc = 0
  let k = rows.value.length - 1
  for (const row of rows.value) { acc += row.p; if (r < acc) { k = row.i; break } }
  counts.value = counts.value.map((c, j) => (j === k ? c + 1 : c))
  last.value = k
  flash.value += 1
}
const flash = ref(0)
let burst = 0
function stopBurst() { if (burst) clearInterval(burst); burst = 0 }
function draw(n, e) {
  stopBurst()
  touched = true
  if (n === 1 || reduceMotion) { for (let i = 0; i < n; i++) drawOne() }
  else {
    let left = n
    drawOne(); left--
    burst = setInterval(() => { drawOne(); if (--left <= 0) stopBurst() }, 70)
  }
  if (e?.detail) e.currentTarget.blur()
}
// A new distribution starts a new tally (not when it came from the other window).
let remoteTS = ''
watch([T, s], () => {
  if (JSON.stringify([T.value, s.value]) === remoteTS) { remoteTS = ''; return }
  stopBurst()
  counts.value = props.words.map(() => 0)
  last.value = -1
})

// ---- the chosen word pushed through ------------------------------------------------------------------
const push = computed(() => {
  const r = rows.value[sel.value]
  return {
    w: r.w,
    terms: rows.value.map((q) => ({ i: q.i, s: fmt(q.s, 1) })),
    e: sig4(r.e),
    sum: sig4(total.value),
    p: fmt(r.p, 3),
  }
})
const Ts = computed(() => fmt(T.value, 2))

// ---- presenter ↔ audience -------------------------------------------------------------------------------
const { $page, $renderContext } = useSlideContext()
const instance = Math.random().toString(36).slice(2)
const syncKey = () => `SoftmaxTemperature:${$page.value}:${props.syncId}`
let chan = null
let shared = ''
let pending = 0
const stateJSON = () => JSON.stringify({ T: T.value, s: s.value, sel: sel.value, counts: counts.value, last: last.value, seq: seq.value })
function post(msg) { chan?.postMessage({ key: syncKey(), from: instance, ...msg }) }
watch([T, s, sel, counts, last, seq], () => {
  if (!chan || pending) return
  pending = requestAnimationFrame(() => {
    pending = 0
    const st = stateJSON()
    if (st === shared) return
    shared = st
    post({ type: 'state', state: st })
  })
})
onMounted(() => {
  const ctx = $renderContext?.value
  if (typeof BroadcastChannel === 'undefined' || (ctx !== 'slide' && ctx !== 'presenter')) return
  shared = stateJSON()
  chan = new BroadcastChannel('course-interactive-figures')
  chan.onmessage = ({ data: m }) => {
    if (!m || m.key !== syncKey() || m.from === instance) return
    if (m.type === 'state') {
      stopBurst()
      shared = m.state
      touched = true
      const st = JSON.parse(m.state)
      const key = JSON.stringify([st.T, st.s])
      remoteTS = key !== JSON.stringify([T.value, s.value]) ? key : ''
      T.value = st.T
      s.value = st.s
      sel.value = st.sel
      counts.value = st.counts
      if (st.last !== last.value) flash.value += 1
      last.value = st.last
      seq.value = st.seq
    } else if (m.type === 'hello' && touched) {
      post({ type: 'state', state: stateJSON() })
    }
  }
  post({ type: 'hello' })
})
onBeforeUnmount(() => {
  stopBurst()
  if (pending) cancelAnimationFrame(pending)
  chan?.close()
  chan = null
})
</script>

<template>
  <section class="ism">
    <!-- No direct <div> children: the theme turns those of a .fig-fill into
         shrinking flex columns (custom-slides.css, FILL). -->
    <header class="ism-prompt">
      <span>{{ prompt }}</span>
      <span class="ism-blank" :class="{ 'ism-blank-empty': last < 0 }">
        <span :key="flash" class="ism-word">{{ last >= 0 ? words[last] : '…' }}</span>
      </span>
    </header>

    <section class="ism-table" role="table" aria-label="Scores into probabilities">
      <div class="ism-tr ism-th" role="row">
        <span role="columnheader">next word</span>
        <span role="columnheader" class="ism-num">score <i class="ism-mi">s</i> <em>drag ↔</em></span>
        <span role="columnheader" class="ism-num"><i class="ism-mi">s</i>/<i class="ism-mi">T</i></span>
        <span role="columnheader" class="ism-num"><span class="ism-m">e</span><sup><i class="ism-mi">s</i>/<i class="ism-mi">T</i></sup></span>
        <span role="columnheader" class="ism-num"><i class="ism-mi">p</i></span>
        <span role="columnheader" />
        <span role="columnheader" class="ism-num">drawn</span>
      </div>
      <div
        v-for="r in rows"
        :key="r.i"
        class="ism-tr"
        :class="{ 'ism-sel': r.i === sel, 'ism-hit': r.i === last }"
        role="row"
        @pointerdown="pick(r.i, $event)"
      >
        <span class="ism-w" role="cell">{{ r.w }}</span>
        <span
          class="ism-num ism-score"
          :class="{ 'ism-scrub': scrubbing === r.i }"
          role="slider"
          tabindex="0"
          :aria-label="`score of ${r.w}`"
          :aria-valuemin="-5"
          :aria-valuemax="5"
          :aria-valuenow="r.s"
          @pointerdown="scoreDown($event, r.i)"
          @mousedown.prevent
          @keydown="scoreKey($event, r.i)"
        >{{ fmt(r.s, 1) }}</span>
        <span class="ism-num ism-mid" role="cell">{{ fmt(r.z, 3) }}</span>
        <span class="ism-num ism-mid" role="cell" v-html="sig4(r.e)" />
        <span class="ism-num ism-p" role="cell">{{ fmt(r.p, 3) }}</span>
        <span class="ism-barcell" role="cell">
          <span class="ism-bar" :style="{ width: `${r.p * 100}%` }" />
        </span>
        <span class="ism-num ism-count" role="cell">{{ counts[r.i] || '' }}</span>
      </div>
      <div class="ism-tr ism-tsum" role="row">
        <span />
        <span />
        <span />
        <span class="ism-num ism-mid" role="cell"><span class="ism-m">Σ</span> = <span v-html="sig4(total)" /></span>
        <span class="ism-num" role="cell">1.000</span>
        <span />
        <span class="ism-num ism-count" role="cell">{{ drawn || '' }}</span>
      </div>
    </section>

    <figure class="ism-math ism-line">
      <span class="ism-general"><i>p</i><sub><i>i</i></sub> = <span class="ism-frac"><span>e<sup><i>s</i><sub><i>i</i></sub>/<i>T</i></sup></span><span><span class="ism-sum">Σ</span><sub><i>j</i></sub> e<sup><i>s</i><sub><i>j</i></sub>/<i>T</i></sup></span></span></span>
      <span class="ism-spec">
        <i>p</i>(<span class="ism-on">{{ push.w }}</span>) =
        <span class="ism-frac">
          <span>e<sup>{{ push.terms[sel].s }}/{{ Ts }}</sup></span>
          <span><template v-for="(q, k) in push.terms" :key="q.i">{{ k ? ' + ' : '' }}<span :class="{ 'ism-on': q.i === sel }">e<sup>{{ q.s }}/{{ Ts }}</sup></span></template></span>
        </span>
        = <span class="ism-frac"><span v-html="push.e" /><span v-html="push.sum" /></span>
        = <b class="ism-on">{{ push.p }}</b>
      </span>
    </figure>

    <footer class="ism-controls">
      <span class="ism-tname"><i class="ism-mi">T</i> = <b>{{ Ts }}</b></span>
      <div
        class="ism-slider"
        role="slider"
        tabindex="0"
        aria-label="temperature"
        :aria-valuemin="T_MIN"
        :aria-valuemax="T_MAX"
        :aria-valuenow="T"
        @pointerdown="sliderDown"
        @mousedown.prevent
        @keydown="sliderKey"
      >
        <span class="ism-track">
          <span class="ism-fill" :style="{ width: `${uOf(T) * 100}%` }" />
          <span v-for="c in T_CHIPS" :key="'d' + c" class="ism-dec" :style="{ left: `${uOf(c) * 100}%` }" />
          <span class="ism-thumb" :style="{ left: `${uOf(T) * 100}%` }" />
        </span>
      </div>
      <div class="ism-chips">
        <button
          v-for="c in T_CHIPS"
          :key="c"
          type="button"
          class="ism-chip"
          :class="{ 'ism-chip-on': c === T }"
          @mousedown.prevent
          @pointerdown.stop
          @click="chipT(c, $event)"
        >{{ c }}</button>
      </div>
      <div class="ism-buttons">
        <button type="button" class="ism-btn ism-btn-main" @mousedown.prevent @pointerdown.stop @click="draw(1, $event)">draw</button>
        <button type="button" class="ism-btn" @mousedown.prevent @pointerdown.stop @click="draw(20, $event)">×20</button>
      </div>
    </footer>
  </section>
</template>

<style scoped>
.ism {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 0.7rem;
  height: 21rem;
  min-height: 0;
  user-select: none;
  -webkit-user-select: none;
  color: var(--fg);
  font-family: var(--font-sans);
  font-variant-numeric: tabular-nums;
}

.ism-prompt {
  display: flex;
  align-items: baseline;
  gap: 0.6rem;
  font-size: 1.3em;
  color: var(--fg-2);
}
.ism-blank {
  display: inline-block;
  min-width: 6.5em;
  padding: 0 0.3em 0.05em;
  border-bottom: 1.5px solid var(--accent);
  text-align: center;
}
.ism-blank-empty { border-bottom-color: var(--hair-strong); }
.ism-word { display: inline-block; color: var(--accent); font-weight: 600; animation: ism-pop 0.45s var(--ease); }
.ism-blank-empty .ism-word { color: var(--dim); font-weight: 400; animation: none; }
@keyframes ism-pop {
  from { opacity: 0; transform: translateY(0.35em); }
  to { opacity: 1; transform: none; }
}

/* ---- the table ---- */
.ism-table { display: flex; flex-direction: column; }
.ism-tr {
  display: grid;
  grid-template-columns: 7.5rem 7.2rem 5.2rem 6.6rem 4.6rem minmax(0, 1fr) 4rem;
  align-items: center;
  column-gap: 0.9rem;
  min-height: 2.35rem;
  padding: 0 0.6rem;
  border-top: 1px solid var(--hair);
  cursor: pointer;
  transition: background-color 0.3s var(--ease);
}
.ism-tr:last-child { border-bottom: 1px solid var(--hair); }
.ism-th {
  min-height: 1.7rem;
  border-top: none;
  cursor: default;
  font-size: 0.8rem;
  letter-spacing: 0.06em;
  color: var(--dim);
}
.ism-th em { font-style: normal; font-size: 0.85em; color: var(--accent); opacity: 0.8; margin-left: 0.25em; }
.ism-tsum { cursor: default; min-height: 1.9rem; color: var(--dim); font-size: 0.95rem; }
.ism-num { text-align: right; white-space: nowrap; }
.ism-w { font-size: 1.15rem; color: var(--fg); }
.ism-sel { background: rgba(125, 211, 252, 0.05); }
.ism-sel .ism-w { color: var(--accent); font-weight: 600; }
.ism-mid { color: var(--fg-2); font-size: 1rem; }
.ism-p { font-size: 1.15rem; font-weight: 500; }
.ism-sel .ism-p { color: var(--accent); }
.ism-count { color: var(--dim); font-size: 0.95rem; }
.ism-hit .ism-count { color: var(--accent); }

.ism-score {
  justify-self: end;
  min-width: 3.4rem;
  padding: 0.12rem 0.5rem;
  border-radius: 4px;
  border: 1px dashed var(--hair-strong);
  font-size: 1.1rem;
  cursor: ew-resize;
  touch-action: none;
  outline: none;
  transition: border-color 0.3s var(--ease), color 0.3s var(--ease);
}
.ism-score:hover,
.ism-score:focus-visible,
.ism-scrub { border-color: var(--accent); color: var(--accent); }

.ism-barcell { position: relative; height: 0.85rem; background: rgba(255, 255, 255, 0.03); border-radius: 2px; overflow: hidden; }
.ism-bar {
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  background: var(--fg-2);
  opacity: 0.6;
  border-radius: 2px;
  transition: width 0.35s var(--ease);
}
.ism-sel .ism-bar { background: var(--accent); opacity: 0.9; }

/* ---- math, set like the slides' KaTeX ---- */
.ism-math,
.ism-m {
  font-family: KaTeX_Main, 'Times New Roman', serif;
}
.ism-math i,
.ism-mi,
.ism-tname {
  font-family: KaTeX_Math, 'Times New Roman', serif;
  font-style: italic;
}
.ism-th .ism-mi,
.ism-th .ism-m { font-size: 1.2em; letter-spacing: 0; }
.ism-math sup,
.ism-math sub,
.ism-th sup,
.ism-mid :deep(sup) { font-size: 0.7em; line-height: 0; }
.ism-math sup sub { font-size: 0.85em; }
.ism-line {
  margin: 0;
  display: flex;
  align-items: center;
  gap: 2.2rem;
  font-size: 1.21em;
  white-space: nowrap;
}
.ism-general { color: var(--fg-2); }
.ism-sum { font-size: 1.15em; margin-right: 0.05em; }
.ism-frac {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  vertical-align: middle;
  margin: 0 0.1em;
}
.ism-frac > span { padding: 0 0.2em; line-height: 1.35; }
.ism-frac > span:first-child { border-bottom: 1px solid currentColor; }
.ism-on { color: var(--accent); }
.ism-line b { font-weight: 400; }

/* ---- controls ---- */
.ism-controls {
  display: grid;
  grid-template-columns: 6.2rem minmax(0, 1fr) auto auto;
  align-items: center;
  gap: 1rem;
}
.ism-tname { font-size: 1.3em; white-space: nowrap; }
.ism-tname b { font-family: KaTeX_Main, 'Times New Roman', serif; font-style: normal; font-weight: 400; color: var(--accent); }
.ism-slider {
  display: flex;
  align-items: center;
  height: 2rem;
  padding: 0 7px;
  cursor: pointer;
  touch-action: none;
  outline: none;
  border-radius: 4px;
}
.ism-slider:focus-visible { box-shadow: 0 0 0 1px var(--hair-strong); }
.ism-track { position: relative; flex: 1; height: 2px; background: var(--hair-strong); border-radius: 1px; }
.ism-fill { position: absolute; left: 0; top: 0; bottom: 0; background: var(--accent); opacity: 0.55; }
.ism-dec { position: absolute; top: -4px; bottom: -4px; width: 0; border-left: 1px solid var(--dim); opacity: 0.7; }
.ism-thumb {
  position: absolute;
  top: 50%;
  width: 18px;
  height: 18px;
  margin: -9px 0 0 -9px;
  border-radius: 50%;
  background: var(--accent);
  transition: transform 0.25s var(--ease);
}
.ism-slider:hover .ism-thumb,
.ism-slider:focus-visible .ism-thumb { transform: scale(1.2); }
.ism-chips,
.ism-buttons { display: flex; gap: 0.4rem; }
.ism-chip,
.ism-btn {
  font-family: var(--font-sans);
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--fg-2);
  background: none;
  border: 1px solid var(--hair-strong);
  border-radius: 4px;
  padding: 0.3rem 0.6rem;
  cursor: pointer;
  transition: color 0.3s var(--ease), border-color 0.3s var(--ease);
}
.ism-chip { min-width: 2.6rem; font-variant-numeric: tabular-nums; }
.ism-btn { letter-spacing: 0.1em; text-transform: uppercase; padding: 0.36rem 0.8rem; }
.ism-chip:hover,
.ism-chip:focus-visible,
.ism-btn:hover,
.ism-btn:focus-visible { color: var(--accent); border-color: var(--accent); outline: none; }
.ism-chip-on { color: var(--accent); border-color: var(--accent); }
.ism-btn-main { color: var(--accent); border-color: color-mix(in srgb, var(--accent) 55%, transparent); }

@media (prefers-reduced-motion: reduce) {
  .ism-word { animation: none; }
  .ism-tr,
  .ism-score,
  .ism-bar,
  .ism-thumb,
  .ism-chip,
  .ism-btn { transition: none; }
}
</style>
