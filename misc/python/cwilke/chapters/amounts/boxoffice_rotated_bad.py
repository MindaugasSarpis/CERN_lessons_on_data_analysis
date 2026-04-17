"""Vertical bars with rotated x-tick labels — Wilke's "ugly" example.

Rotated axis tick labels are hard to read and waste vertical space.
Prefer a horizontal bar chart instead.
"""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, hgrid, save, stamp_ugly


def render() -> None:
    apply_base()
    df = D.boxoffice().sort_values("amount", ascending=False)

    fig, ax = plt.subplots(figsize=(5.6, 5.4))
    ax.bar(df["title_short"], df["amount"] / 1e6,
           color=PRIMARY_BLUE, alpha=0.9, width=0.6)
    ax.set_ylabel("weekend gross (million USD)")
    ax.set_ylim(0, 75)
    ax.set_yticks([0, 20, 40, 60])

    # Rotated tick labels — the ugly part.
    plt.setp(ax.get_xticklabels(), rotation=45,
             ha="right", rotation_mode="anchor")
    hgrid(ax)
    ax.tick_params(axis="x", length=0)
    stamp_ugly(fig)
    fig.tight_layout()
    save(fig, "amounts", "boxoffice_rotated_bad")


if __name__ == "__main__":
    render()
