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

// Paired seminar page in the published workbook. The pairing comes from
// decks.json (`seminar` in lectures.json), not from the slug number: Lecture 1
// has no seminar and Lecture 2 is taught with Seminar 1.
const seminarNo = computed(() => data.value.decks.find((d) => d.slug === current)?.seminar ?? null)
const seminarHref = computed(() =>
  seminarNo.value
    ? `${home}workbook/seminars/seminar_${String(seminarNo.value).padStart(2, '0')}/`
    : '',
)

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
    <a :href="home" class="deck-nav-btn" title="Course home" aria-label="Course home">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 11.5 12 5l8 6.5M6.5 9.8V19h11V9.8" /></svg>
    </a>
    <button
      class="deck-nav-btn"
      :class="{ active: open }"
      :aria-expanded="open"
      title="All lectures"
      aria-label="All lectures"
      @click="open = !open"
    >
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 7.5h14M5 12h14M5 16.5h14" /></svg>
    </button>

    <transition name="dn-fade">
      <div v-if="open" class="deck-nav-panel">
        <div class="dn-links">
          <a :href="home" class="dn-link">← Course home</a>
          <a v-if="seminarHref" :href="seminarHref" class="dn-link">Seminar {{ seminarNo }} brief →</a>
        </div>
        <template v-for="g in grouped" :key="g.block">
          <div class="dn-block"><span class="dn-key">Block {{ g.block }}</span><span>{{ g.label }}</span></div>
          <component
            :is="d.draft ? 'span' : 'a'"
            v-for="d in g.items"
            :key="d.slug"
            :href="d.draft ? undefined : home + d.slug + '/'"
            class="dn-item"
            :class="{ current: d.slug === current, soon: d.draft, opt: d.optional }"
            :aria-current="d.slug === current ? 'page' : undefined"
          >
            <span class="dn-n">{{ String(d.n).padStart(2, '0') }}</span>
            <span class="dn-t">{{ d.title }}</span>
            <span v-if="d.draft" class="dn-tag">coming soon</span>
            <span v-else-if="d.optional" class="dn-tag">optional</span>
            <span v-else class="dn-arrow" aria-hidden="true">&#8594;</span>
          </component>
        </template>
      </div>
    </transition>
  </div>
</template>

<style scoped>
/* Styled as the landing page's lecture list (landing/src/style.css):
   hairlines, one accent, uppercase tracked labels, row hover = title nudge +
   accent number + arrow. Tokens come from theme/styles/tokens.css. */
.deck-nav {
  position: fixed;
  top: 0.55rem;
  right: 0.6rem;
  z-index: 90;
  display: flex;
  gap: 0.35rem;
  align-items: flex-start;
  pointer-events: none; /* clicks fall through to the slide */
  font-family: var(--font-sans);
}
.deck-nav-btn {
  pointer-events: auto;
  width: 1.9rem;
  height: 1.9rem;
  padding: 0;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  color: var(--fg-2);
  background: transparent;
  border: 1px solid var(--hair-strong);
  opacity: 0.55;
  cursor: pointer;
  transition: opacity 0.35s var(--ease), color 0.35s var(--ease), border-color 0.35s var(--ease);
}
.deck-nav-btn svg {
  width: 1rem;
  height: 1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.5;
  stroke-linecap: square;
}
.deck-nav-btn:hover,
.deck-nav-btn:focus-visible,
.deck-nav-btn.active {
  opacity: 1;
  color: var(--accent);
  border-color: var(--accent);
  outline: none;
}

