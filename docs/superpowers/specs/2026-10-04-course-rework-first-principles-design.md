# Course rework: delivery order, first principles, one standard

Date: 2026-10-04. Approved by the lecturer in conversation ("yes, the order is
right"). This file is the working brief for reworking lectures 04–16, their
seminar pages and their workbook pages.

## 1. What the lecturer asked for

In his words, over one day:

- "I want to start from the very basics (like we have) but then rigorously
  build a perceptron, explain data fitting from first principles and similar
  things."
- "Some of the content was generated with simple LLM, don't hesitate to expand,
  restructure, add new things."
- "It's not bad to have too much material and not complete everything it would
  be worse if we run out of material along the way."
- "The in-line quizes I just skip through, maybe they could be at the end of
  the lecture for self-reflection... but yes fill it up with content. But good
  coherent content as in textbook."
- On Lecture 02 as delivered: "a bit dry and sloppy".
- "We will need fewer iterations later in the course": get each lecture right
  now, so that later weeks need small fixes only.

## 2. The order

Thirteen sessions in 2026, Tuesdays, 90 min lecture + 90 min seminar. The decks
are numbered in delivery order.

| # | Date | Lecture | Block | Seminar page |
|--|--|--|--|--|
| 01 | 8 Sep | Orientation & Motivation | A | none |
| 02 | 29 Sep | Introduction to Data | A | seminar_01 |
| 03 | 6 Oct | How Computers Work | A | seminar_03 |
| 04 | 13 Oct | Command Line & File Handling | A | seminar_04 |
| 05 | 20 Oct | Version Control with Git | A | seminar_05 |
| 06 | 27 Oct | Python Foundations | B | seminar_06 |
| 07 | 3 Nov | Python for Data & NumPy | B | seminar_07 |
| 08 | 10 Nov | Data Visualisation | C | seminar_08 |
| 09 | 17 Nov | Probability & Statistics | C | seminar_09 |
| 10 | 1 Dec | Data Fitting from First Principles | C | seminar_10 |
| 11 | 8 Dec | The Perceptron | C | seminar_11 |
| 12 | 15 Dec | Pandas & Data Cleaning | D | seminar_12 |
| 13 | 22 Dec | Reproducible Workflows & Automation | D | seminar_13 |
| 14 | extra | Concepts of Data Analysis | E | seminar_14 |
| 15 | extra | Computing Infrastructure & HPC | E | seminar_15 |
| 16 | extra | Machine Learning & AI | E | seminar_16 |

Lectures 01–03 are delivered and live. 04–16 are drafts. Block E is material
for when there is time; it is not scheduled.

The former Lecture 05 "Markdown & VS Code" is dissolved: week 2 now teaches
Markdown, the project folder and text editing. Its file is
`lectures/content/parked/05_Markdown_and_VS_Code.md`.

Git commit `3a27c06` is the state before the renumbering. Old paths can be read
from it, for example
`git show 3a27c06:lectures/content/slides/13_NumPy_and_Pandas.md`.

| Old file (in 3a27c06) | Now |
|--|--|
| `slides/05_Markdown_and_VS_Code.md` | parked; parts go to 04, 05, 06, 13 |
| `slides/06_Version_Control.md` | `slides/05_Version_Control.md` |
| `slides/07_Python_Foundations.md` | `slides/06_Python_Foundations.md` |
| `slides/08_Python_for_Data.md` | `slides/07_Python_for_Data_and_NumPy.md` |
| `slides/09_Concepts_of_Data_Analysis.md` | `slides/14_Concepts_of_Data_Analysis.md` |
| `slides/10_Data_Visualisation.md` | `slides/08_Data_Visualisation.md` |
| `slides/11_Probability_and_Statistics.md` | `slides/09_Probability_and_Statistics.md` |
| `slides/12_Data_Fitting.md` | `slides/10_Data_Fitting.md` |
| `slides/13_NumPy_and_Pandas.md` | `slides/12_Pandas_and_Data_Cleaning.md` (NumPy half goes to 07) |
| `slides/14_Reproducible_Workflows.md` | `slides/13_Reproducible_Workflows.md` |
| `slides/16_Machine_Learning_and_AI.md` | stays 16; its perceptron core goes to the new 11 |
| `seminars/seminar_05.md` (write the README) | removed; its content belongs to seminar_04 |
| `seminars/seminar_06…08` | `seminar_05…07` |
| `seminars/seminar_09` (data-quality audit) | `seminar_14`; its core also serves seminar_12 |
| `seminars/seminar_10…12` | `seminar_08…10` |
| `seminars/seminar_13…14` | `seminar_12…13` |

## 3. What the room knows, week by week

A lecture or seminar may use only what was taught before it, plus what it
teaches itself. The audience starts from zero. Many have used only Excel. Some
program. Laptops are Windows and macOS, a few Linux.

| After | The room has | Not yet |
|--|--|--|
| 02 + S1 | VS Code, Command Palette, the project folder (`data/raw`, `data/processed`, `scripts`, `results`, `README.md`), file names, Markdown, find and replace, multiple cursors, CSV as text, provenance in the README | terminal, Python, Git |
| 03 + S3 | bits, bytes, hex, integers and floats, encodings, file sizes; the VS Code terminal with `pwd`, `ls`, `cd`; the Hex Editor extension. Python and Git are installed at home and checked once with `python --version` | any other command, running programs |
| 04 + S4 | the shell: files and folders, pipes, `grep` and regular expressions, a first shell script, checksums, backups, paths; running a handed-out Python script | writing Python, Git |
| 05 + S5 | Git locally and with a remote, from the Source Control view and typed | Python |
| 06 + S6 | Python: values, types, control flow, lists, dicts, strings, tracebacks, scripts | functions as tools, NumPy |
| 07 + S7 | functions, files, `csv`, NumPy arrays, masks, vectorised arithmetic, `np.loadtxt` | plotting |
| 08 + S8 | Matplotlib, the grammar of a figure, histograms, error bars | statistics |
| 09 + S9 | probability, distributions, mean and variance, standard error, error propagation, likelihood | fitting |
| 10 + S10 | least squares from likelihood, the straight-line fit in closed form, parameter uncertainties, gradient descent, `curve_fit`, goodness of fit | classification |
| 11 + S11 | the perceptron and the logistic neuron, trained by gradient descent in NumPy | deep networks |
| 12 + S12 | Pandas, cleaning by script | |
| 13 + S13 | environments, a one-command rebuild, tests | |

The terminal is `zsh` on macOS and **PowerShell 7** on Windows, both inside
VS Code, shown side by side wherever the two differ (amended 6 Oct 2026: Git
Bash is dropped). PowerShell 7, Python and Git are installed in class in
Seminar 4; before that, Windows laptops run the built-in Windows PowerShell
5.1, whose `>` writes UTF-16. Commands that both shells share (git, python,
cd) are shown once. Where they differ, give both (`shasum -a 256` against
`Get-FileHash`, `wc -l` against `(Get-Content f).Count`). Output that must
have the same bytes on every system is written by a Python script with
`newline="\n"`, not by a shell redirect. No session depends on homework.

## 4. The running examples

Use these instead of inventing new data. Seminars follow along on them; at
home students repeat the step on a dataset of their own choice. Never call the
D⁰ analysis "the course project": the semester project is each student's own.

- **The pendulum table**, `lectures/workbook/docs/data/pendulum.csv`: nine
  lengths in cm and the time of 10 swings in s. Example values close to
  T = 2π√(L/g). Cleaned by hand in week 2 from `pendulum_raw.csv`; its bytes
  are read in week 3. It is the table to plot (08), to propagate errors on
  (09), to fit (10: T² against L is a straight line whose slope gives g) and
  to clean by script (12: `pd.read_csv(sep=";", decimal=",")` on the raw file).
- **The LHCb file**, `lectures/workbook/docs/data/D0_KPi.csv`: 91 583 rows,
  four columns `M, PT, TAU, IPCHI2`, no other columns. `TAU = -100` marks a
  missing value (49 rows). `M` is the K⁻π⁺ invariant mass in MeV/c², with the
  D⁰ peak near 1865. Histogram (08), peak fit (10), missing values (12).
- The former seminar briefs mention momentum, charge and particle-ID columns.
  The file does not have them. Do not use them.

## 5. The standard for a deck

Read `CLAUDE.md` first: commands, conventions, gotchas. Then look at the
models: `slides/02_Introduction_to_Data.md` from "# Markdown & **Text
Editing**" on, and in `slides/03_How_Computers_Work.md` the slides "n Bits, 2ⁿ
Values", "Why 0.1 Is Not Exact", "The Steps Between Floats", "How UTF-8 Packs
a Code Point", "A Checksum by Hand".

1. **Derive, do not assert.** A result is reached in steps the room can
   follow, from what it already knows. A formula comes with a worked example
   in real numbers. A section reads like a chapter of a textbook: each slide
   needs the one before it.
2. **Every number is computed.** Run it in Python
   (`/Users/mindaugas/miniconda3/envs/rework/bin/python` has NumPy, SciPy,
   Matplotlib, Pandas, scikit-learn) and put the result on the slide. Code on
   a slide has been run exactly as shown.
3. **Laconic, literal wording.** Name the thing. No metaphor titles, no
   slogans, no teasers, no chains of clauses joined by dashes. Short declarative
   sentences. Numbers instead of comparisons.
4. **No promises.** A deck says what this lecture does. No "Lecture N covers",
   "in the seminar you will", "Seminar N tie-in", "(from week N)", "next week".
   Referring back to something already taught is fine. Speaker notes follow
   the same rule.
5. **No untaught vocabulary**: see section 3.
6. **Quizzes close the deck.** `<MCQ>` slides go after the Recap under a
   `layout: section` slide titled exactly `# Check **Yourself**`, with the line
   "Questions on this lecture, for after it. They are not part of the lecture
   time." A quiz there uses numbers the lecture did not work through. The
   place a quiz leaves is filled with content.
7. **Timing.** `pnpm timing` must show the deck between 105 and 145 min; aim
   for 125–140. Too much is better than too little.
8. **Zero overflow.** Every slide fits the 980×552 frame; the gate is below.
9. **Structure.** Cover, quote, learning objectives, sections, Recap, then
   Check Yourself. Card system, `## 📊 **Title**` with the emoji outside the
   bold. Cover frontmatter is `layout: cover` and `title:` only; the title is
   fixed by `decks.json`, do not change it.
10. **Figures.** Prefer a figure to a paragraph. Scripted figures go in
    `figures/src/<family>.py` (`style.py` gives the dark course style; register
    in the module's `FIGURES` dict; run with
    `/Users/mindaugas/miniconda3/envs/rework/bin/python figures/src/build.py --only <family>`)
    and are committed as `public/figures/viz_<family>_*.svg`. Families already
    registered for this rework: `arrays` (07), `probability` (09), `fitting`
    (10), `perceptron` (11), `cleaning` (12), `ml` (16). Seeded data,
    deterministic output.
11. **Runnable code.** Decks 06–12 may use `{monaco-run} {autorun:false}`
    Python fences (see the Monaco gotchas in CLAUDE.md and how
    `slides/12_Pandas_and_Data_Cleaning.md` declares its `python:` block on the
    cover). A plotting fence stays under about 10 lines.

## 6. The standard for a seminar page

One page per seminar, for the person at the front, in the form of
`seminars/seminar_01.md` and `seminars/seminar_03.md`: a header line with
`**~120 min**`, the parts, "How to use this page", a clock table, prerequisites,
then numbered sections. Each section has a lead paragraph (what to tell the
room), numbered steps restarting at 1 (what to do on the projector), "You
should now see", and at most one "Watch for" box. Blocks to type go in `text`
fences with lines under 75 characters. Keys and commands for Windows and
macOS. Then wrap-up, "Next steps, at home" on the student's own dataset,
stretch goals with answers, "If students ask for more", "Aims practised".
Every stated result (a count, a size, an output line) has been produced by
running the step.

## 7. The standard for a lecture page

`lectures/workbook/docs/lectures/lecture_N.md`, N without a leading zero, in
the form of `lecture_2.md` and `lecture_3.md`: one paragraph placing the
lecture after the previous one, "What the lecture covers", "The lecture in 90
minutes" (clock table with slide numbers, skip table that brings the estimate
to about 90 min, notes on what not to cut and what is shown live), "Check
yourself" (the quiz questions with answers), "Paired seminar", "Take-aways".
Slide numbers are those of the finished deck: recount at the end.

