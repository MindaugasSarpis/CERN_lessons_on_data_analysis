# FF-2026 Workstream B — Video Asset-Pipeline Port Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the CERN_lessons single-tier HEVC-web video pipeline with a two-tier pipeline — **H.264 web** (universal browser support) + **HEVC visually-lossless HQ** venue masters — ported and simplified from the outreach monorepo, with multi-machine `pull`/`pull-hq` and an HQ-aware `VideoPlayer` fallback chain.

**Architecture:** Three storage tiers: (1) **GDrive** raw masters (`rclone`), (2) **web** H.264 encodes published to the `videos` GitHub Release, (3) **HQ** HEVC golden masters published to a parallel `videos-hq` Release (oversized masters `hq_from_raw` ship from GDrive). `scripts/videos.py` is the manifest-driven driver; `VideoPlayer.vue` resolves HQ-local → web-local → web-release at runtime.

**Tech stack:** Python 3.11 (`tomllib`, stdlib), `ffmpeg` (libx264 web / libx265 HQ), `rclone` (GDrive), `gh` (Releases), Vue 3 / Slidev (`VideoPlayer.vue`, Vite env).

**Source of truth for the port:** `/home/mindaugas_wsl/outreach_talks/scripts/videos.py` (the mature two-tier implementation) and `/home/mindaugas_wsl/outreach_talks/components/VideoPlayer.vue`. This plan expresses the port as **exact deltas** against those known-good files.

---

## Port decisions (read before starting — these differ from a verbatim copy)

1. **Web tier → H.264 (libx264), not HEVC.** The roadmap §2.3 mis-describes outreach's web tier as H.264; outreach's actual `standard` profile is **libx265 (HEVC)**. HEVC-in-browser is unreliable (Windows/Linux Chrome, Firefox). Per roadmap §4 decision, the FF **web tier uses H.264** universally. **Consequence:** the 22 clips currently `remux` (HEVC stream-copy) must be **re-encoded** to H.264 for web — a one-time multi-hour encode that also right-sizes bloated web files (e.g. `Cloud_Chamber_Audio.mp4` is 383 MB today). Sources already H.264/VP8 stay `remux`.
2. **HQ tier stays HEVC** (`hq-visually-lossless`, libx265 CRF 16). HQ is local/venue only — HEVC decodes fine there.
3. **Drop the shared-clip registry.** Outreach's `shared.toml` / `_shared_protect` / `cmd_shared_check` / shared-release fallback exist to share clips across *multiple talks*. CERN_lessons is a single repo with one manifest — YAGNI. Omit them; re-addable later. This simplifies `videos.py` and shortens `VideoPlayer`'s fallback chain to 3 links.
4. **Single-repo path scheme.** No monorepo-root walking, no `outreach.toml`. Config comes solely from `videos/manifest.toml [defaults]` plus code fallbacks (`long_edge_px=1920`, `max_size_mb=200`). Script is run from repo root (`python3 scripts/videos.py`).
5. **VideoPlayer fallback chain:** `public/videos-hq/<src>` → `public/videos/<src>` → `<web release>/<src>`. Env-configurable via `VITE_VIDEO_REPO` / `VITE_VIDEO_RELEASE`, with hardcoded defaults so it works without a `.env`.

## Path remap (outreach → CERN_lessons)

| Constant | outreach (`TALK`=cwd talk dir) | CERN_lessons (cwd = repo root) |
|---|---|---|
| `REPO_ROOT` | `Path.cwd()` (talk) | `Path.cwd()` (repo root) |
| `MANIFEST` | `<talk>/videos/manifest.toml` | `videos/manifest.toml` |
| `RAW_DIR` | `<talk>/videos/raw` | `videos/raw` |
| `WEB_DIR` | `<talk>/public/videos` | `lectures/content/public/videos` |
| `HQ_DIR` | `<talk>/videos/hq` | `videos/hq` |
| `HQ_LINK_DIR` | `<talk>/public/videos-hq` | `lectures/content/public/videos-hq` |
| `SLIDES_DIR` (ref scan) | `<talk>` | `lectures/content` |

## Files

