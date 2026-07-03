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

# Lazy-mount imported slides: don't eagerly build all 248 Vue components
# up front. First visit to a given slide has a small mount cost; initial
# load and steady-state navigation are much faster.
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
src: slides/01_Orientation.md
---

---
src: slides/02_Introduction_to_CERN.md
---

---
src: slides/04_Command_Line_and_Files.md
---

---
src: slides/03_How_Computers_Work.md
---

---
---

---
---

---
src: slides/05_Markdown_and_VS_Code.md
---

---
src: slides/06_Version_Control.md
---

---
src: slides/07_Python_Foundations.md
---

---
src: slides/08_Python_for_Data.md
---

---
src: slides/09_Concepts_of_Data_Analysis.md
---

---
src: slides/10_Data_Visualisation.md
---

---
src: slides/11_Probability_and_Statistics.md
---