## 8. Per lecture

**04 Command Line & File Handling.** The deck is `slides/04_…`. Keep the shell
part and make it the spine: the terminal as a place where a step can be written
down and repeated. Start from `pwd`, `ls`, `cd` as known. Windows uses Git
Bash. Its second half repeats week 2 (five file-naming slides, the folder
layout under other names, raw is read-only, a README slide, rebuilding the
skeleton as `my_project`): cut those to a short recap that uses the week-2
layout, and use the room for what is new. New: regular expressions, taken from
the parked L05 (find and replace with regex in VS Code, capture groups) and
joined to `grep -E`, with the decimal-comma file as the example; the README as
a full document (anatomy, licence, columns and units, how to rebuild), from
the parked L05; backups as a method (3-2-1); checksums in practice; paths. No
Git, no "clone", no "commit". Python appears only as "run this script".
Seminar 4: files and folders from the shell, pipes on the data file, a regex,
a first script, the README completed. Old `seminar_05.md` (in 3a27c06) is a
source for the README part.

**05 Version Control with Git.** After its six quizzes move, the deck is about
20 min short: fill it. Build the model before the commands: a commit is a
snapshot with a parent and an identifier, and the identifier is a SHA hash of
the content (hashes were taught in 03); the three areas; history as a graph.
Then the commands, each shown first in the Source Control view of VS Code and
then typed. Add from the parked L05: the diff view, the Git graph. Add:
`.gitignore` for a data project (large and raw data stay out, the README says
how to fetch them), undoing (restore, revert), reading history (log, diff,
blame). Install and `git config` were homework: one check slide. Remotes over
HTTPS first; SSH as the alternative. The old deck's `about_me.md` becomes the
project's `README.md`. Seminar 5: the project folder under Git, Source Control
view first, then the same steps typed; a remote; a branch and a merge.

