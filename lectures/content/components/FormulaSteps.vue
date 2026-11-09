<!--
  FormulaSteps — a formula evaluated one step per click.

  One step per line of the `steps` attribute, in a small subset of LaTeX
  (no escaping needed in a plain attribute):

    <FormulaSteps steps="
      \bar{x} = \frac{x_1 + x_2 + x_3 + x_4}{N}
      = \frac{27.3 + 25.6 + 24.6 + 23.6}{4}
      = \frac{101.1}{4}
      = 25.275
    " />

  or an array (in a bound attribute a backslash must be doubled):
    <FormulaSteps :steps="['s = 8.85', '\\frac{s}{\\sqrt{N}} = \\frac{8.85}{\\sqrt{100}}', '= 0.885']" />

  The first step shows at once; each click adds the next (Slidev's own
  clicks, so the presenter's clicker, the presenter view and the audience
  window agree). What changed at the current step is in the accent colour.
  Every step's room is kept from the start, so the slide never grows.

    mode="stack"  (default) each step on its own line, aligned at the first "="
    mode="morph"  one line that turns into the next step: the parts that stay
                  glide to their new place, the parts that change fade
    at="3"        start at click 3 (default "+1", after the clicks before it)
    :hl="false"   no accent on what changed

  LaTeX subset: \frac{}{} \sqrt{} \bar{} \hat{} \text{} \hl{} (accent), _ ^ { },
  Greek letters, \sum \prod \cdot \times \pm \approx \le \ge \ne \to \infty
  \ldots \exp \ln \log, and \, \; \quad for space. A single letter is set in
  italic, a word upright. Tokens are separated by spaces outside braces.
-->
<script>
const GREEK = {
  alpha: 'α', beta: 'β', gamma: 'γ', delta: 'δ', epsilon: 'ε', varepsilon: 'ε', zeta: 'ζ',
  eta: 'η', theta: 'θ', iota: 'ι', kappa: 'κ', lambda: 'λ', mu: 'μ', nu: 'ν', xi: 'ξ',
  pi: 'π', rho: 'ρ', sigma: 'σ', tau: 'τ', upsilon: 'υ', phi: 'φ', varphi: 'φ', chi: 'χ',
  psi: 'ψ', omega: 'ω', Gamma: 'Γ', Delta: 'Δ', Theta: 'Θ', Lambda: 'Λ', Xi: 'Ξ', Pi: 'Π',
  Sigma: 'Σ', Phi: 'Φ', Psi: 'Ψ', Omega: 'Ω',
}
const BIG = { sum: 'Σ', prod: 'Π', int: '∫' }
const REL = { approx: '≈', le: '≤', leq: '≤', ge: '≥', geq: '≥', ne: '≠', neq: '≠', to: '→', rightarrow: '→', propto: '∝', sim: '∼', in: '∈' }
const BIN = { cdot: '·', times: '×', pm: '±', mp: '∓' }
const ORD = { infty: '∞', ldots: '…', dots: '…', cdots: '⋯', partial: '∂', nabla: '∇', circ: '∘', degree: '°', '%': '%', '{': '{', '}': '}', '_': '_', '#': '#', '&': '&amp;' }
const SPACE = { ',': '<span class="fs-sp1"></span>', ':': '<span class="fs-sp1"></span>', ';': '<span class="fs-sp2"></span>', quad: '<span class="fs-sp3"></span>', qquad: '<span class="fs-sp3"></span><span class="fs-sp3"></span>' }
const UPRIGHT = new Set(['exp', 'ln', 'log', 'sin', 'cos', 'tan', 'min', 'max', 'arg', 'det'])
const RELCH = new Set(['=', '<', '>', '≈', '≤', '≥', '≠', '→'])
const BINCH = new Set(['+', '−', '·', '×', '±'])

const esc = (t) => t.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c])

