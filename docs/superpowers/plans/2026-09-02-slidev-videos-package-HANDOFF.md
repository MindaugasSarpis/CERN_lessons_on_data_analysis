# HANDOFF — slidev-videos package (D2), 2026-09-02 ~02:00 EEST

State at handoff (WSL session hit the account rate limit; maintainer continues on the Mac).

## Where things stand

- github.com/MindaugasSarpis/slidev-videos `main` @ `fd0f1fd` (pushed): Tasks 1–3 of
  `docs/superpowers/plans/2026-09-02-slidev-videos-package.md` are implemented.
  - Task 1 (config layer): reviewed clean (byte-identical to the plan).
  - Task 2 (pipeline lift + patch): reviewed clean — the reviewer regenerated
    `pipeline.py` from outreach `20196d3` + the plan's patch script and got an
    empty diff. 31 tests pass (`python3 -m pytest tests -q`).
  - Task 3 (addon component + example deck): implemented and builds
    (`pnpm install && pnpm build:example` → `example/dist/`); its REVIEW DIED
    MID-FLIGHT on the rate limit — **re-run it or spot-check by diffing
    `components/VideoPlayer.vue`, `package.json`, `example/*` against the
    Task 3 heredocs in the plan** before trusting it.
- NOT DONE: Task 4 (Playwright smoke `scripts/smoke-example.mjs` — note the
  corrected path: it must serve `example/dist`, Slidev resolves `--out`
  against the entry dir), Task 5 (CI workflow + real README — the pushed
  README still says "scaffold only"), Task 6 (final gates, tag `v0.1.0`,
  push tag). **No tag exists yet — do not `pip install @v0.1.0` until Task 6.**

## How to resume (any machine with both repos)

    # regenerate a task brief (N = 4, 5, 6):
    ~/.claude/plugins/cache/claude-plugins-official/superpowers/*/skills/subagent-driven-development/scripts/task-brief \
      docs/superpowers/plans/2026-09-02-slidev-videos-package.md N

Execute per superpowers:subagent-driven-development, implementation commits to
`~/slidev-videos` on `main`.

## Rulings made during execution (undo any you disagree with)

1. `trim` implemented as input-side `-ss` + output-side `-t end-start`
   (spec §4.3 said `-to`; input seeking resets timestamps, `-t` is correct).
2. Shared release may live on another repo → `repo` threaded through
   `_pull_tier`/`_remote_assets`/`_remote_asset_sizes` and the
   `--include-shared`/`preflight` call sites; `shared-check` reads the
   bundled registry (its cross-talk scan is vacuous outside a monorepo).
3. Example reaches the component via `example/components → ../components`
   symlink; verifying the real `addons:` npm resolution is deferred to the
   course-migration plan (D4).
4. Smoke serves `example/dist` (plan corrected in commit `18ed8d2`).
5. ffmpeg testsrc encode smoke deferred to D3; CHANGELOG deferred; licence set
   to MIT in pyproject (repo has no LICENSE file yet — add one or change both).

## After D2: what only the Mac can do (D3, spec §5)

The shared-library encode needs rclone + the gdrive raws
(`gdrive:CERN_videos/raw`, `gdrive:work/outreach/resources/videos/released`)
— present on the Mac, absent on WSL. D3 = fill `src/slidev_videos/shared.toml`
with the 33 entries (spec §5.3 table), encode 1080p H.264 via the freshly
lifted CLI, publish to this repo's `videos-shared` release. Then D4 (course
migration + reel pass 2) per spec §7/§8.1.1.

Course-side status is unchanged from the deployed state: L01/L02 re-split live,
`pnpm release 2` before sharing the Moodle link.
