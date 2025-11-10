#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# --- Reproducibility ---------------------------------------------------------
rng = np.random.default_rng(42)

# --- Toy model: Gaussian "signal" + exponential "background" -----------------
mu, sigma = 5.0, 1.0
n_sig, n_bkg = 15_000, 100_000
signal = rng.normal(mu, sigma, n_sig)
background = rng.exponential(scale=2.0, size=n_bkg)
x = np.concatenate([signal, background])

# We'll display the same fixed window for all histograms
XRANGE = (0.0, 12.0)

# --- Make four panels with different binnings --------------------------------
bin_choices = {
    "Coarse (2 bins)": 2,
    "Medium (5 bins)": 5,
    "Finer (10 bins)": 10,
    "Fine (100 bins)":  100,
    "Fine (500 bins)":  500,
    "Fine (2000 bins)": 2000,
}

for i, (title, bins) in enumerate(bin_choices.items()):
    fig, ax = plt.subplots(figsize=(6, 4))

    # Compute histogram
    counts, bin_edges = np.histogram(x, bins=bins, range=XRANGE)
    counts = counts / counts.max()  # Normalize to max bin

    # Plot as step
    ax.step(bin_edges[:-1], counts, where='mid', linewidth=2, label="Total")
    ax.set_xlabel("x")
    ax.set_ylabel("Arb. Units")
    ax.grid(True, alpha=0.3)
    ax.set_title(title)

    plt.tight_layout()
    plt.show()
