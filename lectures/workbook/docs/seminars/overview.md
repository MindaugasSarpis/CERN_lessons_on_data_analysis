# The Seminars — How They Work

Every lecture is paired with a 2-hour **hands-on seminar**. Each brief is
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

## The seminar dataset

The briefs are written against the **LHCb open-data masterclass** sample from the
CERN Open Data Portal: ~60,000 events pre-selected to contain **D⁰ → K⁻π⁺** decay
candidates. Each event gives the kaon and pion momenta, from which you reconstruct
the **K–π invariant mass** — and see the D⁰ appear as a peak near **1865 MeV**.

- Source: CERN Open Data Portal — *LHCb event file for real measurement*,
  [record 401](https://opendata.cern.ch/record/401),
  DOI `10.7483/OPENDATA.LHCb.E7EJ.JUWR` (event-display files:
  [record 400](https://opendata.cern.ch/record/400)). You find and record this
  in **Seminar 2**.
- Why this one: real collision data, a genuine signal to find, fit and classify,
  and small enough to work with on a laptop.

**Prefer a dataset from your own field?** Any tabular dataset with a few
thousand+ rows and at least one numeric column with interesting structure works —
daily weather, prices, anonymised measurements, survey microdata. Wherever a brief
says "invariant mass / D⁰ peak", read "your numeric variable / the pattern you're
looking for". Mention your choice to the instructor in Seminar 2.

> Offline or the portal is down? The instructor can provide a local copy of the
> LHCb sample, and starting files for any later seminar.

## The seminar repository

Seminar 1 creates a small repository that later seminars reuse:

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
| 1 | Toolkit installed; repo skeleton + first commit |
| 2 | A dataset downloaded into `data/raw/`; provenance recorded |
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
