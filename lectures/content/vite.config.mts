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
import { defineConfig } from 'vite'

const OWN_CHUNK = ['file-saver', 'vue', '@vue']

export default defineConfig({
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
