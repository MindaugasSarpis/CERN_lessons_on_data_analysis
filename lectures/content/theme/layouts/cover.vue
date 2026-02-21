<script setup lang="ts">
import { computed, ref, onMounted } from 'vue'
import { handleBackground } from '../layoutHelper'

const props = defineProps({
  background: {
    default: '/figures/background_intro.jpg',
  },
})

const style = computed(() => handleBackground(props.background, true))
const mounted = ref(false)

onMounted(() => {
  // Stagger the entrance animation
  setTimeout(() => { mounted.value = true }, 100)
})
</script>

<template>
  <div class="slidev-layout cover-animated" :style="style">
    <!-- Animated background shapes -->
    <div class="bg-shapes">
      <div class="shape shape-1"></div>
      <div class="shape shape-2"></div>
      <div class="shape shape-3"></div>
      <div class="shape shape-4"></div>
      <div class="shape shape-5"></div>
      <div class="shape shape-6"></div>
      <div class="shape shape-7"></div>
    </div>

    <!-- Gradient mesh overlay -->
    <div class="gradient-mesh"></div>

    <!-- Grid lines (subtle) -->
    <div class="grid-lines">
      <div class="grid-line grid-line-h1"></div>
      <div class="grid-line grid-line-h2"></div>
      <div class="grid-line grid-line-v1"></div>
      <div class="grid-line grid-line-v2"></div>
    </div>

    <!-- Main content -->
    <div class="cover-content" :class="{ 'is-mounted': mounted }">
      <!-- Decorative accent bar -->
      <div class="accent-bar"></div>

      <div class="content-inner">
        <slot />
      </div>

      <!-- Bottom decorative element -->
      <div class="bottom-decoration">
        <div class="pulse-dot"></div>
        <div class="line-decoration"></div>
        <div class="pulse-dot"></div>
      </div>
    </div>

    <!-- Corner accents -->
    <div class="corner-accent corner-tl"></div>
    <div class="corner-accent corner-br"></div>
  </div>
</template>

<style scoped>
/* === Color Palette === */
:root {
  --cover-cream: #F5F0EB;
  --cover-sage: #93B1B5;
  --cover-teal: #4A8B8B;
  --cover-slate: #2C4A5A;
  --cover-dark: #1B1B2F;
}

.cover-animated {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
  display: grid;
  place-items: center;
  background: linear-gradient(135deg, #1B1B2F 0%, #2C4A5A 40%, #1B1B2F 100%);
}

/* === Floating Geometric Shapes === */
.bg-shapes {
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 1;
}

.shape {
  position: absolute;
  border-radius: 50%;
  opacity: 0;
  animation: floatIn 1s ease-out forwards;
}

.shape-1 {
  width: 300px;
  height: 300px;
  top: -80px;
  right: -60px;
  background: radial-gradient(circle at 30% 30%, rgba(74, 139, 139, 0.35), rgba(44, 74, 90, 0.1));
  border: 1px solid rgba(147, 177, 181, 0.15);
  animation-delay: 0.2s;
  animation-duration: 1.2s;
}

.shape-1::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  animation: pulse-glow 4s ease-in-out infinite;
  background: radial-gradient(circle, rgba(74, 139, 139, 0.2), transparent 70%);
}

.shape-2 {
  width: 200px;
  height: 200px;
  bottom: -40px;
  left: -40px;
  background: radial-gradient(circle at 60% 60%, rgba(147, 177, 181, 0.25), rgba(27, 27, 47, 0.1));
  border: 1px solid rgba(147, 177, 181, 0.12);
  animation-delay: 0.4s;
}

.shape-3 {
  width: 120px;
  height: 120px;
  top: 20%;
  left: 8%;
  background: rgba(74, 139, 139, 0.12);
  border: 1px solid rgba(74, 139, 139, 0.2);
  border-radius: 24px;
  transform: rotate(45deg);
  animation-delay: 0.6s;
  animation-name: floatInRotate;
}

.shape-4 {
  width: 80px;
  height: 80px;
  top: 15%;
  right: 15%;
  background: rgba(245, 240, 235, 0.06);
  border: 1px solid rgba(245, 240, 235, 0.1);
  border-radius: 16px;
  animation-delay: 0.8s;
  animation-name: floatInRotate;
}