// LaTeX subset → HTML (numbers and letters only come from the author's steps).
// `st.prev` (start | open | op | atom) carries over from token to token, so a
// "+" between two tokens is a binary operator with its spaces, as in LaTeX.
function tex(src, st = { prev: 'start' }) {
  let i = 0
  let out = ''
  const s = src
  const readArg = () => {
    while (s[i] === ' ') i++
    if (s[i] === '{') {
      const start = ++i
      let depth = 1
      while (i < s.length && depth) {
        if (s[i] === '\\') { i += 2; continue }
        if (s[i] === '{') depth++
        else if (s[i] === '}') depth--
        i++
      }
      return s.slice(start, i - 1)
    }
    if (s[i] === '\\') {
      const m = /^\\([A-Za-z]+|.)/.exec(s.slice(i))
      i += m[0].length
      return m[0]
    }
    const ch = /^\p{L}\p{M}*|^./u.exec(s.slice(i))?.[0] ?? ''
    i += ch.length
    return ch
  }
  const op = (ch, rel) => {
    if (rel) { out += `<span class="fs-rel">${esc(ch)}</span>`; st.prev = 'op'; return }
    if (st.prev === 'atom') { out += `<span class="fs-bin">${esc(ch)}</span>`; st.prev = 'op'; return }
    out += esc(ch)                    // unary: −3, (−0.055)
    st.prev = 'op'
  }
  while (i < s.length) {
    const c = s[i]
    if (c === '\\') {
      const m = /^\\([A-Za-z]+|.)/.exec(s.slice(i))
      i += m[0].length
      const name = m[1]
      if (name === 'frac' || name === 'dfrac' || name === 'tfrac') {
        const a = readArg()
        const b = readArg()
        out += `<span class="fs-frac"><span>${tex(a)}</span><span>${tex(b)}</span></span>`
        st.prev = 'atom'
      } else if (name === 'sqrt') {
        out += `<span class="fs-sqrt"><span class="fs-rad">√</span><span class="fs-under">${tex(readArg())}</span></span>`
        st.prev = 'atom'
      } else if (name === 'bar' || name === 'overline') {
        const arg = readArg()
        const lo = /^[a-zα-ω]$/.test(arg.trim()) ? ' fs-bar-lo' : ''
        out += `<span class="fs-bar${lo}">${tex(arg)}</span>`
        st.prev = 'atom'
      } else if (name === 'hat') {
        out += `<span class="fs-hat">${tex(readArg())}</span>`
        st.prev = 'atom'
      } else if (name === 'text' || name === 'mathrm' || name === 'textrm' || name === 'operatorname') {
        out += `<span class="fs-up">${esc(readArg())}</span>`
        st.prev = 'atom'
      } else if (name === 'hl') {
        out += `<span class="fs-hl">${tex(readArg())}</span>`
        st.prev = 'atom'
      } else if (name === 'left' || name === 'right') {
        // sizes are not drawn; the delimiter that follows is
      } else if (name in GREEK) {
        const g = GREEK[name]
        out += g === g.toLowerCase() ? `<i>${g}</i>` : g
        st.prev = 'atom'
      } else if (name in BIG) {
        out += `<span class="fs-big">${BIG[name]}</span>`
        st.prev = 'op'
      } else if (name in REL) {
        op(REL[name], true)
      } else if (name in BIN) {
        op(BIN[name], false)
      } else if (name in ORD) {
        out += ORD[name]
        st.prev = 'atom'
      } else if (name in SPACE) {
        out += SPACE[name]
      } else if (UPRIGHT.has(name)) {
        out += `<span class="fs-up">${name}</span>`
        st.prev = 'op'
      } else {
        out += esc(name)
        st.prev = 'atom'
      }
    } else if (c === '{') {
      out += tex(readArg())
      st.prev = 'atom'
    } else if (c === '_' || c === '^') {
      i++
      const tag = c === '_' ? 'sub' : 'sup'
      out += `<${tag}>${tex(readArg())}</${tag}>`
      st.prev = 'atom'
    } else if (c === '°' && /[CF]/.test(s[i + 1] || '')) {
      out += `<span class="fs-up fs-unit">°${s[i + 1]}</span>`
      i += 2
      st.prev = 'atom'
    } else if (/\p{L}/u.test(c)) {
      const w = /^(?:\p{L}\p{M}*)+/u.exec(s.slice(i))[0]
      i += w.length
      const one = [...w].length === 1 || /^\p{L}\p{M}+$/u.test(w)
      // one letter is a variable (italic), except a capital Greek one (Σ, Δ: upright, as in LaTeX)
      out += one && !/^[Α-Ω]$/.test(w) ? `<i>${esc(w)}</i>` : `<span class="fs-up">${esc(w)}</span>`
      st.prev = 'atom'
    } else if (c === '-' || c === '−') {
      i++
      op('−', false)
    } else if (c === '*') {
      i++
      op('·', false)
    } else if (BINCH.has(c)) {
      i++
      op(c, false)
    } else if (RELCH.has(c)) {
      i++
      op(c, true)
    } else if (c === '(' || c === '[') {
      i++
      out += c
      st.prev = 'open'
    } else if (c === ' ') {
      i++                             // math mode: spacing comes from the operators
    } else if (c === '~') {
      i++
      out += '&nbsp;'
    } else {
      i++
      out += esc(c)
      st.prev = 'atom'
    }
  }
  return out
}

