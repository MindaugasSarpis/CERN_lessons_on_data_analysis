"""Slopegraph of top-10 CO2-emission changes, 2000 vs 2010
(Wilke fig 12.14)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke.theme import PRIMARY_BLUE, apply_base, save


def render() -> None:
    apply_base()
    # Ten countries with the largest per-capita changes (from the book).
    rows = [
        ("Qatar",               55.5, 44.0),
        ("Trinidad and Tobago", 38.5, 22.5),
        ("Kuwait",              31.8, 27.0),
        ("United Arab Emirates",25.2, 19.5),
        ("Bahrain",             23.8, 19.5),
        ("Oman",                17.1, 10.4),
        ("Equatorial Guinea",    7.2,  1.0),
        ("Kazakhstan",          14.3, 10.3),
        ("Singapore",            7.2,  2.9),
        ("Netherlands Antilles",12.1, 24.2),
    ]
    countries = [r[0] for r in rows]
    v2010 = [r[1] for r in rows]
    v2000 = [r[2] for r in rows]

    fig, ax = plt.subplots(figsize=(5.2, 5.2))
    for c, a, b in zip(countries, v2000, v2010):
        ax.plot([2000, 2010], [a, b], color="#9e9e9e", linewidth=1.0, zorder=1)
        ax.scatter([2000, 2010], [a, b], s=60,
                   facecolors="white", edgecolors=PRIMARY_BLUE,
                   linewidths=1.2, zorder=2)
        ax.scatter([2000, 2010], [a, b], s=18,
                   color=PRIMARY_BLUE, zorder=3)
        ax.text(2010 + 0.4, b, c, va="center", fontsize=9,
                color="#444444")
    ax.set_xlim(1998, 2018)
    ax.set_ylim(0, 63)
    ax.set_xticks([2000, 2010])
    ax.set_xticklabels(["2000", "2010"])
    ax.xaxis.set_ticks_position("top")
    ax.xaxis.set_label_position("top")
    ax.set_ylabel("CO$_2$ emissions (tons / person)")
    ax.spines["bottom"].set_visible(False)
    ax.tick_params(axis="x", length=0)

    fig.tight_layout()
    save(fig, "associations", "co2_slopegraph")


if __name__ == "__main__":
    render()
