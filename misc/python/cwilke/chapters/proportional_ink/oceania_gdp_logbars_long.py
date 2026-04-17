"""Same log-scale bars, but starting at 10^-9 B — just as arbitrary (17.8)."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from cwilke.data import oceania_gdp
from cwilke.theme import PRIMARY_BLUE, apply_base, save, stamp_bad, vgrid


def render() -> None:
    apply_base()
    df = oceania_gdp().sort_values("GDP")
    x_start = 0.0  # log10(1 USD)
    log_gdp = np.log10(df["GDP"].values)

    fig, ax = plt.subplots(figsize=(7.0, 3.6))
    ax.barh(df["country"], log_gdp - x_start, left=x_start,
            color=PRIMARY_BLUE, height=0.7,
            edgecolor="#2c3e50", linewidth=0.5)
    exps = [0, 2, 4, 6, 8, 10, 12]
    ax.set_xticks(exps)
    ax.set_xticklabels([f"$10^{{{e - 9}}}$" for e in exps])
    ax.set_xlim(0, np.log10(9.9e11))
    ax.set_xlabel("GDP (billion USD)")
    vgrid(ax)
    stamp_bad(fig)
    save(fig, "proportional_ink", "oceania_gdp_logbars_long")


if __name__ == "__main__":
    render()
