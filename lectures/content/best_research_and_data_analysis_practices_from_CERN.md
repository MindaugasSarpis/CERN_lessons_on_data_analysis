---
theme: ./theme
colorSchema: dark
class: text-left
hideInToc: true
addons:
  - slidev-addon-python-runner

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
src: slides/05_Python_Foundations.md
---

---
src: slides/06_Version_Control.md
---

---
src: slides/07_Data_Visualisation.md
---

---
src: slides/08_Data_Quality_and_Uncertainty.md
---

---
src: slides/09_Parameter_Estimation_and_Fitting.md
---

---
src: slides/10_Classification_and_the_Perceptron.md
---

---
src: slides/11_From_Neurons_to_Language_Models.md
---

---
src: slides/12_Code_That_Lasts.md
---


---
src: slides/14_Concepts_of_Data_Analysis.md
---

---
src: slides/15_Computing_Infrastructure.md
---

---
src: slides/16_Machine_Learning_and_AI.md
---
