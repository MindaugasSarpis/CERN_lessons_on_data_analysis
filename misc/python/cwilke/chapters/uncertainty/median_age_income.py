"""Income vs age with 2D error bars, Pennsylvania counties (Wilke 16.11)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke.data import pa_income_age
from cwilke.theme import apply_base, open_axes, save


def render() -> None:
    apply_base()
    df = pa_income_age()

    fig, ax = plt.subplots(figsize=(6.2, 4.6))
    ax.errorbar(df["age"], df["income"],
                xerr=df["age_moe"], yerr=df["income_moe"],
                fmt="o", color="#0072B2", ecolor="#0072B2",
                elinewidth=0.7, capsize=0, markersize=3)
    ax.set_xlabel("median age (years)")
    ax.set_ylabel("median income (USD)")
    ax.yaxis.set_major_formatter(
        plt.FuncFormatter(lambda v, _: f"${int(v/1000)}k"))
    open_axes(ax)
    save(fig, "uncertainty", "median_age_income")


if __name__ == "__main__":
    render()