**06 Python Foundations.** After its quizzes move the deck is just under the
floor: fill it. Connect to 03: a Python `int` does not overflow, a `float` is
the float64 of Lecture 03, a `str` is Unicode. Values, types, variables,
control flow, lists, dicts, strings to numbers, f-strings, reading a traceback,
scripts. Add: how to run a script from VS Code and from the terminal, the
Python extension (from the parked L05), finding a bug with `print` and with
the debugger (breakpoint, step, inspect). The install slide goes: it was
homework. Seminar 6: parse one line of the data file into numbers, then a
loop over the first lines.

**07 Python for Data & NumPy.** The old deck plus the NumPy half of
`3a27c06:…/13_NumPy_and_Pandas.md`. Functions and exceptions, `pathlib`,
reading CSV with the `csv` module, then NumPy as the reason arrays exist:
one type per array (dtype, with the int8 overflow of Lecture 03), creating,
indexing, slicing, boolean masks, vectorised arithmetic and broadcasting,
`mean`, `std`, `np.loadtxt`, `np.histogram`. The argparse, docstring and
module slides of the old deck belong to 13, which teaches argparse again:
drop them here. Seminar 7: read the whole file into an array, mask the
missing values (`TAU != -100`), report counts and summary numbers.

**08 Data Visualisation.** This deck was overhauled in July and is the largest
(87 slides). Do not rebuild it. Move the quizzes, remove pointers to other
lectures and seminars, and check that nothing needs statistics the room does
not have yet: standard error, the normal distribution and the IQR now come a
week later, so define what is used where it is used. Matplotlib is new here
and NumPy is known. Add near the start the two running examples as first
plots: the pendulum table as points with labelled axes and units, the mass
column as a histogram. Seminar 8: those two figures made, saved to `results/`
and placed in `report.md`.

