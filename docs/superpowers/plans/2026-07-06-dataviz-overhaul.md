# Lecture 10 Dataviz Overhaul Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace lecture 10's ~73 third-party Wilke SVGs with a self-owned scripted matplotlib pipeline in a dark course style, add a click-by-click D⁰ figure-anatomy slide and live monaco-run examples, and restyle the Monaco runner theme-wide.

**Architecture:** A `figures/src/` Python package (shared `style.py` + one module per figure family, registered in `build.py`) emits SVGs to `lectures/content/public/figures/` under `viz_*` names that mirror the old `cwilke_*` basenames (`cwilke_X.svg` → `viz_X.svg`), so the deck-10 reference swap is mechanical. Slides never invoke Python — outputs are committed.

**Tech Stack:** Python 3.11+, matplotlib ≥3.8, numpy, seaborn (datasets only), Slidev v-click, slidev-addon-python-runner (monaco-run).

**Spec:** docs/superpowers/specs/2026-07-06-dataviz-lecture-overhaul-design.md

## Global Constraints

- **Sequencing:** do NOT start until the 2026-07-06 content wave is merged and pushed (it edits `10_Data_Visualisation.md`; base all edits on the post-wave file).
- Naming rule: every regenerated figure is `viz_<old-basename-without-cwilke_>.svg` (e.g. `cwilke_amounts_cleveland_dot_plot.svg` → `viz_amounts_cleveland_dot_plot.svg`). New figures (anatomy stages) are `viz_anatomy_stage{1..6}.svg`.
- Figure inventory (old name → slide heading): `.superpowers/sdd/content-fix/fig-inventory.tsv` — 76 rows, ~73 unique files. Every unique file gets a `viz_` replacement.
- Style: ONLY through `figures.src.style` — dark-transparent background, light strokes/text `#e6edf6`, dimmed `#8b97a6`, course cyan `#7dd3fc` as first series color within a colorblind-safe (Okabe-Ito-derived, dark-adapted) cycle; Space Grotesk font; no per-figure style overrides beyond what `style.py` exposes.
- All data deterministic: seaborn bundled datasets or synthetic with fixed seeds. No network access in figure code (font download happens once in Task 1, committed).
- Outputs: SVG only, `fig.savefig(..., format="svg")` via the shared `save()` helper; sized for slide cards (default 7×4.2 in; the helper controls size).
- Zero slide overflow (`pnpm qa`) is the blocking gate for all slide edits; monaco-run code blocks ≤ ~14 lines.
- Figure-family implementers: this is chart code — read the harness `dataviz` skill (palette/mark rules) before writing figures; the `style.py` palette is the validated starting point.
- Repo has no test framework: verification = running `pnpm figures` (or `--only family`) + opening/reading the emitted SVGs + `pnpm qa --only 10-data-visualisation,12-data-fitting`.
- Commit messages end with the two project trailer lines (Co-Authored-By Claude Fable 5 + Claude-Session, as used throughout this branch).

## File Map

- Create: `figures/src/style.py`, `figures/src/build.py`, `figures/src/anatomy.py`, `figures/src/amounts.py`, `figures/src/distributions.py`, `figures/src/associations.py`, `figures/src/emphasis.py`, `figures/src/color.py`, `figures/src/proportions.py`, `figures/src/story.py`, `figures/fonts/SpaceGrotesk-Regular.ttf` (+ `-Medium`, `-Bold`), `lectures/content/theme/styles/monaco.css`
- Modify: `package.json` (figures script), `lectures/content/slides/10_Data_Visualisation.md` (ref swap + new slides), theme style import file (wherever `custom-slides.css` is imported), `CLAUDE.md`
- Delete (Task 11): `lectures/content/public/figures/cwilke_*.svg`
- Generated (committed): `lectures/content/public/figures/viz_*.svg`

---

### Task 1: Pipeline scaffold — style, builder, fonts, anatomy reference family

**Files:**
- Create: `figures/src/style.py`, `figures/src/build.py`, `figures/src/anatomy.py`, `figures/fonts/*.ttf`
- Modify: `package.json`