- Modify (near-rewrite): `scripts/videos.py`
- Replace: `lectures/content/components/VideoPlayer.vue`
- Migrate: `videos/manifest.toml`
- Create: `lectures/content/.env`
- Modify: `package.json` (add video scripts)
- Modify: `.gitignore` (HQ tier)
- Modify: `env.yaml` (ensure ffmpeg/rclone/gh)
- Modify: `README.md` (pipeline docs section)

---

## Task 1: HQ tier gitignore + directory scaffolding

**Files:**
- Modify: `.gitignore`
- Create: `videos/hq/.gitkeep`

- [ ] **Step 1: Add HQ paths to `.gitignore`**

Current video-related lines are `lectures/content/public/videos/`, `videos/raw/`, `videos/web/`. Add the HQ tier and its symlink; `videos/web/` is stale (unused) — leave it or remove. Append:

```gitignore
# HQ tier: visually-lossless venue masters (local + parallel GH release)
videos/hq/
lectures/content/public/videos-hq
```

- [ ] **Step 2: Verify the ignore** — `git check-ignore videos/hq/foo.mp4 lectures/content/public/videos-hq` prints both paths. Do **not** add a `videos/hq/.gitkeep`: the dir is ignored, so `git add` would refuse it without `-f`, and `encode-hq` `mkdir -p`s it at runtime anyway. The empty dir simply stays untracked.

- [ ] **Step 3: Commit**

```bash
git add .gitignore
git commit -m "chore(videos): gitignore HQ tier (videos/hq + public/videos-hq symlink)"
```

---

## Task 2: Rewrite `scripts/videos.py` as the single-repo two-tier port

**Files:**
- Modify: `scripts/videos.py` (base = outreach `scripts/videos.py`)

Approach: **copy the outreach file as the base, then apply the 7 edits below.** Copying the known-good base avoids re-typing ~1000 lines.

- [ ] **Step 1: Copy the outreach base**

```bash
cp /home/mindaugas_wsl/outreach_talks/scripts/videos.py scripts/videos.py
```

- [ ] **Step 2: Edit — replace the path-constants block** (outreach lines ~42-57, `TALK = …` through `_find_monorepo_root`). Replace with the single-repo block (drops monorepo-root walking):

```python
# Repo root = current working directory (scripts are run as `python3 scripts/videos.py`
# from the repo root via package.json). Single repo — no monorepo-root walking.
REPO_ROOT = Path.cwd().resolve()
MANIFEST = REPO_ROOT / "videos" / "manifest.toml"
RAW_DIR = REPO_ROOT / "videos" / "raw"
WEB_DIR = REPO_ROOT / "lectures" / "content" / "public" / "videos"
HQ_DIR = REPO_ROOT / "videos" / "hq"
HQ_LINK_DIR = REPO_ROOT / "lectures" / "content" / "public" / "videos-hq"
SLIDES_DIR = REPO_ROOT / "lectures" / "content"


def _auto_release_tag(prefix: str) -> str:
    return prefix  # single repo: web -> "videos", hq -> "videos-hq"
```

Note: this deletes `_find_monorepo_root` and changes `_auto_release_tag` (outreach derived it from the talk dir name; here the web tag is just `videos`). Downstream calls `_auto_release_tag("videos")` → `"videos"` and `_auto_release_tag("videos-hq")` → `"videos-hq"`, matching the manifest defaults.

**Also fix the two surviving `TALK` references** (they live in functions this port keeps untouched, so the rename would leave them undefined → `NameError` before the encode batch even runs):
- in `cmd_encode` (outreach ~line 355): `WEB_DIR.relative_to(TALK)` → `WEB_DIR.relative_to(REPO_ROOT)`
- in `cmd_encode_hq` (outreach ~line 961): `HQ_DIR.relative_to(TALK)` → `HQ_DIR.relative_to(REPO_ROOT)`

After this edit, `grep -n "\bTALK\b" scripts/videos.py` must return nothing.

- [ ] **Step 3: Edit — replace the `PROFILES` dict** (outreach lines ~91-136) with H.264 web profiles + the HEVC HQ profile. `{LONG_EDGE}` is substituted at encode time.

