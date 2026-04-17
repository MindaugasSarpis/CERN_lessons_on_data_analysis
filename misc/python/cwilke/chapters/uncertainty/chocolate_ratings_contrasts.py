"""Contrasts of mean ratings vs US baseline (Wilke fig 16.8)."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t as student_t

from cwilke.data import cacao_ratings
from cwilke.theme import apply_base, hgrid, save


def render() -> None:
    apply_base()
    df = cacao_ratings()
    others = ["Austria", "Belgium", "Canada", "Peru", "Switzerland"]
    us = df[df["location"] == "US"]["rating"].values
    us_mean = us.mean()
    us_var = us.var(ddof=1)
    us_n = len(us)

    colors = {"99%": "#9fc1dd", "95%": "#4a87b3", "80%": "#0f4c75"}
    widths = {"99%": 1.5,       "95%": 2.75,      "80%": 4.0}

    rows = []
    for c in others:
        vals = df[df["location"] == c]["rating"].values
        n = len(vals)
        mean = vals.mean()
        diff = mean - us_mean
        se = np.sqrt(vals.var(ddof=1) / n + us_var / us_n)
        cis = {}
        for lev, p in [("99%", 0.995), ("95%", 0.975), ("80%", 0.90)]:
            crit = student_t.ppf(p, n + us_n - 2)
            cis[lev] = (diff - crit * se, diff + crit * se)
        rows.append((c, diff, cis))
    rows.sort(key=lambda r: r[1])

    fig, ax = plt.subplots(figsize=(7.8, 4.0))
    ax.axvline(0, color="gray", linestyle="--", linewidth=0.8)
    ys = np.arange(len(rows))
    for y, (c, diff, cis) in zip(ys, rows):
        for lev in ("80%", "95%", "99%"):
            lo, hi = cis[lev]
            ax.hlines(y, lo, hi, colors=colors[lev], linewidth=widths[lev])
        ax.plot(diff, y, "o", color="#D55E00", markersize=7)

    ax.set_yticks(ys)
    ax.set_yticklabels([r[0] for r in rows])
    ax.set_xlabel("difference in mean rating  (country minus US)")

    import matplotlib.lines as mlines
    handles = [mlines.Line2D([], [], color=colors[k], linewidth=widths[k],
                              label=k) for k in ("80%", "95%", "99%")]
    ax.legend(handles=handles, title="confidence level",
              loc="lower right", frameon=False, ncol=3)
    hgrid(ax)
    fig.tight_layout()
    save(fig, "uncertainty", "chocolate_ratings_contrasts")


if __name__ == "__main__":
    render()
