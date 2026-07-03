# Seminar 10 — Reproduce a Figure ⚡

**Paired lecture:** 10 Data Visualisation · **Format:** hackathon · **~90 min**

> **Running project — this session adds:** your first committed figure — the
> D⁰ → K⁻π⁺ mass spectrum.

## Goal
Turn the mass data into a clear, honest figure and **find the physics** hiding in it.

## Prerequisites
Seminar 8 (`masses.csv`). Matplotlib available.

## Tasks
1. In `scripts/plot_spectrum.py`, load the masses and draw a **histogram** of `M`.
2. Apply the lecture's principles: axis labels **with units** (GeV), a title that
   states the finding, a sensible bin width, no chart-junk.
3. Zoom into **1.80–1.94 GeV**: the **D⁰ peak** rises at **~1865 MeV** over a
   near-flat combinatorial background. Try a **log y-scale** to judge how far the
   signal stands above the background.
4. Save the figure to `results/mass_spectrum.png` and commit it.

## Stretch goals
- Annotate the D⁰ peak and its mass directly on the plot.
- Overlay the **signal** window and two **sideband** windows as shaded bands.

## Solution notes (instructor)
The "aha" is seeing a real particle — the D⁰ — emerge from a column of numbers.
Insist on the units and a finding-as-title. The moment the peak resolves out of
the background is a great live beat.

## Aims practised
📁 data → insight · ♻️ a script that regenerates the figure · 🔧 any plotting lib
