# The Seminars — How They Work

Every lecture is paired with a **hands-on seminar**. The first session in class
is Seminar 2, which starts from zero; Seminar 1 (installing Python and Git) is
done at home after it. Each brief is
**self-contained**: it states its goal, prerequisites, tasks, stretch goals and a
wrap-up, and sizes to ~120 min. The seminars practise the course's four aims —
🔧 tool-agnostic, ♻️ reproducible, ⚙️ automated, 📁 well-organised data & files.

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

From **Seminar 2** on you work on **a dataset of your own choice** — any tabular
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

## The seminar repository

Seminar 2 creates a small project folder that later seminars reuse:

```text
analysis-project/
|- README.md            # what this is, data provenance, how to rebuild (S5)
|- data/
|  |- raw/              # the CSV exactly as downloaded — READ ONLY (S2, S4)
|  |- processed/        # cleaned tables, produced by scripts only (S13)
|- scripts/            # one script per step (S7-S16)
|- results/            # figures and numbers, all regenerable (S10-S12)
|- environment.yml / requirements.txt   # pinned dependencies (S14)
|- Makefile            # `make all` rebuilds everything (S14)
```

The same layout is a sound default for your own project.

**The golden rule:** you could delete everything except `data/raw/` and `scripts/`
and rebuild the whole thing with one command. If that's true, you've succeeded.

## What each seminar covers

| Seminar | Hands-on focus |
|--|--|
| 1 | Python and Git installed *(at home, after the first session)* |
| 2 | VS Code; the project folder; a data file in `data/raw/`; provenance recorded |
| 3 | The raw file understood as bytes (encoding, size, format) |
| 4 | `raw/`–`processed/` structure; clean filenames; CLI inspection |
| 5 | A real `README.md` (provenance, columns, units, rebuild steps) |
| 6 | The repo under Git; a feature branch made and merged |
| 7 | First parsing: one event line → numbers |
| 8 | Ingest script: whole CSV read into Python (no Pandas) |
| 9 | Data-quality audit (missing, duplicate, impossible values) |
| 10 | A first committed figure (the K–π mass spectrum) |
| 11 | A measurement with an uncertainty (a value ± SE) |
| 12 | A fit: a peak (Gaussian + background) → value ± error, χ² |
| 13 | A clean, tidy `processed/` table produced with Pandas |
| 14 | One-command reproducible rebuild (environment + Makefile) |
| 15 | The pipeline run as a batch/remote-style job, at scale *(optional)* |
| 16 | A trained + honestly-evaluated classifier *(optional)* |