```python
PROFILES: dict[str, list[str]] = {
    # remux: stream-copy already-web-friendly sources (H.264/VP8/AV1 <= ~5 Mbps).
    # Do NOT use for HEVC sources destined for the web tier.
    "remux": [
        "-c", "copy",
        "-movflags", "+faststart",
    ],
    # Web tier: H.264 High profile, universal browser playback. CRF 21 ~ HEVC CRF 24.
    "standard": [
        "-c:v", "libx264", "-profile:v", "high", "-level", "4.2",
        "-preset", "slow", "-crf", "21",
        "-pix_fmt", "yuv420p",
        "-vf", "scale='min({LONG_EDGE},iw)':-2",
        "-c:a", "aac", "-b:a", "128k", "-ac", "2",
        "-movflags", "+faststart",
    ],
    "standard-tight": [
        "-c:v", "libx264", "-profile:v", "high", "-level", "4.2",
        "-preset", "slow", "-crf", "24",
        "-pix_fmt", "yuv420p",
        "-vf", "scale='min({LONG_EDGE},iw)':-2",
        "-c:a", "aac", "-b:a", "128k", "-ac", "2",
        "-movflags", "+faststart",
    ],
    "silent-loop": [
        "-c:v", "libx264", "-profile:v", "high", "-level", "4.2",
        "-preset", "slow", "-crf", "23",
        "-pix_fmt", "yuv420p",
        "-vf", "scale='min({LONG_EDGE},iw)':-2",
        "-an",
        "-movflags", "+faststart",
    ],
    "high-motion": [
        "-c:v", "libx264", "-profile:v", "high", "-level", "4.2",
        "-preset", "slow", "-crf", "19",
        "-pix_fmt", "yuv420p",
        "-vf", "scale='min({LONG_EDGE},iw)':-2",
        "-c:a", "aac", "-b:a", "192k", "-ac", "2",
        "-movflags", "+faststart",
    ],
    # HQ tier: HEVC visually-lossless venue master (local/venue only).
    "hq-visually-lossless": [
        "-c:v", "libx265", "-tag:v", "hvc1",
        "-preset", "slow", "-crf", "16", "-tune", "grain",
        "-pix_fmt", "yuv420p",
        "-vf", "scale='min({LONG_EDGE},iw)':-2",
        "-c:a", "copy",
        "-movflags", "+faststart",
    ],
}
```

- [ ] **Step 3b: Edit — guard `-movflags +faststart` for non-MP4 outputs.** The `remux` profile carries `-movflags +faststart`, which the WebM/Matroska muxer rejects (`Option movflags not found`) — so `Expansion_Funnel_H264_1080p.webm` (kept as `remux`) would FAIL to encode. Add a helper and apply it to the built ffmpeg `cmd` in both `_encode_one` and `_encode_one_hq`, just before `subprocess.run`:

```python
def _strip_movflags_for_non_mp4(cmd: list[str], out: Path) -> list[str]:
    """WebM/Matroska muxers reject the mov-only -movflags option."""
    if out.suffix.lower() in {".mp4", ".mov", ".m4v"}:
        return cmd
    pruned, i = [], 0
    while i < len(cmd):
        if cmd[i] == "-movflags":
            i += 2  # drop flag + its value
            continue
        pruned.append(cmd[i]); i += 1
    return pruned
```

Apply as `cmd = _strip_movflags_for_non_mp4(cmd, tmp)` (web) / `_strip_movflags_for_non_mp4(cmd, hq)` (HQ) before the subprocess call. (Pre-existing quirk in the current CERN script; worth fixing since the H.264 migration re-runs every clip.)

- [ ] **Step 4: Edit — simplify config loading.** Delete `_load_global_defaults` (outreach ~60-69). Replace `load_manifest` (outreach ~174-180) with a version that merges only code defaults + manifest `[defaults]`:

```python
def load_manifest() -> tuple[dict, list[VideoEntry]]:
    with MANIFEST.open("rb") as f:
        data = tomllib.load(f)
    defaults = {
        "long_edge_px": 1920,
        "max_size_mb": 200,
        **data.get("defaults", {}),
    }
    defaults.setdefault("release_tag", "videos")
    defaults.setdefault("release_tag_hq", "videos-hq")
    return defaults, _videos_from_data(data)
```