**Interfaces (Produces — every later task consumes these exactly):**
- `style.use()` — activates the course rcParams (call once per process; `build.py` does it).
- `style.CYCLE` — list of series colors, `CYCLE[0] == "#7dd3fc"`.
- `style.FG`, `style.DIM`, `style.GRID` — text/dim/grid colors.
- `style.new_fig(w=7, h=4.2)` → `(fig, ax)` pre-styled.
- `style.save(fig, name)` — saves to `lectures/content/public/figures/<name>.svg` (transparent), closes fig. `name` WITHOUT extension.
- `build.py` registry: each family module defines `FIGURES: dict[str, Callable[[], None]]` mapping output name (no extension) → zero-arg function that builds AND saves via `style.save`. `python3 figures/src/build.py [--only family[,family]]` imports registered modules and runs all their FIGURES.

- [ ] **Step 1: Vendor Space Grotesk TTFs (OFL)**

```bash
mkdir -p figures/fonts figures/src
for w in Regular Medium Bold; do
  curl -sL "https://github.com/floriankarsten/space-grotesk/raw/master/fonts/ttf/SpaceGrotesk-$w.ttf" -o "figures/fonts/SpaceGrotesk-$w.ttf"
done
ls -la figures/fonts/   # expect 3 files, each > 50KB
```

If the URLs 404, fall back to `https://github.com/google/fonts/raw/main/ofl/spacegrotesk/SpaceGrotesk%5Bwght%5D.ttf` saved as `SpaceGrotesk-Regular.ttf` (variable font registers as one face; acceptable).

- [ ] **Step 2: Create `figures/src/style.py`**

```python
"""Course figure style — the ONLY styling entry point for figure code.

Dark-transparent figures for the dark slide theme. Colorblind-safe cycle:
Okabe-Ito brightened for dark backgrounds, with the course cyan first.
"""
from pathlib import Path

import matplotlib as mpl
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "lectures" / "content" / "public" / "figures"
FONTS = Path(__file__).resolve().parents[1] / "fonts"

FG = "#e6edf6"      # light text/strokes
DIM = "#8b97a6"     # secondary text, ticks
GRID = "#2a3140"    # hairline grid on dark
ACCENT = "#7dd3fc"  # course cyan — first series color
BAD = "#f47069"     # 'wrong' highlight (What's Wrong panels)
CYCLE = [ACCENT, "#f5b95f", "#66d9ab", "#e88bc4", "#8f9dfb", "#f0e07a", "#d55e00"]

def use() -> None:
    for f in FONTS.glob("*.ttf"):
        fm.fontManager.addfont(str(f))
    mpl.rcParams.update({
        "figure.facecolor": "none", "axes.facecolor": "none",
        "savefig.facecolor": "none", "savefig.transparent": True,
        "font.family": "Space Grotesk" if list(FONTS.glob("*.ttf")) else "DejaVu Sans",
        "text.color": FG, "axes.labelcolor": FG, "axes.edgecolor": DIM,
        "xtick.color": DIM, "ytick.color": DIM,
        "axes.titlecolor": FG, "axes.titlesize": 15, "axes.titleweight": "bold",
        "axes.labelsize": 12, "xtick.labelsize": 10, "ytick.labelsize": 10,
        "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6,
        "axes.axisbelow": True,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.prop_cycle": mpl.cycler(color=CYCLE),
        "legend.frameon": False, "legend.fontsize": 10,
        "lines.linewidth": 2.0, "patch.linewidth": 0.8,
        "svg.fonttype": "none",  # keep text as text — crisp at any zoom
        "figure.constrained_layout.use": True,
    })

def new_fig(w: float = 7, h: float = 4.2):
    fig, ax = plt.subplots(figsize=(w, h))
    return fig, ax

def save(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / f"{name}.svg", format="svg", bbox_inches="tight")
    plt.close(fig)
    print(f"  + {name}.svg")
```

- [ ] **Step 3: Create `figures/src/build.py`**

