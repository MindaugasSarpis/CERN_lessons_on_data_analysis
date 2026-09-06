#!/usr/bin/env node
/**
 * changed-decks.mjs — which decks does a change set touch? Powers
 * `pnpm qa --changed-since <ref>` (scripts/qa-all.mjs) so a slides-only push
 * QAs only the decks it edited instead of all 16.
 *
 *   node scripts/changed-decks.mjs <ref>     print the decision (no build)
 *
 * Rules (selectDecks):
 *   - lectures/content/slides/X.md  → every deck listing X in `srcs` (a slide
 *     file no deck lists — the LX template, the combined entry — touches nothing)
 *   - paths that never reach a rendered deck are ignored: docs/, the workbook,
 *     videos/, misc/, figures/src/ (outputs live in public/figures and DO count),
 *     the non-build scripts (videos.py, timing-report, release), editor/agent
 *     config, root-level markdown
 *   - anything else — theme, components, setup, public/, layouts, the build/QA
 *     scripts, landing/, decks.json, package.json, the lockfile, workflows —
 *     widens to every deck. So does a ref git cannot resolve.
 *
 * changedPaths(ref) diffs the WORKING TREE against the merge-base of <ref> and
 * HEAD (committed + uncommitted + untracked), so it is the same answer locally
 * before a push and in CI after checkout.
 */
import { spawnSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { join, dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const IGNORE = [
  /^docs\//, /^lectures\/workbook\//, /^videos\//, /^misc\//, /^figures\/src\//,
  /^scripts\/(videos\.py|timing-report\.mjs|release\.mjs)$/,
  /^\.agents\//, /^\.claude\//, /^\.vscode\//, /^\.gitignore$/, /^LICENSE/,
  /^[^/]+\.md$/,
];
const SLIDE = /^lectures\/content\/slides\/([^/]+)$/;

/** @returns {{ all: boolean, slugs: string[], reason: string }} */
export function selectDecks(changed, decks) {
  const hit = new Set();
  const widen = [];
  for (const p of changed) {
    if (IGNORE.some((re) => re.test(p))) continue;
    const m = p.match(SLIDE);
    if (m) {
      for (const d of decks) if (d.srcs.includes(m[1])) hit.add(d.slug);
      continue;
    }
    widen.push(p);
  }
  if (widen.length) {
    const shown = widen.slice(0, 4).join(', ') + (widen.length > 4 ? ` (+${widen.length - 4} more)` : '');
    return { all: true, slugs: decks.map((d) => d.slug), reason: `shared file(s) changed: ${shown}` };
  }
  const slugs = decks.map((d) => d.slug).filter((s) => hit.has(s)); // manifest order
  return {
    all: false,
    slugs,
    reason: slugs.length ? `slide sources changed for: ${slugs.join(', ')}` : 'no deck-affecting change',
  };
}

/** Paths changed in the working tree vs merge-base(ref, HEAD); null if ref is unknown. */
export function changedPaths(ref, cwd) {
  const git = (...args) => spawnSync('git', args, { cwd, encoding: 'utf8' });
  const mb = git('merge-base', ref, 'HEAD');
  if (mb.status !== 0) return null;
  const base = mb.stdout.trim();
  const diff = git('diff', '--name-only', base);
  if (diff.status !== 0) return null;
  const untracked = git('ls-files', '--others', '--exclude-standard');
  const lines = (s) => (s || '').split('\n').map((l) => l.trim()).filter(Boolean);
  return [...new Set([...lines(diff.stdout), ...lines(untracked.stdout)])];
}

/** One-call helper for qa-all.mjs: the decision for <ref> against the manifest. */
export function decideFor(ref, root) {
  const manifest = JSON.parse(readFileSync(join(root, 'lectures', 'content', 'decks.json'), 'utf8'));
  const changed = changedPaths(ref, root);
  if (changed === null) {
    return { all: true, slugs: manifest.decks.map((d) => d.slug), reason: `cannot resolve ${ref} in this checkout` };
  }
  return selectDecks(changed, manifest.decks);
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const ref = process.argv[2];
  if (!ref) { console.error('usage: node scripts/changed-decks.mjs <ref>'); process.exit(2); }
  const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
  const pick = decideFor(ref, root);
  console.log(`${pick.all ? 'every deck' : `${pick.slugs.length} deck(s)`} — ${pick.reason}`);
  for (const s of pick.slugs) console.log(`  ${s}`);
}