// A step's tokens: split at spaces outside braces.
function tokens(step) {
  const out = []
  let depth = 0
  let cur = ''
  for (let i = 0; i < step.length; i++) {
    const c = step[i]
    if (c === '\\' && i + 1 < step.length) { cur += c + step[++i]; continue }
    if (c === '{') depth++
    if (c === '}') depth = Math.max(0, depth - 1)
    if (/\s/.test(c) && depth === 0) { if (cur) out.push(cur); cur = ''; continue }
    cur += c
  }
  if (cur) out.push(cur)
  return out
}

// Which tokens of b are tokens of a kept in place (longest common subsequence).
function lcsPairs(a, b) {
  const n = a.length
  const m = b.length
  const L = Array.from({ length: n + 1 }, () => new Int16Array(m + 1))
  for (let i = n - 1; i >= 0; i--) {
    for (let j = m - 1; j >= 0; j--) L[i][j] = a[i] === b[j] ? L[i + 1][j + 1] + 1 : Math.max(L[i + 1][j], L[i][j + 1])
  }
  const pairs = new Map()                // index in b → index in a
  let i = 0
  let j = 0
  while (i < n && j < m) {
    if (a[i] === b[j]) { pairs.set(j, i); i++; j++ }
    else if (L[i + 1][j] >= L[i][j + 1]) i++
    else j++
  }
  return pairs
}

let uid = 0
</script>

<script setup>
import { computed, onMounted, onUnmounted, ref, watchEffect } from 'vue'
import { useSlideContext } from '@slidev/client'

const props = defineProps({
  // One step per line (a string) or one per item (an array).
  steps: { type: [String, Array], required: true },
  mode: { type: String, default: 'stack' },
  at: { type: [Number, String], default: '+1' },
  hl: { type: Boolean, default: true },
})

const CLICKS_MAX = 999999
const reduceMotion = typeof window !== 'undefined'
  && window.matchMedia?.('(prefers-reduced-motion: reduce)').matches

const list = computed(() => (Array.isArray(props.steps) ? props.steps : props.steps.split('\n'))
  .map((t) => String(t).trim())
  .filter(Boolean))

// Each step as tokens with keys that persist while a token stays.
const parsed = computed(() => {
  let next = 0
  const out = []
  let prevHtml = []
  let prevKeys = []
  for (const step of list.value) {
    const st = { prev: 'start' }
    const html = tokens(step).map((t) => tex(t, st))
    const pairs = lcsPairs(prevHtml, html)
    const keys = html.map((_, j) => (pairs.has(j) ? prevKeys[pairs.get(j)] : `t${next++}`))
    const fresh = html.map((_, j) => out.length > 0 && !pairs.has(j))
    // stack: split at the first relation (=, ≈, …) so the steps line up there
    let cut = html.findIndex((h) => /^<span class="fs-rel">/.test(h))
    if (cut < 0) cut = 0
    out.push({ html, keys, fresh, cut })
    prevHtml = html
    prevKeys = keys
  }
  return out
})
const n = computed(() => parsed.value.length)

