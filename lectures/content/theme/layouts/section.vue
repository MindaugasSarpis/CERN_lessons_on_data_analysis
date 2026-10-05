<script setup lang="ts">
import { computed, ref, onMounted } from 'vue'
import { useSlideContext } from '@slidev/client'

// "Section 03": this section's place among the deck's section slides.
const { $slidev, $page } = useSlideContext()
const label = computed(() => {
  try {
    const slides = $slidev.nav.slides as any[]
    const n = slides.filter((r) =>
      r.no <= $page.value && r.meta?.slide?.frontmatter?.layout === 'section').length
    return n > 0 ? `Section ${String(n).padStart(2, '0')}` : 'Section'
  } catch { return 'Section' }
})
const mounted = ref(false)
onMounted(() => {
  requestAnimationFrame(() => requestAnimationFrame(() => { mounted.value = true }))
})
</script>

<template>
  <!-- The landing's block head, at slide scale: a small accent kicker, a large
       title, and a hairline that draws in from the left. Left-aligned. -->
  <div class="slidev-layout section section-hero" :class="{ 'is-mounted': mounted }">
    <div class="section-inner">
      <div class="section-kicker" aria-hidden="true">{{ label }}</div>
      <div class="section-body">
        <slot />
      </div>
      <div class="section-rule"></div>
    </div>
  </div>
</template>

<style scoped>
.section-hero {
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100%;
  padding-left: 4rem;
  padding-right: 4rem;
}
/* Slide sources sometimes put `text-center` on a section; the system is
   left-aligned like the landing. */
.section-inner { text-align: left; }

.section-kicker {
  font-size: 0.7rem;
  font-weight: 500;
  color: var(--accent);
  text-transform: uppercase;
  letter-spacing: 0.12em;
  margin-bottom: 1rem;
  opacity: 0;
  transition: opacity 0.8s var(--ease) 0.05s;
}
.section-body {
  opacity: 0;
  transform: translateY(26px);
  transition: opacity 0.8s var(--ease) 0.1s, transform 0.8s var(--ease) 0.1s;
}
.section-rule {
  margin-top: 1.4rem;
  height: 1px;
  width: 100%;
  background: linear-gradient(90deg, var(--hair-strong), var(--hair) 70%, transparent);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 1.1s var(--ease) 0.25s;
}
.is-mounted .section-kicker { opacity: 1; }
.is-mounted .section-body { opacity: 1; transform: none; }
.is-mounted .section-rule { transform: scaleX(1); }

.section-hero :deep(h1) {
  margin: 0;
  color: var(--fg);
  text-wrap: balance;
}
.section-hero :deep(h1 strong) {
  color: var(--accent);
  font-weight: 700;
}
.section-hero .section-body :deep(p) {
  margin-top: 1rem;
  color: var(--fg-2);
  opacity: 1;
  font-size: 1.1rem;
}

@media (prefers-reduced-motion: reduce) {
  .section-kicker, .section-body, .section-rule { transition: none; }
}
</style>
