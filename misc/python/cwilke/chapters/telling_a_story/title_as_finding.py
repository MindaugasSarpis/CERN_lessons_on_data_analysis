"""Use the title to state the finding, not the variables (Wilke ch. 29).

A descriptive title ("HDI vs CPI") leaves the reader to do the
interpretive work. A finding-as-title ("Cleaner government correlates
with higher human development") frames what the reader should take
away before they inspect the marks.
"""

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

    fig, ax = plt.subplots(figsize=(8.6, 5.4))

    for cont in continents:
        sub = df[df["continent"] == cont]
        ax.scatter(sub["cpi"], sub["hdi"], s=52,
                   color=palette[cont], alpha=0.9,
                   edgecolors="white", linewidths=0.6,
                   label=cont)

    # Trend curve (log fit)
    x = df["cpi"].values
    y = df["hdi"].values
    coeff = np.polyfit(np.log(x), y, 1)
    xg = np.linspace(x.min(), x.max(), 200)
    yg = coeff[0] * np.log(xg) + coeff[1]
    ax.plot(xg, yg, color="#2c3e50", linewidth=1.4, alpha=0.7,
            linestyle="--", zorder=1)

    ax.set_xlabel("Corruption Perceptions Index (higher = cleaner)")
    ax.set_ylabel("Human Development Index")
    ax.legend(loc="lower right", fontsize=9, ncol=2, title="continent")
    open_axes(ax)

    # Finding-as-title + supportive subtitle + source caption
    fig.suptitle("Cleaner government correlates with higher human development",
                 fontsize=15, fontweight="bold", x=0.04, y=0.975, ha="left")
    fig.text(0.04, 0.915,
             f"n = {len(df)} countries  ·  simulated CPI / HDI data",
             fontsize=10.5, color="#2c3e50", ha="left")
    fig.text(0.04, 0.02,
             "Each dot is one country. Source: Transparency International / UNDP (synthetic stand-in).",
             fontsize=9, color=MUTED, ha="left", style="italic")

    fig.subplots_adjust(top=0.85, bottom=0.14, left=0.09, right=0.97)
    save(fig, "telling_a_story", "title_as_finding")


if __name__ == "__main__":
    render()
