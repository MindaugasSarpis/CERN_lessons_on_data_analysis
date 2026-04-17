"""Temperatures plotted against each other — same units, same aspect ratio.

Plots Houston's daily temperature normal vs San Diego's, in °F and °C.
Because both axes carry the same units, grid lines must form perfect
squares (coord_fixed). The two versions look identical — that's the
point (Wilke fig 3.3).
"""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, grid, save


def _f_to_c(f):
    return (f - 32) * 5 / 9


def render() -> None:
    apply_base()
    df = D.ncdc_normals_4locs().sort_values(["location", "day"])
    hou = df[df["location"] == "Houston"].set_index("day")["temperature"]
    sdi = df[df["location"] == "San Diego"].set_index("day")["temperature"]
    days = hou.index.values

    fig, axes = plt.subplots(1, 2, figsize=(10.0, 5.0))

    # Panel a: degrees F
    ax = axes[0]
    ax.plot(sdi, hou, color=PRIMARY_BLUE, linewidth=1.5)
    ax.set_xlabel("temperature in San Diego (°F)")
    ax.set_ylabel("temperature in Houston (°F)")
    ax.set_xlim(45, 85)
    ax.set_ylim(48, 88)
    ax.set_aspect("equal")
    grid(ax)
    ax.set_title("a", loc="left", fontweight="bold", color="#455a64")

    # Panel b: degrees C
    ax = axes[1]
    ax.plot(_f_to_c(sdi), _f_to_c(hou), color=PRIMARY_BLUE, linewidth=1.5)
    ax.set_xlabel("temperature in San Diego (°C)")
    ax.set_ylabel("temperature in Houston (°C)")
    ax.set_xlim(_f_to_c(45), _f_to_c(85))
    ax.set_ylim(_f_to_c(48), _f_to_c(88))
    ax.set_aspect("equal")
    grid(ax)
    ax.set_title("b", loc="left", fontweight="bold", color="#455a64")

    # Highlight the four seasonal anchor days (1 Jan, 1 Apr, 1 Jul, 1 Oct)
    anchor_days = [1, 92, 183, 274]
    anchor_lbls = ["Jan 1", "Apr 1", "Jul 1", "Oct 1"]
    for lbl, d in zip(anchor_lbls, anchor_days):
        if d in sdi.index and d in hou.index:
            x_f, y_f = float(sdi[d]), float(hou[d])
            axes[0].scatter([x_f], [y_f], s=30, color="#2c3e50", zorder=5)
            axes[0].annotate(lbl, (x_f, y_f), xytext=(5, 5),
                             textcoords="offset points", fontsize=9)
            x_c, y_c = _f_to_c(x_f), _f_to_c(y_f)
            axes[1].scatter([x_c], [y_c], s=30, color="#2c3e50", zorder=5)
            axes[1].annotate(lbl, (x_c, y_c), xytext=(5, 5),
                             textcoords="offset points", fontsize=9)

    fig.tight_layout()
    save(fig, "coordinates_axes", "houston_vs_san_diego")


if __name__ == "__main__":
    render()
