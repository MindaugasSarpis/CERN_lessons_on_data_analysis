"""Four views of a 25/75 pie rotated in 3D (Wilke fig 26.1).

Rotating a flat pie into space distorts the slice sizes. Only the
straight-on (top) view is faithful.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Wedge

from cwilke.theme import apply_base, save, stamp_bad


def _slice_ellipse(ax, cx, cy, rx, ry, start_deg, end_deg, color):
    """Draw a filled wedge on an ellipse from start_deg to end_deg (CCW)."""
    # Sample the arc
    theta = np.linspace(np.deg2rad(start_deg), np.deg2rad(end_deg), 80)
    x = cx + rx * np.cos(theta)
    y = cy + ry * np.sin(theta)
    poly_x = np.concatenate([[cx], x, [cx]])
    poly_y = np.concatenate([[cy], y, [cy]])
    ax.fill(poly_x, poly_y, color=color, edgecolor="white", linewidth=1.2)


def _draw_panel(ax, tilt, label):
    """tilt in [0,1]: 1 = flat top-down; 0 = edge-on."""
    cx, cy = 0.0, 0.0
    rx = 1.0
    ry = tilt * 1.0
    # rim thickness is set by (1 - tilt)
    thickness = 0.18 * (1 - tilt) + 0.02

    # "side wall" of the pie, darkened — sketch with a dark band at bottom
    # Draw side as band (below the top ellipse), for the 25% and 75% slices.
    # For simplicity just draw the top ellipse.
    # 25% slice (blue): from 90 to 0 (top-right quadrant)
    _slice_ellipse(ax, cx, cy, rx, ry, 0, 90, "#0072B2")
    # 75% slice (light gray): from 90 to 360 (rest)
    _slice_ellipse(ax, cx, cy, rx, ry, 90, 360, "#cccccc")

    # outline
    e = Ellipse((cx, cy), 2 * rx, 2 * ry, fill=False,
                edgecolor="#2c3e50", linewidth=1.0)
    ax.add_patch(e)

    # side wall hint: fill a strip below centerline
    if tilt < 0.95:
        # side band showing the "height" of the pie
        side = Wedge((cx, cy - thickness), rx, 180, 360,
                     width=0, edgecolor="none")
        # Draw simple rectangle behind for depth illusion
        xs = np.linspace(-rx, rx, 200)
        ys_top = cy - ry * np.sqrt(np.clip(1 - (xs / rx) ** 2, 0, 1))
        ys_bot = ys_top - thickness
        ax.fill_between(xs, ys_bot, ys_top, color="#4c6a8c", linewidth=0,
                        zorder=1)

    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ("top", "right", "left", "bottom"):
        ax.spines[s].set_visible(False)
    ax.set_title(label, fontsize=11)


def render() -> None:
    apply_base()
    fig, axes = plt.subplots(2, 2, figsize=(6.8, 6.4))
    panels = [
        (axes[0, 0], 0.25, "(a) flat angle"),
        (axes[0, 1], 0.55, "(b)"),
        (axes[1, 0], 0.80, "(c)"),
        (axes[1, 1], 1.00, "(d) top-down (correct)"),
    ]
    for ax, tilt, lab in panels:
        _draw_panel(ax, tilt, lab)
    fig.suptitle("The same 25% / 75% pie seen from four angles",
                 fontsize=12, y=0.98)
    stamp_bad(fig)
    save(fig, "no_3d_jitter", "rotated_pie")


if __name__ == "__main__":
    render()
