"""Trellis (faceted) bar chart of Virginia mortality (Wilke fig 26.8)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke.data import va_deaths
from cwilke.theme import PRIMARY_BLUE, apply_base, hgrid, save


def render() -> None:
    apply_base()
    df = va_deaths()

    groups = ["rural female", "rural male", "urban female", "urban male"]
    mapping = {
        "rural female": "Rural Female",
        "rural male":   "Rural Male",
        "urban female": "Urban Female",
        "urban male":   "Urban Male",
    }

    fig, axes = plt.subplots(2, 2, figsize=(7.6, 5.2), sharex=True, sharey=True)
    axes = axes.flatten()

    for ax, name in zip(axes, groups):
        sub = df[df["group"] == mapping[name]]
        ax.bar(sub["age"].astype(str), sub["rate"],
               color=PRIMARY_BLUE, alpha=0.85, width=0.75,
               edgecolor="#2c3e50", linewidth=0.4)
        ax.set_title(name, fontsize=11)
        ax.set_ylim(0, 80)
        hgrid(ax)

    for ax in axes[2:]:
        ax.set_xlabel("age group")
    for ax in axes[::2]:
        ax.set_ylabel("deaths / 1000")

    fig.tight_layout()
    save(fig, "no_3d_jitter", "va_deaths_trellis")


if __name__ == "__main__":
    render()
