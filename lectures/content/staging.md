---
background: /figures/background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false

transition: fade
hideInToc: true

addons:
  - slidev-addon-python-runner
mermaid: true

# Lazy-mount imported slides — matters even more here since staging.md pulls
# in every lecture. Big initial-load win; tiny mount cost on first visit.
defaults:
  preload: false

---

# Dr. Mindaugas Šarpis
# Best Research and Data Analysis Practices from CERN

## Index of Lectures

---
hideInToc: true
---

# **Index of Lectures**

<Toc text-xl minDepth="1" maxDepth="1" columns="2" />

---
src: slides/10_Data_Visualisation.md
---
