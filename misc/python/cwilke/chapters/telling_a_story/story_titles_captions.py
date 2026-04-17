"""Telling a story with title, subtitle, caption (Wilke ch. 29)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import MUTED, OKABE_ITO, apply_base, open_axes, save


def render() -> None:
    apply_base()

    df = D.corrupt()
    continents = sorted(df["continent"].unique())
    palette = {c: OKABE_ITO[i + 1] for i, c in enumerate(continents)}

    fig, ax = plt.subplots(figsize=(8.4, 5.2))

    for cont in continents:
        sub = df[df["continent"] == cont]
        ax.scatter(sub["cpi"], sub["hdi"], s=48,
                   color=palette[cont], alpha=0.9,
                   edgecolors="white", linewidths=0.6,
                   label=cont)

    # fit a simple log-style trend and overlay
    x = df["cpi"].values
    y = df["hdi"].values
    coeff = np.polyfit(np.log(x), y, 1)
    xg = np.linspace(x.min(), x.max(), 200)
    yg = coeff[0] * np.log(xg) + coeff[1]
    ax.plot(xg, yg, color="#2c3e50", linewidth=1.6, alpha=0.7,
             linestyle="--", zorder=1, label="trend")

    ax.set_xlabel("Corruption Perceptions Index (CPI)")
    ax.set_ylabel("Human Development Index (HDI)")
    ax.legend(loc="lower right", fontsize=9, ncol=2)
    open_axes(ax)

    # Title, subtitle, caption
    fig.suptitle("Less-corrupt countries have higher human-development scores",
                 fontsize=14, fontweight="bold", x=0.04, y=0.97, ha="left")
    fig.text(0.04, 0.915,
             "CPI and HDI for 70 countries, 2018",
             fontsize=10.5, color="#2c3e50", ha="left")
    fig.text(0.04, 0.02,
             "Higher CPI = cleaner government. "
             "Source: Transparency International / UNDP.",
             fontsize=9, color=MUTED, ha="left", style="italic")

    fig.subplots_adjust(top=0.86, bottom=0.13, left=0.10, right=0.97)
    save(fig, "telling_a_story", "story_titles_captions")


if __name__ == "__main__":
    render()
