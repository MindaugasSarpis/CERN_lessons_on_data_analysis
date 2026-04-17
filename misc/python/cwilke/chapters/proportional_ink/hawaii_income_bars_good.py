"""Bars starting from 0 give an honest sense of Hawaii county incomes."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke.data import hawaii_income
from cwilke.theme import PRIMARY_BLUE, apply_base, hgrid, save


def render() -> None:
    apply_base()

    df = hawaii_income()
    df = df[df["year"] == 2015].sort_values("median_income", ascending=False)

    fig, ax = plt.subplots(figsize=(6.8, 4.2))
    ax.bar(df["county"], df["median_income"],
           color=PRIMARY_BLUE, width=0.7,
           edgecolor="#2c3e50", linewidth=0.5)
    ax.set_ylim(0, 78000)
    ax.set_xlabel("county")
    ax.set_ylabel("median income (USD)")
    ax.yaxis.set_major_formatter(
        plt.FuncFormatter(lambda x, _: f"${int(x):,}"))
    hgrid(ax)
    save(fig, "proportional_ink", "hawaii_income_bars_good")


if __name__ == "__main__":
    render()
