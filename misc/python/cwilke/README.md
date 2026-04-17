# cwilke — Python ports of Claus Wilke's *Fundamentals of Data Visualization*

Re-implementations of figures from C. O. Wilke's *Fundamentals of Data
Visualization* (original R/ggplot2 source: `../../../CWilke_Data_Viz`) in
matplotlib, in a deck-consistent modern style. Used by `L07 Data
Visualisation`.

## Layout

- `theme.py` — matplotlib rcParams, Okabe–Ito palette, grid helpers (hgrid /
  vgrid / grid / open_axes), `stamp_ugly/bad/wrong`, and the `save(fig,
  chapter, name)` helper that writes paired SVG+PNG outputs.
- `data.py` — dataset loaders (inline small; synthetic stand-ins for
  `dviz.supp`; CSV cache under `data/`).
- `render.py` — CLI that imports each script and calls its `render()`.
- `chapters/<name>/*.py` — one script per figure; each exposes `render()`.
- `figs/<chapter>/<name>.{svg,png}` — generated outputs.

## Running

From the repo root:

```bash
# render all chapters
/Users/mindaugas/miniconda3/envs/analysis/bin/python -m misc.python.cwilke.render

# a single chapter
/Users/mindaugas/miniconda3/envs/analysis/bin/python -m misc.python.cwilke.render amounts

# a single figure
/Users/mindaugas/miniconda3/envs/analysis/bin/python -m misc.python.cwilke.render amounts/boxoffice_horizontal
```

Each script is also executable on its own:

```bash
/Users/mindaugas/miniconda3/envs/analysis/bin/python -m cwilke.chapters.amounts.boxoffice_horizontal
```

## Fidelity target

Same teaching point, modern style. Not pixel-identical to Wilke's originals.
Palettes, fonts, and grids are tuned so figures sit naturally inside the
course's Slidev dark deck when exported as SVG.

## Dataset substitutions

Where Wilke relies on `dviz.supp` or other R-only packages (`blue_jays`,
`happy`, `lincoln_temps`, etc.), `data.py` synthesises plausible stand-ins.
The statistical distribution is preserved where it matters for the teaching
point; exact values differ.