// ---- clicks: the same registration as Slidev's own v-switch ---------------------------
const { $clicksContext: clicks } = useSlideContext()
const offset = ref(0)
const id = `formula-steps-${++uid}`
onMounted(() => {
  if (n.value < 2) { offset.value = CLICKS_MAX; return }
  const info = clicks?.calculateSince(props.at, n.value - 1)
  if (!info) { offset.value = CLICKS_MAX; return }
  clicks.register(id, info)
  watchEffect(() => { offset.value = info.currentOffset.value + 1 })
})
onUnmounted(() => { clicks?.unregister?.(id) })
const step = computed(() => Math.max(0, Math.min(n.value - 1, offset.value)))

const current = computed(() => {
  const p = parsed.value[step.value]
  if (!p) return []
  return p.html.map((h, j) => ({ key: p.keys[j], html: h, fresh: props.hl && p.fresh[j] }))
})

// TransitionGroup: a leaving token keeps its place while it fades.
function beforeLeave(el) {
  el.style.left = `${el.offsetLeft}px`
  el.style.top = `${el.offsetTop}px`
  el.style.width = `${el.offsetWidth}px`
  el.style.height = `${el.offsetHeight}px`
}
</script>

<template>
  <section class="fs" :class="[`fs-${mode === 'morph' ? 'morph' : 'stack'}`, { 'fs-still': reduceMotion }]" role="math" :aria-label="list[step]">
    <span v-if="mode !== 'morph'" class="fs-grid">
      <template v-for="(p, k) in parsed" :key="k">
        <span class="fs-lhs" :class="{ 'fs-past': k < step, 'fs-future': k > step, 'fs-now': k === step }" :aria-hidden="k > step">
          <span
            v-for="(h, j) in p.html.slice(0, p.cut)"
            :key="j"
            class="fs-tok"
            :class="{ 'fs-fresh': hl && k === step && p.fresh[j] }"
            v-html="h"
          />
        </span>
        <span class="fs-rhs" :class="{ 'fs-past': k < step, 'fs-future': k > step, 'fs-now': k === step }" :aria-hidden="k > step">
          <span
            v-for="(h, j) in p.html.slice(p.cut)"
            :key="j"
            class="fs-tok"
            :class="{ 'fs-fresh': hl && k === step && p.fresh[j + p.cut] }"
            v-html="h"
          />
        </span>
      </template>
    </span>
    <span v-else class="fs-cell">
      <!-- every step, invisible, in the same cell: the room of the widest and tallest -->
      <span v-for="(p, k) in parsed" :key="'s' + k" class="fs-line fs-sizer" aria-hidden="true">
        <span v-for="(h, j) in p.html" :key="j" class="fs-tok" v-html="h" />
      </span>
      <TransitionGroup tag="span" name="fs" class="fs-line fs-live" @before-leave="beforeLeave">
        <span v-for="t in current" :key="t.key" class="fs-tok" :class="{ 'fs-fresh': t.fresh }" v-html="t.html" />
      </TransitionGroup>
    </span>
  </section>
</template>

