<script setup lang="ts">
import { computed, ref, onMounted } from 'vue'
import { useSlideContext } from '@slidev/client'
import manifest from '../../decks.json'

// The cover is the landing hero carried into the deck: same black, same type,
// same staggered line-in, same corner labels. Every lecture cover has the same
// markdown (author #, course #, lecture ##, aims badge #####), and this layout
// re-casts it — the lecture title becomes the hero, the course title a small
// link home. Spec: docs/superpowers/specs/2026-10-05-decks-match-landing-design.md

const { $slidev } = useSlideContext()
const coverRoot = ref<HTMLElement | null>(null)
const mounted = ref(false)

// "LECTURE 02 · BLOCK A" from the manifest, matched on the deck title (set by
// gen-entries.mjs from decks.json, so it works in dev and build). The combined
// authoring deck has its own title → no match → no label.
const deckLabel = computed(() => {
  const title = $slidev?.configs?.title
  const i = manifest.decks.findIndex((d: { title: string }) => d.title === title)
  if (i < 0) return ''
  const d = manifest.decks[i]
  const n = String(i + 1).padStart(2, '0')
  return `Lecture ${n} · Block ${d.block}`
})
// Same text as the landing's top-right corner (scripts/gen-landing.mjs).
const term = 'Autumn 2026'

onMounted(() => {
  const el = coverRoot.value
  if (!el) return
  const reduce = window.matchMedia?.('(prefers-reduced-motion: reduce)').matches

  // Split the hero title into words, each in a clipping wrapper, so they rise
  // in one after another like the landing title's lines.
  const hero = el.querySelector<HTMLElement>('.cover-content h2')
  if (hero && !hero.dataset.split) {
    hero.dataset.split = '1'
    const words = (hero.textContent || '').trim().split(/\s+/)
    hero.textContent = ''
    words.forEach((w, i) => {
      const wrap = document.createElement('span')
      wrap.className = 'w-wrap'
      const inner = document.createElement('span')
      inner.className = 'w'
      inner.style.setProperty('--i', String(i))
      inner.textContent = w
      wrap.appendChild(inner)
      hero.appendChild(wrap)
      if (i < words.length - 1) hero.appendChild(document.createTextNode(' '))
    })
  }
  if (reduce) mounted.value = true
  else requestAnimationFrame(() => requestAnimationFrame(() => { mounted.value = true }))

  // The course title links back to the landing page (one path segment up from
  // the deck base), for every deck without editing each cover's markdown.
  const home = (import.meta.env.BASE_URL || '/').replace(/[^/]+\/$/, '') || '/'
  const h1s = Array.from(el.querySelectorAll<HTMLElement>('.cover-content h1'))
  const title = h1s.find((h) => /Best Research and Data Analysis/i.test(h.textContent || ''))
  if (title && !title.dataset.homeLink) {
    title.dataset.homeLink = '1'
    title.classList.add('cover-home-link')
    title.setAttribute('role', 'link')
    title.setAttribute('tabindex', '0')
    title.setAttribute('title', 'Course home')
    const go = () => { window.location.href = home }
    title.addEventListener('click', go)
    title.addEventListener('keydown', (e: KeyboardEvent) => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); go() }
    })
  }
})
</script>

<template>
  <div class="slidev-layout cover cover-root" :class="{ 'is-mounted': mounted }" ref="coverRoot">
    <div class="corner corner-tr" aria-hidden="true">{{ term }}</div>
    <div v-if="deckLabel" class="corner corner-br" aria-hidden="true">{{ deckLabel }}</div>

    <div class="cover-content">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.cover-root {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 2.4rem 4rem;
}

/* Corner labels — the landing's .corner */
.corner {
  position: absolute;
  right: 4rem;
  color: var(--dim);
  font-size: 0.62rem;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  opacity: 0;
  transition: opacity 1s var(--ease) 0.9s;
}
.corner-tr { top: 2.2rem; }
.corner-br { bottom: 2.2rem; }
.is-mounted .corner { opacity: 1; }

/* Re-cast the cover markdown into the hero order with flex `order`:
   author kicker → course link → hero lecture title → aims badge → rest. */
.cover-content {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  max-width: 88%;
}

/* # Dr. … — the landing's kicker */
.cover-root :deep(.cover-content h1:first-child) {
  order: 1;
  font-size: 0.7rem;
  font-weight: 500;
  color: var(--accent);
  text-transform: uppercase;
  letter-spacing: 0.12em;
  line-height: 1.4;
  margin: 0 0 0.35rem;
}

/* # Best Research … — small, dim, links home */
.cover-root :deep(.cover-content h1:not(:first-child)) {
  order: 2;
  font-size: 0.7rem;
  font-weight: 500;
  color: var(--dim);
  text-transform: uppercase;
  letter-spacing: 0.12em;
  line-height: 1.4;
  margin: 0 0 1.6rem;
}
.cover-root :deep(.cover-home-link) {
  cursor: pointer;
  width: fit-content;
  border-bottom: 1px solid transparent;
  transition: color 0.35s var(--ease), border-color 0.35s var(--ease);
}
.cover-root :deep(.cover-home-link:hover),
.cover-root :deep(.cover-home-link:focus-visible) {
  color: var(--accent);
  border-bottom-color: var(--accent);
  outline: none;
}

/* ## Lecture title — the hero */
.cover-root :deep(.cover-content h2) {
  order: 3;
  margin: 0;
  font-size: 3.7rem;
  font-weight: 700;
  line-height: 0.98;
  letter-spacing: -0.02em;
  text-transform: uppercase;
  color: var(--fg);
  text-wrap: balance;
}
.cover-root :deep(.w-wrap) {
  display: inline-block;
  overflow: hidden;
  vertical-align: top;
  /* Room for descender-free caps; the clip must not cut accents (Š). */
  padding-top: 0.06em;
  margin-top: -0.06em;
}
.cover-root :deep(.w) {
  display: inline-block;
  transform: translateY(112%);
  transition: transform 0.9s var(--ease);
  transition-delay: calc(0.15s + var(--i) * 0.09s);
}
.cover-root.is-mounted :deep(.w) { transform: translateY(0); }

/* ##### aims badge (and any extra line such as L08's "Inspired by") */
.cover-root :deep(.cover-content h3),
.cover-root :deep(.cover-content h5),
.cover-root :deep(.cover-content p) {
  order: 4;
  margin: 1.8rem 0 0;
  font-size: 0.7rem;
  font-weight: 500;
  color: var(--dim);
  letter-spacing: 0.08em;
  opacity: 0;
  transition: opacity 1s var(--ease) 0.7s;
}
.cover-root :deep(.cover-content h5 + h5) { margin-top: 0.6rem; }
.cover-root.is-mounted :deep(.cover-content h3),
.cover-root.is-mounted :deep(.cover-content h5),
.cover-root.is-mounted :deep(.cover-content p) { opacity: 1; }

@media (prefers-reduced-motion: reduce) {
  .corner,
  .cover-root :deep(.w),
  .cover-root :deep(.cover-content h3),
  .cover-root :deep(.cover-content h5),
  .cover-root :deep(.cover-content p) { transition: none; }
}
</style>
