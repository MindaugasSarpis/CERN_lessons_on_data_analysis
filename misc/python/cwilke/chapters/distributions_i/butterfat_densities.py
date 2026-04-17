"""Density plots of butterfat % by cattle breed (Wilke fig 7.9).

For a small number of reasonably distinct groups, overlaid density
curves are a clean way to show multiple distributions at once — much
clearer than stacked or overlapping histograms.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

from cwilke import data as D
from cwilke.theme import (
    OKABE_ITO,
    apply_base,
    hgrid,
    save,
)


def render() -> None:
    apply_base()
    df = D.cows_butterfat()

    breeds = ["Ayrshire", "Guernsey", "Holstein-Friesian", "Jersey"]
    colors = [OKABE_ITO[2], OKABE_ITO[1], OKABE_ITO[6], OKABE_ITO[3]]

    xs = np.linspace(2.5, 7.5, 400)

    fig, ax = plt.subplots(figsize=(7.4, 4.2))
    for breed, color in zip(breeds, colors):
        vals = df.loc[df["breed"] == breed, "butterfat"].values
        kde = gaussian_kde(vals, bw_method=0.35)
        y = kde(xs)
        ax.fill_between(xs, y, alpha=0.35, color=color, linewidth=0)
        ax.plot(xs, y, color=color, linewidth=2.0, label=breed)

        # Label at peak.
        peak_i = y.argmax()
        ax.text(xs[peak_i], y[peak_i] + 0.03, breed,
                color=color, fontsize=10, ha="center")

    ax.set_xlabel("butterfat (%)")
    ax.set_ylabel("density")
    ax.set_xlim(2.5, 7.5)
    hgrid(ax)
    fig.tight_layout()
    save(fig, "distributions_i", "butterfat_densities")


if __name__ == "__main__":
    render()
