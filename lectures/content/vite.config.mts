// Vite settings for every deck built from lectures/content/ (Slidev merges a
// vite.config.* found in the deck's folder over its own, and ours wins).
// `.mts`, not `.ts`: an ES module whatever package.json says (Vite warns that
// its coming native config loader would read a `.ts` here as CommonJS).
//
// Why it exists: the mobile load of the decks with a Python runner block
// ({monaco-run}: Lectures 03, 05 and 07 in Nov 2026). Slidev's own
// `manualChunks` (@slidev/cli 53, `createConfigPlugin`) puts ALL of Shiki,
// every grammar and theme, into one chunk `modules/shiki`, and all the Monaco
// type declarations into one chunk `monaco/bundled-types`. The entry preloads
// both: 3.6 MB (gzip) of JavaScript before slide 1 could be drawn. Returning
// nothing for those modules lets the bundler split them along their own
// dynamic imports: the entry preloads 0.17 MB, and the editor, its types and
// a grammar load with the first slide that holds a runner block (Slidev
// renders the other slides in the background a few seconds after slide 1).
// Lecture 07 on Slow 4G with a 4x slower CPU: slide 1 after 4.2 s instead of
// 41.3 s (Nov 2026).
//
// The two rules kept are Slidev's: the icons in one chunk, Vue and file-saver
// each in their own. Compare with Slidev's function after a Slidev upgrade.
//
// The second part, figureHash(): every figure URL a built deck holds carries
// the figure's content hash, `/figures/viz_x.svg?v=1a2b3c4d`. A file in
// public/ keeps its name when its content changes, and GitHub Pages lets a
// browser keep a file for 10 minutes (max-age=600): after the deploy of
// 10 Nov 2026 a browser in the lecture room showed an old figure in a new
// layout. With the hash in the URL a changed figure is a new URL, and the
// chunk that names it changes its own hashed name with it. Slide sources keep
// `/figures/viz_x.svg`; dev (`pnpm dev`) is left as it is.
import { createHash } from 'node:crypto'
import { existsSync, readFileSync } from 'node:fs'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'
import { defineConfig, type Plugin } from 'vite'

const OWN_CHUNK = ['file-saver', 'vue', '@vue']

const FIGURES = join(dirname(fileURLToPath(import.meta.url)), 'public', 'figures')
// A figure URL as it stands in a built chunk: `<base>figures/<name>.<ext>`
// closed by a quote, a backtick, a parenthesis, a space or a `#`. One that
// already has a query is left alone.
const FIGURE_URL = /\/figures\/([\w\-./]+?\.(?:svg|png|jpe?g|jfif|gif|webp|avif))(?=[`'"\s)#])/g

function figureHash(): Plugin {
  const hashes = new Map<string, string | null>()
  const hashOf = (name: string) => {
    if (!hashes.has(name)) {
      const file = join(FIGURES, name)
      hashes.set(name, !name.includes('..') && existsSync(file)
        ? createHash('sha256').update(readFileSync(file)).digest('hex').slice(0, 8)
        : null)
    }
    return hashes.get(name)
  }
  return {
    name: 'course:figure-hash',
    apply: 'build',
    // after Vite's own asset plugin, which writes the base into public URLs
    enforce: 'post',
    buildStart() { hashes.clear() },
    // the slides' code
    renderChunk(code) {
      const out = withHashes(code)
      return out === code ? null : { code: out, map: null }
    },
    // index.html: Slidev's <link rel="preload" as="image"> of every figure
    transformIndexHtml: { order: 'post', handler: withHashes },
  }
  function withHashes(code: string) {
    return code.replace(FIGURE_URL, (url, name: string) => {
      const h = hashOf(name)
      return h ? `${url}?v=${h}` : url
    })
  }
}

export default defineConfig({
  plugins: [figureHash()],
  build: {
    rollupOptions: {
      output: {
        manualChunks(id: string) {
          if (id.startsWith('~icons/'))
            return 'modules/unplugin-icons'
          const dep = OWN_CHUNK.find(name => id.includes(`/node_modules/${name}`))
          if (dep)
            return `modules/${dep.replace('@', '').replace('/', '-')}`
          // everything else, Shiki and the Monaco types included: the bundler decides
          return undefined
        },
      },
    },
  },
})
