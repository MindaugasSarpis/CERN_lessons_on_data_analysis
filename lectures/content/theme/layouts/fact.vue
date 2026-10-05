<template>
  <div class="slidev-layout fact fact-hero">
    <div class="my-auto">
      <slot />
    </div>
  </div>
</template>

<style scoped>
/* A giant white figure, the keyword in the accent, a tracked caption below. */
.fact-hero :deep(h1) { color: var(--fg); }
.fact-hero :deep(h1 strong),
.fact-hero :deep(h2 strong) { color: var(--accent); }
.fact-hero :deep(h1 + p) { color: var(--fg-2); }
.fact-hero :deep(p + p) {
  color: var(--dim);
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
}
</style>
