# Seminar 10 — Reproduce a Figure ⚡

**Paired lecture:** 10 Data Visualisation · **Format:** hackathon · **~90 min**

> **Running project — this session adds:** your first committed figure — the
> dimuon invariant-mass spectrum.

## Goal
Turn the mass data into a clear, honest figure and **find the physics** hiding in it.

## Prerequisites
Seminar 8 (`masses.csv`). Matplotlib available.

## Tasks
1. In `scripts/plot_spectrum.py`, load the masses and draw a **histogram** of `M`.
2. Apply the lecture's principles: axis labels **with units** (GeV), a title that
   states the finding, a sensible bin width, no chart-junk.
3. The peaks are squeezed on a linear axis — redraw with a **log y-scale** (and/or
   zoom into 2–4 GeV). Can you see the **J/ψ** (~3.1), **Υ** (~9.5), **Z** (~91 GeV)?
4. Save the figure to `results/mass_spectrum.png` and commit it.

## Stretch goals
- Annotate each resonance peak directly on the plot.
- Make a small-multiples grid: the spectrum in three mass windows.

## Solution notes (instructor)
The "aha" is seeing real particles emerge from a column of numbers. Insist on the
units and a finding-as-title. The log-scale step is where the resonances appear —
a great live moment.

## Aims practised
📁 data → insight · ♻️ a script that regenerates the figure · 🔧 any plotting lib
