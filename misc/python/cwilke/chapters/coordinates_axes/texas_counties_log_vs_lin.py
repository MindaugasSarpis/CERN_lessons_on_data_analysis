"""Texas county populations, relative to the median (Wilke figs 3.5-3.6).

Left: linear y — crammed near zero, obscuring values below the median.
Right: log10 y — symmetric about 1 and easy to read. The linear panel
is stamped "bad"; the log panel is the recommended design.
"""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, hgrid, save


def render() -> None:
    apply_base()
    df = D.us_tx_counties_population().copy()
    df["index"] = df["rank"]

    top6 = df.nlargest(3, "pop2010")["county"].tolist()
    bot3 = df.nsmallest(3, "pop2010")["county"].tolist()
    highlight = set(top6 + bot3)

    fig, (ax_bad, ax_good) = plt.subplots(1, 2, figsize=(11.2, 4.6))

    # --- Bad: linear y scale
    ax_bad.scatter(df["index"], df["popratio"], s=6,
                   color=PRIMARY_BLUE, alpha=0.9)
    for county in top6:
        row = df[df["county"] == county].iloc[0]
        ax_bad.annotate(county, (row["index"], row["popratio"]),
                        xytext=(8, -4), textcoords="offset points",
                        fontsize=9, color="#2c3e50")
    ax_bad.set_xlabel("Texas counties, from most to least populous")
    ax_bad.set_ylabel("population / median")
    ax_bad.set_xlim(0, len(df) + 1)
    ax_bad.set_xticks([])
    hgrid(ax_bad)
    ax_bad.set_title("linear scale", color="#b34b4b", fontweight="bold")

    # --- Good: log y scale
    ax_good.axhline(1, linestyle="--", color="#546e7a", linewidth=0.8)
    ax_good.scatter(df["index"], df["popratio"], s=6,
                    color=PRIMARY_BLUE, alpha=0.9)
    for county in highlight:
        row = df[df["county"] == county].iloc[0]
        ax_good.annotate(county, (row["index"], row["popratio"]),
                         xytext=(6, -4), textcoords="offset points",
                         fontsize=9, color="#2c3e50")
    ax_good.set_yscale("log")
    ax_good.set_yticks([0.01, 0.1, 1, 10, 100])
    ax_good.set_yticklabels(["0.01", "0.1", "1", "10", "100"])
    ax_good.set_ylabel("population / median")
    ax_good.set_xlabel("Texas counties, from most to least populous")
    ax_good.set_xlim(0, len(df) + 1)
    ax_good.set_xticks([])
    hgrid(ax_good)
    ax_good.set_title("log scale", color="#2c8a4b", fontweight="bold")

    fig.tight_layout()
    save(fig, "coordinates_axes", "texas_counties_log_vs_lin")


if __name__ == "__main__":
    render()
