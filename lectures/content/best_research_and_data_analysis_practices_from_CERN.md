---
background: /figures/background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false

hideInToc: true

addons:
  - slidev-addon-python-runner
mermaid: true

# Combined "everything" deck: imports all 16 lectures for authoring/preview and
# PDF export. NOT the deployed artifact — GitHub Pages ships one deck per lecture
# (see decks.json + scripts/build-all.mjs). Lazy-mount imported slides so the
# initial load and navigation stay fast despite the size.
defaults:
  preload: false

---

# Dr. Mindaugas Šarpis
# Best Research and Data Analysis Practices from CERN

## All Sixteen Lectures

---
hideInToc: true
---

# **Index of Lectures**

<Toc text-xl minDepth="1" maxDepth="1" columns="2" />

---
src: slides/01_Orientation.md
---

---
src: slides/02_Introduction_to_Data.md
---

---
src: slides/03_How_Computers_Work.md
---

---
src: slides/04_Command_Line_and_Files.md
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

---
src: slides/12_Data_Fitting.md
---

---
src: slides/13_NumPy_and_Pandas.md
---

---
src: slides/14_Reproducible_Workflows.md
---

---
src: slides/15_Computing_Infrastructure.md
---

---
src: slides/16_Machine_Learning_and_AI.md
---
