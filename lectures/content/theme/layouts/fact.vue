<template>
  <div class="slidev-layout fact fact-kinetic">
    <div class="my-auto">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.fact-kinetic :deep(h1) {
  font-family: var(--font-display);
  background: linear-gradient(100deg, var(--accent-cyan), var(--accent-violet));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  filter: drop-shadow(0 0 30px rgba(34, 211, 238, 0.25));
}
.fact-kinetic :deep(h1 strong) { -webkit-text-fill-color: transparent; }
</style>