- [ ] **Step 5: Edit — delete the shared-registry machinery.** Remove these entirely:
  - `load_shared_manifest` (outreach ~183-199)
  - `_shared_protect` (outreach ~542-555)
  - `cmd_shared_check` (outreach ~758-830)
  - the `shared-check` subparser block in `main()` (outreach ~1018-1019)
  - the `protected=` / `protected` parameter and its use in the `_publish_tier` and `_pull_tier` bodies (outreach ~386-387, 396, 443-448, 471-472, 479, 521-523) — delete the param and its `.startswith`/`in protected` guards.
  - the `protected=_shared_protect(...)` call argument in **all four** command functions (miss one → `NameError` at runtime): `cmd_publish` (~line 570), **`cmd_publish_hq` (~line 592)**, `cmd_pull` (~line 606), and `cmd_pull_hq`'s prune block (~lines 652-669). Remove the argument in each.
  - Step 9's grep for `shared`/`protected` is the backstop for any straggler.

- [ ] **Step 6: Edit — simplify `cmd_check`** (outreach ~694-755) to drop shared handling. Replace with:

```python
def cmd_check(_: argparse.Namespace) -> int:
    _, videos = load_manifest()
    manifest_names = {v.name for v in videos}
    raw_files = {p.name for p in RAW_DIR.glob("*") if p.is_file() and not p.name.startswith(".")}
    web_files = {p.name for p in WEB_DIR.glob("*") if p.is_file() and not p.name.startswith(".")}
    refs = _slide_references()

    problems = 0
    for name in sorted(manifest_names - raw_files):
        print(f"  MISSING RAW:      {name}")
        problems += 1
    for name in sorted(raw_files - manifest_names):
        print(f"  ORPHAN RAW:       {name}")
        problems += 1
    for name in sorted(web_files - manifest_names):
        print(f"  ORPHAN WEB:       {name}")
        problems += 1
    for name in sorted(set(refs) - manifest_names):
        where = ", ".join(sorted(set(refs[name])))
        print(f"  UNKNOWN REF:      {name}  (in {where})")
        problems += 1
    for v in videos:
        if v.name not in refs:
            print(f"  UNUSED MANIFEST:  {v.name}")
            problems += 1

    if problems == 0:
        print(f"OK: {len(manifest_names)} manifest clip(s), {len(refs)} referenced, all consistent.")
        return 0
    print(f"\n{problems} issue(s) found.")
    return 1
```

Keep `VIDEO_REF_RE` and `_slide_references` as-is (the latter already `rglob`s `SLIDES_DIR`, now `lectures/content`).

- [ ] **Step 7: Edit — update the module docstring** (outreach ~1-29) to drop the shared-registry paragraph and the `shared-check` subcommand line; reflect the single-repo, H.264-web/HEVC-HQ design.

- [ ] **Step 8: Byte-compile + smoke the CLI**

Run: `python3 -m py_compile scripts/videos.py && python3 scripts/videos.py --help`
Expected: no syntax error; help lists `sync encode publish pull check encode-hq publish-hq pull-hq` and **no** `shared-check`.

- [ ] **Step 9: Grep for leftover shared refs**

Run: `grep -n "shared\|monorepo\|outreach.toml\|_find_monorepo" scripts/videos.py`
Expected: no matches (or only in comments you intend). Fix any stragglers.

- [ ] **Step 10: Commit**

```bash
git add scripts/videos.py
git commit -m "feat(videos): two-tier H.264-web/HEVC-HQ pipeline (single-repo port)"
```

---

## Task 3: Migrate `videos/manifest.toml` to the two-tier schema + H.264 profiles

**Files:**
- Modify: `videos/manifest.toml`

- [ ] **Step 1: Update `[defaults]`** — add the HQ release tag and long-edge; keep `source_remote`:

```toml
[defaults]
source_remote  = "gdrive:CERN_videos/raw"
release_tag    = "videos"       # web tier (H.264) GH Release
release_tag_hq = "videos-hq"    # HQ tier (HEVC venue masters) GH Release
long_edge_px   = 1920           # web scale cap
max_size_mb    = 200            # warn if an encoded web file exceeds this
```

