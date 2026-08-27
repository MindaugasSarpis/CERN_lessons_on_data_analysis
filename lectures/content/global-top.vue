<!--
  Persistent in-deck navigation overlay, rendered on every slide of every deck.
  - ⌂ links back to the course landing page (one level up from the deck's base).
  - ☰ opens a menu of all lectures (fetched from <base>/lectures.json, which is
    generated from decks.json by scripts/gen-entries.mjs). Decks flagged
    `draft` are listed greyed and unlinked — they are not deployed yet.
  The outer container is pointer-events:none so it never blocks slide content
  (MCQ buttons, live-code editors); only the controls themselves are clickable.
-->
<script setup>
import { ref, computed, onMounted } from 'vue'

const base = import.meta.env.BASE_URL || '/'
// The landing lives one path segment above the deck base: /repo/<slug>/ -> /repo/
const home = base.replace(/[^/]+\/$/, '') || '/'
const current = (base.match(/([^/]+)\/$/) || [, ''])[1]

const open = ref(false)
const data = ref({ blocks: {}, decks: [] })

onMounted(async () => {
  try {
    const res = await fetch(base + 'lectures.json')
    if (res.ok) data.value = await res.json()
  } catch (e) {
    /* menu stays empty — the Home link still works */
  }
})

const grouped = computed(() => {
  const out = []
  for (const d of data.value.decks) {
    let g = out.find((x) => x.block === d.block)
    if (!g) {
      g = { block: d.block, label: data.value.blocks?.[d.block] || d.block, items: [] }
      out.push(g)
    }
    g.items.push(d)
  }
  return out
})
</script>

<template>
  <div class="deck-nav" :class="{ 'is-open': open }">
    <a :href="home" class="deck-nav-btn" title="Course home" aria-label="Course home">⌂</a>
    <button
      class="deck-nav-btn"
      :class="{ active: open }"
      :aria-expanded="open"
      title="All lectures"
      aria-label="All lectures"
      @click="open = !open"
    >☰</button>

    <transition name="dn-fade">
      <div v-if="open" class="deck-nav-panel">
        <a :href="home" class="dn-home">← Course home</a>
        <template v-for="g in grouped" :key="g.block">
          <div class="dn-block">{{ g.block }} · {{ g.label }}</div>
          <component
            :is="d.draft ? 'span' : 'a'"
            v-for="d in g.items"
            :key="d.slug"
            :href="d.draft ? undefined : home + d.slug + '/'"
            class="dn-item"
            :class="{ current: d.slug === current, soon: d.draft }"
          >
            <span class="dn-n">{{ String(d.n).padStart(2, '0') }}</span>
            <span class="dn-t">{{ d.title }}</span>
            <span v-if="d.draft" class="dn-soon">coming soon</span>
            <span v-else-if="d.optional" class="dn-opt">optional</span>
          </component>
        </template>
      </div>
    </transition>
  </div>
</template>

<style scoped>
.deck-nav {
  position: fixed;
  top: 0.55rem;
  right: 0.6rem;
  z-index: 90;
  display: flex;
  gap: 0.35rem;
  align-items: flex-start;
  pointer-events: none; /* clicks fall through to the slide */
  font-family: 'Inter', system-ui, sans-serif;
}
.deck-nav-btn {
  pointer-events: auto;
  width: 1.9rem;
  height: 1.9rem;
  border-radius: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1rem;
  line-height: 1;
  text-decoration: none;
  color: #cfe3ff;
  background: rgba(15, 31, 61, 0.5);
  border: 1px solid rgba(125, 211, 252, 0.28);
  backdrop-filter: blur(6px);
  opacity: 0.5;
  transition: opacity 0.18s, background 0.18s;
  cursor: pointer;
}
.deck-nav-btn:hover,
.deck-nav-btn.active {
  opacity: 1;
  background: rgba(37, 99, 235, 0.55);
}

.deck-nav-panel {
  pointer-events: auto;
  position: absolute;
  top: 2.4rem;
  right: 0;
  width: 20rem;
  max-height: 78vh;
  overflow-y: auto;
  padding: 0.5rem;
  border-radius: 0.7rem;
  background: rgba(9, 17, 33, 0.94);
  border: 1px solid rgba(125, 211, 252, 0.25);
  backdrop-filter: blur(10px);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.5);
}
.dn-home {
  display: block;
  color: #7dd3fc;
  text-decoration: none;
  font-size: 0.8rem;
  padding: 0.3rem 0.5rem 0.45rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  margin-bottom: 0.25rem;
}
.dn-home:hover {
  color: #eef4ff;
}
.dn-block {
  font-size: 0.62rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #93b7dd;
  opacity: 0.8;
  padding: 0.5rem 0.5rem 0.2rem;
}
.dn-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.32rem 0.5rem;
  border-radius: 0.4rem;
  text-decoration: none;
  color: #dbe7f5;
  font-size: 0.82rem;
}
.dn-item:hover {
  background: rgba(37, 99, 235, 0.35);
  color: #fff;
}
.dn-item.current {
  background: rgba(56, 189, 248, 0.2);
  color: #eef4ff;
}
.dn-item.soon {
  cursor: default;
}
.dn-item.soon:hover {
  background: none;
  color: #dbe7f5;
}
.dn-item.soon .dn-n,
.dn-item.soon .dn-t {
  opacity: 0.4;
}
.dn-soon {
  font-size: 0.6rem;
  color: #93b7dd;
  opacity: 0.7;
}
.dn-n {
  font-variant-numeric: tabular-nums;
  color: #7dd3fc;
  font-size: 0.72rem;
  min-width: 1.4rem;
}
.dn-t {
  flex: 1;
}
.dn-opt {
  font-size: 0.6rem;
  color: #fcd34d;
  opacity: 0.85;
}

.dn-fade-enter-active,
.dn-fade-leave-active {
  transition: opacity 0.15s, transform 0.15s;
}
.dn-fade-enter-from,
.dn-fade-leave-to {
  opacity: 0;
  transform: translateY(-4px);
}

@media print {
  .deck-nav {
    display: none !important;
  }
}
</style>
