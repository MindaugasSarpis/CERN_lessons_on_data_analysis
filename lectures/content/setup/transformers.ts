/**
 * Markdown transformers (Slidev setup hook, runs at build time).
 *
 * Mermaid: the slides' semantic classDefs (input / process / output / check /
 * bad and their aliases, theme/mermaid-config.md) still spell out the old navy
 * fills. Mermaid turns a classDef into an INLINE `style="… !important"` that no
 * stylesheet can outrank, so fill / stroke / color are dropped from those
 * classDefs here and the `.node.<class>` rules in setup/mermaid.ts colour them.
 * Slide sources need no edit; classDefs with other names are left alone.
 */
// No @slidev/types import (not hoisted under pnpm — see shiki.ts); the
// define* helpers are identity functions, a plain default export works.

// classDef names whose colours come from mermaid.ts themeCSS.
const SEMANTIC = new Set([
  'input', 'action', 'highlight', 'accent',
  'output', 'good', 'success',
  'check', 'decision', 'warning', 'warn',
  'bad', 'fail', 'error',
  'process', 'step', 'stage',
])
const COLOUR_KEYS = new Set(['fill', 'stroke', 'color'])

/** Drop fill / stroke / color from semantic classDefs (keep e.g. font-size). */
export function recolourClassDefs(code: string): string {
  return code.replace(/^(\s*classDef\s+)([\w,-]+)(\s+)([^\n]*?)(;?)[ \t]*$/gm,
    (line, head, names, gap, styles, semi) => {
      if (!String(names).split(',').every(n => SEMANTIC.has(n)))
        return line
      const kept = String(styles).split(',')
        .filter(s => !COLOUR_KEYS.has(s.split(':')[0].trim()))
      // An empty classDef is a parse error; stroke-width is what themeCSS sets anyway.
      return `${head}${names}${gap}${kept.length ? kept.join(',') : 'stroke-width:1px'}${semi}`
    })
}

const FENCE = /^([ \t]*)(`{3,}|~{3,})mermaid\b[^\n]*\n[\s\S]*?^\1\2[ \t]*$/gm

export default () => ({
  pre: [
    (ctx: { s: { toString(): string, overwrite(a: number, b: number, c: string): unknown } }) => {
      const src = ctx.s.toString()
      for (const m of src.matchAll(FENCE)) {
        const out = recolourClassDefs(m[0])
        if (out !== m[0])
          ctx.s.overwrite(m.index!, m.index! + m[0].length, out)
      }
    },
  ],
})
