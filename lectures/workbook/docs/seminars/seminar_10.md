# Seminar 12 — Fit a Model and Report It ± Error ⚡

**Paired lecture:** 12 Practical Data Fitting · **Format:** hackathon · **~120 min**

**Suggested timing:** 0:00 warm-up & recap · 0:10 core tasks · 1:20 stretch goals · 1:50 wrap-up & commit

> **This session builds:** a fit of a resonance peak — mass ± error
> with a goodness-of-fit.

## Goal
Fit a signal-plus-background model to a resonance and extract a parameter with a
principled uncertainty and a χ² check.

## Prerequisites
`scipy.optimize.curve_fit` available. The shared LHCb D⁰ → K⁻π⁺ sample, a starter
script, and a rough initial estimate of the peak position (~1865 MeV) are provided.

## Tasks
1. Histogram `M` in a window around a peak; take bin centres, counts, and
   `√count` as the per-bin uncertainty.
2. Define a model: **Gaussian (signal) + smooth background** (linear or exponential).
3. Fit with `curve_fit`, passing `sigma=` **and `absolute_sigma=True`** (so the
   covariance is not silently rescaled by χ²/dof) and good initial guesses (use the
   provided estimate for the mean; `sigma` ≈ FWHM / 2.35 read off the histogram).
4. Report the peak mass and width as `value ± error` (from the covariance), and
   compute **χ²/dof**. Overlay the fit on the histogram and save to `results/`.
5. Wrap the whole procedure (histogram → fit → report) in `scripts/fit_peak.py`,
   parameterised by the window bounds, so one command reproduces the whole result.
6. Inspect the **pull** distribution: `(data - fit) / error` per bin. It should scatter
   around 0 with roughly unit spread — a large outlier pull flags where the model fails
   to describe the data, a more rigorous check than χ²/dof alone.

## Stretch goals
- Compare a linear vs exponential background: which gives a better χ²/dof?
- Fit a second resonance and tabulate both masses against the published values.
- Widen and narrow the fit window and re-fit: does the mass estimate move within its
  uncertainty? A shift larger than the error bar is a **systematic**, not statistical, effect.

## Wrap-up (last 10 min)
- Wipe `results/` and re-run `scripts/fit_peak.py` clean — confirm you get the identical
  mass, width, and χ²/dof.
- Commit the script and the fit figure: `git add -A && git commit -m "Add D0 peak fit
  with uncertainty"`.
- Note one lesson in the README, e.g. which initial-guess choice mattered most for
  convergence.

## Solution notes (instructor)
This is the fitting workflow made real. Stress honest reporting: a number without
an uncertainty is not a measurement. Bad initial guesses → non-convergence; that's
a teachable moment, not a failure. In the 120-minute slot, timebox the initial-guess
trial-and-error in task 3 to ~15 minutes — hand out working values to any group still
not converging, so tasks 5–6 (scripting, pulls) keep their time.

## Aims practised
📊 quantitative result with error · ⚙️ fit-as-script · 🔧 any fitting library
