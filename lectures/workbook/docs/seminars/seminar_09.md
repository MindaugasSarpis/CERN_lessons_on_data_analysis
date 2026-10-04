# Seminar 11 — Quantify Uncertainty on a Measurement

**Paired lecture:** 11 Probability & Statistics · **Format:** hands-on · **~120 min**

**Suggested timing:** 0:00 warm-up & recap · 0:10 core tasks · 1:20 stretch goals · 1:50 wrap-up & commit

> **This session builds:** a real measurement reported **with an
> uncertainty**.

## Goal
Estimate a physical quantity from the data and attach an honest uncertainty,
distinguishing standard deviation from standard error.

## Prerequisites
Seminar 10 (you can see the peaks).

## Tasks
1. Select events in a window around the D⁰ peak (e.g. `1.84 < M < 1.89` GeV).
2. Compute the **mean** mass in that window, the **standard deviation** (spread of
   events), and the **standard error** SE = σ/√n (uncertainty of the mean).
3. Report the peak mass as `mean ± SE`. State clearly which number answers
   "how spread are the events" vs "how well do I know the average".
4. Halve the window and re-measure: does your estimate move within its uncertainty?
5. Wrap the computation in `scripts/measure_peak.py`, taking the window bounds as
   arguments and printing `mean ± SE` — task 4's re-measurement becomes a one-line rerun.
6. Compute a 68% confidence interval on the mean and state in one sentence what it
   means. Then compute the **Poisson counting uncertainty** √N on the number of events
   in your window, and explain why it answers a different question than the SE on the mean.

## Stretch goals
- Bootstrap: resample the window with replacement 1000× and compare the spread of
  means to your SE.
- How many events would you need to halve the uncertainty? (Recall SE ∝ 1/√n.)
- Compute the SE in a sideband (background-only) window of the same width and compare
  its size to your peak-window SE — confirming SE depends on *n* and spread, not on
  sitting on a peak.

## Wrap-up (last 10 min)
- Run `scripts/measure_peak.py` again in a fresh terminal — it should print the
  identical `mean ± SE`, proving the measurement is push-button reproducible.
- Commit: `git add -A && git commit -m "Add peak mass measurement with uncertainty"`.
- Note one lesson in the README, e.g. how the SD-vs-SE distinction changed the way you
  read an error bar.

## Solution notes (instructor)
The SD-vs-SE distinction is the crux (revisit the lecture slide). Error bars on a
*mean* should be SE, not SD. The published D⁰ mass is 1864.84 MeV — a nice check. In
the 120-minute slot, timebox the SD-vs-SE derivation (task 2) to ~15 minutes on the
board — that's where groups stall, not in task 5's scripting.

## Aims practised
📊 honest uncertainty · ♻️ a reproducible measurement script
