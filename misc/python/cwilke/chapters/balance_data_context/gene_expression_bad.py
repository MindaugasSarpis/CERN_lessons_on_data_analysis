"""Paired data with a grid but no diagonal — structure hidden (Wilke fig 23.14)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, grid, save, stamp_bad


def render() -> None:
    apply_base()
    df = D.gene_expression_t7()

    fig, ax = plt.subplots(figsize=(5.4, 5.4))
    ax.scatter(df["tpm_wt"], df["tpm_mutant"], s=54,
               color="#0072B2", alpha=0.85,
               edgecolor="white", linewidth=0.6, zorder=3)
    for _, row in df[df["label"] != ""].iterrows():
        ax.annotate(row["label"], (row["tpm_wt"], row["tpm_mutant"]),
                    xytext=(7, -10), textcoords="offset points",
                    fontsize=10, fontstyle="italic",
                    color="#2c3e50")

    lo, hi = 2e-4, 3.3e-1
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(lo, hi)
    ax.set_ylim(lo, hi)
    ax.set_aspect("equal")
    ax.set_xlabel("wild-type mRNA abundance (TPM)")
    ax.set_ylabel("mutant mRNA abundance (TPM)")
    grid(ax)

    stamp_bad(fig)
    fig.tight_layout()
    save(fig, "balance_data_context", "gene_expression_bad")


if __name__ == "__main__":
    render()