.shape-5 {
  width: 60px;
  height: 60px;
  bottom: 25%;
  right: 10%;
  background: radial-gradient(circle, rgba(147, 177, 181, 0.2), transparent);
  animation-delay: 0.5s;
}

.shape-6 {
  width: 160px;
  height: 160px;
  top: 50%;
  right: 25%;
  background: rgba(44, 74, 90, 0.15);
  border: 1px solid rgba(74, 139, 139, 0.1);
  animation-delay: 0.7s;
}

.shape-7 {
  width: 40px;
  height: 40px;
  bottom: 15%;
  left: 20%;
  background: rgba(74, 139, 139, 0.25);
  border: 1px solid rgba(74, 139, 139, 0.3);
  border-radius: 10px;
  animation-delay: 0.9s;
  animation-name: floatInRotate;
}

/* Continuous floating animation after shapes appear */
.shape-1 { animation: floatIn 1.2s ease-out forwards, float-slow 8s ease-in-out 1.4s infinite; }
.shape-2 { animation: floatIn 1s ease-out 0.4s forwards, float-slow 10s ease-in-out 1.6s infinite reverse; }
.shape-3 { animation: floatInRotate 1s ease-out 0.6s forwards, float-rotate 12s ease-in-out 1.8s infinite; }
.shape-4 { animation: floatInRotate 1s ease-out 0.8s forwards, float-rotate 9s ease-in-out 2s infinite reverse; }
.shape-5 { animation: floatIn 1s ease-out 0.5s forwards, float-slow 7s ease-in-out 1.7s infinite; }
.shape-6 { animation: floatIn 1s ease-out 0.7s forwards, float-slow 11s ease-in-out 1.9s infinite reverse; }
.shape-7 { animation: floatInRotate 1s ease-out 0.9s forwards, float-rotate 8s ease-in-out 2.1s infinite; }

/* === Gradient Mesh Overlay === */
.gradient-mesh {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(ellipse at 20% 50%, rgba(74, 139, 139, 0.15) 0%, transparent 50%),
    radial-gradient(ellipse at 80% 20%, rgba(147, 177, 181, 0.1) 0%, transparent 40%),
    radial-gradient(ellipse at 60% 80%, rgba(44, 74, 90, 0.2) 0%, transparent 50%);
  z-index: 2;
  pointer-events: none;
}

/* === Subtle Grid Lines === */
.grid-lines {
  position: absolute;
  inset: 0;
  z-index: 2;
  pointer-events: none;
  opacity: 0;
  animation: fadeIn 2s ease-out 1s forwards;
}

.grid-line {
  position: absolute;
  background: rgba(147, 177, 181, 0.06);
}

.grid-line-h1 { top: 30%; left: 0; right: 0; height: 1px; }
.grid-line-h2 { top: 70%; left: 0; right: 0; height: 1px; }
.grid-line-v1 { left: 25%; top: 0; bottom: 0; width: 1px; }
.grid-line-v2 { left: 75%; top: 0; bottom: 0; width: 1px; }

/* === Main Content === */
.cover-content {
  position: relative;
  z-index: 10;
  text-align: center;
  padding: 2rem;
  max-width: 85%;
  opacity: 0;
  transform: translateY(30px);
  transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}

.cover-content.is-mounted {
  opacity: 1;
  transform: translateY(0);
}

/* Glassmorphism card behind content */
.content-inner {
  position: relative;
  padding: 2.5rem 3rem;
  background: rgba(27, 27, 47, 0.45);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-radius: 24px;
  border: 1px solid rgba(147, 177, 181, 0.15);
  box-shadow:
    0 25px 60px rgba(0, 0, 0, 0.3),
    inset 0 1px 0 rgba(245, 240, 235, 0.05);
  transition: border-color 0.4s ease, box-shadow 0.4s ease;
}

.content-inner:hover {
  border-color: rgba(147, 177, 181, 0.3);
  box-shadow:
    0 30px 80px rgba(0, 0, 0, 0.4),
    inset 0 1px 0 rgba(245, 240, 235, 0.08),
    0 0 40px rgba(74, 139, 139, 0.1);
}

/* Inner glow */
.content-inner::before {
  content: '';
  position: absolute;
  top: 0;
  left: 10%;
  right: 10%;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(147, 177, 181, 0.4), transparent);
}

