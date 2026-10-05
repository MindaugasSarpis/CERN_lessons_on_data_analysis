<template>
  <div class="slidev-layout statement statement-hero">
    <div class="my-auto">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.statement-hero :deep(h1) { color: var(--fg); text-wrap: balance; }
.statement-hero :deep(h1 strong) { color: var(--accent); }
</style>
