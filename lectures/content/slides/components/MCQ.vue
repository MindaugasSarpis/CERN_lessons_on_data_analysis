<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  question: { type: String, required: true },
  options:  { type: Array,  required: true },   // array of strings
  correct:  { type: Number, required: true },   // 0-based index
  explanation: { type: String, default: '' },
})

const picked = ref(null)
const isCorrect = computed(() => picked.value === props.correct)
</script>

<template>
  <div class="space-y-4">
    <h2 class="text-xl font-bold">{{ question }}</h2>

    <ul class="space-y-2">
      <li v-for="(opt, i) in options" :key="i">
        <button
          class="w-full text-left px-4 py-2 rounded border hover:shadow transition"
          :class="[
            picked === i && i === correct ? 'border-green-500 ring-1 ring-green-500' : '',
            picked === i && i !== correct ? 'border-red-500 ring-1 ring-red-500' : ''
          ]"
          @click="picked = i"
        >
          <span class="mr-2">
            <span v-if="picked === i && i === correct">✅</span>
            <span v-else-if="picked === i && i !== correct">❌</span>
            <span v-else>⬜️</span>
          </span>
          <span v-html="opt"></span>
        </button>
      </li>
    </ul>

    <div v-if="picked !== null" class="mt-2">
      <p v-if="isCorrect" class="font-semibold">Correct! 🎉</p>
      <p v-else>Try again.</p>
    </div>

    <details v-if="explanation" class="mt-2">
      <summary class="cursor-pointer">Explanation</summary>
      <div class="mt-1 whitespace-pre-wrap">{{ explanation }}</div>
    </details>
  </div>
</template>

<style scoped>
button { background: var(--slidev-theme-background); }
</style>
