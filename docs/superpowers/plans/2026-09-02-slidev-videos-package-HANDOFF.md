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

---

# Update 2026-09-03 (Mac) — D2 closed, D3 done

## State

- **D2 closed**: Tasks 4–6 landed on `main` (`41d6333` smoke, `c07d08f` CI + README +
  LICENSE) and `v0.1.0` is tagged. The Task 3 review that died on WSL was not re-run;
  the smoke test exercises the built example instead.
- **D3 done** (spec §5): `src/slidev_videos/shared.toml` holds the **34-clip** library
  (the spec's "33" was a miscount — one table row lists three clips). All 34 raws are in
  `~/slidev-videos/videos/raw/` (32 rclone'd from Drive, `hubble.mp4` + `stars_pan_audio.mp4`
  from the course's HEVC release — no Drive original), encoded to `public/videos/` and
  uploaded to release **`videos-shared`** on `MindaugasSarpis/slidev-videos` (34 assets,
  `shared-check` clean). The package repo is now itself a slidev-videos project
  (`videos.toml` with `shared = false`, `encoder = "cpu"`).
- Commits on `~/slidev-videos` `main`, **not yet pushed** (maintainer pushes):
  `919579e` D3 registry + manifest + test, `c398719` loudness-trim fix (below).
- Gate results: ffprobe sweep — every asset H.264 (VP8 for the one `remux` webm), long
  edge ≤ 1920, bitrate ≤ 8.3 Mbps; R128 sweep — every clip with real audio within
  −16.2…−15.5 LUFS after the fix. `preflight` is slide-driven, so in the package repo
  it only sees the README/example placeholders — the sweep was done by hand (see
  `_measure_loudness` for the equivalent ffmpeg call).

## Rulings made on the Mac (undo any you disagree with)

6. **Loudness of trimmed clips**: the two-pass loudnorm measured the whole raw while the
   encode trimmed it. `perseverance_rover_landing_nasa.mp4` (1:40–3:10 cut) came out at
   −18.7 LUFS because the whole clip's LRA (19.7) made loudnorm silently fall back to
   dynamic mode, although the 90 s segment (LRA 8.6) qualifies for linear.
   `_measure_loudness` now takes the encode's `_trim_args`; the six trimmed clips were
   re-encoded (all −16.2…−15.9 LUFS) and re-published. Tests pin the seek placement.
7. **Not changed, worth knowing**: (a) outreach's recipe passes `offset=target_offset`
   into pass 2; in linear mode loudnorm overrides it, in dynamic mode (clip's own TP/LRA
   forbids linear) it acts as extra gain — the three clips that still go dynamic
   (`cassini`, `cern_footage_2022_013_001/006`) land within 0.2 LU anyway, so left alone.
   (b) Seven encodes carry a `tmcd` timecode data track inherited from the `.mov` masters
   (ffmpeg's default mapping copies it into mp4). Browsers ignore it; `preflight` does
   not flag it. Add `-dn` to the profile args if it ever matters.
8. The package is **not pip-installed** in any conda env on the Mac; the CLI ran as
   `PYTHONPATH=src python -c 'from slidev_videos.cli import main; main()' <cmd>` with
   `~/miniconda3/envs/outreach_talks/bin` (gh, ffmpeg, rclone) on PATH. `python -m
   slidev_videos` does not work (no `__main__.py`). pytest was installed into the session
   scratchpad only, not into an env.

## Next: D4 (course migration + reel pass 2, spec §7 / §8.1.1) — after the 7 Sept lecture

Not started. When starting: write the D4 plan from spec §7 first (per the roadmap's
spec→plan→build rule), keep the course's HEVC release `videos` under
`archive_release_tags` until the migrated decks are verified live, and re-check the
`addons:` npm resolution deferred in ruling 3.
