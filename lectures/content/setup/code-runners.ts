// Slidev code-runners setup: route matplotlib figures into the runner output,
// and show tracebacks the way plain Python prints them.
//
// The `python`/`py` runners come from slidev-addon-python-runner (Pyodide).
// That runner relays only stdout/stderr. `plt.show()` under Pyodide's
// matplotlib backend draws the figure into a DOM node appended to
// `document.pyodideMplTarget`, falling back to `document.body` — which in
// Slidev's fixed-viewport layout sits below the slide frame, so the plot
// renders but is never visible (L10 "Try It — Bin Width", every L13 plot).
//
// Project setups run after addon setups and receive the accumulated runner
// map, so this wraps the addon's runner: each run gets a fresh container that
// becomes the figure target and is returned as an `element` output, which
// Slidev mounts inside `.slidev-runner-output`. Figure chrome/sizing is
// styled in theme/styles/monaco.css (.slidev-python-figures).
//
// No @slidev/types import (not hoisted under pnpm); the setup is a plain
// function, same as setup/shiki.ts. `vue` is deduped by Slidev.
import { toValue } from 'vue'

type Runner = (code: string, ctx: unknown) => Promise<unknown>

// An error arrives as one red line per traceback line, and Pyodide's
// traceback holds frames of its own machinery (`File "/lib/python3…/_pyodide/
// …"`) next to the student's code (`File "<exec>"`). Show what plain Python
// would: drop every frame in Pyodide's `_pyodide` package (the `File` line
// and the indented source / `^^^` lines under it), in each traceback of a
// chained error, and the `PythonError: ` prefix of the first line. Frames in
// library code (numpy, pandas) stay, as in plain Python.
function trimTraceback(items: any[]) {
  const red = (it: any) => it && it.class === 'text-red' && typeof it.text === 'string'
  const out: any[] = []
  let skipping = false
  let first = true
  for (const it of items) {
    if (!red(it)) {
      out.push(it)
      continue
    }
    const text: string = it.text
    if (/^\s+File "[^"]*\/_pyodide\//.test(text)) {
      skipping = true
      continue
    }
    // a skipped frame's own lines are indented deeper than `  File`
    if (skipping && /^\s{4,}/.test(text))
      continue
    skipping = false
    out.push(first ? { ...it, text: text.replace(/^PythonError:\s*/, '') } : it)
    first = false
  }
  // the message ends in a newline: no empty red rows under it
  while (out.length && red(out[out.length - 1]) && !out[out.length - 1].text.trim())
    out.pop()
  return out
}

export default function setup(runners: Record<string, Runner>) {
  const base = runners.python ?? runners.py
  if (!base)
    return {}

  const run: Runner = async (code, ctx) => {
    const figures = document.createElement('div')
    figures.className = 'slidev-python-figures'
    ;(document as any).pyodideMplTarget = figures

    const outputs = await base(code, ctx)
    // The addon returns a reactive getter (stdout lines arrive while the code
    // runs); keep it lazy so Slidev re-renders as lines are appended. The
    // container is always included — matplotlib appends into it later, and an
    // empty container is hidden by CSS.
    return () => {
      const items = toValue(outputs as any)
      return [...trimTraceback(Array.isArray(items) ? items : [items]), { element: figures }]
    }
  }

  return { python: run, py: run }
}
