# Landing Polish (5 items) + Video Fetch Workflow — Design Spec

**Status:** Approved (author, 2026-07-06) · **Branch:** `ff2026`
**Parents:** `2026-07-06-landing-fibers-design.md` (landing), `videos/manifest.toml` pipeline (videos)

## A. Landing polish (all five approved)

1. **Art-directed title breaks.** `decks.json` gains optional `titleLines`
   (`["Best Research", "and Data Analysis", "Practices from CERN"]`);
   `gen-landing.mjs` uses it when present, falls back to the auto word-split;
   `.title` gets `text-wrap: balance` as a safety net for wrapped lines.
2. **Social metadata.** `decks.json` gains `site.url` (canonical Pages URL).
   When present, `gen-landing.mjs` emits `<meta name="description">`, OG
   (title/description/type/url/image) and `twitter:card` tags. The OG image
   is a 1200×630 hero screenshot generated once and committed at
   `landing/og.png`; `build-landing.mjs` copies it to `<out>/assets/og.png`.
3. **Exit transition + prefetch.** Clicking a lecture row (plain left-click
   only — modified clicks keep browser defaults) adds `.leaving` to `<html>`,
   fading `.wrap` + `#field` out over ~300 ms before navigating; instant
   under reduced motion. First hover on a row injects
   `<link rel="prefetch" href="<deck>/">`. Both work without the WebGL field.
4. **Pulse-on-hover.** Fibers gain a burst uniform (`uBurstStart` +
   `uBurstSpeed`); `fibers.burst()` fires an extra pulse from the fiber's
   start, alternating fibers per call; `sim.js` `onImpulse` triggers it, so
   hovering a lecture "transmits" it down a fiber.
5. **Corner labels.** Hero-absolute tiny uppercase labels: top-right
   "Autumn 2026", bottom-right "`N` lectures · `N` seminars" computed from
   `manifest.decks.length` (each lecture has a paired seminar).

QA: existing 3-pass `check-landing.mjs` must stay green; screenshot review
desktop + 390 px.

## B. Video fetch workflow + L15 embeds

**Problem.** Two YouTube iframes in `15_Computing_Infrastructure.md`
(CPU-vs-GPU demo, computer-memory explainer) letterbox instead of
filling the frame — violating the video-fullscreen requirement. YouTube
iframes cannot `object-fit: cover`.

**Workflow.** New `fetch` subcommand in `scripts/videos.py`
(+ `pnpm videos:fetch`):
`videos.py fetch <url> --name <Name[.mp4]> [--profile remux] [--used-in L15]`
1. Downloads via `yt-dlp` into `videos/raw/<Name>.mp4`, preferring H.264
   MP4 ≤1080p (`bv*[ext=mp4][vcodec^=avc1][height<=1080]+ba[ext=m4a]/…`)
   so the default `remux` profile is lossless and fast.
2. Appends a `[[videos]]` manifest entry (profile, used_in, notes with the
   source URL) unless the name already exists.
3. Then the standard pipeline applies: `videos:encode` → `videos:publish`
   (GitHub Release `videos` tag). Encode/publish must tolerate the other
   entries' raws being absent locally (verify before running; add the
   minimal `--only` flag if the current commands can't).

**Tooling:** `yt-dlp` + static `ffmpeg` installed to `~/.local/bin`
(user approved).

**L15 edits (user approved, incl. the third-party re-hosting call):** both
iframe slides become full-screen `<VideoPlayer src="<Name>.mp4" />` slides
following the existing video-slide pattern (component only, no heading —
the player covers the slide). Names: `CPU_vs_GPU_Demo.mp4`,
`How_Computer_Memory_Works.mp4`.

QA: `pnpm qa --only 15-computing-infrastructure` green;
`pnpm videos:check` consistent; videos published BEFORE the site deploy so
the deployed deck can stream them.

## Ship

One deploy at the end covers both: commit, push `ff2026`, deploy
`ff2026:bs2026` (CI builds the decks), verify live.
