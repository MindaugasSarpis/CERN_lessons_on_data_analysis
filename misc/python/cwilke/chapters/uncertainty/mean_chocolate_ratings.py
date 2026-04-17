"""Graded error bars of mean chocolate ratings by country (Wilke 16.7)."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t as student_t

from cwilke.data import cacao_ratings
from cwilke.theme import apply_base, hgrid, save


def render() -> None:
    apply_base()
    df = cacao_ratings()
    countries = ["Austria", "Belgium", "Canada", "Peru", "Switzerland", "US"]
    # compute CIs
    colors = {"99%": "#9fc1dd", "95%": "#4a87b3", "80%": "#0f4c75"}
    widths = {"99%": 1.5,       "95%": 2.75,      "80%": 4.0}

    rows = []
    for c in countries:
        vals = df[df["location"] == c]["rating"].values
        n = len(vals)
        mean = vals.mean()
        se = vals.std(ddof=1) / np.sqrt(n)
        cis = {}
        for lev, p in [("99%", 0.995), ("95%", 0.975), ("80%", 0.90)]:
            crit = student_t.ppf(p, n - 1)
            cis[lev] = (mean - crit * se, mean + crit * se)
        rows.append((c, mean, cis))
    rows.sort(key=lambda r: r[1])

    fig, ax = plt.subplots(figsize=(7.8, 4.2))
    ys = np.arange(len(rows))
    for y, (c, mean, cis) in zip(ys, rows):
        for lev in ("80%", "95%", "99%"):
            lo, hi = cis[lev]
            ax.hlines(y, lo, hi, colors=colors[lev], linewidth=widths[lev])
        ax.plot(mean, y, "o", color="#D55E00", markersize=7)

    ax.set_yticks(ys)
    ax.set_yticklabels([r[0] for r in rows])
    ax.set_xlabel("mean rating")
    ax.set_xlim(2.6, 3.6)

    import matplotlib.lines as mlines
    handles = [mlines.Line2D([], [], color=colors[k], linewidth=widths[k],
                              label=k) for k in ("80%", "95%", "99%")]
    ax.legend(handles=handles, title="confidence level",
              loc="lower right", frameon=False, ncol=3)
    hgrid(ax)
    fig.tight_layout()
    save(fig, "uncertainty", "mean_chocolate_ratings")


if __name__ == "__main__":
    render()
