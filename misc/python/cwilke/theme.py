"""Plotting theme for CWilke-derived figures.

Mirrors the spirit of Wilke's _common.R themes (hgrid/vgrid/grid/open) using
matplotlib. Colour palettes are Okabe-Ito (colourblind-safe), matching the
palette Wilke uses throughout Fundamentals of Data Visualization.

All figure scripts should:

    from cwilke.theme import apply_base, hgrid, vgrid, grid, open_axes, save
    fig, ax = plt.subplots(figsize=(6, 4))
    ...
    hgrid(ax)
    save(fig, "amounts", "boxoffice_horizontal")

`save` emits both SVG and PNG into misc/python/cwilke/figs/<chapter>/<name>.{svg,png}.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt

# --- Palettes --------------------------------------------------------------

# Okabe-Ito 8-colour palette (black + 7 hues). Distinguishable under the
# common forms of colour-vision deficiency.
OKABE_ITO = [
    "#000000",  # black
    "#E69F00",  # orange
    "#56B4E9",  # sky blue
    "#009E73",  # bluish green
    "#F0E442",  # yellow
    "#0072B2",  # blue
    "#D55E00",  # vermillion
    "#CC79A7",  # reddish purple
]

# The "primary" hue Wilke uses for single-colour bar/dot plots.
PRIMARY_BLUE = "#56B4E9"
PRIMARY_ORANGE = "#E69F00"
PRIMARY_GREEN = "#009E73"
GOOD = "#009E73"
WARN = "#E69F00"
BAD = "#D55E00"
MUTED = "#7f8c8d"

# Sequential / diverging (used in the colour chapter).
VIRIDIS = "viridis"
CIVIDIS = "cividis"
PLASMA = "plasma"
ROCKET = "rocket"

# --- Global rcParams -------------------------------------------------------

BASE_RC = {
    "font.family": ["Helvetica", "Arial", "DejaVu Sans"],
    "font.size": 12,
    "axes.titlesize": 13,
    "axes.titleweight": "bold",
    "axes.labelsize": 12,
    "axes.labelweight": "normal",
    "axes.edgecolor": "#2c3e50",
    "axes.linewidth": 1.0,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.axisbelow": True,
    "axes.prop_cycle": mpl.cycler(color=OKABE_ITO),
    "xtick.color": "#2c3e50",
    "ytick.color": "#2c3e50",
    "xtick.labelsize": 11,
    "ytick.labelsize": 11,
    "xtick.direction": "out",
    "ytick.direction": "out",
    "xtick.major.size": 4,
    "ytick.major.size": 4,
    "xtick.major.width": 0.9,
    "ytick.major.width": 0.9,
    "legend.frameon": False,
    "legend.fontsize": 11,
    "grid.color": "#b0bec5",
    "grid.linewidth": 0.6,
    "grid.alpha": 0.7,
    "figure.dpi": 110,
    "savefig.dpi": 150,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.12,
    "savefig.facecolor": "white",
    "figure.facecolor": "white",
    "axes.facecolor": "white",
}


def apply_base() -> None:
    """Apply the base rcParams. Call at the top of every figure script."""
    mpl.rcParams.update(BASE_RC)


# --- Grid themes -----------------------------------------------------------

def hgrid(ax: plt.Axes) -> None:
    """Horizontal gridlines only (for vertical-bar plots)."""
    ax.yaxis.grid(True, which="major", linestyle="-")
    ax.xaxis.grid(False)
    ax.set_axisbelow(True)
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", length=0)


def vgrid(ax: plt.Axes) -> None:
    """Vertical gridlines only (for horizontal-bar plots)."""
    ax.xaxis.grid(True, which="major", linestyle="-")
    ax.yaxis.grid(False)
    ax.set_axisbelow(True)
    ax.spines["bottom"].set_visible(False)
    ax.tick_params(axis="x", length=0)


def grid(ax: plt.Axes) -> None:
    """Both-axis gridlines."""
    ax.grid(True, which="major", linestyle="-")
    ax.set_axisbelow(True)


def open_axes(ax: plt.Axes) -> None:
    """No grid, clean spines — useful for scatter/association plots."""
    ax.grid(False)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)


# --- Annotations for "bad" / "ugly" examples --------------------------------

def stamp_ugly(fig: plt.Figure, text: str = "ugly") -> None:
    """Diagonal red stamp across the figure (à la Wilke's `stamp_ugly`)."""
    fig.text(
        0.5, 0.5, text,
        ha="center", va="center",
        fontsize=72, color="red", alpha=0.18,
        rotation=30, fontweight="bold",
        transform=fig.transFigure, zorder=1000,
    )


def stamp_bad(fig: plt.Figure) -> None:
    stamp_ugly(fig, text="bad")


def stamp_wrong(fig: plt.Figure) -> None:
    stamp_ugly(fig, text="wrong")


# --- Save helper -----------------------------------------------------------

_FIGS_DIR = Path(__file__).resolve().parent / "figs"


def save(fig: plt.Figure, chapter: str, name: str) -> tuple[Path, Path]:
    """Write fig to figs/<chapter>/<name>.svg and .png."""
    out_dir = _FIGS_DIR / chapter
    out_dir.mkdir(parents=True, exist_ok=True)
    svg_path = out_dir / f"{name}.svg"
    png_path = out_dir / f"{name}.png"
    fig.savefig(svg_path)
    fig.savefig(png_path)
    plt.close(fig)
    return svg_path, png_path


# --- Convenience ----------------------------------------------------------

def despine(ax: plt.Axes, *, left: bool = False, bottom: bool = False,
            top: bool = True, right: bool = True) -> None:
    for side, hide in (("left", left), ("bottom", bottom),
                        ("top", top), ("right", right)):
        ax.spines[side].set_visible(not hide)
