"""Pet ownership — clear but forgettable bar plot (Wilke fig 29.8)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, save, vgrid


def render() -> None:
    apply_base()

    df = D.pet_ownership().sort_values("households")
    colours = ["#BD3828D0" if p == "cats" else "#B0B0B0D0"
               for p in df["pet"]]

    fig, ax = plt.subplots(figsize=(7.6, 3.0))
    ax.barh(df["pet"], df["households"],
            color=colours, edgecolor="white", linewidth=0.4)

    for i, (_, row) in enumerate(df.iterrows()):
        ax.text(row["households"] + 5e5, i,
                f"{row['households'] / 1e6:.1f}M",
                va="center", fontsize=10, color="#2c3e50")

    ax.set_xlabel("households")
    ax.set_xlim(0, 47e6)
    ax.set_xticks([0, 10e6, 20e6, 30e6, 40e6])
    ax.set_xticklabels(["0", "10M", "20M", "30M", "40M"])
    vgrid(ax)

    fig.tight_layout()
    save(fig, "telling_a_story", "petownership_bar")


if __name__ == "__main__":
    render()
