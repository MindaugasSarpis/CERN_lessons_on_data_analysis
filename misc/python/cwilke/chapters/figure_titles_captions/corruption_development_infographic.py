"""CPI vs HDI with integrated title / subtitle / source (Wilke fig 30.2)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import MUTED, OKABE_ITO, apply_base, grid, save


REGIONS = [
    "OECD", "Americas", "Asia Pacific",
    "Europe and\nCentral Asia", "Middle East\nand North Africa",
    "Sub-Saharan\nAfrica",
]
HIGHLIGHT = {
    "Germany", "Norway", "United States", "Greece",
    "Singapore", "Rwanda", "Russia", "Venezuela", "Sudan",
    "Iraq", "Ghana", "Niger", "Chad", "Kuwait", "Qatar",
    "Myanmar", "Nepal", "Chile", "Argentina", "Japan", "China",
}


def render() -> None:
    apply_base()

    df = D.corruption_2015()
    palette = {r: OKABE_ITO[i + 1] for i, r in enumerate(REGIONS)}

    fig, ax = plt.subplots(figsize=(8.6, 6.0))

    x = df["cpi"].values
    y = df["hdi"].values
    coeff = np.polyfit(np.log(x), y, 1)
    xg = np.linspace(x.min(), x.max(), 200)
    yg = coeff[0] * np.log(xg) + coeff[1]
    ax.plot(xg, yg, color="#2c3e50", linewidth=1.6, alpha=0.8)

    for region, col in palette.items():
        sub = df[df["region"] == region]
        ax.scatter(sub["cpi"], sub["hdi"], s=52,
                   facecolor=col + "80", edgecolor=col, linewidth=0.8,
                   label=region)

    for _, row in df.iterrows():
        if row["country"] in HIGHLIGHT:
            ax.annotate(row["country"],
                        (row["cpi"], row["hdi"]),
                        xytext=(5, 4), textcoords="offset points",
                        fontsize=8, color="#2c3e50")

    ax.set_xlim(10, 95)
    ax.set_ylim(0.3, 1.05)
    ax.set_xlabel("Corruption Perceptions Index, 2015")
    ax.set_ylabel("Human Development Index, 2015")
    ax.legend(loc="lower right", fontsize=8, ncol=2, frameon=False)
    grid(ax)

    fig.suptitle("Corruption and human development",
                 fontsize=15, fontweight="bold", x=0.04, y=0.98, ha="left")
    fig.text(0.04, 0.935,
             "The most developed countries experience the least corruption",
             fontsize=11, color="#2c3e50", ha="left")
    fig.text(0.04, 0.015,
             "Data sources: Transparency International & UN Human Development Report",
             fontsize=8.5, color=MUTED, ha="left", style="italic")

    fig.subplots_adjust(top=0.86, bottom=0.09, left=0.09, right=0.97)
    save(fig, "figure_titles_captions", "corruption_development_infographic")


if __name__ == "__main__":
    render()