- [ ] **Step 2: Re-classify every `[[videos]]` profile** away from blanket `remux` (which keeps HEVC) to H.264 re-encode profiles. Policy: `remux` only for already-H.264/VP8 sources; `silent-loop` only for clearly-silent b-roll/timelapse/loops (it strips audio); `high-motion` for CGI/sims; `standard` (or `standard-tight` for long clips) otherwise. Apply this mapping:

| name | new profile | why |
|---|---|---|
| `Skylapse.mp4` | `silent-loop` | silent timelapse loop |
| `Drone_Climbing_Mountain.mp4` | `standard` | cinematic |
| `NASA_Mars_Mariner_4_Pan_Audio.mp4` | `standard` | has audio |
| `Perseverence_Rover_Landing_NASA.mp4` | `standard` | landing footage |
| `Cassini_Grand_Finale_NO_VO.mp4` | `silent-loop` | NO_VO = silent |
| `Stars_Pan_Audio.mp4` | `standard` | has audio |
| `Telescope.mp4` | `silent-loop` | silent b-roll |
| `Hubble.mp4` | `silent-loop` | silent reel |
| `Webb_Reel.mp4` | `standard-tight` | 3 min, budget |
| `Milky_Way_Sim_Audio.mp4` | `high-motion` | CGI + audio |
| `Expansion_Funnel_H264_1080p.webm` | `remux` | VP8 webm, web-safe |
| `QGP_Formation.mp4` | `high-motion` | sim |
| `Voyage_in_to_the_world_of_atoms.mp4` | `standard` | animation |
| `Cloud_Chamber_Audio.mp4` | `standard` | has audio (was 383 MB) |
| `CERN_Overview_Short.mp4` | `standard` | overview |
| `ATLAS-VIDEO-2021-001-001-1080p.mp4` | `standard` | reel |
| `ATLAS-FOOTAGE-2022-004-002-1080p_Shaft.mp4` | `silent-loop` | construction b-roll |
| `LHCb.mp4` | `standard` | detector reel |
| `CERN-FOOTAGE-2023-019-001-2160p.mp4` | `silent-loop` | b-roll |
| `CERN-VIDEO-2020-064-001-2160p.mp4` | `remux` | already H.264 |
| `CERN-FOOTAGE-2024-006-001.mp4` | `silent-loop` | b-roll |
| `CERN-FOOTAGE-2024-010-002.mp4` | `silent-loop` | 10 s b-roll |
| `GTC_2020_1080p.mp4` | `standard` | excerpt |
| `Technology_Size_Comparison.mp4` | `standard` | animation |
| `VU_VM.mp4` | `standard-tight` | unchanged |

Keep each entry's `name`, `used_in`, and `notes`. Update the header comment block's "Profiles:" legend to describe the H.264 web / HEVC HQ profiles.

- [ ] **Step 3: ffprobe audio guard** — silent-loop strips audio, so verify the `silent-loop` picks are actually silent (only run if raws are present locally):

```bash
for f in Skylapse Cassini_Grand_Finale_NO_VO Telescope Hubble ATLAS-FOOTAGE-2022-004-002-1080p_Shaft CERN-FOOTAGE-2023-019-001-2160p CERN-FOOTAGE-2024-006-001 CERN-FOOTAGE-2024-010-002; do
  echo -n "$f: "; ffprobe -v error -select_streams a -show_entries stream=codec_type -of csv=p=0 "videos/raw/$f".* 2>/dev/null | head -1 || echo "(no raw)"
done
```
Expected: empty (no audio) for each. Any that report `audio` → switch that entry to `standard` to preserve the track.

- [ ] **Step 4: Validate the manifest parses** with the new script:

Run: `python3 scripts/videos.py check`
Expected: it loads the manifest without a TOML error. `MISSING RAW`/`ORPHAN WEB` lines are expected until re-encode (raws not synced, old HEVC web files still present) — the point of this step is only that parsing + profile lookup succeed (no `unknown profile`).

- [ ] **Step 5: Commit**

```bash
git add videos/manifest.toml
git commit -m "feat(videos): migrate manifest to two-tier schema + H.264 web profiles"
```

---

## Task 4: Replace `VideoPlayer.vue` with the HQ-aware 3-link fallback

