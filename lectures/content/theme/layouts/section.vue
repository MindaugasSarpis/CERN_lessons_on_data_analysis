<script setup lang="ts">
import { ref, onMounted } from 'vue'

const mounted = ref(false)
onMounted(() => { setTimeout(() => { mounted.value = true }, 50) })
</script>

<template>
  <div class="slidev-layout section section-kinetic">
    <!-- animated colour-shifting backdrop (class from animations.css) -->
    <div class="aurora"></div>

    <div class="section-inner my-auto text-center">
      <div class="section-body" :class="{ 'is-mounted': mounted }">
        <slot />
      </div>
      <div class="section-accent" :class="{ 'is-mounted': mounted }"></div>
    </div>
  </div>
</template>

<style scoped>
.section-kinetic {
  position: relative;
  overflow: hidden;
  display: grid;
}
.section-inner {
  position: relative;
  z-index: 2;
}
.section-body {
  opacity: 0;
  transform: translateY(18px);
  transition: opacity 0.7s ease-out 0.1s,
              transform 0.7s cubic-bezier(0.16, 1, 0.3, 1) 0.1s;
}
.section-body.is-mounted {
  opacity: 1;
  transform: none;
}
.section-accent {
  margin: 1.2rem auto 0;
  width: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent, #38bdf8, #ffffff, #38bdf8, transparent);
  transition: width 0.9s cubic-bezier(0.16, 1, 0.3, 1) 0.3s;
}
.section-accent.is-mounted {
  width: min(48%, 520px);
}

/* Crisp white heading; the **bold** keyword picks up a clean blue accent. */
.section-kinetic :deep(h1) {
  font-family: var(--font-display);
  font-weight: 600;
  color: #eef4ff;
  -webkit-text-fill-color: currentColor;
  background: none;
}
.section-kinetic :deep(h1 strong) {
  color: #7dd3fc;
  -webkit-text-fill-color: currentColor;
  font-weight: 800;
}

@media (prefers-reduced-motion: reduce) {
  .section-body { transition: none; opacity: 1; transform: none; }
  .section-accent { transition: none; width: min(48%, 520px); }
}
</style>
