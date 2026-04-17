"""Athletes composite — inconsistent visual language across panels (bad).

Panel (a) uses a single neutral blue for both sexes; panel (b) uses
pink/blue for F/M; panel (c) uses green/blue for F/M. Sex ordering
also flips in panel (c) (Wilke fig 21.7).
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import apply_base, hgrid, save, stamp_bad


def _boxplot_by(ax, df, *, groupby, value, group_order, colors, width=0.34):
    positions = np.arange(len(group_order))
    for i, sex in enumerate(("f", "m")):
        sub = df[df["sex"] == sex]
        data = [sub[sub[groupby] == g][value].dropna().values
                for g in group_order]
        bp = ax.boxplot(
            data,
            positions=positions + (i - 0.5) * (width + 0.04),
            widths=width,
            patch_artist=True,
            showfliers=False,
            medianprops={"color": "#2c3e50", "linewidth": 1.3},
        )
        for box in bp["boxes"]:
            box.set_facecolor(colors[i])
            box.set_edgecolor(colors[i])
            box.set_alpha(0.55)
        for whisker in bp["whiskers"] + bp["caps"]:
            whisker.set_color(colors[i])
    ax.set_xticks(positions)
    ax.set_xticklabels(group_order)


def render() -> None:
    apply_base()
    df = D.aus_athletes()
    df = df[df["sport"].isin(["track (sprint)", "track (400m)",
                              "field", "swimming", "basketball",
                              "water polo"])].copy()
    df["sport"] = df["sport"].str.replace("track.*", "track", regex=True)

    fig = plt.figure(figsize=(10.0, 7.5))
    gs = fig.add_gridspec(2, 2, width_ratios=[0.9, 1.4],
                          height_ratios=[1, 1],
                          hspace=0.45, wspace=0.35)
    ax_a = fig.add_subplot(gs[0, 0])
    ax_b = fig.add_subplot(gs[0, 1])
    ax_c = fig.add_subplot(gs[1, :])

    # --- (a) counts of f / m with same blue for both -----------------------
    counts = df["sex"].value_counts().reindex(["f", "m"])
    ax_a.bar(["female", "male"], counts.values,
             color="#56B4E9", alpha=0.85, width=0.65)
    ax_a.set_ylabel("number")
    ax_a.set_ylim(0, 95)
    hgrid(ax_a)
    ax_a.set_title("a", loc="left", fontweight="bold", color="#455a64")

    # --- (b) scatter rcc vs wcc, pink/blue --------------------------------
    sex_colors_b = {"f": "#CC79A7", "m": "#56B4E9"}
    for sex, color in sex_colors_b.items():
        sub = df[df["sex"] == sex]
        marker = "o" if sex == "f" else "s"
        ax_b.scatter(sub["rcc"], sub["wcc"], s=30, color=color,
                     edgecolor="white", linewidth=0.6, alpha=0.85,
                     label="female" if sex == "f" else "male",
                     marker=marker)
    ax_b.set_xlabel("RBC count")
    ax_b.set_ylabel("WBC count")
    ax_b.set_xlim(3.8, 6.4)
    ax_b.set_ylim(2.2, 11)
    hgrid(ax_b)
    ax_b.legend(loc="lower right", fontsize=9)
    ax_b.set_title("b", loc="left", fontweight="bold", color="#455a64")

    # --- (c) boxplot with green/blue and reversed order -------------------
    sports = sorted(df["sport"].unique())
    _boxplot_by(ax_c, df, groupby="sport", value="pcBfat",
                group_order=sports, colors=["#009E73", "#56B4E9"])
    ax_c.set_ylabel("% body fat")
    ax_c.set_xlabel("")
    hgrid(ax_c)
    # legend — note reversed colours vs. panel b (the bad part)
    from matplotlib.patches import Patch
    legend_handles = [
        Patch(facecolor="#009E73", label="male", alpha=0.6),
        Patch(facecolor="#56B4E9", label="female", alpha=0.6),
    ]
    ax_c.legend(handles=legend_handles, loc="upper right", fontsize=9)
    ax_c.set_title("c", loc="left", fontweight="bold", color="#455a64")

    stamp_bad(fig)
    fig.tight_layout()
    save(fig, "multi_panel", "athletes_composite_inconsistent")


if __name__ == "__main__":
    render()