.deck-nav-panel {
  pointer-events: auto;
  position: absolute;
  top: 2.4rem;
  right: 0;
  width: 21rem;
  max-height: 78vh;
  overflow-y: auto;
  padding: 0.35rem 0.9rem 0.6rem;
  border-radius: 6px;
  background: rgba(5, 5, 7, 0.97);
  border: 1px solid var(--hair-strong);
  scrollbar-width: thin;
  scrollbar-color: var(--hair-strong) transparent;
}
.dn-links {
  display: flex;
  justify-content: space-between;
  gap: 0.5rem;
  padding: 0.45rem 0 0.15rem;
}
.dn-link,
.dn-block,
.dn-tag {
  text-transform: uppercase;
  letter-spacing: 0.12em;
}
.dn-link {
  font-size: 0.6rem;
  font-weight: 700;
  color: var(--dim);
  text-decoration: none;
  border-bottom: 1px solid transparent;
  transition: color 0.35s var(--ease), border-color 0.35s var(--ease);
}
.dn-link:hover,
.dn-link:focus-visible {
  color: var(--accent);
  border-bottom-color: var(--accent);
  outline: none;
}
.dn-block {
  display: flex;
  gap: 0.7rem;
  align-items: baseline;
  font-size: 0.62rem;
  font-weight: 500;
  color: var(--dim);
  padding: 0.95rem 0 0.45rem;
}
.dn-key {
  color: var(--accent);
  white-space: nowrap;
}
.dn-item {
  display: grid;
  grid-template-columns: 1.6rem 1fr auto;
  align-items: baseline;
  gap: 0.6rem;
  padding: 0.42rem 0.1rem;
  border-top: 1px solid var(--hair);
  text-decoration: none;
  color: var(--fg);
}
.dn-block + .dn-item {
  border-top-color: var(--hair-strong);
}
.dn-n {
  font-variant-numeric: tabular-nums;
  color: var(--dim);
  font-size: 0.72rem;
  transition: color 0.35s var(--ease);
}
.dn-t {
  font-size: 0.82rem;
  font-weight: 500;
  line-height: 1.25;
  opacity: 0.86;
  transition: opacity 0.35s var(--ease), transform 0.35s var(--ease), color 0.35s var(--ease);
}
.dn-arrow {
  color: var(--accent);
  font-size: 0.82rem;
  opacity: 0;
  transform: translateX(-8px);
  transition: opacity 0.35s var(--ease), transform 0.35s var(--ease);
}
a.dn-item:hover .dn-t,
a.dn-item:focus-visible .dn-t {
  opacity: 1;
  transform: translateX(6px);
}
a.dn-item:hover .dn-n,
a.dn-item:focus-visible .dn-n {
  color: var(--accent);
}
a.dn-item:hover .dn-arrow,
a.dn-item:focus-visible .dn-arrow {
  opacity: 1;
  transform: translateX(0);
}
a.dn-item:focus-visible {
  outline: none;
}
a.dn-item.opt .dn-t {
  opacity: 0.62;
}
.dn-item.current .dn-n,
.dn-item.current .dn-t {
  color: var(--accent);
  opacity: 1;
}
.dn-item.soon {
  cursor: default;
}
.dn-item.soon .dn-t,
.dn-item.soon .dn-n {
  opacity: 0.35;
}
.dn-tag {
  font-size: 0.5rem;
  font-weight: 700;
  color: var(--dim);
  border: 1px solid var(--hair);
  border-radius: 999px;
  padding: 0.12rem 0.45rem;
  align-self: center;
  white-space: nowrap;
}

.dn-fade-enter-active,
.dn-fade-leave-active {
  transition: opacity 0.35s var(--ease), transform 0.35s var(--ease);
}
.dn-fade-enter-from,
.dn-fade-leave-to {
  opacity: 0;
  transform: translateY(-4px);
}

@media (prefers-reduced-motion: reduce) {
  .deck-nav-btn,
  .dn-link,
  .dn-n,
  .dn-t,
  .dn-arrow,
  .dn-fade-enter-active,
  .dn-fade-leave-active {
    transition: none !important;
  }
  a.dn-item:hover .dn-t,
  a.dn-item:focus-visible .dn-t {
    transform: none;
  }
}

@media print {
  .deck-nav {
    display: none !important;
  }
}
</style>

<style>
/* Slidev's own chrome (bottom-left nav bar, its pop-up menus, the `g` goto
   dialog) on the course tokens: near-black, hairline border, no shadow or
   blur, accent on hover. Not scoped: these elements belong to @slidev/client. */
#slide-container nav > div,
#slidev-goto-dialog > div,
#slidev-goto-dialog .autocomplete-list {
  background: rgba(5, 5, 7, 0.94) !important;
  border: 1px solid var(--hair-strong) !important;
  border-radius: 4px !important;
  box-shadow: none !important;
  backdrop-filter: none !important;
  color: var(--fg-2);
  font-family: var(--font-sans);
}
#slide-container nav .slidev-icon-btn {
  border-radius: 4px;
  transition: opacity 0.35s var(--ease), color 0.35s var(--ease);
}
#slide-container nav .slidev-icon-btn:hover,
#slide-container nav .slidev-icon-btn.active {
  color: var(--accent);
  background: transparent;
}
#slide-container nav .slidev-icon-btn:focus-visible {
  outline-color: var(--accent);
}
#slide-container nav > div > .px2 {
  font-variant-numeric: tabular-nums;
}
#slide-container nav > div > .px2 > span:first-child {
  color: var(--fg);
}
#slidev-goto-dialog input {
  color: var(--fg);
  font-family: var(--font-sans);
}
#slidev-goto-dialog .autocomplete-list li {
  border-color: var(--hair) !important;
}
#slidev-goto-dialog .autocomplete-list li.bg-active {
  color: var(--accent);
  background: transparent;
}
@media (prefers-reduced-motion: reduce) {
  #slide-container nav .slidev-icon-btn {
    transition: none;
  }
}
</style>
