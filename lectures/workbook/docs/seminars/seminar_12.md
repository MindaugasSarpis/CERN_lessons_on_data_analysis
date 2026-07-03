# Seminar 12 — Fit a Model and Report It ± Error ⚡

**Paired lecture:** 12 Practical Data Fitting · **Format:** hackathon · **~90 min**

> **Running project — this session adds:** a fit of a resonance peak — mass ± error
> with a goodness-of-fit.

## Goal
Fit a signal-plus-background model to a resonance and extract a parameter with a
principled uncertainty and a χ² check.

## Prerequisites
Seminar 11. `scipy.optimize.curve_fit` available.

## Tasks
1. Histogram `M` in a window around a peak; take bin centres, counts, and
   `√count` as the per-bin uncertainty.
2. Define a model: **Gaussian (signal) + smooth background** (linear or exponential).
3. Fit with `curve_fit`, passing `sigma=` and good initial guesses (use your
   Seminar 11 estimate for the mean).
4. Report the peak mass and width as `value ± error` (from the covariance), and
   compute **χ²/dof**. Overlay the fit on the histogram and save to `results/`.

## Stretch goals
- Compare a linear vs exponential background: which gives a better χ²/dof?
- Fit a second resonance and tabulate both masses against the published values.

## Solution notes (instructor)
This is the fitting workflow made real. Stress honest reporting: a number without
an uncertainty is not a measurement. Bad initial guesses → non-convergence; that's
a teachable moment, not a failure.

## Aims practised
📊 quantitative result with error · ⚙️ fit-as-script · 🔧 any fitting library
