# Video pipeline as a reusable package (`slidev-videos`) + course migration + L01/L02 re-split — design

**Date:** 2026-09-01 · **Status:** approved in discussion, awaiting spec review · **Supersedes:** `docs/superpowers/plans/2026-07-01-ff2026-workstream-b-video-pipeline-port.md` (0/36 steps done, written before outreach's 2026-07-17/18 pipeline changes).

## 1. Summary

The lecture videos are the strongest hook of the course — the maintainer's feedback is that students were "captivated from the very first lecture" by the CERN reel. Today the course repo runs a February-2026 first-generation pipeline (`scripts/videos.py`, 467 lines: `sync fetch encode publish check`, one HEVC web tier, one hard-coded GitHub Release, a two-step player fallback), while the sibling repo `/home/mindaugas_wsl/outreach_talks` has evolved a much more complete pipeline (12 subcommands, H.264 web tier with EBU R128 loudness normalisation, `pull`/`preflight`/`clean`, a shared-clip registry, a four-step player fallback chain with look-ahead preload). Both repos — and at least one more course ("World of Particles") — need the same thing.

This design:

1. extracts the pipeline into a **standalone package repo `MindaugasSarpis/slidev-videos`** — a Python CLI + a Slidev addon holding the player + the canonical **shared clip library** (registry + GitHub Release of 1080p H.264 encodes);
2. **migrates this course** onto it (removing the local `videos.py` and `VideoPlayer.vue`, re-encoding every clip to H.264, publishing to new release tags);
3. **re-splits lectures 01/02**: L01 = orientation → a curated 30-clip motivation reel (§8.1.1), L02 = introduction to data (the current "Data in Your Life" material plus ~30 min of new intro-to-data content).

Sequencing (each stage independently shippable): **§8 re-split first, reel pass 1** (uses today's pipeline and only clips already on the release) → package v0.1.0 (§3–§6, §9) → shared library encode + publish (§5) → course migration incl. **reel pass 2** (§7, §8.1.1: the 12 added clips, the trims, the 1080p Perseverance).

### Goals
- One pipeline and one player, versioned, installable into any Slidev course/talk repo in two lines.
- Browser-safe playback everywhere: **1080p H.264 web tier only** (outreach's 2026-07-18 policy after HEVC/4K freezes at the Yaga venue). Two causes of the lag the maintainer observed in L02's reel: `Perseverance_Rover_Landing_NASA.mp4` on the release is a genuine 3840×2160 H.264 60 fps file (230 MB, 3:10) — the only true-4K asset (the two `…-2160p`-named files carry 1080p streams) — and 23 of the other 26 clips are HEVC, which many lecture-hall browsers decode in software or not at all. The 1920 cap and H.264 fix both.
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
| D1 | L01/L02 re-split (reel pass 1) + new L02 content + bookkeeping | this repo |
| D2 | Package repo `slidev-videos` v0.1.0: CLI, addon, tests, example deck, README | new repo |
| D3 | Shared clip library: `shared.toml` + release `videos-shared` (25 clips, H.264 1080p) | package repo |
| D4 | Course migration: consume D2/D3, re-encode course-specific clips → release `videos-web`, reel pass 2, docs | this repo |

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
Outreach's schema (`name`, `profile`, `used_in`, `notes`, `long_edge_px`, `hq_crf`, `hq_from_raw`, `encoder`, `loudnorm`) plus one new optional field, **`trim = ["0:20", "1:50"]`** (start, end; either may be `""`), applied at encode as `-ss <start>` before the input and `-to <end>` after it — the web tier holds the trimmed clip, the raw stays whole, so a trim is reproducible and reversible. `trim` on a `remux` entry cuts at keyframes (documented; use a re-encode profile for frame-accurate cuts). The course manifest is already schema-compatible. Profiles (web tier, H.264 libx264 / h264_nvenc): `remux`, `standard` (CRF 23, ≤6 Mbps, AAC 128k), `standard-tight` (CRF 26, ≤3.5 Mbps), `silent-loop` (CRF 24, ≤5 Mbps, audio stripped), `high-motion` (CRF 22, ≤8 Mbps, AAC 192k); all `scale=min(web_long_edge_px,iw):-2`, `+faststart`, two-pass loudnorm −16 LUFS on audio-bearing encodes. `remux` is only valid when `preflight` would pass on the raw (H.264/VP8/VP9 + browser-safe audio); `encode` refuses to remux HEVC/PCM sources and says why.

### 4.4 Subcommands
`sync`, `fetch`, `encode`, `encode-hq`, `publish`, `publish-hq`, `pull`, `pull-hq`, `check`, `shared-check`, `clean`, `preflight`, `venue`, `build` — semantics as in outreach (plus the course's `fetch`). `shared-check` runs in the package repo (which is a project whose manifest *is* `shared.toml`). New flag on every command: `--project <dir>`.

### 4.5 Shared library awareness in consumers
The bundled `shared.toml` tells the CLI which names are shared. In a consumer project: `check` reports inherited clips (referenced by slides, absent from the local manifest, present in the registry) and flags references that are in neither; `pull --include-shared` fetches them from the shared release; `clean`/`publish --prune` never touch shared names; `preflight` resolves the same chain the player uses (local HQ → local web → own release → shared release) and ffprobes the winner.

## 5. Shared clip library

### 5.1 Policy
A clip is *shared* when it is generic CERN/LHC/experiment footage, space/astronomy B-roll, or a CGI science sim usable by more than one deck. Course/talk-specific material (venue clips, chart renders, lecture explainers) stays in the consumer's own manifest and release.

### 5.2 Naming
One convention: **lowercase snake_case, no resolution or codec suffixes** (`cern_footage_2022_013_001.mp4`, not `cern_footage_2022_013_001_1080p_lhc.mp4`). CERN CDS clips are named by their report number so the source record is recoverable (`videos.cern.ch` search by report number); the human description lives in the manifest `notes` and in an HTML comment on the slide. Outreach's current names are mapped during its migration (a rename table in the package README); nothing is kept verbatim for its own sake.

### 5.3 Initial contents (33 clips) and sources

Sources: **R** = this course's release `videos`; **D** = the maintainer's Drive `resources/videos/<folder>/`; **O** = an outreach release. Durations from `ffprobe` (release) or the CDS record (Drive).

| shared name | source | what | run | profile |
|---|---|---|---|---|
| skylapse.mp4 | R Skylapse.mp4 | CERN aerial timelapse loop (kept for outreach; no longer in L01) | 7:29 | silent-loop |
| drone_climbing_mountain.mp4 | R | drone ascent | 0:27 | high-motion |
| nasa_mars_mariner_4_pan_audio.mp4 | R | Mariner 4, 1965 | 0:20 | standard |
| perseverance_rover_landing_nasa.mp4 | R (true 4K H.264 60 fps → 1080p; spelling fixed) | Mars landing | 3:10 | high-motion, `trim` |
| cassini_grand_finale.mp4 | R Cassini_Grand_Finale_NO_VO.mp4 | Saturn | 3:41 | standard, `trim` |
| stars_pan_audio.mp4 · telescope.mp4 · hubble.mp4 | R | | 0:20 · 0:40 · 0:33 | standard |
| webb_reel.mp4 | R | JWST reel | 2:58 | standard, `trim` |
| milky_way_sim_audio.mp4 | R | galaxy sim | 1:01 | high-motion |
| sdss_universe_zoom.mp4 | D cosmology/sdss_universe_zoom_trim_3.mp4 | SDSS galaxy map fly-through | ~1:00 | standard |
| expansion_funnel.webm | R Expansion_Funnel_H264_1080p.webm | cosmic expansion (VP8) | 0:30 | remux |
| qgp_formation.mp4 | R | quark-gluon plasma | 0:33 | high-motion |
| cern_footage_2015_006_001.mp4 | D cern/ | Standard Model table animation | 0:34 | standard |
| voyage_in_to_the_world_of_atoms.mp4 | R | hair → quarks | 2:01 | standard |
| cloud_chamber_audio.mp4 | R | cloud chamber | 2:29 | standard, `trim` |
| cern_overview_short.mp4 | R | CERN aerial | 0:11 | standard |
| cern_footage_2022_013_001.mp4 | O yaga / D cern/ | real LHC tunnel travelling | 4:13 | standard, `trim` |
| atlas_footage_2022_004_002.mp4 | R …_Shaft.mp4 | descending the ATLAS shaft (3:2) | 0:29 | standard |
| atlas_video_2021_001_001.mp4 | R | ATLAS overview | 0:49 | standard |
| cms.mp4 | D cern/cms.mp4 | CMS | ~0:30 | standard |
| cern_footage_2022_042_001.mp4 | D cern/ (.mov) | LHCb 3D fly-in | 0:56 | standard |
| lhcb.mp4 | R | LHCb reel with audio | 0:47 | standard |
| cern_footage_2024_006_012.mp4 | D cern/uploaded_cern_footage_2024_006_012.mp4 | beam-pipe collision burst | 0:27 | standard |
| atlas_video_2023_013_001.mp4 | D cern/ | ATLAS event display | 0:30 | standard |
| cern_footage_2022_013_006.mp4 | D cern/ | CERN data centre, tape robot | 2:04 | standard, `trim` |
| cern_footage_2025_048_001.mp4 | D cern/ | WLCG globe (1962×1080 → 1920) | 0:23 | standard |
| cern_footage_2025_049_001.mp4 | D cern/ | "1 exabyte" growth chart | 0:10 | standard |
| cern_video_2015_024_001.mp4 | D cern/ | accelerator complex → detector → data centre → WLCG → Higgs bump | 2:51 | standard |
| cern_footage_2024_006_001.mp4 | R | FCC map aerial | 0:18 | standard |
| cern_video_2025_029_001.mp4 | D cern/ (1080p) | rare B→K*μμ decay through LHCb (captions, no voice) — L02 | 2:28 | standard |
| cern_video_2019_050_008.mp4 | O videos-shared (…_1080ph265) | vacuum / beam-pipe animation (outreach) | 1:35 | standard |
| cern_footage_2025_014_002.mp4 | O sceptics | FCC map with labels (outreach) | 0:18 | standard |
| cern_footage_2024_010_002.mp4 | R | FCC-hh tunnel render (outreach) | 0:10 | standard |

Not in the initial library (they stay on the archived course release; add later if a deck wants them): `CERN-FOOTAGE-2023-019-001` (ALPHA-g, narrated), `CERN-VIDEO-2020-064-001` (HEV ventilator, narrated), `VU_VM.mp4` (superseded by the faculty clip).

Source preference for the one-time encode: (1) the raw on gdrive (`gdrive:CERN_videos/raw` for course clips; `gdrive:work/outreach/resources/videos/released` for outreach clips) when rclone is available — this machine has none, the maintainer's Mac does; (2) otherwise the released file as the "raw" (`gh release download … --dir videos/raw`), documented in the package README as the fallback with its small generational-loss cost. Every result must pass `preflight` (H.264, ≤1920 long edge, ≤10 Mbps, browser-safe audio, loudness within ±2 LU of −16 LUFS) before publish.

Course-specific clips (stay in this course, release `videos-web`, same renaming rule): `vu_physics_faculty.mp4` (maintainer-supplied, the L01 reel opener; profile `standard`), `gtc_2020.mp4`, `technology_size_comparison.mp4`, `cpu_vs_gpu_demo.mp4`, `how_computer_memory_works.mp4` (`standard-tight`; will still exceed `max_size_mb` — accepted, warning only). Dropped: `VU_VM.mp4`, the orphan `VU_VM_Zoom.*` and the misspelt duplicate `Perseverence_…` release asset (after pass 2; pass 1 still references it, §8.1.1).

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

### 8.1 L01 — "Orientation & Motivation" (≈ 113 min after pass 1, ≈ 131 after pass 2)
Order: cover · Who am I talking to · quote · Course Structure … Learning Outcomes (as today) · How This Course Works (as today) · Seminars & Your Project (as today) · `# Breaks…` · section **What is CERN?** with its four context slides (CERN at a Glance, LHC, Accelerator Chain, How a Detector Sees a Collision) · the **motivation reel** (§8.1.1, three acts with the *Half-time* slide after Act I) · closing slide **Why You Need These Skills** (moved from L02) · the existing "What You Need / Today's Task" slide stays last. Estimate: 74.1 + 0.5 + 9.0 + reel (18 × 1.5 = 27 at pass 1; 30 × 1.5 = 45 at pass 2) + ~2.5 for the section/Half-time/closer slides.

#### 8.1.1 The reel — three acts, 30 clips, ≈ 24 min of footage plus the faculty clip
Curated on 2026-09-01 against the release probes, the maintainer's Drive pool (`resources/videos/{cern,cosmology,science}/`) and the CDS catalogue. Principles: **no clip longer than 1:30** (long ones get a manifest `trim`, §4.3); **each act ends on data**; **every LHC experiment appears**; **nothing narrated** (the reel runs with the lights down and no talk-over — the presenter notes on the two section slides stay); off-topic clips leave. Every video slide carries an HTML comment naming what the clip shows (the CDS names are opaque). "Pass" says when the clip enters: **1** = the re-split (already on the release), **2** = with the shared-library encode.

**Act I — From the Cosmos** (section slide as today)

| # | `src` | what | run (after trim) | pass |
|---|---|---|---|---|
| 1 | vu_physics_faculty.mp4 | maintainer-supplied VU Physics Faculty clip — the opener, replacing Skylapse + VU_VM. Slot reserved; until the file is delivered the act opens at #2 | — | when delivered |
| 2 | drone_climbing_mountain.mp4 | Earth, human scale | 0:27 | 1 |
| 3 | nasa_mars_mariner_4_pan_audio.mp4 | 1965: the first data from another planet | 0:20 | 1 |
| 4 | perseverance_rover_landing_nasa.mp4 | Mars landing — pass 1 references the existing 1080p HEVC asset `Perseverence_Rover_Landing_NASA.mp4` (misspelt, 34 MB) instead of the 4K one | 3:10 → 1:30 | 1 (trim at 2) |
| 5 | cassini_grand_finale.mp4 | Saturn | 3:41 → 1:30 | 1 (trim at 2) |
| 6–8 | stars_pan_audio · telescope · hubble | | 0:20 · 0:40 · 0:33 | 1 |
| 9 | webb_reel.mp4 | JWST | 2:58 → 1:30 | 1 (trim at 2) |
| 10 | milky_way_sim_audio.mp4 | the galaxy | 1:01 | 1 |
| 11 | sdss_universe_zoom.mp4 | the SDSS map — a universe drawn from a dataset | ~1:00 | 2 |
| 12 | expansion_funnel.webm | Big Bang expansion | 0:30 | 1 |

*Half-time* slide — unchanged ("Every scene so far ends as data someone must turn into understanding…").

**Act II — …to the Quantum** (no section slide; runs straight from Half-time)

| # | `src` | what | run | pass |
|---|---|---|---|---|
| 13 | qgp_formation.mp4 | primordial soup | 0:33 | 1 |
| 14 | cern_footage_2015_006_001.mp4 | the Standard Model table builds up | 0:34 | 2 |
| 15 | voyage_in_to_the_world_of_atoms.mp4 | hair → quarks | 2:01 | 1 |
| 16 | cloud_chamber_audio.mp4 | particles made visible | 2:29 → 1:30 | 1 (trim at 2) |

**Act III — Inside CERN** (section slide as today; real → machine → collision → data)

| # | `src` | what | run | pass |
|---|---|---|---|---|
| 17 | cern_overview_short.mp4 | aerial | 0:11 | 1 |
| 18 | cern_footage_2022_013_001.mp4 | real LHC tunnel travelling | 4:13 → 1:00 | 2 |
| 19 | atlas_footage_2022_004_002.mp4 | descending the ATLAS shaft (3:2, `fit` cover) | 0:29 | 1 |
| 20 | atlas_video_2021_001_001.mp4 | ATLAS overview | 0:49 | 1 |
| 21 | cms.mp4 | CMS | ~0:30 | 2 |
| 22 | cern_footage_2022_042_001.mp4 | LHCb 3D fly-in, human for scale | 0:56 | 2 |
| 23 | lhcb.mp4 | LHCb reel — home of the seminar dataset | 0:47 | 1 |
| 24 | cern_footage_2024_006_012.mp4 | beam-pipe collision burst | 0:27 | 2 |
| 25 | atlas_video_2023_013_001.mp4 | ATLAS event display — a collision as data | 0:30 | 2 |
| 26 | cern_footage_2022_013_006.mp4 | CERN data centre, tape robot | 2:04 → 0:45 | 2 |
| 27 | cern_footage_2025_048_001.mp4 | WLCG globe, transfer arcs | 0:23 | 2 |
| 28 | cern_footage_2025_049_001.mp4 | "1 exabyte" growth chart | 0:10 | 2 |
| 29 | cern_video_2015_024_001.mp4 | Earth → accelerator chain → detector → trigger → data centre → WLCG → Higgs bump — the closer | 2:51 | 2 |
| 30 | cern_footage_2024_006_001.mp4 | FCC map — the future | 0:18 | 1 |

Removed from the reel (they stay on the archived release, nothing is deleted): Skylapse and VU_VM (superseded by #1), CERN-FOOTAGE-2023-019-001 (ALPHA-g, narrated, off-topic), CERN-VIDEO-2020-064-001 (HEV ventilator interviews), GTC_2020 (NVIDIA keynote — L15 material), CERN-FOOTAGE-2024-010-002 (FCC-hh render). Pass 1 therefore plays 18 clips in the order above (plus #1 when delivered) with the pass-1 file names (today's mixed-case release names); the pass-2 rename is a mechanical `src=` substitution (§7).

### 8.2 L02 — "Introduction to Data" (target ≈ 110 min)
Order: cover (retitled) · quote · Learning Objectives (rewritten for data) · section **Data in Your Life** (16 slides, moved verbatim from L01) · section **Four Eyes on the Ring** incl. *Meet the Particle You'll Analyse* · section **Why Data?** (Why Data Analysis Matters, From Collision to Dataset, From Events to Petabytes, Why It Has to Be Real-Time) · **new** section **Open Data & Provenance** (~4 slides, ~10 min: open-data portals — CERN Open Data, NASA, Eurostat, Zenodo; records, DOIs and licences; what a README/provenance note must say; the seminar-2 dataset record 401 as the worked example) · **new** section **A Dataset Up Close** (~3 slides + 1 MCQ, ~10 min, opening with `cern_video_2025_029_001.mp4` — a rare B → K*μμ decay followed through LHCb, 2:28, captions, no voice, pass 2 — then the D⁰ → K⁻π⁺ file: rows are events, columns are measurements, units, measurement vs metadata, a first look at the invariant-mass column) · section **Beyond the Ring** (CERN's Impact, A Planet-Sized Computer, Open Data Up Close) · **new** MCQ on data lifecycle/provenance · Careers at CERN · A Day in the Data · Recap (rewritten). Estimate: 3 + 34.2 + 8.8 + 18.4 + 10 + 10 + 8.0 + 3 + ~7 ≈ 102–110 — the two new sections are sized so the gate reports ≥ 108; if the first `pnpm timing` lands under, the new sections grow (never the reel returns).

### 8.3 Bookkeeping
- `lectures/content/decks.json`: `01-orientation` title → "Orientation & Motivation"; `02-cern` → slug `02-intro-to-data`, title "Introduction to Data" (URL change accepted; the landing regenerates from the manifest; old `/02-cern/` links 404).
- Files: `02_Introduction_to_CERN.md` → `02_Introduction_to_Data.md` (and the combined authoring entry's `src:` line).
- Workbook: `mkdocs.yml` nav + `docs/index.md` titles; `docs/lectures/lecture_2.md` (currently an empty stub) gets a page mirroring the new L02 sections; `docs/lectures/lecture_1.md` title updated; `seminar_01.md` / `seminar_02.md` "Paired lecture" lines.
- `videos/manifest.toml` `used_in` → `["L01"]` for the 18 pass-1 reel clips, `[]` for the six removed ones (this stage keeps the old names; §7 renames). Pass 1 adds a manifest entry for the existing misspelt 1080p asset `Perseverence_Rover_Landing_NASA.mp4` with a note that pass 2 retires it.
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
| Sequencing | re-split first (reel pass 1), adds/trims with the library (pass 2) | the maintainer's first ask; independent of the package; the reel streams from the existing release today |
| Reel opener | maintainer-supplied VU Physics Faculty clip replaces Skylapse + VU_VM | maintainer's call, 2026-09-01 |
| Reel length | ≤ 1:30 per clip via manifest `trim`; six long clips trimmed | six clips carried 20 of the 34 minutes; reproducible trims beat hand-cut files |

## 12. Follow-ups (not in this design)
- Migrate `outreach_talks` to the package (delete its `scripts/videos.py` + `components/`, add `videos.toml` files, map `perseverence_…` and the `h265` name, decide which of its remaining shared clips join `shared.toml`).
- World of Particles: `pnpm add` + `pip install` + a `videos:` headmatter block; no own release needed until it has course-specific clips.
- Optional CI `preflight` step in `qa.yml` once the chain is stable.
- Before any week-1 delivery on reel pass 1: verify the venue browser decodes HEVC — 17 of the 18 pass-1 clips are HEVC-only or HEVC+AAC; only `Expansion_Funnel_H264_1080p.webm` plays on every browser. Pass 2 removes this constraint.
