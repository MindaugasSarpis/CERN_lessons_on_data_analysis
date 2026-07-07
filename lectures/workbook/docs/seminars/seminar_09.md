# Seminar 9 — Data-Quality Audit

**Paired lecture:** 09 Concepts of Data Analysis · **Format:** hands-on · **~120 min**

**Suggested timing:** 0:00 warm-up & recap · 0:10 core tasks · 1:20 stretch goals · 1:50 wrap-up & commit

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
4. Turn the policy into code: extend `scripts/audit.py` to actually apply it,
   writing the surviving rows to `data/processed/audited.csv` and printing the
   before/after row counts — the drop is now documented in output, not just
   words. (Seminar 13 will redo this in a few lines of Pandas; for now, do it
   by hand.)
5. Beyond "impossible" values, scan for **statistical outliers** in `M`: flag
   any value more than ~5 standard deviations from the mean (or outside a sane
   physical window like [1700, 2050] MeV) and report the count — then decide
   in the README whether they look like genuine rare events or data errors.

## Stretch goals
- Classify the "missingness": is it random, or tied to a particular Run?
- Write the flagged rows to `data/processed/flagged.csv` for review.
- Compare your audit's row-drop rate against a neighbour's — do you agree on
  what counts as "impossible", and why might policies legitimately differ?

## Wrap-up (last 10 min)
- Re-run `python scripts/audit.py` on a fresh copy of the raw file and confirm
  every count reproduces exactly — an audit that isn't re-runnable isn't
  trustworthy.
- Commit it: `git add -A && git commit -m "Data-quality audit + documented drop policy"`.
- Note one lesson in the README: the single check that caught the most rows,
  and whether that surprised you.

## Solution notes (instructor)
The output is a **written policy**, not just numbers — "we drop rows where … because …".
Connect to the lecture's documented-case study: silent bad rows produce confident
wrong conclusions. In the 120-minute slot, task 3's policy discussion is where
groups want to linger — cap it at ~15 minutes of debate before insisting they
write it down and move to tasks 4–5.

## Aims practised
📁 trustworthy data · ♻️ a documented, re-runnable audit