/* === Accent Bar === */
.accent-bar {
  width: 60px;
  height: 4px;
  margin: 0 auto 1.5rem;
  border-radius: 2px;
  background: linear-gradient(90deg, #4A8B8B, #93B1B5);
  opacity: 0;
  transform: scaleX(0);
  animation: scaleIn 0.6s cubic-bezier(0.16, 1, 0.3, 1) 0.8s forwards;
}

/* === Bottom Decoration === */
.bottom-decoration {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  margin-top: 1.5rem;
  opacity: 0;
  animation: fadeIn 0.8s ease-out 1.2s forwards;
}

.pulse-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #4A8B8B;
  animation: pulse 2s ease-in-out infinite;
}

.line-decoration {
  width: 40px;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(147, 177, 181, 0.5), transparent);
}

/* === Corner Accents === */
.corner-accent {
  position: absolute;
  width: 80px;
  height: 80px;
  z-index: 3;
  pointer-events: none;
  opacity: 0;
  animation: fadeIn 1s ease-out 1.5s forwards;
}

.corner-tl {
  top: 20px;
  left: 20px;
  border-top: 2px solid rgba(74, 139, 139, 0.3);
  border-left: 2px solid rgba(74, 139, 139, 0.3);
  border-radius: 4px 0 0 0;
}

.corner-br {
  bottom: 20px;
  right: 20px;
  border-bottom: 2px solid rgba(74, 139, 139, 0.3);
  border-right: 2px solid rgba(74, 139, 139, 0.3);
  border-radius: 0 0 4px 0;
}

/* === Typography overrides for cover === */
.cover-animated :deep(h1) {
  color: #F5F0EB !important;
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.2;
  text-shadow: 0 2px 20px rgba(0, 0, 0, 0.3);
  opacity: 0;
  transform: translateY(20px);
  animation: slideUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) 0.4s forwards;
}

.cover-animated :deep(h1:first-of-type) {
  animation-delay: 0.4s;
}

.cover-animated :deep(h1:nth-of-type(2)) {
  animation-delay: 0.6s;
}

.cover-animated :deep(h2) {
  color: #93B1B5 !important;
  font-weight: 500;
  letter-spacing: 0.02em;
  opacity: 0;
  transform: translateY(20px);
  animation: slideUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) 0.8s forwards;
  position: relative;
  display: inline-block;
}

.cover-animated :deep(h2::after) {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 50%;
  transform: translateX(-50%);
  width: 0;
  height: 2px;
  background: linear-gradient(90deg, #4A8B8B, #93B1B5);
  border-radius: 1px;
  animation: expandLine 0.6s cubic-bezier(0.16, 1, 0.3, 1) 1.2s forwards;
}

.cover-animated :deep(p) {
  color: rgba(245, 240, 235, 0.7);
  opacity: 0;
  animation: fadeIn 0.8s ease-out 1s forwards;
}

/* === Keyframe Animations === */
@keyframes floatIn {
  from {
    opacity: 0;
    transform: scale(0.5) translateY(40px);
  }
  to {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}

@keyframes floatInRotate {
  from {
    opacity: 0;
    transform: rotate(45deg) scale(0.5);
  }
  to {
    opacity: 1;
    transform: rotate(45deg) scale(1);
  }
}

@keyframes float-slow {
  0%, 100% { transform: translate(0, 0); }
  25% { transform: translate(10px, -15px); }
  50% { transform: translate(-5px, 10px); }
  75% { transform: translate(8px, 5px); }
}

@keyframes float-rotate {
  0%, 100% { transform: rotate(45deg) translate(0, 0); }
  25% { transform: rotate(50deg) translate(5px, -8px); }
  50% { transform: rotate(42deg) translate(-3px, 6px); }
  75% { transform: rotate(48deg) translate(4px, 3px); }
}

@keyframes pulse-glow {
  0%, 100% { opacity: 0.3; }
  50% { opacity: 0.6; }
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scaleX(0);
  }
  to {
    opacity: 1;
    transform: scaleX(1);
  }
}

@keyframes expandLine {
  from { width: 0; }
  to { width: 80%; }
}

@keyframes pulse {
  0%, 100% { opacity: 0.5; transform: scale(1); }
  50% { opacity: 1; transform: scale(1.3); }
}
</style>
