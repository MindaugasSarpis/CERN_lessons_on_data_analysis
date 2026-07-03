# Seminar 2 — Find & Document a Dataset

**Paired lecture:** 02 Introduction to CERN · **Format:** hands-on · **~90 min**

> **Running project — this session adds:** your chosen dataset (LHCb D⁰ → K⁻π⁺, or your own) in `data/raw/`, with
> its provenance recorded.

## Goal
Acquire the running-project dataset and record **where it came from** — the first
act of reproducibility.

## Prerequisites
Seminar 1 (project skeleton).

## Tasks
1. Choose your track (see the [running-project overview](running-project.md)):
   - **Physics** — find the **LHCb masterclass** dataset on the **CERN Open Data
     Portal** ([record 401](https://opendata.cern.ch/record/401), D⁰ → K⁻π⁺;
     event-display files at [record 400](https://opendata.cern.ch/record/400)).
     Note the record's title, DOI (`10.7483/OPENDATA.LHCb.E7EJ.JUWR`), and licence.
   - **Bring-your-own** — pick a tabular dataset from your own field (weather,
     survey, prices, lab measurements…). Note where it came from and its licence.
2. Download the CSV into `data/raw/` **without renaming it**.
3. In `README.md`, start a **Data** section: source URL, DOI, licence, download
   date, file name, and a one-line description of what a row represents.
4. Record the file's size and row count (you'll verify the tools in Seminar 3):
   note them next to the provenance.

## Stretch goals
- Find and skim the dataset's documentation: what do the columns mean? What are
  the units (GeV)?
- Identify one other open dataset in your own field of interest and note its licence.

## Solution notes (instructor)
Emphasise that "I downloaded it from somewhere" is not provenance. A good entry
lets a stranger obtain the *exact* same file years later. Raw data goes in
`raw/` and is never edited from here on.

## Aims practised
♻️ provenance = reproducibility · 📁 raw data captured, untouched
