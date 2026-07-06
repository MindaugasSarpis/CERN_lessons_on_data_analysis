"""Colour family: palettes, rainbow pitfalls, colour-vision deficiency,
highlighting, and aesthetic mappings — this family IS the colour lesson
(lecture 10, "Data Visualisation"). All plotting through `style`; seaborn
used only for `load_dataset("iris")`.
"""
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Rectangle

import style

MONTHS = ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"]


def _strip_axes(ax) -> None:
    """Bare axes for a swatch/schematic panel: no ticks, spines, or grid."""
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
    for spine in ax.spines.values():
        spine.set_visible(False)


# --- color_palette_* : the three kinds of palette, each its own swatch strip ---

def _palette_qualitative():
    fig, ax = plt.subplots(figsize=(7.4, 1.15))
    n = len(style.CYCLE)
    ax.imshow([list(range(n))], cmap=ListedColormap(style.CYCLE), aspect="auto")
    _strip_axes(ax)
    ax.set_title("Categorical — unordered", color=style.FG, fontsize=13, pad=8)
    style.save(fig, "viz_color_palette_qualitative")


def _palette_sequential():
    fig, ax = plt.subplots(figsize=(7.4, 1.15))
    gradient = np.linspace(0, 1, 256).reshape(1, -1)
    ax.imshow(gradient, aspect="auto", cmap="cividis")
    _strip_axes(ax)
    ax.set_xticks([0, 255])
    ax.set_xticklabels(["low", "high"], color=style.DIM)
    ax.tick_params(length=0)
    ax.set_title("Sequential — cividis", color=style.FG, fontsize=13, pad=8)
    style.save(fig, "viz_color_palette_sequential")


def _palette_diverging():
    fig, ax = plt.subplots(figsize=(7.4, 1.0))
    gradient = np.linspace(-1, 1, 256).reshape(1, -1)
    ax.imshow(gradient, aspect="auto", cmap="RdBu_r", vmin=-1, vmax=1)
    _strip_axes(ax)
    ax.set_xticks([0, 127.5, 255])
    ax.set_xticklabels(["−1", "0", "+1"], color=style.DIM)
    ax.tick_params(length=0)
    ax.set_title("Diverging — centred on 0", color=style.FG, fontsize=13, pad=8)
    style.save(fig, "viz_color_palette_diverging")


# --- color_popgrowth_us_highlight : colour reserved for the signal, rest grey ---

_STATES = [
    "California", "Texas", "Florida", "New York", "Pennsylvania", "Illinois",
    "Ohio", "Georgia", "North Carolina", "Michigan", "New Jersey", "Virginia",
    "Washington", "Arizona", "Massachusetts", "Tennessee", "Indiana", "Missouri",
    "Maryland", "Wisconsin", "Colorado", "Minnesota", "South Carolina", "Alabama",
    "Louisiana", "Kentucky", "Oregon", "Oklahoma", "Connecticut", "Utah",
]
_HIGHLIGHT = {"Utah": 13.8, "Texas": 11.4, "Florida": 10.6}


def _popgrowth_highlight():
    rng = np.random.default_rng(30)
    growth = rng.normal(4.2, 3.0, len(_STATES))
    for state, value in _HIGHLIGHT.items():
        growth[_STATES.index(state)] = value

    order = np.argsort(growth)
    states = [_STATES[i] for i in order]
    values = growth[order]

    fig, ax = plt.subplots(figsize=(7.6, 7.4))
    y = np.arange(len(states))
    colors = [style.ACCENT if s in _HIGHLIGHT else style.DIM for s in states]
    ax.barh(y, values, color=colors, height=0.72, zorder=3)
    ax.axvline(0, color=style.DIM, lw=0.8)
    ax.set_yticks(y)
    ax.set_yticklabels(states, fontsize=8.5)
    for label in ax.get_yticklabels():
        if label.get_text() in _HIGHLIGHT:
            label.set_color(style.ACCENT)
            label.set_fontweight("bold")
        else:
            label.set_color(style.DIM)
    for i, s in enumerate(states):
        if s in _HIGHLIGHT:
            ax.text(values[i] + 0.35, i, f"+{values[i]:.1f}%", color=style.ACCENT,
                     va="center", fontsize=9, fontweight="bold")
    ax.set_xlabel("Growth rate (%)")
    ax.set_title("Population Growth by State")
    ax.yaxis.grid(False)
    ax.xaxis.grid(True)
    style.save(fig, "viz_color_popgrowth_us_highlight")


