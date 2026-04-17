"""Five aesthetics at once: displacement, mpg, power, weight, cylinders
(Wilke fig 2.5).

x = displacement, y = mpg, colour (sequential) = hp, size = weight,
shape = number of cylinders.
"""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, grid, save


def render() -> None:
    apply_base()
    df = D.mtcars().copy()

    shapes = {4: "D", 6: "^", 8: "o"}
    sizes = (df["wt"] - df["wt"].min()) / (df["wt"].max() - df["wt"].min())
    marker_sizes = 40 + 280 * sizes

    fig, ax = plt.subplots(figsize=(7.2, 5.4))

    # Scatter, using shape for cylinders
    for cyl, mk in shapes.items():
        mask = df["cyl"] == cyl
        sc = ax.scatter(df.loc[mask, "disp"], df.loc[mask, "mpg"],
                        c=df.loc[mask, "hp"], s=marker_sizes[mask],
                        cmap="viridis", vmin=df["hp"].min(),
                        vmax=df["hp"].max(),
                        marker=mk, edgecolor="white", linewidth=0.7,
                        alpha=0.95)

    ax.set_xlabel("displacement (cu. in.)")
    ax.set_ylabel("fuel efficiency (mpg)")
    grid(ax)

    cbar = fig.colorbar(sc, ax=ax, fraction=0.045, pad=0.02)
    cbar.set_label("power (hp)", fontsize=10)

    # Legends for shape (cylinders) and size (weight)
    from matplotlib.lines import Line2D
    shape_handles = [
        Line2D([0], [0], marker=shapes[c], color="w",
               markerfacecolor="#607d8b", markeredgecolor="white",
               markersize=10, label=f"{c}")
        for c in shapes
    ]
    ax.legend(handles=shape_handles, title="cylinders",
              loc="upper right", fontsize=9, title_fontsize=10,
              frameon=False)

    # Size legend as separate text block
    size_handles = [
        Line2D([0], [0], marker="o", color="w",
               markerfacecolor="#607d8b", markeredgecolor="white",
               markersize=ms, label=f"{w:.1f}")
        for ms, w in [(5, 1.6), (8, 3.2), (12, 5.4)]
    ]
    ax.add_artist(ax.legend(handles=shape_handles, title="cylinders",
                            loc="upper right", fontsize=9,
                            title_fontsize=10, frameon=False))
    ax.legend(handles=size_handles, title="weight (1000 lbs)",
              loc="upper center", bbox_to_anchor=(0.55, 1.0),
              fontsize=9, title_fontsize=10, frameon=False)

    fig.tight_layout()
    save(fig, "aesthetic_mapping", "mtcars_five_scale")


if __name__ == "__main__":
    render()
