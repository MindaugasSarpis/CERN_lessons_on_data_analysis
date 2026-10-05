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
// Question text is plain text with optional `code` spans: escape HTML, then
// turn backtick spans into <code> so authors can write `git init` naturally.
const esc = (t) => t.replace(/[&<>]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]))
const questionHtml = computed(() => esc(props.question).replace(/`([^`]+)`/g, '<code>$1</code>'))
</script>

<template>
  <div class="mcq-container">
    <h2 class="mcq-question" v-html="questionHtml"></h2>

    <ul class="mcq-options">
      <li
        v-for="(opt, i) in options"
        :key="i"
        :class="{
          'mcq-li-correct': picked === i && i === correct,
          'mcq-li-wrong': picked === i && i !== correct,
        }"
      >
        <button
          class="mcq-btn"
          :class="{
            'mcq-correct': picked === i && i === correct,
            'mcq-wrong': picked === i && i !== correct,
          }"
          @click="picked = i"
        >
          <span class="mcq-idx">{{ String.fromCharCode(65 + i) }}</span>
          <span class="mcq-text" v-html="opt"></span>
          <!-- '×' and '→' are in Space Grotesk; '✓'/'✗' fall back to a
               system font that may have no glyph (blank on Linux Chromium). -->
          <span class="mcq-arrow" aria-hidden="true">{{
            picked === i && i !== correct ? '×' : '→'
          }}</span>
        </button>
      </li>
    </ul>

    <!-- Feedback always occupies layout space (invisible until answered):
         revealing it must never grow the slide, so the static overflow gate
         measures the true worst-case height of every MCQ slide. -->
    <div class="mcq-feedback" :class="{ 'mcq-pending': picked === null }">
      <p class="mcq-result" :class="isCorrect ? 'mcq-correct-text' : 'mcq-wrong-text'">
        {{ picked === null || isCorrect ? 'Correct' : 'Try again' }}
      </p>
      <div v-if="explanation" class="mcq-explanation">
        {{ explanation }}
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Same idiom as the landing's lecture rows (landing/src/style.css .rows):
   hairline rows, a dim tabular index that turns accent, the text nudging
   6px right and an accent arrow fading in on hover. */
.mcq-container {
  display: flex;
  flex-direction: column;
  /* Top-aligned at a fixed offset: centring made the question jump between
     quiz slides (a long explanation, reserved before an answer is picked,
     pushed it up). Same place on every quiz slide, like a content title. */
  justify-content: flex-start;
  padding-top: 2.2rem;
  height: 100%;
  gap: 0.9rem;
}

.mcq-question {
  font-family: var(--font-sans);
  font-size: 1.3em;
  font-weight: 500;
  letter-spacing: -0.015em;
  line-height: 1.3;
  color: var(--fg);
  margin: 0;
}

.mcq-options {
  list-style: none;
  padding: 0;
  margin: 0;
}

.mcq-options li {
  margin: 0;
  padding: 0;
  border-top: 1px solid var(--hair);
  transition: border-color 0.35s var(--ease);
}
.mcq-options li::before { content: none; }
.mcq-options li:last-child { border-bottom: 1px solid var(--hair); }

/* A picked row gets a tinted hairline above and below (its own top line and
   the next row's top line), never a fill. */
.mcq-options li.mcq-li-correct,
.mcq-options li.mcq-li-correct + li {
  border-top-color: color-mix(in srgb, var(--ok) 55%, transparent);
}
.mcq-options li.mcq-li-correct:last-child {
  border-bottom-color: color-mix(in srgb, var(--ok) 55%, transparent);
}
.mcq-options li.mcq-li-wrong,
.mcq-options li.mcq-li-wrong + li {
  border-top-color: color-mix(in srgb, var(--warn) 55%, transparent);
}
.mcq-options li.mcq-li-wrong:last-child {
  border-bottom-color: color-mix(in srgb, var(--warn) 55%, transparent);
}

.mcq-btn {
  width: 100%;
  display: grid;
  grid-template-columns: 2ch 1fr auto;
  align-items: baseline;
  gap: 1.1rem;
  text-align: left;
  padding: 0.7rem 0.2rem;
  margin: 0;
  background: none;
  border: none;
  border-radius: 0;
  color: var(--fg);
  font-family: var(--font-sans);
  font-size: 0.95em;
  line-height: 1.35;
  cursor: pointer;
}
.mcq-btn:focus { outline: none; }
.mcq-btn:focus-visible { outline: 1px solid var(--hair-strong); outline-offset: 2px; }

.mcq-idx {
  font-variant-numeric: tabular-nums;
  font-weight: 500;
  color: var(--dim);
  transition: color 0.35s var(--ease);
}

.mcq-text {
  display: block;
  min-width: 0;
  opacity: 0.86;
  transition: opacity 0.35s var(--ease), transform 0.35s var(--ease), color 0.35s var(--ease);
}

.mcq-arrow {
  color: var(--accent);
  opacity: 0;
  transform: translateX(-14px);
  transition: opacity 0.35s var(--ease), transform 0.35s var(--ease);
}

.mcq-btn:hover .mcq-text,
.mcq-btn:focus-visible .mcq-text { opacity: 1; transform: translateX(6px); }
.mcq-btn:hover .mcq-idx,
.mcq-btn:focus-visible .mcq-idx { color: var(--accent); }
.mcq-btn:hover .mcq-arrow,
.mcq-btn:focus-visible .mcq-arrow { opacity: 1; transform: translateX(0); }

/* Picked: index, text and mark take the semantic colour (no fill). */
.mcq-correct .mcq-idx,
.mcq-correct .mcq-text,
.mcq-correct .mcq-arrow,
.mcq-correct:hover .mcq-idx,
.mcq-correct:hover .mcq-arrow { color: var(--ok); }
.mcq-wrong .mcq-idx,
.mcq-wrong .mcq-text,
.mcq-wrong .mcq-arrow,
.mcq-wrong:hover .mcq-idx,
.mcq-wrong:hover .mcq-arrow { color: var(--warn); }
.mcq-correct .mcq-text,
.mcq-wrong .mcq-text { opacity: 1; }
.mcq-correct .mcq-arrow,
.mcq-wrong .mcq-arrow { opacity: 1; transform: translateX(0); }

.mcq-feedback {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  transition: opacity 0.35s var(--ease);
}

.mcq-pending {
  visibility: hidden; /* keeps layout height, unlike v-if */
  opacity: 0;
}

.mcq-result {
  font-size: 0.85em;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  margin: 0;
}

.mcq-correct-text { color: var(--ok); }
.mcq-wrong-text { color: var(--warn); }

.mcq-explanation {
  color: var(--fg-2);
  font-size: 0.85em;
  line-height: 1.5;
}

@media (prefers-reduced-motion: reduce) {
  .mcq-options li,
  .mcq-idx,
  .mcq-text,
  .mcq-arrow,
  .mcq-feedback { transition: none !important; }
  .mcq-btn:hover .mcq-text,
  .mcq-btn:focus-visible .mcq-text { transform: none; }
}
</style>
