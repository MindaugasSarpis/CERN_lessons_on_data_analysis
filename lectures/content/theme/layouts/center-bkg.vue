<template>
  <div class="slidev-layout center-bkg h-full grid place-content-center" :style="backgroundStyle">
    <slot />
  </div>
</template>

<script>
// A centred slide. With an explicit `background:` image it shows that image;
// otherwise it sits on the course backdrop like every other slide.
export default {
  props: {
    background: {
      type: String,
      default: '',
    },
  },
  computed: {
    backgroundStyle() {
      if (!this.background) return {}
      return {
        backgroundImage: `url('${this.background}')`,
        backgroundRepeat: 'no-repeat',
        backgroundSize: 'cover',
        backgroundPosition: 'center',
      }
    },
  },
}
</script>