# --- pitfalls_of_color_use_rainbow_* : jet's false boundaries vs viridis ---

def _rainbow_field():
    x = np.linspace(-3, 3, 220)
    y = np.linspace(-3, 3, 220)
    xx, yy = np.meshgrid(x, y)
    bumps = [(-1.4, -1.0, 1.0, 0.9), (1.2, 1.3, 0.85, 1.3),
             (0.3, -1.6, 0.65, 0.6), (-1.6, 1.4, 0.75, 0.55)]
    z = np.zeros_like(xx)
    for cx, cy, amp, s in bumps:
        z += amp * np.exp(-((xx - cx) ** 2 + (yy - cy) ** 2) / (2 * s ** 2))
    return xx, yy, z


def _field_plot(cmap: str, name: str, title_color: str):
    xx, yy, z = _rainbow_field()
    fig, ax = plt.subplots(figsize=(5.4, 4.6))
    cf = ax.contourf(xx, yy, z, levels=16, cmap=cmap)
    _strip_axes(ax)
    ax.set_title(cmap, color=title_color, fontweight="bold")
    cb = fig.colorbar(cf, ax=ax, fraction=0.046, pad=0.03)
    cb.ax.tick_params(colors=style.DIM, labelsize=8)
    cb.outline.set_visible(False)
    style.save(fig, name)


def _rainbow_bad():
    _field_plot("jet", "viz_pitfalls_of_color_use_rainbow_bad", style.BAD)


def _rainbow_fix():
    _field_plot("viridis", "viz_pitfalls_of_color_use_rainbow_fix", style.FG)


# --- pitfalls_of_color_use_red_green_cvd_sim : red/green collapses under CVD ---

def _red_green_cvd():
    rng = np.random.default_rng(7)
    n = 60
    xa, ya = rng.normal(0, 1, n), rng.normal(0, 1, n)
    xb, yb = rng.normal(2.3, 1, n), rng.normal(2.0, 1, n)
    red, green, muddy = "#e0393e", "#2f9e44", "#8a7a5c"

    fig, axes = plt.subplots(1, 2, figsize=(8.6, 4.1))

    ax = axes[0]
    ax.scatter(xa, ya, s=26, color=red, label="Group A", alpha=0.85)
    ax.scatter(xb, yb, s=26, color=green, label="Group B", alpha=0.85)
    ax.set_title("Normal vision", color=style.FG)
    ax.legend(loc="upper left")

    ax = axes[1]
    ax.scatter(xa, ya, s=26, color=muddy, alpha=0.85)
    ax.scatter(xb, yb, s=26, color=muddy, alpha=0.85)
    ax.set_title("Deuteranopia (simulated)", color=style.BAD)
    ax.text(0.5, -0.06, "same colour — groups collapse", transform=ax.transAxes,
             ha="center", color=style.BAD, fontsize=10)

    for ax in axes:
        _strip_axes(ax)
    style.save(fig, "viz_pitfalls_of_color_use_red_green_cvd_sim")


# --- aesthetic_mapping_* : the visual channels a mark can carry ---

def _iris_aesthetics():
    iris = sns.load_dataset("iris")
    species = sorted(iris["species"].unique())
    colors = {sp: style.CYCLE[i] for i, sp in enumerate(species)}
    markers = {sp: m for sp, m in zip(species, ["o", "s", "^"])}
    length = iris["petal_length"]
    size = 18 + 60 * (length - length.min()) / (length.max() - length.min())
    x, y = iris["sepal_length"], iris["sepal_width"]

    fig, axes = plt.subplots(2, 2, figsize=(7.6, 6.8))

    ax = axes[0, 0]
    ax.scatter(x, y, s=30, color=style.ACCENT, alpha=0.85)
    ax.set_title("position")

    ax = axes[0, 1]
    for sp in species:
        m = iris["species"] == sp
        ax.scatter(x[m], y[m], s=30, color=colors[sp], label=sp, alpha=0.9)
    ax.set_title("colour")
    ax.legend(fontsize=8, loc="upper right")

    ax = axes[1, 0]
    ax.scatter(x, y, s=size, color=style.ACCENT, alpha=0.7)
    ax.set_title("size")

    ax = axes[1, 1]
    for sp in species:
        m = iris["species"] == sp
        ax.scatter(x[m], y[m], s=30, marker=markers[sp], color=style.ACCENT,
                   label=sp, alpha=0.9)
    ax.set_title("shape")
    ax.legend(fontsize=8, loc="upper right")

    for ax in axes.flat:
        ax.set_xlabel("sepal length")
        ax.set_ylabel("sepal width")
    style.save(fig, "viz_aesthetic_mapping_iris_aesthetics")


