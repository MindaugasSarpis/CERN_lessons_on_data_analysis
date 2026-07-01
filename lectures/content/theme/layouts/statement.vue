<template>
  <div class="slidev-layout statement statement-kinetic">
    <div class="my-auto">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.statement-kinetic :deep(h1) {
  font-family: var(--font-display);
  background: linear-gradient(100deg, var(--accent-amber), var(--accent-cyan));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  filter: drop-shadow(0 0 26px rgba(251, 191, 36, 0.20));
}
.statement-kinetic :deep(h1 strong) { -webkit-text-fill-color: transparent; }
</style>