```python
#!/usr/bin/env python3
"""Regenerate the course's scripted figures. Usage:
    python3 figures/src/build.py [--only family[,family...]]
Families are modules in figures/src that define FIGURES: {name: callable}.
"""
import argparse
import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import style

FAMILIES = ["anatomy", "amounts", "distributions", "associations",
            "emphasis", "color", "proportions", "story"]

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="comma-separated family list")
    args = ap.parse_args()
    wanted = args.only.split(",") if args.only else FAMILIES
    unknown = [w for w in wanted if w not in FAMILIES]
    if unknown:
        print(f"error: unknown families {unknown}; known: {FAMILIES}", file=sys.stderr)
        return 2
    style.use()
    total = 0
    for fam in wanted:
        mod = importlib.import_module(fam)
        print(f"[{fam}] {len(mod.FIGURES)} figure(s)")
        for name, fn in mod.FIGURES.items():
            fn()
            total += 1
    print(f"Done: {total} figure(s) → {style.OUT}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

Note: modules that aren't implemented yet will fail to import — while families are being built out (Tasks 2–8 run in any order), run with `--only <your-family>` and, if `build.py`'s import of another family fails during full runs, that's expected until all tasks land; Task 11 runs the full build.

- [ ] **Step 4: Create `figures/src/anatomy.py` (reference family — the pattern all family tasks copy)**

```python
"""Anatomy of a figure: the D0 -> K-pi+ spectrum built element by element.
Six cumulative stages with IDENTICAL geometry/limits, for a v-click build-up
slide. Synthetic stand-in for the real seminar data: Gaussian peak at
1865 MeV on a falling background, fixed seed.
"""
import numpy as np

import style

RNG = np.random.default_rng(1865)
LO, HI, NBINS = 1780, 1950, 60

def _data():
    bkg = RNG.uniform(LO, HI, 6000)
    sig = RNG.normal(1865, 8.5, 2200)
    counts, edges = np.histogram(np.concatenate([bkg, sig]), bins=NBINS, range=(LO, HI))
    centers = 0.5 * (edges[:-1] + edges[1:])
    return centers, counts

def _stage(n: int):
    """Build the figure up to stage n (1..6) and save viz_anatomy_stage{n}."""
    centers, counts = _data()
    fig, ax = style.new_fig(7.6, 4.4)
    ax.set_xlim(LO, HI)
    ax.set_ylim(0, counts.max() * 1.25)
    if n < 2:
        ax.set_xticklabels([]); ax.set_yticklabels([])
        ax.grid(False)
    if n >= 2:
        ax.set_xlabel(r"$m(K^-\pi^+)$ [MeV/$c^2$]")
        ax.set_ylabel(f"Candidates / {(HI-LO)//NBINS} MeV")
    if n >= 3:
        ax.plot(centers, counts, "o", ms=3.5, color=style.ACCENT, zorder=3)
    if n >= 4:
        ax.errorbar(centers, counts, yerr=np.sqrt(counts), fmt="none",
                    ecolor=style.DIM, elinewidth=1, zorder=2)
    if n >= 5:
        ax.axvline(1865, color=style.CYCLE[1], lw=1.2, ls="--")
        ax.annotate(r"$D^0$ peak (~1865 MeV)", xy=(1865, counts.max() * 1.02),
                    xytext=(1890, counts.max() * 1.12), color=style.CYCLE[1],
                    arrowprops=dict(arrowstyle="->", color=style.CYCLE[1]))
    if n >= 6:
        ax.set_title(r"$D^0 \rightarrow K^-\pi^+$ invariant-mass spectrum")
    style.save(fig, f"viz_anatomy_stage{n}")