def _common_aesthetics():
    fig, axes = plt.subplots(2, 3, figsize=(7.8, 4.7))
    for ax in axes.flat:
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        _strip_axes(ax)

    ax = axes[0, 0]
    ax.plot([0.15, 0.45, 0.8], [0.2, 0.55, 0.85], "o", color=style.ACCENT, ms=9)
    ax.axhline(0.05, color=style.DIM, lw=1)
    ax.axvline(0.05, color=style.DIM, lw=1)
    ax.set_title("position", fontsize=11)

    ax = axes[0, 1]
    for i, marker in enumerate(["o", "s", "^"]):
        ax.plot(0.2 + i * 0.3, 0.5, marker=marker, color=style.ACCENT, ms=13, ls="none")
    ax.set_title("shape", fontsize=11)

    ax = axes[0, 2]
    for i, ms in enumerate([7, 13, 21]):
        ax.plot(0.2 + i * 0.3, 0.5, "o", color=style.ACCENT, ms=ms)
    ax.set_title("size", fontsize=11)

    ax = axes[1, 0]
    for i, c in enumerate(style.CYCLE[:4]):
        ax.add_patch(Rectangle((0.06 + i * 0.225, 0.3), 0.17, 0.4, color=c))
    ax.set_title("colour", fontsize=11)

    ax = axes[1, 1]
    for i, lw in enumerate([1, 2.5, 4.5]):
        yy = 0.22 + i * 0.3
        ax.plot([0.1, 0.9], [yy, yy], color=style.ACCENT, lw=lw)
    ax.set_title("linewidth", fontsize=11)

    ax = axes[1, 2]
    for i, ls in enumerate(["-", "--", ":"]):
        yy = 0.22 + i * 0.3
        ax.plot([0.1, 0.9], [yy, yy], color=style.ACCENT, lw=2, linestyle=ls)
    ax.set_title("linetype", fontsize=11)

    style.save(fig, "viz_aesthetic_mapping_common_aesthetics")


def _temp_normals_heatmap():
    rng = np.random.default_rng(12)
    locations = ["Death Valley", "Phoenix", "Chicago", "Denver", "Seattle", "Anchorage"]
    means = np.array([28, 24, 10, 8, 11, -6])
    amps = np.array([14, 12, 16, 15, 6, 12])
    months = np.arange(12)
    data = np.array([
        m - a * np.cos(2 * np.pi * months / 12) + rng.normal(0, 0.6, 12)
        for m, a in zip(means, amps)
    ])

    fig, ax = plt.subplots(figsize=(7.8, 4.2))
    im = ax.imshow(data, cmap="cividis", aspect="auto")
    ax.set_xticks(range(12))
    ax.set_xticklabels(MONTHS)
    ax.set_yticks(range(len(locations)))
    ax.set_yticklabels(locations)
    ax.grid(False)
    ax.tick_params(length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    cb = fig.colorbar(im, ax=ax, fraction=0.04, pad=0.02)
    cb.set_label("Mean temperature (°C)", color=style.DIM)
    cb.ax.tick_params(colors=style.DIM, labelsize=8)
    cb.outline.set_visible(False)
    ax.set_title("Monthly Temperature Normals")
    style.save(fig, "viz_aesthetic_mapping_temp_normals_heatmap")


FIGURES = {
    "viz_color_palette_qualitative": _palette_qualitative,
    "viz_color_palette_sequential": _palette_sequential,
    "viz_color_palette_diverging": _palette_diverging,
    "viz_color_popgrowth_us_highlight": _popgrowth_highlight,
    "viz_pitfalls_of_color_use_rainbow_bad": _rainbow_bad,
    "viz_pitfalls_of_color_use_rainbow_fix": _rainbow_fix,
    "viz_pitfalls_of_color_use_red_green_cvd_sim": _red_green_cvd,
    "viz_aesthetic_mapping_iris_aesthetics": _iris_aesthetics,
    "viz_aesthetic_mapping_common_aesthetics": _common_aesthetics,
    "viz_aesthetic_mapping_temp_normals_heatmap": _temp_normals_heatmap,
}
