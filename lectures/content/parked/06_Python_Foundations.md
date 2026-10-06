<!--
Parked slides from slides/06_Python_Foundations.md, taken out on 2026-10-06.

They left the deck when it was reworked to open on the handed-out script
scripts/clean_pendulum.py (run in Seminar 4) and to read its clean() line by
line, so that the deck stays inside the 105-145 min band. The format-on-save
part of "The Editor Does the Typing" is now one sentence on the PEP 8 slide;
the notebook paragraph and the links of "Read More" are on the workbook page
lecture_6.md. This file is not in decks.json: it is not built, not gated and
not deployed. A comment before each slide says where it stood. To restore
one, move it back into the lecture file.
-->

<!-- Parked 2026-10-06 from Lecture 06, slide 4, between 'Learning Objectives' and the section 'Running Python': replaced by the opening slide 'The Script from Seminar 4' -->

---
hideInToc: true
---

# Why **Python**

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🔬 **At CERN**

At ATLAS, CMS, ALICE and LHCb the analysis is written in Python: selecting candidates, filling histograms, fitting, plotting. The libraries underneath are C++. Python is the layer that people type.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🗺️ **Other languages**

R for statistics. C++, Julia and Rust for speed. SQL for databases. Values, types, loops and functions exist in each of them under another spelling. What is learned here carries over.

</div>

<div class="card card-warning card-glass pad-compact">

## 🖱️ **A calculation by clicking**

A spreadsheet shows the result and not the steps. Nobody can see which cells were dragged, and the work cannot be run again on a new file.

</div>

<div class="card card-success card-glass pad-compact">

## 📄 **A calculation as a script**

A script is a text file that states every step. It runs again with one command, gives the same result on Windows, macOS and Linux, and goes into Git next to the README.

</div>

</div>

<!--
Speaker: the reason for a language is the bottom row. A script is the record
of the calculation, in the same way as the README is the record of the data.
Python is free and open source. (~2 min)
-->


<!-- Parked 2026-10-06 from Lecture 06, section 'Code That Can Be Read', after 'PEP 8: One Style for Everyone': format on save moved into the PEP 8 slide -->

---
hideInToc: true
---

# The Editor Does the **Typing**

<div class="grid-3 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## ⌨️ **Completion**

Type `per` and a list offers `period_s`. `Tab` accepts it. `Ctrl+Space` opens the list at any time.

A name that was completed is not misspelled.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧩 **Snippets**

A short word that expands into lines you often type. Command Palette, **Snippets: Configure Snippets**, then `python`.

Example: `hdr` for the first comment lines of a script.

</div>

<div class="card card-accent card-glass pad-compact">

## 🧹 **Format on save**

Install the extension **Black Formatter**. **Format Document** is `Shift+Alt+F` (macOS `Shift+Option+F`).

The setting **Editor: Format On Save** runs it at every save.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

⚙️ A formatter rewrites the layout of the file to PEP 8: spaces, quotes, line length. It does not change what the script does, and it does not choose names.

</div>

<!--
Speaker: show the formatter on a line typed without spaces, x=9.02/10. It
becomes x = 9.02 / 10 at the save. (~2 min)
-->



<!-- Parked 2026-10-06 from Lecture 06, section 'Code That Can Be Read', after 'The Editor Does the Typing', before the Recap: the notebook paragraph moved to lecture_6.md -->

---
hideInToc: true
---

# Script or **Notebook**

<div class="grid-2 gap-md mt-md">

<div class="card card-success card-glass pad-compact">

## 📜 **Script**, a `.py` file

- Plain text, run from top to bottom
- The same order at every run, so the same result
- Git shows what changed, line by line
- One command runs it: `python scripts/periods.py`

</div>

<div class="card card-primary card-glass pad-compact">

## 📓 **Notebook**, an `.ipynb` file

- Cells of code with their output and plots below each
- Cells can be run in any order, and the names of every earlier run stay
- A result may depend on a cell that was changed or deleted since
- Suited to trying things out

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

This course writes scripts. A notebook is trusted once it gives the same output after **Restart** and **Run All**. That test is what a script passes every time it runs.

</div>

<!--
Speaker: some of the room know Jupyter. Nothing is wrong with it for a first
look at data. Work that someone has to run again goes into a script. (~2 min)
-->



<!-- Parked 2026-10-06 from Lecture 06, between the Recap and the section 'Check Yourself': the links moved to lecture_6.md -->

---
hideInToc: true
---

# Read **More**

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 📖 **Python**

- [The Python Tutorial](https://docs.python.org/3/tutorial/), chapters 3 to 5: numbers, strings, lists, `if`, `for`, dictionaries
- [Built-in Functions](https://docs.python.org/3/library/functions.html): the full list, one paragraph each
- [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [PEP 8](https://peps.python.org/pep-0008/), the style guide

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧰 **VS Code**

- [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
- [Python debugging in VS Code](https://code.visualstudio.com/docs/python/debugging)
- [Snippets in VS Code](https://code.visualstudio.com/docs/editing/userdefinedsnippets)

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

All of these are free. At the prompt, `help(round)` prints the description of a function, and `help(str)` lists every string method.

</div>

<!--
Speaker: the official tutorial covers everything of today in about an hour of
reading. (~1 min)
-->