FIGURES = {f"viz_anatomy_stage{n}": (lambda n=n: _stage(n)) for n in range(1, 7)}
```

- [ ] **Step 5: Add the pnpm script**

In `package.json` scripts, after `"build:landing:assets"`:

```json
"figures": "python3 figures/src/build.py",
```

- [ ] **Step 6: Verify end-to-end**

```bash
python3 -c 'import seaborn' 2>/dev/null || pip install --user seaborn
pnpm figures --only anatomy
ls lectures/content/public/figures/viz_anatomy_stage*.svg | wc -l   # expect 6
```

Read one emitted SVG as an image (convert or open) OR spot-check the XML contains `Space Grotesk`. Expected: 6 stage SVGs, transparent background, identical viewBox across stages (verify: `grep -h viewBox lectures/content/public/figures/viz_anatomy_stage*.svg | sort -u | wc -l` → 1).

- [ ] **Step 7: Commit**

```bash
git add figures/ package.json lectures/content/public/figures/viz_anatomy_stage*.svg
git commit -m "feat(figures): scripted figure pipeline — course style, builder, D0 anatomy stages"
```

---

## Family tasks 2–8 — shared contract

Tasks 2–8 are independent (parallel-safe: disjoint modules) and share this contract; each task below only lists its module, figure specs, and dataset notes.

**Every family task:**
1. Read the harness `dataviz` skill FIRST (this is chart code) — palette is fixed by `style.py`; take mark/axis/legend rules from the skill.
2. Read `figures/src/style.py` + `figures/src/anatomy.py` (the pattern: module-level `FIGURES` dict, every function ends in `style.save(fig, name)`).
3. For EACH figure, read its slide in `lectures/content/slides/10_Data_Visualisation.md` (headings are in `.superpowers/sdd/content-fix/fig-inventory.tsv`) — the figure must make the slide's exact pedagogical point. "Bad" variants must be genuinely bad in the taught way (e.g. truncated axis) while still course-styled; use `style.BAD` to accent the flaw where helpful.
4. Datasets: seaborn bundled (`sns.load_dataset("mpg"|"titanic"|"iris"|"penguins"|"flights")`) where they fit; otherwise synthetic via `np.random.default_rng(<fixed seed>)`. Import seaborn ONLY for `load_dataset` — all plotting is matplotlib through `style`.
5. Verify: `pnpm figures --only <family>` runs clean; every output name matches the naming rule; render 2–3 of your SVGs to PNG (`python3 -c` with cairosvg, or read the SVG text for sanity) and READ them — dark-styled, legible, correct point.
6. Commit: `git add figures/src/<module>.py lectures/content/public/figures/viz_<family-prefixes>*` with message `feat(figures): <family> family`.
7. Report per figure: one line (name → what it shows). Note any figure you could not make convincing.

### Task 2: `amounts.py` — bars, dots, heatmap amounts (12 figures)

| Output (viz_…) | What it must show |
|---|---|
| amounts_boxoffice_horizontal | Horizontal bar chart, 5 films × opening-weekend gross (synthetic values fine), sorted desc — the "good" version |
| amounts_boxoffice_rotated_bad | Same data, vertical bars, long x-labels rotated 45° — the "bad rotated labels" version |
| amounts_cleveland_dot_plot | Cleveland dot plot of same data — "the sober bar" |
| amounts_lifeexp_alpha_order_bad | ~20 countries' life expectancy, dot plot ordered ALPHABETICALLY (bad) |
| amounts_lifeexp_bars_bad | Same, as bars starting at 0 — shows bars waste range when values cluster (60–82) |
| amounts_lifeexp_dot_plot | Same, dots sorted by value (good) |
| amounts_health_heatmap | Countries × decades life-expectancy heatmap (sequential colormap, light-on-dark readable) |
| amounts_students_stacked_bars | Stacked bars, student counts by year × category |
| proportional_ink_truncated_bar_bad | Bar chart with y-axis starting at ~48 exaggerating small differences |
| proportional_ink_truncated_bar_fixed | Same data, y from 0 |
| proportional_ink_log_scale | Values spanning 4 decades: linear bars unreadable vs log-scale — single figure with two panels labeled |
| viz note | life-expectancy data: synthetic but plausible (seeded), or `sns.load_dataset("healthexp")` if available |

### Task 3: `distributions.py` — histograms, densities, box/violin, QQ, ECDF (11 figures)

| Output (viz_…) | What it must show |
|---|---|
| distributions_i_anscombes_quartet | The classic quartet, 2×2 panels, identical fits — hardcode Anscombe's actual numbers (public domain) |
| distributions_i_titanic_density | Age distribution (titanic), filled density by class or overall histogram+density — matches "What are Histograms?" |
| distributions_i_titanic_hist_binwidth | Same data, 3 panels: too-narrow / good / too-wide bin widths |
| distributions_i_titanic_ecdf | ECDF of titanic ages |
| distributions_i_qq_plot | QQ plot: near-normal sample against theoretical quantiles, reference diagonal |
| distributions_ii_mpg_boxplot | mpg by cylinders (or class): boxplots |
| distributions_ii_mpg_strip_jitter | Same, jittered strip plot |
| distributions_ii_mpg_violin | Same, violins |
| distributions_ii_ridgeline | Ridgeline: one distribution per month (flights or synthetic temps), vertically offset filled densities |
| avoid_line_drawings_iris_densities_lines | Iris petal-length densities, UNFILLED thin lines (the "avoid" version) |
| avoid_line_drawings_iris_densities_filled | Same, filled translucent densities (good) |

### Task 4: `associations.py` — scatter, bubbles, slopes, correlations, trends, panels (10 figures)

| Output (viz_…) | What it must show |
|---|---|
| associations_blue_jays_scatter | Two continuous vars scatter (penguins bill length × depth works), one series |
| associations_blue_jays_bubble | Same + third variable as point size, size legend |
| associations_co2_slopegraph | Slopegraph: ~8 entities, two time points, lines connecting — a few highlighted with CYCLE colors, rest DIM |
| associations_mtcars_corr_heatmap | Correlation heatmap (mpg dataset numeric cols), diverging colormap centered at 0 |
| multi_panel_correlogram | Pair plot 3×3 (penguins, 3 vars): scatters off-diagonal, histograms on diagonal |
| multi_panel_small_multiples_gapminder | Small multiples: 6 panels, same x/y scale, one series each (synthetic gapminder-like growth curves) |
| trends_keeling_curve | Keeling-style CO₂ curve: rising oscillating series 1958→now (synthetic formula: trend + seasonal sine) |
| trends_lincoln_temps_raw_smooth | Daily-ish noisy series with LOWESS/rolling-mean smooth overlaid — "show the data AND the trend" |
| trends_keeling_decomposition | 3 stacked panels: observed / trend / seasonal residual of the synthetic Keeling series |
| trends_detrended_price | Series minus its trend — seasonality isolated |

### Task 5: `emphasis.py` — overplotting, 3D, redundancy, label sizes (9 figures)

| Output (viz_…) | What it must show |
|---|---|
| overlapping_points_nycflights_points | ~20k point scatter, solid points — unreadable blob (the "bad") |
| overlapping_points_nycflights_hex_bins | Same data, hexbin with sequential colormap — structure visible |
| no_3d_jitter_overplot_jitter_alpha | Moderate overplot fixed by jitter + alpha (the "three fixes" slide) |
| no_3d_jitter_bar_3d_bad | Fake-3D bars (matplotlib 3d bar) distorting comparison — the "bad" |
| no_3d_jitter_bar_2d_fixed | Same data, flat 2D bars |
| redundant_coding_tech_stocks_bad_legend | 4 line series + separate legend box forcing eye travel (the "bad") |
| redundant_coding_tech_stocks_good_no_legend | Same, direct labels at line ends, no legend |
| small_axis_labels_aus_athletes_too_small | Scatter with absurdly small fonts (override rc INSIDE the function only for this figure) |
| small_axis_labels_aus_athletes_balanced | Same, correct sizes |

### Task 6: `color.py` — palettes, rainbow pitfalls, CVD, highlights, aesthetics (10 figures)

| Output (viz_…) | What it must show |
|---|---|
| color_palette_qualitative | Swatch strip of style.CYCLE — labeled "categorical" |
| color_palette_sequential | Swatch strip of a sequential colormap (e.g. `cividis`/`mako`-like) |
| color_palette_diverging | Swatch strip of a diverging colormap centered on 0 |
| color_popgrowth_us_highlight | ~30 sorted bars, all DIM except 2–3 in ACCENT — "use colour to highlight" |
| pitfalls_of_color_use_rainbow_bad | 2D field (gaussian bumps) with jet colormap — false boundaries visible |
| pitfalls_of_color_use_rainbow_fix | Same field with perceptually-uniform colormap (viridis) |
| pitfalls_of_color_use_red_green_cvd_sim | Two-panel: red/green scatter vs the same two colors as seen with deuteranopia (simulate by desaturating both toward the same muddy brown) — point: they collapse |
| aesthetic_mapping_iris_aesthetics | One dataset, 2×2 panels: same scatter mapped by position/color/size/shape |
| aesthetic_mapping_common_aesthetics | Grid of labeled aesthetic swatches: position, shape, size, color, linewidth, linetype (schematic, drawn with patches) |
| aesthetic_mapping_temp_normals_heatmap | Months × locations temperature-normals heatmap, sequential colormap |

### Task 7: `proportions.py` — pies, stacks, treemap (6 figures)

| Output (viz_…) | What it must show |
|---|---|
| proportions_pie_bad | 6-slice pie with similar-sized slices — hard to rank (the "bad" of "three ways") |
| proportions_proportions_side_by_side_bars | Same data as bars — instantly rankable |
| proportions_proportions_stacked_bar | Same data, one stacked bar — good for part-of-whole |
| proportions_bundestag_pie_good | Parliament-style pie with 3 clearly-different slices — "when pies actually work" |
| proportions_marketshare_pies_bad | 3 pies side-by-side across years — comparison fails (the "bad" companion) |
| proportions_treemap | Treemap of ~12 hierarchical values (use `matplotlib` rectangles via the squarify algorithm — implement a ~20-line squarify inline or `pip install --user squarify`) |

### Task 8: `story.py` — annotation, titles, reference lines, context, uncertainty (12 figures)

| Output (viz_…) | What it must show |
|---|---|
| telling_a_story_annotated_vs_plain | Two panels: bare line chart vs same with arrow+one-line annotation at the inflection |
| telling_a_story_story_titles_captions | One chart laid out with title / subtitle / caption zones labeled (schematic callouts) |
| telling_a_story_title_as_finding | Same chart twice: label-title ("Sales 2019–2025") vs finding-title ("Sales doubled after 2022") |
| balance_data_context_gene_expression_bad | Scatter of effect sizes with NO reference line (bad) |
| balance_data_context_gene_expression_good | Same + zero reference line + highlighted outliers |
| balance_data_context_grid_vs_no_grid | Two panels: heavy default grid vs minimal hairline grid — "less ink, same data" |
| balance_data_context_price_plot_ggplot_default | Line chart drowning in gray-background/heavy-grid look (recreate the ggplot-default feel) |
| balance_data_context_price_plot_no_grid | Same, course style |
| balance_data_context_titanic_survival_bad | Small multiples with DIFFERENT y-scales per panel (bad) |
| balance_data_context_titanic_survival_good | Same panels sharing one scale |
| uncertainty_error_bars | Point estimates with error bars (means ± SE of 5 groups) |
| uncertainty_ci_band | Regression line with shaded 95% CI band |
| uncertainty_election_quantile_dot | Quantile dot plot: 100 dots in columns approximating a distribution — "probability you can count" |
| uncertainty_hop_demo | Static frame representing a hypothetical-outcome plot: several faint draws + one bold draw, caption "one plausible world per frame" |

---

### Task 9: Deck-10 integration — ref swap, anatomy slide, monaco examples

**Files:**
- Modify: `lectures/content/slides/10_Data_Visualisation.md`

**Interfaces:**
- Consumes: all `viz_*.svg` outputs from Tasks 1–8 (naming rule `cwilke_X.svg` → `viz_X.svg`), the deck-12 `monaco-run` pattern.
- Produces: the final deck; Task 11 QA-gates it.

- [ ] **Step 1: Mechanical ref swap**

```bash
sed -i 's#figures/cwilke_#figures/viz_#g' lectures/content/slides/10_Data_Visualisation.md
grep -c "figures/viz_" lectures/content/slides/10_Data_Visualisation.md   # expect ~76
grep -c "cwilke" lectures/content/slides/10_Data_Visualisation.md          # expect 0
```

Then verify every referenced file exists:

```bash
for f in $(grep -o 'figures/viz_[A-Za-z0-9_.-]*' lectures/content/slides/10_Data_Visualisation.md | sort -u); do
  [ -f "lectures/content/public/$f" ] || echo "MISSING: $f"
