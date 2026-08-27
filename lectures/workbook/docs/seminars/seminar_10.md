# Seminar 10 — Reproduce a Figure ⚡

**Paired lecture:** 10 Data Visualisation · **Format:** hackathon · **~120 min**

**Suggested timing:** 0:00 warm-up & recap · 0:10 core tasks · 1:20 stretch goals · 1:50 wrap-up & commit

> **This session builds:** your first committed figure — the
> D⁰ → K⁻π⁺ mass spectrum.

## Goal
Turn the mass data into a clear, honest figure and **find the physics** hiding in it.

## Prerequisites
A `masses.csv` starter (one D⁰ → K⁻π⁺ candidate mass `M` per row, in GeV) is
provided. Matplotlib available.

## Tasks
1. In `scripts/plot_spectrum.py`, load the masses and draw a **histogram** of `M`.
2. Apply the lecture's principles: axis labels **with units** (GeV), a title that
   states the finding, a sensible bin width, no chart-junk.
3. Zoom into **1.80–1.94 GeV**: the **D⁰ peak** rises at **~1865 MeV** over a
   near-flat combinatorial background. Try a **log y-scale** to judge how far the
   signal stands above the background.
4. Save the figure to `results/mass_spectrum.png` and commit it.
5. Add a vector export alongside the PNG — `results/mass_spectrum.svg`
   (vector, for print/publication) — and set a small reusable style once
   (e.g. a `plt.rcParams.update({...})` block or a tiny `style.py` you
   import) so every later figure you make shares fonts and colours.

## Stretch goals
- Annotate the D⁰ peak and its mass directly on the plot.
- Overlay the **signal** window and two **sideband** windows as shaded bands.
- Make the sideband overlay colourblind-safe (or distinguish it with
  hatching/line style instead of colour alone) — check it by squinting at a
  grayscale copy.

## Wrap-up (last 10 min)
- Re-run `python scripts/plot_spectrum.py` from a clean terminal and confirm
  the regenerated PNG matches the committed one — same script, same figure,
  every time.
- Commit it: `git add -A && git commit -m "First committed figure: mass spectrum"`.
- Note one lesson in the README: the plotting choice (bin width, scale,
  colour) that most changed what the figure seemed to say.

## Solution notes (instructor)
The "aha" is seeing a real particle — the D⁰ — emerge from a column of numbers.
Insist on the units and a finding-as-title. The moment the peak resolves out of
the background is a great live beat. In the 120-minute slot, protect ~20
minutes for task 2's polish pass (labels, title-as-finding, bin width) even
though it's tempting to rush to the peak — a busy, unlabeled histogram
undersells the same discovery.

## Aims practised
📁 data → insight · ♻️ a script that regenerates the figure · 🔧 any plotting lib
