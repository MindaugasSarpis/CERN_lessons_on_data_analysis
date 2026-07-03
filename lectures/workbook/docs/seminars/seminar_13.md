# Seminar 13 — Clean the Dataset with Pandas ⚡

**Paired lecture:** 13 NumPy & Pandas · **Format:** hackathon · **~90 min**

> **Running project — this session adds:** a tidy `processed/` table, produced
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

## Stretch goals
- Use `groupby` to count events per resonance region.
- Reproduce the Seminar 10 spectrum straight from the cleaned DataFrame with
  `df['M'].plot.hist(...)`.

## Solution notes (instructor)
The payoff moment: ~10 lines of Pandas replace a page of hand-rolled parsing.
Reinforce that raw stays untouched and the cleaned table is fully **regenerable**.

## Aims practised
📁 efficient data work · ⚙️ one clean-script → derived table · 🔧 concept over library
