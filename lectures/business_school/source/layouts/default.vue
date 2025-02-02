<script>
export default {
}
</script>
<template>
  <div class="slidev-layout default">
    <slot/>
  </div>
</template>
<style lang="postcss">
.slidev-layout.default {
  background-image: url('images/default_background.svg');
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center center;
}
</style>