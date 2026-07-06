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
        "svg.hashsalt": "cern-course",  # deterministic element ids across runs
        "figure.constrained_layout.use": True,
    })

def new_fig(w: float = 7, h: float = 4.2):
    fig, ax = plt.subplots(figsize=(w, h))
    return fig, ax

def save(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    # metadata Date=None: drop the embedded timestamp so repeated builds are
    # byte-identical (otherwise every run dirties all 80+ committed SVGs).
    fig.savefig(OUT / f"{name}.svg", format="svg", bbox_inches="tight",
                metadata={"Date": None})
    plt.close(fig)
    print(f"  + {name}.svg")
