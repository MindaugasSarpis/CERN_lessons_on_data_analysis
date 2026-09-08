<script setup>
import { ref, computed, watch, nextTick, onMounted, onUnmounted } from 'vue'
import { useIsSlideActive, useSlideContext } from '@slidev/client'

const REMOTE_BASE = 'https://github.com/MindaugasSarpis/CERN_lessons_on_data_analysis/releases/download/videos'

const props = defineProps({
  src:      { type: String, required: true },
  fallback: { type: String, default: '' },
  // Start playing when the slide becomes active. `false` = wait for the
  // presenter to press play (the clip still preloads so its first frame and
  // the controls are visible).
  autoplay: { type: Boolean, default: true },
  loop:     { type: Boolean, default: false },
  muted:    { type: Boolean, default: false },
  controls: { type: Boolean, default: true },
  // Native controls stay hidden and only appear while the pointer is over the
  // bottom control strip, or for a few seconds after a click/tap on the video.
  // `false` = controls always visible (when `controls` is on).
  autoHideControls: { type: Boolean, default: true },
  hq:       { type: Boolean, default: true },
})

const base = import.meta.env.BASE_URL || '/'
const hqSrc = computed(() => `${base}videos-hq/${props.src}`)
const localSrc = computed(() => `${base}videos/${props.src}`)
const remoteSrc = computed(() => props.fallback || `${REMOTE_BASE}/${props.src}`)

// Source chain, front to back. `pnpm dev` serves the gitignored local copies,
// so prefer them there (fast, offline): the venue-quality HQ copy written by
// `pnpm videos:encode-hq` first, then the web copy, then the release. In the
// deployed build the local dirs are stripped (served from the GitHub release
// instead), so play straight from the release CDN — requesting an absent local
// file first only 404s and delays playback; the local entries stay at the back
// as the offline tier of a `--keep-videos` build. A build made with
// `VITE_VIDEOS_LOCAL_FIRST=1 pnpm build --keep-videos` prefers the kept local
// copies even in PROD — an offline backup that never waits on the venue network.
const preferRemote = import.meta.env.PROD && import.meta.env.VITE_VIDEOS_LOCAL_FIRST !== '1'
const chain = computed(() => {
  const local = props.hq ? [hqSrc.value, localSrc.value] : [localSrc.value]
  const order = preferRemote ? [remoteSrc.value, ...local] : [...local, remoteSrc.value]
  return [...new Set(order)]
})

const videoRef = ref(null)
const sourceRef = ref(null)
const chainIndex = ref(0)
const currentSrc = computed(() => chain.value[chainIndex.value])
const status = ref('idle')
const isActive = useIsSlideActive()
const hasBeenActive = ref(false)

// Only the real slide (and the presenter's main view) gets a <video>. The
// overview / next-slide preview render a static placeholder instead: the
// overview mounts every slide at once, so a video-heavy deck would put ~20
// media elements on a phone, and its copy of the CURRENT slide is "active"
// too, so it re-downloaded the clip being watched.
const { $renderContext } = useSlideContext()
const isLive = computed(() => $renderContext.value === 'slide' || $renderContext.value === 'presenter')

const mimeType = computed(() => {
  const ext = props.src.split('.').pop()?.toLowerCase()
  if (ext === 'webm') return 'video/webm'
  return 'video/mp4'
})

let switching = false
function onError() {
  if (switching || !hasBeenActive.value) return
  // Advance to the next source in the chain; give up when it is exhausted.
  if (chainIndex.value < chain.value.length - 1) {
    switching = true
    status.value = 'loading'
    chainIndex.value += 1
    nextTick(() => {
      videoRef.value?.load()
      switching = false
    })
  } else {
    status.value = 'error'
  }
}

