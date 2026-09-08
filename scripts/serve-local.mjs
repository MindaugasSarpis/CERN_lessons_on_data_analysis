// Lecture-day static server for a `--keep-videos` build: serves `dist/` with
// HTTP Range support (Chrome/Safari need 206 responses to play mp4 without
// downloading the whole file first — python's http.server ignores Range).
// Usage: node scripts/serve-local.mjs [port]   (default 8123)
import { createServer } from 'node:http';
import { createRequire } from 'node:module';
import { resolve } from 'node:path';
const require = createRequire(import.meta.url);
// sirv is a transitive dep (Vite/Slidev), not a direct one — resolve it from the store.
const sirv = require(resolve(import.meta.dirname, '..', 'node_modules/.pnpm/sirv@3.0.2/node_modules/sirv'));
const port = Number(process.argv[2] || 8123);
const dir = resolve(import.meta.dirname, '..', 'dist');
const handler = sirv(dir, { dev: true, etag: true });
createServer(handler).listen(port, () => console.log(`serving ${dir} on http://localhost:${port}/`));
