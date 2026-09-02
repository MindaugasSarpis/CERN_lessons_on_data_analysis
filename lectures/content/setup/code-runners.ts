// Slidev code-runners setup: route matplotlib figures into the runner output.
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
      return [...(Array.isArray(items) ? items : [items]), { element: figures }]
    }
  }

  return { python: run, py: run }
}