done   # expect no output
```

- [ ] **Step 2: Add the anatomy fly-in slide**

Insert after the "Aesthetics of Data Visualization" slide (or where the old static Running-Project figure slide sits — read the deck and choose the storytelling-appropriate spot; report which). Slide markup (v-click stacked stages — stage 1 visible, stages 2–6 fly in per click):

```markdown
---
hideInToc: true
---

# Anatomy of a **Figure** — every element earns its place

<div class="anatomy-stack mt-md">
  <img src="/figures/viz_anatomy_stage1.svg" alt="">
  <img v-click class="anatomy-layer" src="/figures/viz_anatomy_stage2.svg" alt="">
  <img v-click class="anatomy-layer" src="/figures/viz_anatomy_stage3.svg" alt="">
  <img v-click class="anatomy-layer" src="/figures/viz_anatomy_stage4.svg" alt="">
  <img v-click class="anatomy-layer" src="/figures/viz_anatomy_stage5.svg" alt="">
  <img v-click class="anatomy-layer" src="/figures/viz_anatomy_stage6.svg" alt="">
</div>

<!--
Click through: frame → axes with units → the data → its uncertainty →
the annotation that makes the point → the title that states the finding.
If an element doesn't earn its place, it goes.
-->
```

And add to the deck-local style (or theme `custom-slides.css` if a shared utility fits better — prefer deck-local `<style>` block at the end of this slide):

```html
<style>
.anatomy-stack { position: relative; max-width: 82%; margin-inline: auto; }
.anatomy-stack img { width: 100%; display: block; }
.anatomy-layer { position: absolute; inset: 0; }
</style>
```

- [ ] **Step 3: Add two monaco-run slides**

Copy the exact fence pattern from deck 12 (` ```python {monaco-run} `). Slide A — bin-width explorer, inserted right after "Bin Width Matters":

