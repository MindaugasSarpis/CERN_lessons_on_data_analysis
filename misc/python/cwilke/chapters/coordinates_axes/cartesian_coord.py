"""The standard Cartesian coordinate system (Wilke fig 3.1)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke.theme import PRIMARY_BLUE, apply_base, grid, save


def render() -> None:
    apply_base()

    fig, ax = plt.subplots(figsize=(5.0, 4.2))

    # Zero lines
    ax.axhline(0, color="#546e7a", linewidth=1.0)
    ax.axvline(0, color="#546e7a", linewidth=1.0)

    # Guide dashes
    guides = [(0, 2, 1, 1), (2, 2, 0, 1), (0, -1, -1, -1), (-1, -1, 0, -1)]
    for x0, x1, y0, y1 in guides:
        ax.plot([x0, x1], [y0, y1], color="#90a4ae",
                linewidth=0.9, linestyle=(0, (4, 3)))

    # Data points
    pts = [(-1, -1, "(–1, –1)", (-.25, -.35)),
           (0, 0, "(0, 0)",     (.15, .2)),
           (2, 1, "(2, 1)",     (.15, .2))]
    for x, y, label, (dx, dy) in pts:
        ax.scatter([x], [y], s=55, color=PRIMARY_BLUE,
                   zorder=5, edgecolor="white", linewidth=0.8)
        ax.text(x + dx, y + dy, label, fontsize=10, color="#2c3e50")

    # Axis-value callouts
    callouts = [(-1, -.5, "y = –1", "right"),
                (-.5, -1, "x = –1", "center"),
                (1, 1, "x = 2", "center"),
                (2, 0.5, "y = 1", "left")]
    for x, y, lbl, ha in callouts:
        ax.text(x, y, lbl, ha=ha, va="center", fontsize=9,
                color="#455a64", fontstyle="italic")

    ax.set_xlim(-2.2, 3.2)
    ax.set_ylim(-2.2, 2.2)
    ax.set_aspect("equal")
    ax.set_xticks(range(-2, 4))
    ax.set_yticks(range(-2, 3))
    ax.set_xlabel("x axis")
    ax.set_ylabel("y axis")
    grid(ax)

    fig.tight_layout()
    save(fig, "coordinates_axes", "cartesian_coord")


if __name__ == "__main__":
    render()