**Files:**
- Replace: `lectures/content/components/VideoPlayer.vue`

- [ ] **Step 1: Write the new component.** Adapted from outreach `VideoPlayer.vue` minus the shared-release link (3-link chain), keeping the repo's existing native-`controls` template (lower churn than outreach's custom controls). Full file:

```vue
<script setup>
import { ref, computed, watch, nextTick, onMounted } from 'vue'
import { useIsSlideActive } from '@slidev/client'

// Per-repo config via Vite env (lectures/content/.env), with hardcoded fallbacks
// so the component works even without a .env file.
//   VITE_VIDEO_REPO     e.g. "MindaugasSarpis/CERN_lessons_on_data_analysis"
//   VITE_VIDEO_RELEASE  web-tier GH Release tag (default "videos")
// Fallback chain (front-to-back) when hq=true:
//   public/videos-hq/<src>  (local HQ symlink)
//   public/videos/<src>     (bundled web tier)
//   <web release>/<src>     (H.264 assets published to the release)
// hq=false drops the first step.
const REPO    = import.meta.env.VITE_VIDEO_REPO    || 'MindaugasSarpis/CERN_lessons_on_data_analysis'
const RELEASE = import.meta.env.VITE_VIDEO_RELEASE || 'videos'
const REMOTE_BASE = `https://github.com/${REPO}/releases/download/${RELEASE}`

const props = defineProps({
  src:      { type: String, required: true },
  fallback: { type: String, default: '' },
  autoplay: { type: Boolean, default: false },
  loop:     { type: Boolean, default: false },
  muted:    { type: Boolean, default: false },
  controls: { type: Boolean, default: true },
  // Serve the visually-lossless venue master from public/videos-hq/<src>
  // (symlink to videos/hq/) when present; else fall through to the web tier.
  hq:       { type: Boolean, default: true },
})

const base = computed(() => import.meta.env.BASE_URL || '/')
const hqLocalSrc  = computed(() => `${base.value}videos-hq/${props.src}`)
const webLocalSrc = computed(() => `${base.value}videos/${props.src}`)
const webRemoteSrc = computed(() => props.fallback || `${REMOTE_BASE}/${props.src}`)
const fallbackChain = computed(() => {
  const chain = props.hq
    ? [hqLocalSrc.value, webLocalSrc.value, webRemoteSrc.value]
    : [webLocalSrc.value, webRemoteSrc.value]
  return chain.filter((url, i) => i === 0 || url !== chain[i - 1])
})
const localSrc = computed(() => props.hq ? hqLocalSrc.value : webLocalSrc.value)

const videoRef = ref(null)
const sourceRef = ref(null)
const currentSrc = ref(localSrc.value)
const status = ref('idle')
const isActive = useIsSlideActive()
const hasBeenActive = ref(false)

const mimeType = computed(() => {
  const ext = props.src.split('.').pop()?.toLowerCase()
  if (ext === 'webm') return 'video/webm'
  return 'video/mp4'
})

let switching = false
function onError() {
  if (switching || !hasBeenActive.value) return
  const chain = fallbackChain.value
  const idx = chain.indexOf(currentSrc.value)
  if (idx === -1 || idx === chain.length - 1) {
    status.value = 'error'
    return
  }
  switching = true
  status.value = 'loading'
  currentSrc.value = chain[idx + 1]
  nextTick(() => {
    videoRef.value?.load()
    switching = false
  })
}

function syncPlayback() {
  const video = videoRef.value
  if (!video) return
  if (isActive.value) {
    if (!hasBeenActive.value) {
      hasBeenActive.value = true
      status.value = 'loading'
      nextTick(() => videoRef.value?.load())
    }
    video.currentTime = 0
    video.muted = true
    video.play().then(() => {
      if (!props.muted) video.muted = false
    }).catch(() => {})
  } else {
    video.pause()
    video.muted = true
    video.currentTime = 0
  }
}

watch(isActive, syncPlayback, { immediate: true })

function onLoaded() {
  status.value = 'ready'
  syncPlayback()
}

onMounted(() => {
  sourceRef.value?.addEventListener('error', onError)
  syncPlayback()
})
</script>