```markdown
---
hideInToc: true
---

# Try It — **Bin Width**

```python {monaco-run}
import numpy as np, matplotlib.pyplot as plt
rng = np.random.default_rng(7)
data = np.concatenate([rng.normal(0, 1, 800), rng.normal(4, 0.5, 300)])

BINS = 30          # <-- try 5, 30, 200
plt.hist(data, bins=BINS)
plt.title(f"bins = {BINS}")
plt.show()
```
```

Slide B — scale explorer, after the log-scale/axis-choice content:

```markdown
---
hideInToc: true
---

# Try It — **Which Scale?**

```python {monaco-run}
import numpy as np, matplotlib.pyplot as plt
x = np.arange(1, 60)
y = 5 * np.exp(0.18 * x)       # exponential growth

SCALE = "linear"               # <-- try "log"
plt.plot(x, y, "o-", ms=3)
plt.yscale(SCALE)
plt.title(f"y-scale: {SCALE}")
plt.show()
```
```

(If the python-runner needs plot-output config beyond deck 12's usage, mirror whatever deck 12's working slides do — they are the ground truth.)

- [ ] **Step 4: Verify + commit**

```bash
pnpm qa --only 10-data-visualisation
git add lectures/content/slides/10_Data_Visualisation.md
git commit -m "feat(l10): scripted viz_ figures, anatomy fly-in, live monaco examples"
```

