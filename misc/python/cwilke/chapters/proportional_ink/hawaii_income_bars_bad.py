"""Truncated y-axis exaggerates income gaps in Hawaii counties (Wilke 17.1)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke.data import hawaii_income
from cwilke.theme import PRIMARY_BLUE, apply_base, hgrid, save, stamp_bad


def render() -> None:
    apply_base()

    df = hawaii_income()
    df = df[df["year"] == 2015].sort_values("median_income", ascending=False)

    fig, ax = plt.subplots(figsize=(6.8, 4.2))
    ax.bar(df["county"], df["median_income"],
           color=PRIMARY_BLUE, width=0.7,
           edgecolor="#2c3e50", linewidth=0.5)
    ax.set_ylim(50000, 75000)
    ax.set_xlabel("county")
    ax.set_ylabel("median income (USD)")
    ax.yaxis.set_major_formatter(
        plt.FuncFormatter(lambda x, _: f"${int(x):,}"))
    hgrid(ax)
    stamp_bad(fig)
    save(fig, "proportional_ink", "hawaii_income_bars_bad")


if __name__ == "__main__":
    render()