<template>
  <div class="video-player">
    <div v-if="status === 'loading' || status === 'idle'" class="video-status">Loading video&hellip;</div>
    <div v-if="status === 'error'" class="video-status video-error">
      Video not available: <code>{{ src }}</code>
    </div>
    <video
      ref="videoRef"
      :loop="loop"
      :controls="controls"
      muted
      playsinline
      webkit-playsinline
      preload="none"
      @loadeddata="onLoaded"
      @error="onError"
      :class="{ 'video-ready': status === 'ready' }"
    >
      <source ref="sourceRef" :src="hasBeenActive ? currentSrc : ''" :type="mimeType" />
    </video>
  </div>
</template>

<style scoped>
.video-player {
  position: absolute;
  inset: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  background: black;
}
.video-player video {
  width: 100%;
  height: 100%;
  object-fit: contain;
  opacity: 0;
  pointer-events: none;
}
.video-player video.video-ready {
  opacity: 1;
  pointer-events: auto;
}
.video-status {
  position: absolute;
  padding: 2rem;
  opacity: 0.6;
  font-size: 0.9rem;
  color: white;
}
.video-error {
  color: #ef4444;
  opacity: 1;
}
</style>
```

- [ ] **Step 2: Verify the deck still builds** with the new component (no HQ files needed — chain falls through to web):

Run: `pnpm build` (builds the BS deck, which uses `VideoPlayer` heavily)
Expected: build succeeds; no Vue/import errors referencing `VideoPlayer`.

- [ ] **Step 3: Commit**

```bash
git add lectures/content/components/VideoPlayer.vue
git commit -m "feat(VideoPlayer): HQ-aware 3-link fallback (hq-local -> web-local -> release)"
```

---

## Task 5: `.env`, `package.json` scripts

**Files:**
- Create: `lectures/content/.env`
- Modify: `package.json`

- [ ] **Step 1: Create the `.env` at the repo root.** Vite loads `.env` from the process cwd, and `pnpm dev/build` invoke `slidev lectures/content/…md` from the **repo root** — so the override belongs in `./.env` (repo root), not the entry dir. Create `./.env`:

```dotenv
VITE_VIDEO_REPO=MindaugasSarpis/CERN_lessons_on_data_analysis
VITE_VIDEO_RELEASE=videos
```

These values equal the component's hardcoded fallbacks, so playback is correct even if the override isn't picked up — Step 2 confirms the location Vite actually reads and relocates the file if needed.

- [ ] **Step 2: Confirm env pickup** — start dev, confirm `import.meta.env.VITE_VIDEO_REPO` resolves (temporary `console.log` in `VideoPlayer.vue` setup, or check network tab points at the right release). If Vite does **not** load it from `lectures/content/.env`, move the file to the repo root and re-verify. Remove the temporary log. (The component's hardcoded fallbacks mean playback works either way; this step only confirms env override.)

- [ ] **Step 3: Add the video scripts to `package.json`.** The `scripts` block currently has `sync`/`encode`/`publish`/`check`. Add the HQ + pull commands so it reads:

```json
    "videos:sync": "python3 scripts/videos.py sync",
    "videos:encode": "python3 scripts/videos.py encode",
    "videos:encode-hq": "python3 scripts/videos.py encode-hq",
    "videos:publish": "python3 scripts/videos.py publish",
    "videos:publish-hq": "python3 scripts/videos.py publish-hq",
    "videos:pull": "python3 scripts/videos.py pull",
    "videos:pull-hq": "python3 scripts/videos.py pull-hq",
    "videos:check": "python3 scripts/videos.py check"