Expected: deck 10 zero overflow. If any slide overflows, fix the offending slide (usually: shrink `.anatomy-stack` max-width or split content) before committing.

---

### Task 10: Monaco restyle (theme-wide)

**Files:**
- Create: `lectures/content/theme/styles/monaco.css`
- Modify: the theme's style index (find where `custom-slides.css` is imported — `grep -r "custom-slides" lectures/content/theme/` — and register `monaco.css` the same way)

**Interfaces:** pure CSS; regression surface = deck 12's four `monaco-run` slides + deck 10's two new ones.

- [ ] **Step 1: Create `lectures/content/theme/styles/monaco.css`**

```css
/* Monaco / python-runner blocks — course chrome. Scoped to slidev's
   monaco containers so ordinary code fences are untouched. */
.slidev-monaco-container {
  border: 1px solid rgba(139, 151, 166, 0.25);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 8px 28px rgba(0, 0, 0, 0.35);
  background: #0b0e14;
}
.slidev-monaco-container .monaco-editor,
.slidev-monaco-container .monaco-editor .margin,
.slidev-monaco-container .monaco-editor-background {
  background: #0b0e14 !important;
}
/* header strip */
.slidev-monaco-container::before {
  content: "";
  display: block;
  height: 0.9rem;
  background: linear-gradient(90deg, rgba(125, 211, 252, 0.16), rgba(125, 211, 252, 0.03));
  border-bottom: 1px solid rgba(139, 151, 166, 0.18);
}
/* runner output area */
.slidev-runner-output, .slidev-monaco-container + .slidev-runner-output {
  border: 1px solid rgba(139, 151, 166, 0.18);
  border-radius: 10px;
  margin-top: 0.5rem;
  padding: 0.4rem 0.7rem;
  background: rgba(11, 14, 20, 0.8);
  font-size: 0.8em;
}
```

