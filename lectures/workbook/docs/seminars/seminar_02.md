# Seminar 2 — Find & Document a Dataset

**Paired lecture:** 02 Introduction to CERN · **Format:** hands-on · **~120 min**

**Suggested timing:** 0:00 warm-up & recap · 0:10 core tasks · 1:20 stretch goals · 1:50 wrap-up & commit

> **This session builds:** your chosen dataset (LHCb D⁰ → K⁻π⁺, or your own) in `data/raw/`, with
> its provenance recorded.

## Goal
Acquire the seminar dataset and record **where it came from** — the first
act of reproducibility.

## Prerequisites
Seminar 1 (project skeleton).

## Tasks
1. Choose your dataset (see the [seminar overview](overview.md)):
   - **Physics** — find the **LHCb masterclass** dataset on the **CERN Open Data
     Portal** ([record 401](https://opendata.cern.ch/record/401), D⁰ → K⁻π⁺;
     event-display files at [record 400](https://opendata.cern.ch/record/400)).
     Note the record's title, DOI (`10.7483/OPENDATA.LHCb.E7EJ.JUWR`), and licence.
   - **Your own field** — pick a tabular dataset from your own field (weather,
     survey, prices, lab measurements…). Note where it came from and its licence.
2. Download the CSV into `data/raw/` **without renaming it**.
3. In `README.md`, start a **Data** section: source URL, DOI, licence, download
   date, file name, and a one-line description of what a row represents.
4. Record the file's size and row count (you'll verify the tools in Seminar 3):
   note them next to the provenance.
5. Fingerprint the download so anyone can verify they hold the *exact* same
   bytes, and record the hash in the **Data** section:
   ```bash
   sha256sum data/raw/*.csv    # macOS: shasum -a 256
   ```
6. Cross-check your provenance against the portal's own metadata: open the
   record's JSON export (linked on the record page) and compare title, DOI,
   licence and file size with what you wrote. Add any field you had missed.

## Stretch goals
- Find and skim the dataset's documentation: what do the columns mean? What are
  the units (GeV)?
- Identify one other open dataset in your own field of interest and note its licence.
- Fetch an event-display file from record 400 too and note how it differs from
  the CSV (format, size, intended use).

## Wrap-up (last 10 min)
- Snapshot today's work: `git add -A && git commit -m "Add dataset + provenance"`
  (a large raw file can stay out of Git — provided your **Data** section says
  exactly how to fetch it).
- The acid test: could a stranger re-download the byte-identical file from your
  README alone, and confirm it with your checksum? Fix whatever they couldn't.
- Note one lesson in the README — e.g. what "provenance" turned out to include
  that you hadn't expected.

## Solution notes (instructor)
Emphasise that "I downloaded it from somewhere" is not provenance. A good entry
lets a stranger obtain the *exact* same file years later. Raw data goes in
`raw/` and is never edited from here on. In the 120-minute slot the portal hunt
(task 1) is the time sink — if it passes ~25 minutes, hand out the local copy
and let students backfill provenance from the record page.

## Aims practised
♻️ provenance = reproducibility · 📁 raw data captured, untouched
