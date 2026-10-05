<template>
  <!-- A quotation set like the landing hero's sub-text: large sentence-case
       Grotesk, the **bold** word at full weight, the attribution as a tracked
       label under a hairline. -->
  <div class="slidev-layout quote quote-hero">
    <div class="my-auto quote-inner">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.quote-hero { padding-left: 4rem; padding-right: 5rem; }
.quote-inner { max-width: 46rem; }
.quote-hero :deep(h1) {
  font-size: 2rem;
  font-weight: 400;
  line-height: 1.25;
  letter-spacing: -0.015em;
  color: var(--fg-2);
  text-wrap: pretty;
}
.quote-hero :deep(h1 strong) {
  color: var(--fg);
  font-weight: 700;
}
.quote-hero :deep(h1::before) {
  content: "“";
  display: block;
  font-size: 3.2rem;
  line-height: 0.6;
  height: 0.55em;
  color: var(--accent);
}
.quote-hero :deep(h1 + p) {
  margin-top: 1.6rem;
  padding-top: 0.9rem;
  border-top: 1px solid var(--hair);
  max-width: 28rem;
  font-size: 0.68rem;
  font-weight: 500;
  color: var(--dim);
  opacity: 1;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  line-height: 1.8;
}
.quote-hero :deep(h1 + p em) { font-style: normal; color: var(--fg-2); }
</style>
