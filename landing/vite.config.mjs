import { defineConfig } from 'vite';
import { fileURLToPath } from 'node:url';
import { dirname, resolve } from 'node:path';

const here = dirname(fileURLToPath(import.meta.url));

// Builds the landing enhancement bundle to FIXED filenames (no hashes) so
// gen-landing.mjs can reference them statically. base './' keeps every URL
// relative → works under any GitHub Pages --base prefix.
export default defineConfig({
  root: here,
  base: './',
  build: {
    outDir: resolve(here, 'dist-assets'),
    emptyOutDir: true,
    target: 'es2019',
    rollupOptions: {
      input: { landing: resolve(here, 'src/main.js') },
      output: {
        entryFileNames: 'assets/[name].js',
        chunkFileNames: 'assets/[name].js',
        assetFileNames: 'assets/[name][extname]',
      },
    },
  },
});
