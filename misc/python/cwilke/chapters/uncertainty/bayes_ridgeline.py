"""Ridgeline plot of Bayesian posteriors with graded regions (Wilke 16.14)."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

from cwilke.data import cacao_ratings
from cwilke.theme import apply_base, hgrid, save


def render() -> None:
    apply_base()
    df = cacao_ratings()
    countries = ["Austria", "Belgium", "Canada", "Peru", "Switzerland", "US"]
    rows = []
    for c in countries:
        vals = df[df["location"] == c]["rating"].values
        n = len(vals)
        rows.append((c, vals.mean(), vals.std(ddof=1) / np.sqrt(n)))
    rows.sort(key=lambda r: r[1])

    fig, ax = plt.subplots(figsize=(7.8, 4.8))
    xg = np.linspace(2.4, 3.8, 500)
    ax.axvline(0, color="gray", alpha=0)  # noop

    for y, (c, mu, se) in enumerate(rows):
        dens = norm.pdf(xg, mu, se)
        # scale so peak = 0.85
        dens = 0.85 * dens / dens.max()
        # shade by 80%/95%/99%
        lvl_colors = [
            (0.005, 0.995, "#00000000"),  # invisible outer
            (0.005, 0.025, "#D1E2F1D0"),
            (0.025, 0.10,  "#7FA8C8D0"),
            (0.10,  0.90,  "#0F4C75D0"),
            (0.90,  0.975, "#7FA8C8D0"),
            (0.975, 0.995, "#D1E2F1D0"),
        ]
        for lo_q, hi_q, col in lvl_colors[1:]:
            lo = norm.ppf(lo_q, mu, se)
            hi = norm.ppf(hi_q, mu, se)
            mask = (xg >= lo) & (xg <= hi)
            ax.fill_between(xg[mask], y, y + dens[mask],
                             color=col, linewidth=0)
        # outline
        ax.plot(xg, y + dens, color="#0f2b42", linewidth=0.6)
        # median dot
        ax.plot(mu, y + 0.05, "o", color="#D55E00", markersize=6)

    ax.set_yticks(np.arange(len(rows)))
    ax.set_yticklabels([r[0] for r in rows])
    ax.set_xlim(2.6, 3.6)
    ax.set_xlabel("mean rating")

    import matplotlib.patches as mpatches
    legend = [
        mpatches.Patch(color="#0F4C75D0", label="80%"),
        mpatches.Patch(color="#7FA8C8D0", label="95%"),
        mpatches.Patch(color="#D1E2F1D0", label="99%"),
    ]
    ax.legend(handles=legend, title="posterior prob.", loc="lower right",
              frameon=False, ncol=3)
    hgrid(ax)
    fig.tight_layout()
    save(fig, "uncertainty", "bayes_ridgeline")


if __name__ == "__main__":
    render()
