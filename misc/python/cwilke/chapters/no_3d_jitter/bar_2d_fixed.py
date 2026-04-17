"""Same data as bar_3d_bad, drawn as a flat 2-D bar chart (Wilke ch. 26)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke.theme import OKABE_ITO, apply_base, hgrid, save


def render() -> None:
    apply_base()

    categories = ["A", "B", "C", "D", "E"]
    values = [23, 17, 35, 29, 12]
    colors = [OKABE_ITO[1], OKABE_ITO[2], OKABE_ITO[3],
              OKABE_ITO[5], OKABE_ITO[6]]

    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.bar(categories, values, color=colors, alpha=0.9, width=0.65,
           edgecolor="#2c3e50", linewidth=0.5)
    ax.set_ylabel("value")
    ax.set_xlabel("category")
    hgrid(ax)
    save(fig, "no_3d_jitter", "bar_2d_fixed")


if __name__ == "__main__":
    render()
