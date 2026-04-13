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
# Data Analysis and Artificial Intelligence

## Index of Lectures

---
hideInToc: true
---

# **Index of Lectures**

<Toc text-xl minDepth="1" maxDepth="1" columns="2" />


---
src: slides/L01_Course_Orientation.md
---

---
src: slides/L02_Introduction_to_CERN.md
---

---
src: slides/L03_1_1_Crash_Course_on_Computer_Science.md
---

---
src: slides/L03_1_2_File_Handling_and_Directory_Structure.md
---

---
src: slides/L03_2_Command_Line.md
---

---
src: slides/L03_3_Markdown.md
---

---
src: slides/L03_4_VS_Code.md
---

---
src: slides/L08_Version_Control.md
---

---
src: slides/L05_Crash_Course_on_Python_Programming.md
---

---
src: slides/L06_Concepts_of_Data_Analysis.md
---