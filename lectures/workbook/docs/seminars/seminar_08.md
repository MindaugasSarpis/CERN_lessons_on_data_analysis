# Seminar 8 — Read the Whole File into Python

**Paired lecture:** 08 Python for Data Work · **Format:** hands-on · **~90 min**

> **Running project — this session adds:** an ingest script that reads the entire
> CSV into Python — no Pandas yet.

## Goal
Scale yesterday's one-line parser to the whole file using files, loops, the
`csv` module, and a dictionary of columns — and appreciate what Pandas will later
do for you.

## Prerequisites
Seminar 7 (`parse_line`).

## Tasks
1. In `scripts/ingest.py`, open the CSV with a `with open(...)` block.
2. Read it with the standard-library `csv` module (`csv.DictReader`).
3. Collect the invariant mass `M` of every event into a list of floats,
   skipping any row that fails to parse (count how many you skip).
4. Print summary numbers with your own code: count, min, max, mean of `M`.
5. Save the mass list to `data/processed/masses.csv` (one value per line).

## Stretch goals
- Time how long the read takes; estimate it for a 10× bigger file.
- Add a `--limit N` command-line argument with `argparse` for quick test runs.

## Solution notes (instructor)
Doing it "by hand" first makes the later Pandas version (Seminar 13) feel like the
gift it is. Reinforce: raw stays untouched; `masses.csv` is a **derived** file in
`processed/`, safe to delete and regenerate.

## Aims practised
📁 raw → derived, by script · ⚙️ a re-runnable ingest step · 🔧 stdlib first
