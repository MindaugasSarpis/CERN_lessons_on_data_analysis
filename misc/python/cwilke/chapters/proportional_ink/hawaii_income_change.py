"""Change in median income 2010 -> 2015, Hawaii counties (Wilke 17.5).

Shows that you *can* draw bars of differences — just make the quantity
explicit. Negative values extend downward.
"""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke.data import hawaii_income
from cwilke.theme import PRIMARY_BLUE, apply_base, hgrid, save


def render() -> None:
    apply_base()

    df = hawaii_income()
    wide = df.pivot(index="county", columns="year", values="median_income")
    wide["diff"] = wide[2015] - wide[2010]
    # Keep the ordering by 2015 income
    wide = wide.sort_values(2015, ascending=False)

    fig, ax = plt.subplots(figsize=(6.8, 4.2))
    ax.bar(wide.index, wide["diff"],
           color=PRIMARY_BLUE, width=0.7,
           edgecolor="#2c3e50", linewidth=0.5)
    ax.axhline(0, color="#2c3e50", linewidth=0.8)
    ax.set_ylim(-5000, 25000)
    ax.set_xlabel("county")
    ax.set_ylabel("5-year change in median income (USD)")
    ax.yaxis.set_major_formatter(
        plt.FuncFormatter(lambda x, _: f"${int(x):,}"))
    hgrid(ax)
    save(fig, "proportional_ink", "hawaii_income_change")


if __name__ == "__main__":
    render()