NOTE: the exact class names (`slidev-monaco-container`, runner output class) must be verified against the BUILT deck 12 (`.qa-dist/12-data-fitting/` or dev-serve it and inspect) — Slidev/addon versions vary. Adjust selectors to what actually renders; keep the visual spec (radius 12, hairline border, header strip, dark bg, styled output).

- [ ] **Step 2: Register the stylesheet**

Add the import next to `custom-slides.css` in the theme's style index file, same syntax as its neighbors.

- [ ] **Step 3: Verify + commit**

```bash
pnpm qa --only 10-data-visualisation,12-data-fitting
node scripts/check-slides.mjs .qa-dist/12-data-fitting --shots .qa-shots/12-monaco --only <the 4 monaco slide numbers>
```

Read the shots: rounded bordered editor with header strip, dark background, styled output, NO overflow. Commit:

```bash
git add lectures/content/theme/styles/monaco.css <style index file>
git commit -m "feat(theme): course chrome for monaco-run blocks"
```

---

### Task 11: Cleanup, full QA, docs, ship

**Files:**
- Delete: `lectures/content/public/figures/cwilke_*.svg`
- Modify: `CLAUDE.md`

- [ ] **Step 1: Full figure build + remove old set**

```bash
pnpm figures                            # all families, clean run
grep -rl "cwilke_" lectures/content/ | grep -v public/figures && echo "REFS REMAIN — STOP" || true
git rm lectures/content/public/figures/cwilke_*.svg
```

- [ ] **Step 2: Full QA (blocking)**

```bash
pnpm qa 2>&1 | tail -25    # all 16 decks + landing green
```

- [ ] **Step 3: Screenshot review of deck 10**

```bash
node scripts/check-slides.mjs .qa-dist/10-data-visualisation --shots .qa-shots/10-viz
```

Read ALL shots in batches; every regenerated figure must be legible on the dark theme (this is the visual acceptance of the whole overhaul). Fix and re-run for any figure that reads poorly (wrong contrast, clipped labels, unconvincing "bad" examples).

- [ ] **Step 4: Docs**

CLAUDE.md Commands block, after the videos:fetch line:

```bash
pnpm figures                # regenerate all scripted lecture figures (figures/src/ → public/figures/viz_*.svg)
```

And one Build-pipeline bullet: `**figures/src/** — scripted matplotlib pipeline for lecture figures (dark course style; outputs committed as public/figures/viz_*.svg; decks never invoke Python).`

- [ ] **Step 5: Commit + ship**

```bash
git add -A && git commit -m "feat(figures): complete scripted figure set; retire cwilke SVGs; docs"
git push origin ff2026 && git push origin ff2026:bs2026
```

Watch the Pages run (transient 'Deployment failed, try again later' → rerun failed jobs once). Verify live deck 10 spot-check.

---

## Plan Self-Review (completed)

- **Spec coverage:** pipeline+style+builder (§1→T1), naming rule + committed SVGs (§1→T1/global), all ~73 figures (§1→T2–T8, inventory-complete: 12+11+10+9+10+6+14=72 + 6 anatomy stages in T1; the inventory's 76 rows contain duplicates — T9 Step 1's existence check is the completeness gate), anatomy fly-in (§2→T1+T9), monaco examples (§3→T9), monaco restyle (§4→T10), QA/screenshots/ship (§5→T9/T10/T11), cwilke removal (§1→T11), sequencing guard (spec header→global constraints).
- **Type consistency:** `style.use/new_fig/save/CYCLE/FG/DIM/ACCENT/BAD`, `FIGURES` dict contract, and the `viz_` naming rule are used identically across T1–T9.
- **Placeholder scan:** none; the one deliberate indirection (Monaco selector verification against the built deck) is an explicit verification step, not a TBD.
- **Honest uncertainty:** T5's CVD simulation and T8's ggplot-default recreation are approximations by design; family implementers have judgment latitude within the shared style — that's the intended contract, and T11's screenshot review is the acceptance gate.