**09 Probability & Statistics.** The lecture ends at likelihood, and Lecture
10 starts from it. Own: probability and its rules, random variables, the
binomial, Poisson and Gaussian distributions with where each comes from, mean
and variance, covariance and correlation, the standard error of the mean
derived (σ/√N), the central limit theorem shown by simulation, error
propagation derived by a first-order expansion and applied to g from one
pendulum measurement, then likelihood and maximum likelihood: the estimate of
a Gaussian mean is the sample mean, and with unequal errors it is the weighted
mean. Do not treat χ², least squares or fitting: that is 10. Hypothesis
testing may be a short closing section. Seminar 9: a mean with its standard
error, a histogram against a Gaussian, propagated uncertainty of g.

**10 Data Fitting from First Principles.** Rebuild as one argument.
(1) A fit is a model, data with uncertainties, and a measure of mismatch.
(2) Gaussian errors: maximising the likelihood is minimising
χ² = Σ (yᵢ − f(xᵢ; θ))² / σᵢ². (3) The straight line: set the two derivatives
to zero, solve the normal equations, get slope and intercept in closed form;
do it on the pendulum table as T² against L and obtain g with numbers.
(4) Uncertainties of the parameters from the curvature of χ² (Δχ² = 1) and
the covariance matrix; propagate to g. (5) The same in matrix form, so that
any model linear in its parameters is solved alike; `np.linalg.lstsq`.
(6) Models that are not linear in the parameters: gradient descent on χ²,
with the update rule derived and run by hand for a few steps, then
`scipy.optimize.curve_fit` as the same idea done well; the D⁰ mass peak,
a Gaussian on a linear background. (7) Goodness of fit: χ² per degree of
freedom, residuals and pulls, underfitting and overfitting. (8) What goes
wrong: starting values, correlated parameters, errors that are not Gaussian.
Seminar 10: slope and intercept from the closed formulas in NumPy, g and its
uncertainty, then the same fit with `curve_fit`, then residuals.

