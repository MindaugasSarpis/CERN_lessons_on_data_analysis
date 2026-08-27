# Seminar 13 — Clean the Dataset with Pandas ⚡

**Paired lecture:** 13 NumPy & Pandas · **Format:** hackathon · **~120 min**

**Suggested timing:** 0:00 warm-up & recap · 0:10 core tasks · 1:20 stretch goals · 1:50 wrap-up & commit

> **This session builds:** a tidy `processed/` table, produced
> entirely by a Pandas script.

## Goal
Redo the ingest + audit + cleaning from earlier seminars in a few lines of Pandas,
and produce a clean analysis-ready table.

## Prerequisites
Seminars 8–9 (you know what "clean" means for this data). Pandas available.

## Tasks
1. In `scripts/clean.py`: `pd.read_csv(...)` the raw file.
2. Apply your Seminar 9 policy with vectorised operations: drop invalid rows
   (bad charge, non-physical mass), drop duplicate `(Run, Event)`, handle any NaNs.
3. Add a derived column or two (e.g. a `region` label for each resonance window).
4. Write the result to `data/processed/events_clean.parquet` (or CSV) and print a
   `df.describe()` summary.
5. Compare line count and runtime to your hand-written Seminar 8 ingest.
6. Cross-check: reproduce your Seminar 9 audit counts (invalid rows, duplicates) with
   vectorised Pandas (`df.duplicated()`, boolean masks) and confirm they match your
   hand-written numbers exactly.

## Stretch goals
- Use `groupby` to count events per resonance region.
- Reproduce the Seminar 10 spectrum straight from the cleaned DataFrame with
  `df['M'].plot.hist(...)`.
- Inspect `df.dtypes` and `df.isna().sum()` — do the inferred types and null counts
  match your Seminar 9 audit expectations?

## Wrap-up (last 10 min)
- Delete `events_clean.parquet` and re-run `scripts/clean.py` — confirm it regenerates
  a row-for-row identical table from `data/raw/` alone.
- Commit: `git add -A && git commit -m "Add Pandas cleaning pipeline"`.
- Note one lesson in the README, e.g. which vectorised operation replaced the most
  hand-written code.

## Solution notes (instructor)
The payoff moment: ~10 lines of Pandas replace a page of hand-rolled parsing.
Reinforce that raw stays untouched and the cleaned table is fully **regenerable**. In
the 120-minute slot, keep the vectorisation walkthrough (tasks 1–2) to ~20 minutes —
the extra time buys task 6's cross-check, which is where "my Pandas agrees with my
Seminar 8/9 code" confidence is actually built.

## Aims practised
📁 efficient data work · ⚙️ one clean-script → derived table · 🔧 concept over library
