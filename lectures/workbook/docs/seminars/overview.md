# The Seminars — How They Work

Every lecture from week 2 on is paired with a **hands-on seminar**. Week 1 is
lecture only. The first session in class is
[Seminar 1](seminar_01.md), taught with Lecture 2: it starts from zero and
needs only VS Code. Python and Git are
[installed at home](install_python_git.md) after it. Each brief is
**self-contained**: it states its goal, prerequisites, tasks, stretch goals and a
wrap-up, and sizes to ~120 min. The seminars practise the course's four aims —
🔧 tool-agnostic, ♻️ reproducible, ⚙️ automated, 📁 well-organised data & files.

## The sessions

One new tool or idea per session, each arriving inside VS Code. Nothing is
used before the session that introduces it. A page carries the number of its
lecture, so there is no Seminar 2.

| Date in 2026 | Seminar | New |
|--|--|--|
| 29 Sep | [1](seminar_01.md) | VS Code, Markdown, the project folder, the README, editing many lines at once, provenance |
| 6 Oct | [3](seminar_03.md) | The terminal with `pwd`, `ls`, `cd`; a file as bytes: encoding, line endings, size |
| 13 Oct | [4](seminar_04.md) | The shell: files and folders, pipes, a regular expression, a first script, checksums; the README completed |
| 20 Oct | [5](seminar_05.md) | Git: the project folder under version control, from the Source Control view and typed; a remote; a branch and a merge |
| 27 Oct | [6](seminar_06.md) | Python from the first line: a line of the data file turned into numbers |
| 3 Nov | [7](seminar_07.md) | Functions, reading the whole file, NumPy arrays and masks |
| 10 Nov | [8](seminar_08.md) | Matplotlib: two figures, saved and placed in the report |
| 17 Nov | [9](seminar_09.md) | A mean with its standard error; propagated uncertainty |
| 1 Dec | [10](seminar_10.md) | A straight-line fit from the closed formulas; *g* with its uncertainty; `curve_fit` |
| 8 Dec | [11](seminar_11.md) | A perceptron written from an empty file and trained |
| 15 Dec | [12](seminar_12.md) | Pandas: an audit of the data file, then cleaning by script |
| 22 Dec | [13](seminar_13.md) | An environment file, one command that rebuilds everything, a test |

Seminars 14 to 16 belong to the further topics and are not scheduled.

Every page is a follow-along tutorial for the person at the front: a lead
paragraph, numbered steps, "You should now see", one "Watch for". On Windows
the terminal from Seminar 4 on is Git Bash inside VS Code, so one set of
commands serves every laptop.

## Two things run in parallel

| | **The seminars** | **Your project** |
|--|--|--|
| What | One hands-on exercise per week on a shared, real dataset | One project of your own, developed across the semester |
| Topic | Set by the brief | **Entirely your choice** — field, data, and form (analysis, app, dashboard, educational piece) |
| Continuity | Consecutive briefs build on each other where it helps, but any seminar can be started fresh from instructor-provided files | Grows all term; the seminar skills are meant to be carried into it |
| Assessed | No | Yes — repository, one-page report, short video, final presentation (see Lecture 1) |

How much the two overlap is up to you and will be shaped as the term goes: a
seminar step can be repeated on your own data the same afternoon, or your project
can go somewhere else entirely.

## The example dataset

From **Seminar 1** on you work on **a dataset of your own choice** — any tabular
dataset with a few thousand+ rows and at least one numeric column with
interesting structure: daily weather, prices, anonymised measurements, survey
microdata. You do **not** have to measure the D⁰ mass.

The lectures, and the examples inside the briefs, use the **LHCb open-data
masterclass** sample from the CERN Open Data Portal: events pre-selected to
contain **D⁰ → K⁻π⁺** decay candidates. Each of its 91,583 rows is one candidate,
with its **K–π invariant mass** `M`, transverse momentum `PT`, decay time `TAU`
and impact-parameter score `IPCHI2` — histogram `M` and the D⁰ appears as a peak
near **1865 MeV**. Wherever a brief says "invariant mass / D⁰ peak", read "your
numeric variable / the pattern you're looking for".

- Source: CERN Open Data Portal — *LHCb event file for real measurement*,
  [record 401](https://opendata.cern.ch/record/401),
  DOI `10.7483/OPENDATA.LHCb.E7EJ.JUWR` (event-display files:
  [record 400](https://opendata.cern.ch/record/400)).
- Files: the record holds one ROOT file, `MasterclassData.root`. The examples
  read [`D0_KPi.csv`](../data/D0_KPi.csv), converted from it by
  [`root_to_csv.py`](../data/root_to_csv.py) — values unchanged.
- Why this one: real collision data, a genuine signal to find, fit and classify,
  and small enough to work with on a laptop.

> Offline or the portal is down? The workbook keeps a byte-identical copy of the
> original, [`MasterclassData.root`](../data/MasterclassData.root); the instructor
> can also provide starting files for any later seminar.

## The project folder

Seminar 1 creates a small project folder that every later seminar works in:

```text
analysis-project/
|- README.md            # what this is, where the data came from, how to rebuild
|- data/
|  |- raw/              # files exactly as received, never edited
|  |- processed/        # cleaned tables: by hand in Seminar 1, by script later
|- scripts/             # one script per step, from Seminar 6 on
|- results/             # figures, numbers and the report
|- tests/               # checks of the scripts (Seminar 13)
|- requirements.txt     # pinned versions (Seminar 13)
|- run_all.py           # one command rebuilds everything (Seminar 13)
```

The same layout is a sound default for your own project.

**The golden rule:** you could delete everything except `data/raw/` and `scripts/`
and rebuild the whole thing with one command. If that's true, you've succeeded.

## What each seminar covers

| Seminar | Hands-on focus |
|--|--|
| 1 | VS Code; Markdown; the project folder and its README; a small table cleaned in the editor; a data file in `data/raw/`; provenance recorded |
| At home | Python and Git installed *(after Seminar 1)* |
| 3 | First terminal commands; the raw file understood as bytes (encoding, line endings, size, format) |
| 4 | Work on Files from the Shell |
| 5 | The Project Folder under Git |
| 6 | A Line of Text into Numbers |
| 7 | The Whole File in Python |
| 8 | Two Figures with Matplotlib |
| 9 | A Result with Its Uncertainty |
| 10 | Fit a Straight Line and Measure g |
| 11 | A Perceptron from an Empty File |
| 12 | Clean a Table by Script |
| 13 | One Command Rebuilds the Analysis |
| 14 | Review an Analysis, Plan the Data |
| 15 | Timing, Memory and a Background Job |
| 16 | A Small Network, Measured |