**11 The Perceptron.** New deck `slides/11_The_Perceptron.md` (a skeleton is in
place). Source material: the perceptron and classifier slides of
`3a27c06:…/16_Machine_Learning_and_AI.md`. One argument, built on 09 and 10.
(1) From fitting a number to deciding a class. (2) The neuron: a weighted sum,
a bias and a step; the decision boundary is a line whose normal vector is the
weight vector. (3) Rosenblatt's learning rule, worked by hand on four points
(a logic gate) with the table of updates computed; the convergence theorem
stated and what "linearly separable" means. (4) The step has no useful
gradient: replace it by the sigmoid; the output is a probability. (5) The
Bernoulli likelihood gives the cross-entropy loss, as the Gaussian likelihood
gave χ² in Lecture 10; derive the gradient, ∂L/∂w = (ŷ − y)·x. (6) The
training loop in NumPy, about a dozen lines, on a seeded two-class dataset;
the loss falling; the boundary moving. (7) Scaling the inputs, the learning
rate, a train and test split, accuracy. (8) The limit: XOR is not linearly
separable, shown from the four inequalities; two neurons in a hidden layer
solve it, with weights set by hand and checked. (9) History in three dates:
1958 Rosenblatt, 1969 Minsky and Papert, and what a modern network keeps of
this unit. Seminar 11: the perceptron written from an empty file and trained
on a handed-out two-class file; create that file in
`lectures/workbook/docs/data/` with the script that makes it.