function syncPlayback() {
  const video = videoRef.value
  if (!video) return
  if (isActive.value) {
    // First activation: attach source and start loading
    if (!hasBeenActive.value) {
      hasBeenActive.value = true
      status.value = 'loading'
      nextTick(() => videoRef.value?.load())
    }
    video.currentTime = 0
    if (!props.autoplay) {
      // Manual start: the presenter's click on the controls is the gesture,
      // so it may play with sound straight away.
      video.muted = props.muted
      return
    }
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

// ---- auto-hiding controls -------------------------------------------------
// The native control bar sits along the bottom edge. We toggle the `controls`
// attribute itself (not CSS: the bar's DOM differs per browser), so it is
// simply absent until wanted: pointer inside the bottom strip → shown; pointer
// elsewhere or gone → hidden after a short grace; click/tap on the video →
// shown for a few seconds. When shown, the bar handles its own hit-testing —
// there is no overlay element to steal its clicks. Pointer tracking is done
// on `window`, not the player: Slidev's own navigation bar floats over the
// bottom of the slide and would otherwise swallow the hover.
const CONTROL_STRIP_PX = 72      // the native bar is ~50-60px tall
const HIDE_GRACE_MS = 700        // pointer left the strip
const CLICK_SHOW_MS = 3500       // after a click/tap
const wrapRef = ref(null)
const controlsVisible = ref(false)
const showControls = computed(() => props.controls && (!props.autoHideControls || controlsVisible.value))
let hideTimer = null
function scheduleHide(ms) {
  clearTimeout(hideTimer)
  hideTimer = setTimeout(() => { controlsVisible.value = false }, ms)
}
function reveal(ms) {
  clearTimeout(hideTimer)
  controlsVisible.value = true
  if (ms != null) scheduleHide(ms)
}
function onWindowMove(e) {
  if (!props.autoHideControls || !isActive.value || !wrapRef.value) return
  const r = wrapRef.value.getBoundingClientRect()
  const inside = e.clientX >= r.left && e.clientX <= r.right && e.clientY >= r.top && e.clientY <= r.bottom
  const inStrip = inside && e.clientY >= r.bottom - CONTROL_STRIP_PX
  if (inStrip) reveal()
  else if (controlsVisible.value) scheduleHide(HIDE_GRACE_MS)
}
function onPointerGone() {
  // Pointer left the player (or the window): no further mousemove will come.
  if (props.autoHideControls && controlsVisible.value) scheduleHide(HIDE_GRACE_MS)
}
function onVideoClick(e) {
  if (!props.autoHideControls) return
  const r = e.currentTarget.getBoundingClientRect()
  // A click inside the strip lands on the (now visible) native bar — leave it
  // to the browser. Elsewhere on the picture: reveal for a moment.
  if (e.clientY < r.bottom - CONTROL_STRIP_PX) reveal(CLICK_SHOW_MS)
}
function onVideoTouch() {
  if (props.autoHideControls) reveal(CLICK_SHOW_MS)
}

// ---- keyboard: `p` toggles play/pause on the active slide's player without
// revealing the control bar (Slidev binds space/arrows/o/d/g/f — `p` is free).
function onKey(e) {
  if (!isActive.value || !isLive.value) return
  if (e.key !== 'p' && e.key !== 'P') return
  if (e.metaKey || e.ctrlKey || e.altKey) return
  const t = e.target
  if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.isContentEditable)) return
  const video = videoRef.value
  if (!video) return
  e.preventDefault()
  if (video.paused) {
    video.muted = props.muted
    video.play().catch(() => {})
  } else {
    video.pause()
  }
}

onMounted(() => {
  window.addEventListener('keydown', onKey)
  window.addEventListener('mousemove', onWindowMove, { passive: true })
  document.documentElement.addEventListener('mouseleave', onPointerGone)
  // Source error events don't bubble to <video> on iOS Safari.
  // Attach error listener directly on the <source> DOM element.
  sourceRef.value?.addEventListener('error', onError)
  // The immediate watcher above may fire before refs are populated —
  // re-run once refs exist so the initially-active slide actually loads.
  syncPlayback()
})
onUnmounted(() => {
  window.removeEventListener('keydown', onKey)
  window.removeEventListener('mousemove', onWindowMove)
  document.documentElement.removeEventListener('mouseleave', onPointerGone)
  clearTimeout(hideTimer)
})
</script>

<template>
  <div ref="wrapRef" class="video-player" @mouseleave="onPointerGone">
    <div v-if="!isLive" class="video-placeholder">
      <svg class="video-placeholder-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 4.5v15l12-7.5z" fill="currentColor" /></svg>
      <span class="video-status">{{ src }}</span>
    </div>
    <template v-else>
      <div v-if="status === 'loading' || status === 'idle'" class="video-status">Loading video&hellip;</div>
      <div v-if="status === 'error'" class="video-status video-error">
        Video not available: <code>{{ src }}</code>
      </div>
      <video
        ref="videoRef"
        :loop="loop"
        :controls="showControls"
        muted
        playsinline
        webkit-playsinline
        :preload="autoplay ? 'none' : 'auto'"
        @loadeddata="onLoaded"
        @error="onError"
        @click="onVideoClick"
        @touchstart.passive="onVideoTouch"
        :class="{ 'video-ready': status === 'ready' }"
      >
        <source ref="sourceRef" :src="hasBeenActive ? currentSrc : ''" :type="mimeType" />
      </video>
    </template>
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
  display: block;
  width: 100%;
  height: 100%;
  /* Fill the slide edge-to-edge with no letterbox strip. `contain` left thin
     black bars on clips that weren't exactly 16:9; `cover` fills the frame
     (minimal crop) so video slides are truly full-screen. */
  object-fit: cover;
  /* keep in layout so iOS Safari loads it, but hide visually until ready */
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
.video-placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  color: white;
}
.video-placeholder .video-status {
  position: static;
  padding: 0;
}
.video-placeholder-icon {
  width: 4rem;
  height: 4rem;
  opacity: 0.6;
}
</style>
