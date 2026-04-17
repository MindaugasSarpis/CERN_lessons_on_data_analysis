"""Bar chart with a truncated y-axis exaggerating small differences (Wilke fig 17.1)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke.theme import PRIMARY_BLUE, apply_base, hgrid, save, stamp_bad


def render() -> None:
    apply_base()

    labels = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    values = [22, 25, 31, 28, 36]

    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.bar(labels, values,
           color=PRIMARY_BLUE, alpha=0.9, width=0.7,
           edgecolor="#2c3e50", linewidth=0.5)
    ax.set_ylim(20, 38)
    ax.set_ylabel("sales (million USD)")
    ax.set_xlabel("weekday")
    hgrid(ax)
    stamp_bad(fig)
    save(fig, "proportional_ink", "truncated_bar_bad")


if __name__ == "__main__":
    render()