**12 Pandas & Data Cleaning.** NumPy has moved to 07, so this deck is Pandas
and cleaning. Start from the hand cleaning of week 2 and do the same by
script: `pd.read_csv("pendulum_raw.csv", sep=";", decimal=",")`. DataFrames,
selecting, types, missing values (`TAU = -100`), duplicates, impossible
values, units, tidy tables, `groupby`, joining, writing to `data/processed/`;
raw is read, never written. Take the data-quality section of
`3a27c06:…/09_Concepts_of_Data_Analysis.md`. Seminar 12: an audit of the data
file, then a cleaning script whose output goes to `data/processed/`.

**13 Reproducible Workflows & Automation.** One project layout, the one of
week 2. The command-line interface (argparse) and a config file; environments
and pinned versions; one command that rebuilds everything, in a form that
works on Windows too (`make` is not on Windows by default: give a `run_all.py`
since `make` is not on Windows by default); tests with pytest; continuous
integration; FAIR. Add from the parked L05: diagrams as text (Mermaid) for
drawing the pipeline, and `.vscode/extensions.json`. Seminar 13: environment
file, one-command rebuild, one test.

**14 Concepts of Data Analysis** (extra). Remove what repeats Lecture 02 (data
types, the lifecycle) and what moved to 12 (data quality). Keep and deepen:
what an analysis is, the loop from question to decision, working with others
and review. Add what the course lacks: research integrity and authorship, the
data management plan, ethics and personal data, responsible use of AI tools.
Bring the vocabulary down to the room (no Kafka, Snowflake, Spark).

**15 Computing Infrastructure & HPC** (extra). Remove what repeats 03
(hardware), 07 and 12 (vectorisation, file formats): refer back instead. The
slide "The LHC Computing Grid" in `parked/02_Introduction_to_Data.md` belongs
here. After the quizzes move the deck is under the floor: fill it.

**16 Machine Learning & AI** (extra). It now follows the perceptron. From one
neuron to a network: a hidden layer, backpropagation derived for one hidden
layer by the chain rule, a small network trained in NumPy; then the practice
of the old deck: train, validation and test sets, metrics, ROC, cross-
validation, leakage, clustering; then large language models and their
responsible use. The data file has no momentum columns.

## 9. Working rules for a parallel rework

- One agent per lecture owns three files and nothing else: its deck, its
  seminar page, its lecture page. It may add figures in its registered family
  module and files in `lectures/workbook/docs/data/` or `public/figures/`
  with names that start with its topic.
- Shared files are not touched: `decks.json`, `mkdocs.yml`, `CLAUDE.md`,
  theme and CSS, components, scripts, other decks, `index.md`, `overview.md`,
  `figures/src/build.py`, `style.py`. If a shared file needs a change, report
  it.
- No commits, no pushes, no branch changes.
- Gate, serialised so that parallel runs do not collide:

  ```bash
  until mkdir .qa-lock 2>/dev/null; do
    find .qa-lock -maxdepth 0 -mmin +12 -exec rmdir {} \; 2>/dev/null; sleep 7
  done
  pnpm -s qa:shots --only <slug> 2>&1 | grep -E 'overflow|✗|❌|No overflow|QA summary'
  rmdir .qa-lock
  ```

  Always release the lock, also after a failure. Then read the screenshots of
  the changed slides in `.qa-shots/<slug>/slide-NNN.png` and fix what looks
  wrong: overflow, a wrapped number, a table at the wrong scale (use
  `table-compact` on the card), an empty half-slide.
- `node scripts/timing-report.mjs | grep <file stem>` gives the estimate.
- The workbook is built at the end by the coordinator; keep Markdown plain
  (admonitions, tables, fenced code, `{ #anchor }` on headings).
