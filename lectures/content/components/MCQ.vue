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
  <div class="mcq-container">
    <h2 class="mcq-question">{{ question }}</h2>

    <ul class="mcq-options">
      <li v-for="(opt, i) in options" :key="i">
        <button
          class="mcq-btn"
          :class="{
            'mcq-correct': picked === i && i === correct,
            'mcq-wrong': picked === i && i !== correct,
          }"
          @click="picked = i"
        >
          <span class="mcq-icon">
            <span v-if="picked === i && i === correct">✅</span>
            <span v-else-if="picked === i && i !== correct">❌</span>
            <span v-else>⬜️</span>
          </span>
          <span v-html="opt"></span>
        </button>
      </li>
    </ul>

    <div v-if="picked !== null" class="mcq-result">
      <p v-if="isCorrect" class="mcq-correct-text">Correct! 🎉</p>
      <p v-else class="mcq-wrong-text">Try again.</p>
    </div>

    <div v-if="explanation && picked !== null" class="mcq-explanation">
      {{ explanation }}
    </div>
  </div>
</template>

<style scoped>
.mcq-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100%;
  gap: 1rem;
}

.mcq-question {
  font-size: 1.3em;
  font-weight: 700;
  line-height: 1.3;
}

.mcq-options {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.mcq-btn {
  width: 100%;
  text-align: left;
  padding: 0.8rem 1.2rem;
  border-radius: 12px;
  background: rgba(2, 6, 23, 0.85);
  border: none;
  border-left: 5px solid rgba(148, 163, 184, 0.35);
  color: #e2e8f0;
  font-size: 0.95em;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: transform 0.3s ease, border-color 0.3s ease;
  -webkit-mask-image: linear-gradient(to right, black 60%, transparent 100%);
  mask-image: linear-gradient(to right, black 60%, transparent 100%);
}

.mcq-btn::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: radial-gradient(circle at 20% 0%, rgba(255, 255, 255, 0.3), transparent 55%);
  opacity: 0.15;
  pointer-events: none;
}

.mcq-btn:hover {
  transform: translateX(4px);
  border-left-color: rgba(148, 163, 184, 0.6);
}

.mcq-correct {
  border-left-color: var(--color-success-light) !important;
  background: rgba(16, 185, 129, 0.2);
}

.mcq-wrong {
  border-left-color: var(--color-warning-light) !important;
  background: rgba(245, 158, 11, 0.2);
}

.mcq-icon {
  margin-right: 0.5rem;
}

.mcq-result {
  font-weight: 600;
  font-size: 1.1em;
}

.mcq-correct-text { color: var(--color-success-light); }
.mcq-wrong-text { color: var(--color-warning-light); }

.mcq-explanation {
  padding: 0.8rem 1.2rem;
  border-radius: 12px;
  background: rgba(2, 6, 23, 0.7);
  border-left: 5px solid var(--color-info-light, rgba(125, 211, 252, 0.45));
  font-size: 0.85em;
  opacity: 0.9;
  -webkit-mask-image: linear-gradient(to right, black 60%, transparent 100%);
  mask-image: linear-gradient(to right, black 60%, transparent 100%);
}
</style>
