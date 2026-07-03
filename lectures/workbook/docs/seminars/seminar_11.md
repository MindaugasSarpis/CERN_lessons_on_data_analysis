# Seminar 11 — Quantify Uncertainty on a Measurement

**Paired lecture:** 11 Probability & Statistics · **Format:** hands-on · **~90 min**

> **Running project — this session adds:** a real measurement reported **with an
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

## Stretch goals
- Bootstrap: resample the window with replacement 1000× and compare the spread of
  means to your SE.
- How many events would you need to halve the uncertainty? (Recall SE ∝ 1/√n.)

## Solution notes (instructor)
The SD-vs-SE distinction is the crux (revisit the lecture slide). Error bars on a
*mean* should be SE, not SD. The published D⁰ mass is 1864.84 MeV — a nice check.

## Aims practised
📊 honest uncertainty · ♻️ a reproducible measurement script
