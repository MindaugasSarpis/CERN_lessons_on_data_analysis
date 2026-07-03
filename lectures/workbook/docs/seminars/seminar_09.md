# Seminar 9 — Data-Quality Audit

**Paired lecture:** 09 Concepts of Data Analysis · **Format:** hands-on · **~90 min**

> **Running project — this session adds:** a documented quality audit of your
> dataset.

## Goal
Apply the data-quality checklist from the lecture to real data before trusting any
result.

## Prerequisites
Seminar 8 (ingest).

## Tasks
1. Run the lecture's checklist over the dataset and record findings in the README:
   - **Completeness** — any missing/empty fields? How many rows?
   - **Validity** — any impossible values? (negative mass, `pt` < 0, `|Q|` ≠ 1)
   - **Consistency** — do derived and stored quantities agree? (spot-check that
     `M` is consistent with the two muons' energy/momentum for a few rows)
   - **Duplicates** — any repeated `(Run, Event)` pairs?
2. Write `scripts/audit.py` that prints each check's result as a count.
3. Decide (and document) a policy: which rows do you drop, and why?

## Stretch goals
- Classify the "missingness": is it random, or tied to a particular Run?
- Write the flagged rows to `data/processed/flagged.csv` for review.

## Solution notes (instructor)
The output is a **written policy**, not just numbers — "we drop rows where … because …".
Connect to the lecture's documented-case study: silent bad rows produce confident
wrong conclusions.

## Aims practised
📁 trustworthy data · ♻️ a documented, re-runnable audit
