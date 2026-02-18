<script setup>
import { ref, computed } from 'vue'

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

const currentSrc = ref(localSrc.value)
const status = ref('loading')

function onLoaded() {
  status.value = 'ready'
}

function onError() {
  if (currentSrc.value === localSrc.value) {
    currentSrc.value = remoteSrc.value
    status.value = 'loading'
  } else {
    status.value = 'error'
  }
}
</script>

<template>
  <div class="video-player">
    <div v-if="status === 'loading'" class="video-status">Loading video&hellip;</div>
    <div v-if="status === 'error'" class="video-status video-error">
      Video not available: <code>{{ src }}</code>
    </div>
    <video
      :key="currentSrc"
      :src="currentSrc"
      :autoplay="autoplay"
      :loop="loop"
      :muted="muted"
      :controls="controls"
      preload="auto"
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
