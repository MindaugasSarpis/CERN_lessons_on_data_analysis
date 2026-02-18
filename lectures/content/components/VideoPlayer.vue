<script setup>
import { ref, computed, watch, onMounted, onBeforeUnmount } from 'vue'
import { useIsSlideActive } from '@slidev/client'

const REMOTE_BASE = 'https://github.com/MindaugasSarpis/CERN_lessons_on_data_analysis/releases/download/videos'

const props = defineProps({
  src:      { type: String, required: true },
  fallback: { type: String, default: '' },
  autoplay: { type: Boolean, default: false },
  loop:     { type: Boolean, default: false },
  muted:    { type: Boolean, default: false },
  controls: { type: Boolean, default: true },
})

const localSrc = computed(() => `/videos/${props.src}`)
const remoteSrc = computed(() => props.fallback || `${REMOTE_BASE}/${props.src}`)

const videoRef = ref(null)
const currentSrc = ref(localSrc.value)
const status = ref('loading')
const isActive = useIsSlideActive()
const isLocal = computed(() => currentSrc.value === localSrc.value)

function onError() {
  if (currentSrc.value === localSrc.value) {
    currentSrc.value = remoteSrc.value
    status.value = 'loading'
  } else {
    status.value = 'error'
  }
}

function syncPlayback() {
  const video = videoRef.value
  if (!video) return
  if (isActive.value) {
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

watch(isActive, syncPlayback)

function onLoaded() {
  status.value = 'ready'
  syncPlayback()
}
</script>

<template>
  <div class="video-player">
    <div v-if="status === 'loading'" class="video-status">Loading video&hellip;</div>
    <div v-if="status === 'error'" class="video-status video-error">
      Video not available: <code>{{ src }}</code>
    </div>
    <video
      ref="videoRef"
      :key="currentSrc"
      :src="currentSrc"
      :loop="loop"
      :controls="controls"
      muted
      playsinline
      webkit-playsinline
      :preload="isLocal ? 'auto' : 'metadata'"
      @loadeddata="onLoaded"
      @error="onError"
      v-show="status === 'ready'"
    />
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
}
.video-status {
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
