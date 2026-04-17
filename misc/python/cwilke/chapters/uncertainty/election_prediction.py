"""Normal distribution with shaded yellow/blue win regions (Wilke fig 16.2)."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from cwilke.theme import apply_base, save


def _normal_pdf(x, mu, sd):
    return np.exp(-0.5 * ((x - mu) / sd) ** 2) / (sd * np.sqrt(2 * np.pi))


def render() -> None:
    apply_base()
    mu, sd = 1.02, 0.9
    x = np.linspace(-2.5, 5.0, 400)
    y = _normal_pdf(x, mu, sd)

    fig, ax = plt.subplots(figsize=(7.0, 3.8))
    ax.fill_between(x[x <= 0], y[x <= 0], color="#f8f1a9")
    ax.fill_between(x[x >= 0], y[x >= 0], color="#b1daf4")
    ax.plot(x, y, color="#2c3e50", linewidth=1.0)
    ax.axvline(0, color="gray", linestyle="--", linewidth=0.8)

    # best estimate marker
    ax.plot([mu, mu], [0, _normal_pdf(mu, mu, sd) + 0.04],
            color="#2c3e50", linewidth=0.8)
    ax.annotate("best estimate", xy=(mu + 0.05, _normal_pdf(mu, mu, sd) + 0.04),
                fontsize=10, va="top", ha="left")

    # margin of error (95%) arrow
    lo = mu - 1.96 * sd
    hi = mu + 1.96 * sd
    y_arrow = _normal_pdf(lo, mu, sd) + 0.01
    ax.annotate("", xy=(hi, y_arrow), xytext=(lo, y_arrow),
                arrowprops=dict(arrowstyle="<->", color="#2c3e50", lw=0.9))
    ax.text(mu, y_arrow + 0.005, "margin of error",
            ha="center", va="bottom", fontsize=10)

    ax.text(mu + 2.3 * sd, 0.06, "blue wins", ha="center", fontsize=10)
    ax.text(mu - 2.5 * sd, 0.06, "yellow wins", ha="center", fontsize=10)

    ax.set_xlabel("percentage point advantage for blue")
    ax.set_yticks([])
    ax.set_xlim(-2.5, 5.0)
    ax.set_ylim(0, _normal_pdf(mu, mu, sd) + 0.08)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.1f}%"))
    save(fig, "uncertainty", "election_prediction")


if __name__ == "__main__":
    render()
