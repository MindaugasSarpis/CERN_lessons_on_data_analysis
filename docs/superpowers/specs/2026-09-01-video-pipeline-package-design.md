# Video pipeline as a reusable package (`slidev-videos`) + course migration + L01/L02 re-split — design

**Date:** 2026-09-01 · **Status:** approved in discussion, awaiting spec review · **Supersedes:** `docs/superpowers/plans/2026-07-01-ff2026-workstream-b-video-pipeline-port.md` (0/36 steps done, written before outreach's 2026-07-17/18 pipeline changes).

## 1. Summary

The lecture videos are the strongest hook of the course — the maintainer's feedback is that students were "captivated from the very first lecture" by the CERN reel. Today the course repo runs a February-2026 first-generation pipeline (`scripts/videos.py`, 467 lines: `sync fetch encode publish check`, one HEVC web tier, one hard-coded GitHub Release, a two-step player fallback), while the sibling repo `/home/mindaugas_wsl/outreach_talks` has evolved a much more complete pipeline (12 subcommands, H.264 web tier with EBU R128 loudness normalisation, `pull`/`preflight`/`clean`, a shared-clip registry, a four-step player fallback chain with look-ahead preload). Both repos — and at least one more course ("World of Particles") — need the same thing.

This design:

1. extracts the pipeline into a **standalone package repo `MindaugasSarpis/slidev-videos`** — a Python CLI + a Slidev addon holding the player + the canonical **shared clip library** (registry + GitHub Release of 1080p H.264 encodes);
2. **migrates this course** onto it (removing the local `videos.py` and `VideoPlayer.vue`, re-encoding every clip to H.264, publishing to new release tags);
3. **re-splits lectures 01/02**: L01 = orientation → motivation reel (all 24 clips), L02 = introduction to data (the current "Data in Your Life" material plus ~30 min of new intro-to-data content).

Sequencing (each stage independently shippable): **§8 re-split first** (uses today's pipeline; the reel already streams from the existing release) → package v0.1.0 (§3–§6, §9) → shared library encode + publish (§5) → course migration (§7).

### Goals
- One pipeline and one player, versioned, installable into any Slidev course/talk repo in two lines.
- Browser-safe playback everywhere: **1080p H.264 web tier only** (outreach's 2026-07-18 policy after HEVC/4K freezes at the Yaga venue). Nothing in this course's release was ever truly 4K (the two `…-2160p` files carry 1080p streams); the lag was HEVC decode, so the fix is a re-encode, not a downscale.
- Shared CERN/space clips encoded **once**, served from **one** release, reused by every deck.
- Keep the course's two hard-won player behaviours: `object-fit: cover` (full-bleed, no letterbox) and "prefer the remote in production" (deploy strips local `videos/`, so probing it first only buys a 404).
- L01 opens the semester with the reel; L02 becomes a proper introduction to data; both decks stay inside the 105–145 min timing band.

### Non-goals
- Migrating `outreach_talks` onto the package (its own task in that repo; the package keeps full feature parity so that migration is a config swap).
- Setting up the World of Particles repo (covered by the package README recipe).
- Changing the HQ/HEVC venue tier beyond keeping it opt-in.
- CDN/LFS/cloud buckets. GitHub Releases remain the host (public repos, 2 GB/asset cap).

## 2. Deliverables

| # | Deliverable | Where |
|---|---|---|
| D1 | L01/L02 re-split + new L02 content + bookkeeping | this repo |
| D2 | Package repo `slidev-videos` v0.1.0: CLI, addon, tests, example deck, README | new repo |
| D3 | Shared clip library: `shared.toml` + release `videos-shared` (25 clips, H.264 1080p) | package repo |
| D4 | Course migration: consume D2/D3, re-encode course-specific clips → release `videos-web`, docs | this repo |

## 3. Package repo layout — `MindaugasSarpis/slidev-videos`

```
slidev-videos/
  pyproject.toml              # name "slidev-videos", requires-python >=3.11, no runtime deps
                              # [project.scripts] slidev-videos = "slidev_videos.cli:main"
  src/slidev_videos/
    __init__.py               # __version__
    cli.py                    # argparse: all subcommands (moved from outreach videos.py)
    config.py                 # NEW: project discovery, videos.toml, 3-layer merge, path resolution
    pipeline.py               # moved: encoder probing, profiles, loudnorm, encode/publish/pull/
                              #        check/preflight/clean/venue/build implementations
    fetch.py                  # moved from the course: yt-dlp fetch → raw + manifest entry
    shared.toml               # the shared clip registry (package data, read via importlib.resources)
  package.json                # name "slidev-addon-videos", "files": ["components", "README.md"]
  components/VideoPlayer.vue  # the player (§6)
  example/                    # minimal Slidev deck using the addon; built in CI
    slides.md  package.json
  tests/                      # pytest (§9)
  videos.toml                 # the package repo is itself a project: [project] manifest = "src/slidev_videos/shared.toml",
                              # [defaults] release_tag = "videos-shared", source_remote = gdrive path of the shared raws
  videos/raw/, videos/hq/     # gitignored — raws for the shared library live on gdrive
  public/videos/              # gitignored — encoded shared clips before publish
  .github/workflows/ci.yml    # pytest + `slidev build example/slides.md`
  README.md  CHANGELOG.md  LICENSE
```

Versioning: git tags `vX.Y.Z`; `pyproject.toml` and `package.json` carry the same version. Consumers install by tag:

```bash
pip install "slidev-videos @ git+https://github.com/MindaugasSarpis/slidev-videos@v0.1.0"   # CLI
pnpm add -D github:MindaugasSarpis/slidev-videos#v0.1.0                                     # addon
```

Lift-and-shift rule: `pipeline.py` is outreach's `scripts/videos.py` (2026-07-18, `20196d3`) with the module-level path constants and `outreach.toml` lookup replaced by `config.py` calls. No encode/publish/loudnorm behaviour changes. Two known outreach defects are fixed in the move: `build --sync` crashes because the `build` subparser lacks `--quick` (add it); `videos:build` was documented but never wired (the README documents `slidev-videos build`). The unused `used_in` manifest field stays (documentation value) but is now *read* by `check` to report label drift against the slide scan.

## 4. CLI configuration model

### 4.1 Project discovery
`slidev-videos` walks up from cwd (or `--project <dir>`) to the first directory containing **`videos.toml`**; that directory is the *project root*. A monorepo (outreach layout) has a root `videos.toml` with only `[defaults]`, and each talk directory has its own `videos.toml` (possibly empty) so that running from inside a talk selects the talk as the project and the parent supplies global defaults. Concretely: the nearest `videos.toml` is the project; every `videos.toml` further up contributes `[defaults]` at lower precedence.

### 4.2 `videos.toml`

```toml
[project]                      # all optional; defaults reproduce outreach's talk layout
slides_dir = "."               # scanned recursively for *.md (skips node_modules, dist*, .git, .qa-dist)
public_dir = "public"          # web tier lands in <public_dir>/videos/, HQ symlink at <public_dir>/videos-hq
raw_dir    = "videos/raw"
hq_dir     = "videos/hq"
manifest   = "videos/manifest.toml"

[defaults]                     # same keys and meaning as outreach's [defaults]
repo             = "MindaugasSarpis/CERN_lessons_on_data_analysis"   # default: parsed from `git remote get-url origin`
release_tag      = "videos-web"          # default: "videos-<project dirname, lowercased, _→->"
release_tag_hq   = "videos-hq"           # default: "videos-hq-<dirname>"
shared           = "MindaugasSarpis/slidev-videos@videos-shared"     # default; `false` disables the shared chain
source_remote    = "gdrive:CERN_videos/raw"
web_long_edge_px = 1920
long_edge_px     = 1920
max_size_mb      = 200
encoder          = "cpu"                 # cpu | nvenc | videotoolbox (unset = auto: nvenc if usable, else cpu)
loudnorm         = true
preflight_max_mbps = 10.0
```

This course's `videos.toml` sets `slides_dir = "lectures/content/slides"`, `public_dir = "lectures/content/public"`, `release_tag = "videos-web"`. An outreach talk needs no `[project]` block.

Merge order (highest first): per-video `[[videos]]` keys → manifest `[defaults]` → project `videos.toml` `[defaults]` → ancestor `videos.toml` `[defaults]` → built-in defaults. `max_size_mb` remains a warning (as in outreach); the course manifest's comment claiming it "fails" is corrected.

### 4.3 Manifest
Unchanged from outreach (`name`, `profile`, `used_in`, `notes`, `long_edge_px`, `hq_crf`, `hq_from_raw`, `encoder`, `loudnorm`); the course manifest is already schema-compatible. Profiles (web tier, H.264 libx264 / h264_nvenc): `remux`, `standard` (CRF 23, ≤6 Mbps, AAC 128k), `standard-tight` (CRF 26, ≤3.5 Mbps), `silent-loop` (CRF 24, ≤5 Mbps, audio stripped), `high-motion` (CRF 22, ≤8 Mbps, AAC 192k); all `scale=min(web_long_edge_px,iw):-2`, `+faststart`, two-pass loudnorm −16 LUFS on audio-bearing encodes. `remux` is only valid when `preflight` would pass on the raw (H.264/VP8/VP9 + browser-safe audio); `encode` refuses to remux HEVC/PCM sources and says why.

### 4.4 Subcommands
`sync`, `fetch`, `encode`, `encode-hq`, `publish`, `publish-hq`, `pull`, `pull-hq`, `check`, `shared-check`, `clean`, `preflight`, `venue`, `build` — semantics as in outreach (plus the course's `fetch`). `shared-check` runs in the package repo (which is a project whose manifest *is* `shared.toml`). New flag on every command: `--project <dir>`.

### 4.5 Shared library awareness in consumers
The bundled `shared.toml` tells the CLI which names are shared. In a consumer project: `check` reports inherited clips (referenced by slides, absent from the local manifest, present in the registry) and flags references that are in neither; `pull --include-shared` fetches them from the shared release; `clean`/`publish --prune` never touch shared names; `preflight` resolves the same chain the player uses (local HQ → local web → own release → shared release) and ffprobes the winner.

## 5. Shared clip library

### 5.1 Policy
A clip is *shared* when it is generic CERN/LHC/experiment footage, space/astronomy B-roll, or a CGI science sim usable by more than one deck. Course/talk-specific material (venue clips, chart renders, lecture explainers) stays in the consumer's own manifest and release.

### 5.2 Naming
One convention: **lowercase snake_case, no resolution or codec suffixes** (`cern_footage_2023_019_001.mp4`, not `CERN-FOOTAGE-2023-019-001-2160p.mp4`). CERN CDS IDs keep their digits so the source record is recoverable. Existing outreach names that already conform are kept verbatim (`expansion_funnel_h264_1080p.webm` stays, to avoid churn there).

### 5.3 Initial contents (25 clips) and sources

| shared name | from (course release `videos` unless noted) | profile |
|---|---|---|
| skylapse.mp4 | Skylapse.mp4 | silent-loop |
| drone_climbing_mountain.mp4 | Drone_Climbing_Mountain.mp4 | high-motion |
| nasa_mars_mariner_4_pan_audio.mp4 | NASA_Mars_Mariner_4_Pan_Audio.mp4 | standard |
| perseverance_rover_landing_nasa.mp4 | Perseverance_Rover_Landing_NASA.mp4 (spelling fixed; outreach's `perseverence_…` maps here) | high-motion |
| cassini_grand_finale.mp4 | Cassini_Grand_Finale_NO_VO.mp4 | standard |
| stars_pan_audio.mp4 | Stars_Pan_Audio.mp4 | standard |
| telescope.mp4 | Telescope.mp4 | standard |
| hubble.mp4 | Hubble.mp4 | standard |
| webb_reel.mp4 | Webb_Reel.mp4 | standard-tight (3 min) |
| milky_way_sim_audio.mp4 | Milky_Way_Sim_Audio.mp4 | high-motion |
| expansion_funnel_h264_1080p.webm | Expansion_Funnel_H264_1080p.webm | remux (VP8) |
| qgp_formation.mp4 | QGP_Formation.mp4 | high-motion |
| voyage_in_to_the_world_of_atoms.mp4 | Voyage_in_to_the_world_of_atoms.mp4 | standard |
| cloud_chamber_audio.mp4 | Cloud_Chamber_Audio.mp4 | standard-tight (2:29) |
| cern_overview_short.mp4 | CERN_Overview_Short.mp4 | standard |
| atlas_video_2021_001_001.mp4 | ATLAS-VIDEO-2021-001-001-1080p.mp4 | standard |
| atlas_footage_2022_004_002_shaft.mp4 | ATLAS-FOOTAGE-2022-004-002-1080p_Shaft.mp4 | standard |
| lhcb.mp4 | LHCb.mp4 | standard |
| cern_footage_2023_019_001.mp4 | CERN-FOOTAGE-2023-019-001-2160p.mp4 (1080p stream) | standard |
| cern_video_2020_064_001.mp4 | CERN-VIDEO-2020-064-001-2160p.mp4 (already H.264 1080p) | remux |
| cern_footage_2024_006_001.mp4 | CERN-FOOTAGE-2024-006-001.mp4 | standard |
| cern_footage_2024_010_002.mp4 | CERN-FOOTAGE-2024-010-002.mp4 | standard |
| cern_footage_2022_013_001_1080p_lhc.mp4 | outreach release `videos-2026-07-18-yaga` (LHC tunnel B-roll, H.264 4.1 Mbps) | standard-tight (185 MB → budget) |
| cern_video_2019_050_008.mp4 | outreach `videos-shared` `cern_video_2019_050_008_1080ph265.mp4` (HEVC) | standard |
| cern_footage_2025_014_002.mp4 | outreach release `videos-2026-05-11-sceptics` | standard |

Source preference for the one-time encode: (1) the raw on gdrive (`gdrive:CERN_videos/raw` for course clips; `gdrive:work/outreach/resources/videos/released` for outreach clips) when rclone is available — this machine has none, the maintainer's Mac does; (2) otherwise the released file as the "raw" (`gh release download … --dir videos/raw`), documented in the package README as the fallback with its small generational-loss cost. Every result must pass `preflight` (H.264, ≤1920 long edge, ≤10 Mbps, browser-safe audio, loudness within ±2 LU of −16 LUFS) before publish.

Course-specific clips (stay in this course, release `videos-web`, same renaming rule): `gtc_2020.mp4`, `technology_size_comparison.mp4`, `vu_vm.mp4`, `cpu_vs_gpu_demo.mp4`, `how_computer_memory_works.mp4` (`standard-tight`; will still exceed `max_size_mb` — accepted, warning only). Dropped: the orphan `VU_VM_Zoom.*` and the misspelt duplicate `Perseverence_…` release asset.

### 5.4 Release layout
- Package repo: release **`videos-shared`** (web tier only; no shared HQ release, as in outreach). Old assets are never deleted by `publish --prune` from a consumer.
- This course: release **`videos-web`** for course-specific clips. The existing HEVC release `videos` is listed under `archive_release_tags` (prune-protected) until D4 is verified live, then deleted by hand.

## 6. The player — `components/VideoPlayer.vue` (addon)

Base: outreach's component (`components/VideoPlayer.vue`, 363 lines). Merged course behaviours and changes:

- **Props:** `src` (required, bare filename), `fallback` (explicit URL override), `loop`, `muted`, `controls` (default `true`), `hq` (default `true`), `volume` (0..1), **`fit`** (`cover` | `contain`; default from config, config default `cover`). The `autoplay` prop is removed — it was inert in both repos; playback is slide-driven (`useIsSlideActive`): rewind + play on activation, pause + rewind on deactivation, muted-first then unmute unless `muted`.
- **Chain** (front-to-back), deduped: in `pnpm dev`: `<base>videos-hq/<src>` (if `hq`) → `<base>videos/<src>` → own release → shared release. In production builds the two remote entries come **first** (course rule: deploy strips local copies; a local 404 only delays playback), local entries last (for `--keep-videos`/portable builds). `<source>` `error` advances the chain; chain exhaustion shows "Video not available: `<src>`".
- **Look-ahead preload:** 3 slides ahead, `<link rel="preload" as="video">` in prod pointing at the *most reliable* entry (the shared release for shared names, else own release), early `<source>` attach in dev. `preload="none"` until warmed/active.
- **Config source:** the deck headmatter block

  ```yaml
  videos:
    repo: MindaugasSarpis/CERN_lessons_on_data_analysis
    release: videos-web
    shared: MindaugasSarpis/slidev-videos@videos-shared   # or false
    fit: cover
    hq: true
  ```

  read via `configs` from `@slidev/client` (`configs.videos`). Fallback, in this order: `VITE_VIDEO_REPO` / `VITE_VIDEO_RELEASE` / `VITE_VIDEO_SHARED_RELEASE` (outreach's `.env` files keep working; `VITE_VIDEO_SHARED_REPO` added), then built-ins (`shared` = the package release, `fit` = `cover`). Implementation step 1 verifies that a custom headmatter key survives into `configs`; if it does not, env becomes the primary mechanism and the headmatter block is dropped from this spec's consumer recipe.
- **Course-repo gotcha preserved:** the generated deck entries put `src:` in the headmatter, which makes every headmatter key a per-slide frontmatter override; a `videos:` map is harmless there (no slide uses that key) — documented next to the existing `background` note in `gen-entries.mjs`.
- Styling: `position:absolute; inset:0; background:black`; `object-fit` from `fit`; opacity 0 until ready; hover control bar as in outreach.
- `check` keeps the regex `VideoPlayer\s+src="([^"]+)"`, so `src` stays a double-quoted bare filename.

## 7. Course migration (D4)

| Change | Detail |
|---|---|
| Remove | `scripts/videos.py`, `lectures/content/components/VideoPlayer.vue`, stale `.gitignore` line `videos/web/` |
| Add | `videos.toml` (§4.2 values); `.gitignore` entries `videos/hq/`, `lectures/content/public/videos-hq` |
| `package.json` | devDependency `slidev-addon-videos` (git tag); scripts `videos:*` → `slidev-videos <cmd>` (`sync fetch encode publish pull check preflight clean`) |
| `env.yaml` | add `ffmpeg`, `yt-dlp`, `gh`, `rclone` (conda-forge) and a `pip:` entry for the CLI git tag |
| `scripts/gen-entries.mjs` | add `slidev-addon-videos` under `addons:` and the `videos:` block (§6) to every generated entry |
| `videos/manifest.toml` | only course-specific clips remain (§5.3), renamed, H.264 profiles, `used_in` = current lecture numbers |
| Slides | `src="…"` renamed to the new lowercase names (mechanical sed over `lectures/content/slides/*.md`); `autoplay` attributes removed |
| Unchanged | `build-all.mjs` video strip + `--keep-videos`; `check-slides.mjs` media abort; `timing-report.mjs` +1.5 min per `<VideoPlayer>` |
| Docs | CLAUDE.md commands + gotchas, README "Videos" section (install, day-to-day commands, adding a clip, the shared library), mark the 2026-07-01 port plan superseded |

Gates before pushing `ff2026:bs2026`: `pnpm qa` (zero overflow) · `pnpm timing:check` · `slidev-videos check` (no UNKNOWN REF / UNUSED / drift) · `slidev-videos preflight` against the deployed chain (all H.264, ≤1920, ≤10 Mbps, loudness in band) · manual playback of L01's reel from a `pnpm build` served locally **and** from the Pages deploy in Chrome and Firefox.

## 8. L01/L02 re-split (D1)

Measured with the `timing-report.mjs` model (replica agrees to ±1 min with `pnpm timing`):

| block (current file) | min | slides | vids |
|---|---|---|---|
| L01 opening + admin (cover … Learning Outcomes) | 39.6 | 20 | – |
| L01 How This Course Works | 17.6 | 8 | – |
| L01 Data in Your Life | 34.2 | 16 | – |
| L01 Seminars & Your Project | 16.9 | 8 | – |
| L02 opening + Learning Objectives | 3.0 | 3 | – |
| L02 What is CERN / Four Eyes on the Ring | 9.0 / 8.8 | 5 / 5 | – |
| L02 Why Data / Beyond the Ring | 18.4 / 8.0 | 7 / 4 | – |
| L02 reel "From the Cosmos to the Quantum" (incl. Half-time) | 31.0 | 17 | 15 |
| L02 reel "Inside CERN" | 18.5 | 10 | 9 |
| L02 From Films to Skills (Careers, A Day in the Data, Why You Need These Skills, Recap) | 8.9 | 5 | – |

### 8.1 L01 — "Orientation & Motivation" (target ≈ 133 min)
Order: cover · Who am I talking to · quote · Course Structure … Learning Outcomes (as today) · How This Course Works (as today) · Seminars & Your Project (as today) · `# Breaks…` · section **What is CERN?** with its four context slides (CERN at a Glance, LHC, Accelerator Chain, How a Detector Sees a Collision) · section **From the Cosmos to the Quantum** (15 clips, Half-time intact) · section **Inside CERN** (9 clips) · closing slide **Why You Need These Skills** (moved from L02) · the existing "What You Need / Today's Task" slide stays last. Estimate: 74.1 + 0.5 + 9.0 + 31.0 + 18.5 + ~2 ≈ 135.

### 8.2 L02 — "Introduction to Data" (target ≈ 110 min)
Order: cover (retitled) · quote · Learning Objectives (rewritten for data) · section **Data in Your Life** (16 slides, moved verbatim from L01) · section **Four Eyes on the Ring** incl. *Meet the Particle You'll Analyse* · section **Why Data?** (Why Data Analysis Matters, From Collision to Dataset, From Events to Petabytes, Why It Has to Be Real-Time) · **new** section **Open Data & Provenance** (~4 slides, ~10 min: open-data portals — CERN Open Data, NASA, Eurostat, Zenodo; records, DOIs and licences; what a README/provenance note must say; the seminar-2 dataset record 401 as the worked example) · **new** section **A Dataset Up Close** (~3 slides + 1 MCQ, ~10 min: the D⁰ → K⁻π⁺ file — rows are events, columns are measurements, units, measurement vs metadata, a first look at the invariant-mass column) · section **Beyond the Ring** (CERN's Impact, A Planet-Sized Computer, Open Data Up Close) · **new** MCQ on data lifecycle/provenance · Careers at CERN · A Day in the Data · Recap (rewritten). Estimate: 3 + 34.2 + 8.8 + 18.4 + 10 + 10 + 8.0 + 3 + ~7 ≈ 102–110 — the two new sections are sized so the gate reports ≥ 108; if the first `pnpm timing` lands under, the new sections grow (never the reel returns).

### 8.3 Bookkeeping
- `lectures/content/decks.json`: `01-orientation` title → "Orientation & Motivation"; `02-cern` → slug `02-intro-to-data`, title "Introduction to Data" (URL change accepted; the landing regenerates from the manifest; old `/02-cern/` links 404).
- Files: `02_Introduction_to_CERN.md` → `02_Introduction_to_Data.md` (and the combined authoring entry's `src:` line).
- Workbook: `mkdocs.yml` nav + `docs/index.md` titles; `docs/lectures/lecture_2.md` (currently an empty stub) gets a page mirroring the new L02 sections; `docs/lectures/lecture_1.md` title updated; `seminar_01.md` / `seminar_02.md` "Paired lecture" lines.
- `videos/manifest.toml` `used_in` → `["L01"]` for the 24 reel clips (this stage keeps the old names; §7 renames).
- Presenter notes on the two reel section slides stay; the L01 `Breaks…` slide precedes the reel so the reel doubles as the lights-down break.
- Gates: `pnpm qa --only 01-orientation,02-intro-to-data`, `pnpm timing:check`, `python3 scripts/videos.py check`, landing smoke test via `pnpm qa`.

## 9. Testing

**Package (pytest, CI on every push):** `config.py` — discovery from nested dirs, `--project`, 3-layer merge precedence, `repo` from git remote, auto tags; manifest parsing incl. bad profile / missing name; profile → ffmpeg argument building for cpu/nvenc/videotoolbox and the `remux` refusal on HEVC/PCM (uses a fake `ffprobe` result); the ported `clean` planner tests (outreach `scripts/tests/test_clean_plan.py`); `fetch` name/extension handling with a stubbed `yt-dlp`; `check` slide scan (fixture project with two decks and one shared reference); an end-to-end `encode` of a 2-second `testsrc2` clip through every profile, skipped when `ffmpeg` is absent. **Addon:** CI runs `slidev build example/slides.md`; a Playwright smoke (same approach as `scripts/check-slides.mjs`) asserts the component renders, builds the expected chain for prod vs dev, and shows the error text on chain exhaustion.

**This repo:** `pnpm qa`, `pnpm timing:check`, `slidev-videos check`, `slidev-videos preflight`, the manual playback check in §7.

## 10. Error handling

- Missing binary (`ffmpeg`, `ffprobe`, `yt-dlp`, `gh`, `rclone`): one-line error naming the binary and the `env.yaml`/brew hint; exit 2.
- No `videos.toml` found: error with the searched path and a `slidev-videos init` hint (`init` writes a commented `videos.toml` + empty manifest).
- Release missing: created automatically on `publish` (existing behaviour); `pull` from a missing release lists what exists.
- Encode failure: `.partial` file removed, ffmpeg stderr tail printed, other clips continue; exit 1 at the end.
- Unavailable encoder: degrade to `cpu` with a warning (existing behaviour).
- Player: chain exhaustion → visible red "Video not available"; misconfigured `videos:` block (no repo) → console warning and the built-in shared release still tried.

## 11. Decisions log

| Decision | Choice | Why |
|---|---|---|
| CLI language | keep Python; addon is npm | zero-rewrite reuse of the freshly debugged outreach pipeline; the maintainer's courses already ship a conda env |
| Shared clips home | package repo (`videos-shared` release) | one canonical H.264 set; World of Particles and outreach reuse it without re-uploading |
| L02 gap after the move | write ~30 min of new intro-to-data content | keeps the timing gate honest; the reel goes to L01 as requested |
| Web codec | H.264 only, 1080p cap | browser compatibility (the observed lag); outreach's standing policy |
| Naming | lowercase snake_case, no res/codec suffixes | one convention across repos; misleading `2160p`/`h265` suffixes removed |
| Course release tag | new `videos-web`; old `videos` archived then deleted | zero-downtime cutover |
| L02 slug | `02-intro-to-data` | title/slug agreement on the landing page; bookmark breakage accepted pre-semester |
| Sequencing | re-split first | the maintainer's first ask; independent of the package; the reel streams from the existing release today |

## 12. Follow-ups (not in this design)
- Migrate `outreach_talks` to the package (delete its `scripts/videos.py` + `components/`, add `videos.toml` files, map `perseverence_…` and the `h265` name, decide which of its remaining shared clips join `shared.toml`).
- World of Particles: `pnpm add` + `pip install` + a `videos:` headmatter block; no own release needed until it has course-specific clips.
- Optional CI `preflight` step in `qa.yml` once the chain is stable.