<style scoped>
.fs {
  display: flex;
  justify-content: center;
  font-family: KaTeX_Main, 'Times New Roman', serif;
  font-size: 1.6em;
  line-height: 1.3;
  color: var(--fg);
  font-variant-numeric: tabular-nums;
}
.fs :deep(i) {
  font-family: KaTeX_Math, 'Times New Roman', serif;
  font-style: italic;
}
.fs :deep(.fs-up) { font-style: normal; font-family: KaTeX_Main, 'Times New Roman', serif; }
.fs :deep(sub),
.fs :deep(sup) { font-size: 0.7em; line-height: 0; }
.fs :deep(.fs-bin) { margin: 0 0.22em; }
.fs :deep(.fs-rel) { margin: 0 0.28em; }
.fs :deep(.fs-big) { font-family: KaTeX_Size1, KaTeX_Main, 'Times New Roman', serif; font-size: 1.25em; vertical-align: -0.1em; margin-right: 0.08em; }
.fs :deep(.fs-sp1) { display: inline-block; width: 0.17em; }
.fs :deep(.fs-sp2) { display: inline-block; width: 0.28em; }
.fs :deep(.fs-sp3) { display: inline-block; width: 1em; }
.fs :deep(.fs-frac) {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  vertical-align: middle;
  margin: 0 0.1em;
  font-size: 0.92em;
}
.fs :deep(.fs-frac > span) { padding: 0 0.18em; line-height: 1.25; align-self: stretch; text-align: center; } /* the bar spans the wider of the two */
.fs :deep(.fs-frac > span:first-child) { border-bottom: 0.06em solid currentColor; padding-bottom: 0.06em; }
.fs :deep(.fs-frac > span:last-child) { padding-top: 0.06em; }
.fs :deep(.fs-sqrt) { display: inline-flex; align-items: flex-start; }
.fs :deep(.fs-rad) { margin-right: 0.02em; }
.fs :deep(.fs-under) { border-top: 0.06em solid currentColor; padding: 0.04em 0.08em 0; margin-top: 0.12em; }
.fs :deep(.fs-bar) { position: relative; display: inline-block; }
.fs :deep(.fs-bar)::before {
  content: '';
  position: absolute;
  left: 0.12em;
  right: -0.02em;
  top: 0.02em;
  border-top: 0.055em solid currentColor;
}
.fs :deep(.fs-bar-lo)::before { top: 0.3em; }
/* a unit is text, set like the slides' captions: 0.030 °C */
.fs :deep(.fs-unit) { margin-left: 0.2em; font-family: var(--font-sans); font-size: 0.82em; }
.fs :deep(.fs-hat) { position: relative; display: inline-block; }
.fs :deep(.fs-hat)::before {
  content: '^';
  position: absolute;
  left: 0;
  right: 0;
  top: -0.5em;
  text-align: center;
  font-family: KaTeX_Main, 'Times New Roman', serif;
  font-style: normal;
}
.fs :deep(.fs-hl) { color: var(--accent); }

/* ---- stack: one step per line, the first relation in one column ---- */
.fs-grid {
  display: grid;
  margin: 0;
  grid-template-columns: max-content max-content;
  column-gap: 0;
  row-gap: 0.45em;
  align-items: center;
}
.fs-lhs { justify-self: end; white-space: nowrap; }
.fs-rhs { justify-self: start; white-space: nowrap; }
.fs-tok { display: inline-block; }
.fs-past { color: var(--fg-2); }
.fs-past :deep(.fs-hl) { color: inherit; }
.fs-future { visibility: hidden; opacity: 0; transform: translateY(0.35em); }
.fs-now,
.fs-past { transition: opacity 0.45s var(--ease), transform 0.45s var(--ease), color 0.45s var(--ease); }
.fs-fresh { color: var(--accent); }

/* ---- morph: one line that turns into the next step ---- */
.fs-cell { display: grid; }
.fs-line { grid-area: 1 / 1; white-space: nowrap; justify-self: center; align-self: center; }
.fs-sizer { visibility: hidden; }
.fs-live { position: relative; }
.fs-move { transition: transform 0.55s var(--ease); }
.fs-enter-active { transition: opacity 0.45s var(--ease) 0.12s, transform 0.45s var(--ease) 0.12s; }
.fs-leave-active { position: absolute; transition: opacity 0.3s var(--ease), transform 0.3s var(--ease); }
.fs-enter-from { opacity: 0; transform: translateY(0.45em); }
.fs-leave-to { opacity: 0; transform: translateY(-0.45em); }
.fs-live .fs-tok { transition: color 0.45s var(--ease); }

.fs-still .fs-now,
.fs-still .fs-past,
.fs-still .fs-tok,
.fs-still .fs-move,
.fs-still .fs-enter-active,
.fs-still .fs-leave-active { transition: none !important; }
@media (prefers-reduced-motion: reduce) {
  .fs-now,
  .fs-past,
  .fs-tok,
  .fs-move,
  .fs-enter-active,
  .fs-leave-active { transition: none !important; }
  .fs-future { transform: none; }
}
</style>