```

- [ ] **Step 4: Verify** each script resolves: `pnpm run | grep videos:` lists all eight.

- [ ] **Step 5: Commit**

```bash
git add package.json lectures/content/.env
git commit -m "feat(videos): env config + encode-hq/publish-hq/pull/pull-hq pnpm scripts"
```

---

## Task 6: Toolchain deps (`env.yaml`) + pipeline docs (`README.md`)

**Files:**
- Modify: `env.yaml`
- Modify: `README.md`

- [ ] **Step 1: Ensure `env.yaml` bundles the pipeline tools.** Confirm `ffmpeg`, `rclone`, and `gh` are listed under dependencies; add any missing (conda-forge provides all three).

Run to check: `grep -E "ffmpeg|rclone|gh( |$)|gh=" env.yaml`

- [ ] **Step 2: Add a "Video pipeline" section to `README.md`** documenting: the three tiers (GDrive raws → H.264 web release → HEVC HQ release), the eight `pnpm videos:*` commands, the manifest schema (`profile`, `used_in`, `hq_crf`, `hq_from_raw`, `long_edge_px`), the H.264-web/HEVC-HQ rationale, and the fresh-machine flow (`pnpm install && pnpm videos:pull` for web, `videos:pull-hq` for masters). (If a `CLAUDE.md` exists in this repo, mirror a short pointer there.)

- [ ] **Step 3: Commit**

```bash
git add env.yaml README.md
git commit -m "docs(videos): document two-tier pipeline + ensure ffmpeg/rclone/gh in env"
```

---

## Task 7: End-to-end dry verification (no heavy encode required)

The full re-encode + publish is an operational run (needs raws synced from GDrive; multi-hour). This task verifies the *pipeline wiring* without it.

- [ ] **Step 1: `check` runs clean on structure** — `python3 scripts/videos.py check` loads manifest, scans `lectures/content` refs, reports (raw/web orphan/missing lines expected pre-encode; **no** tracebacks, **no** `unknown profile`).

- [ ] **Step 2: `encode --only` dry path** — with one small raw present (sync a single clip or drop a test file), `pnpm videos:encode --only CERN-FOOTAGE-2024-010-002.mp4` produces an H.264 file in `lectures/content/public/videos/`. Confirm codec:

```bash
ffprobe -v error -select_streams v -show_entries stream=codec_name -of csv=p=0 lectures/content/public/videos/CERN-FOOTAGE-2024-010-002.mp4
```
Expected: `h264`.

- [ ] **Step 3: `encode-hq --only`** on the same clip writes to `videos/hq/`, creates the `lectures/content/public/videos-hq` symlink, and produces HEVC:

```bash
ffprobe -v error -select_streams v -show_entries stream=codec_name -of csv=p=0 videos/hq/CERN-FOOTAGE-2024-010-002.mp4
```
Expected: `hevc`; and `readlink lectures/content/public/videos-hq` → `../../../videos/hq` (or absolute equivalent).

- [ ] **Step 4: `publish --dry-run` / `pull --dry-run`** print the intended `gh release upload`/`download` for `videos` without erroring on auth (they may report the release is missing — that is fine for a dry check; it proves the tag wiring).

- [ ] **Step 5: Full deck build** — `pnpm build` succeeds with the migrated pipeline in place.

- [ ] **Step 6: Final commit — explicit paths, not `git add -A`** (so a parallel Workstream A checkout isn't swept into this commit):

```bash
git add scripts/videos.py videos/manifest.toml \
  lectures/content/components/VideoPlayer.vue \
  package.json .gitignore env.yaml README.md .env
git commit -m "test(videos): verify two-tier pipeline wiring (encode/encode-hq/check/build)"
```

(Add `lectures/content/.env` instead of `.env` if Step 5 settled the env file there.)

---

## Self-review checklist (run after drafting, before execution)
- **Spec coverage:** three tiers (GDrive/web/HQ) ✓ (Tasks 2-3,7); H.264 web ✓ (Task 2 §3, Task 3); HEVC HQ ✓ (Task 2 §3); pull/pull-hq ✓ (Task 2 base, Task 5); VideoPlayer chain ✓ (Task 4); manifest migration ✓ (Task 3); scripts/env/gitignore/docs ✓ (Tasks 1,5,6).
- **Shared-registry removal is complete:** Task 2 §5 enumerates every function + param; Task 2 §9 greps for stragglers.
- **Names consistent:** `release_tag`/`release_tag_hq`, `hq_from_raw`, `hq_crf`, `long_edge_px` match across `videos.py`, `manifest.toml`, and this plan.
- **Operational caveat surfaced:** the H.264 re-encode of the HEVC library is a one-time multi-hour run needing GDrive raws (Task 7 notes it; not blocking the wiring verification).
```
