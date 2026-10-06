<!--
Parked slides from slides/13_Reproducible_Workflows.md, taken out on 2026-10-06.

The lecture now opens on "Delete results/. Now what?", adds a table of g by
method after "One Parameter, Two Results", and shows every shell line in zsh
and in PowerShell. To stay inside the timing band, the slides below were
taken out. A comment before each slide says where it stood. To restore one,
move it back into the lecture file. This file is not in decks.json: it is not
built, not gated and not deployed.
-->

<!-- Parked 2026-10-06 from Lecture 13, section A Script with a Command Line, between 'g by Method' (after 'One Parameter, Two Results') and 'Results as Data': a Mermaid detour inside the command-line thread; its one diff line is in the speaker note of 'Four Commands, in Order' -->

---
hideInToc: true
---

# A Diagram Git Can **Compare**

<div class="grid-2 mt-md gap-md" style="grid-template-columns: 3fr 2fr;">

<div class="card card-primary card-glass pad-compact">

## ➕ **`config.json` joins the diagram in the README**

```diff
git diff
--- a/README.md
+++ b/README.md
@@ -10,6 +10,7 @@ flowchart LR
     clean --> table[processed/pendulum.csv]
     table --> plot([plot.py]) --> png[pendulum_plot.png]
     table --> fit([fit.py]) --> json[fit.json]
+    config[config.json] --> fit
     table --> report([report.py])
     png --> report
     json --> report
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔍 **One arrow, one line**

- The change can be read in the diff, reviewed and undone, like a change of code
- A picture exported from a drawing program changes as a whole. Git can only say that the file differs
- The diagram is changed in the same commit as the script it describes

</div>

</div>

<div class="note-text mt-sm">The output of <code>git diff</code> is shown without its first two lines.</div>

<!--
Speaker: this is the reason for writing diagrams as text. The picture has a
history, and the history is readable. (~1 min)
-->


<!-- Parked 2026-10-06 from Lecture 13, section Beyond One Laptop, between 'Continuous Integration' and 'Docker: the Operating System Too': a tool named and asserted, on the skip list; the checks of form it runs are not part of rebuilding the analysis -->

---
hideInToc: true
---

# **pre-commit**: Checks Before a Commit

<div class="card card-primary card-glass pad-compact mt-sm">

## 🚫 **A commit that is refused**

```text
git add data/raw/D0_KPi.csv
git commit -m "Add the LHCb file"
check for added large files..............................................Failed
- hook id: check-added-large-files
- exit code: 1

data/raw/D0_KPi.csv (3835 KB) exceeds 500 KB.

fix end of files.........................................................Passed
trim trailing whitespace.................................................Passed
```

</div>

<div class="grid-2 mt-sm gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🔍 **What it is**

A program, installed with `pip install pre-commit`, that runs small checks each time `git commit` is typed. The checks are listed in `.pre-commit-config.yaml`. If one fails, the commit does not happen.

</div>

<div class="card card-info card-glass pad-compact">

## 🎯 **What it is for**

Mistakes that are cheap to catch and tedious to undo: a data file of 3.9 MB in the history, spaces at line ends. It checks the form of what is committed. It does not run the analysis.

</div>

</div>

<!--
Speaker: the three checks shown are from the standard set that comes with the
tool. A file that got into the Git history stays there, in every copy, so the
first check pays for itself on the first day. (~2 min)
-->

