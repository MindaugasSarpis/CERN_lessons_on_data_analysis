"""Scales link data values to aesthetics (Wilke fig 2.2).

The numbers 1–4 mapped onto a position scale, a shape scale, and a
colour scale.
"""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke.theme import apply_base, save


def render() -> None:
    apply_base()
    fig, axes = plt.subplots(3, 1, figsize=(6.8, 2.6))

    xs = [1, 2, 3, 4]

    # Position
    ax = axes[0]
    for x in xs:
        ax.scatter(x, 0, s=70, color="#0072B2", zorder=3)
    ax.set_xlim(0.5, 4.5)
    ax.set_xticks(xs)
    ax.set_ylim(-0.6, 0.6)
    ax.set_yticks([])
    ax.set_ylabel("position", rotation=0, ha="right", va="center",
                  fontsize=10, color="#455a64")
    ax.grid(True, axis="x", color="#b0bec5", linewidth=0.6)
    for sp in ("top", "right", "left"):
        ax.spines[sp].set_visible(False)

    # Shape
    ax = axes[1]
    shapes = ["o", "s", "D", "^"]
    for x, mk in zip(xs, shapes):
        ax.scatter(x, 0, s=160, marker=mk, facecolor="#cfd8dc",
                   edgecolor="#455a64", linewidth=1.2, zorder=3)
    ax.set_xlim(0.5, 4.5)
    ax.set_xticks(xs)
    ax.set_ylim(-0.6, 0.6)
    ax.set_yticks([])
    ax.set_ylabel("shape", rotation=0, ha="right", va="center",
                  fontsize=10, color="#455a64")
    for sp in ("top", "right", "left"):
        ax.spines[sp].set_visible(False)

    # Colour
    ax = axes[2]
    palette = ["#0082A6", "#4EBBB9", "#9CDFC2", "#D8F0CD"]
    for x, c in zip(xs, palette):
        ax.add_patch(plt.Rectangle((x - 0.35, -0.3), 0.7, 0.6, color=c))
    ax.set_xlim(0.5, 4.5)
    ax.set_xticks(xs)
    ax.set_ylim(-0.6, 0.6)
    ax.set_yticks([])
    ax.set_ylabel("colour", rotation=0, ha="right", va="center",
                  fontsize=10, color="#455a64")
    for sp in ("top", "right", "left"):
        ax.spines[sp].set_visible(False)

    fig.tight_layout()
    save(fig, "aesthetic_mapping", "basic_scales_example")


if __name__ == "__main__":
    render()
