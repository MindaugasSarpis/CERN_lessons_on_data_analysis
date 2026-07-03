#!/usr/bin/env python3
"""Generate LHCb dimuon running-project demo figures (synthetic but realistic).

Outputs to lectures/content/public/figures/:
  lhcb_dimuon_spectrum.png  — dimuon invariant-mass spectrum (log-y), J/psi, psi(2S), Y peaks
  lhcb_jpsi_fit.png         — zoomed J/psi peak with a Gaussian + background fit
Clean light background to sit in the deck's white figure cards.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.optimize import curve_fit

OUT = Path(__file__).resolve().parents[1] / "lectures/content/public/figures"
rng = np.random.default_rng(1867)

# ---- Simulate a dimuon sample (masses in GeV) ----
def gauss(x, mu, sig):
    return np.exp(-0.5 * ((x - mu) / sig) ** 2)

n_bg = 200_000
bg = rng.exponential(3.0, n_bg)                       # smooth falling background
bg = bg[(bg > 2.0) & (bg < 12.0)]
peaks = np.concatenate([
    rng.normal(3.097, 0.030, 26_000),   # J/psi
    rng.normal(3.686, 0.033, 5_000),    # psi(2S)
    rng.normal(9.460, 0.090, 4_500),    # Upsilon(1S)
])
mass = np.concatenate([bg, peaks])
mass = mass[(mass > 2.0) & (mass < 12.0)]

# ---- Figure 1: full spectrum, log-y ----
plt.figure(figsize=(7.2, 4.0))
counts, edges, _ = plt.hist(mass, bins=240, range=(2, 12),
                            histtype="stepfilled", color="#2563eb", alpha=0.85,
                            edgecolor="#1e3a8a", linewidth=0.4)
plt.yscale("log")
plt.xlabel("Dimuon invariant mass  $m_{\\mu\\mu}$  [GeV]")
plt.ylabel("Candidates / 0.04 GeV")
plt.title("LHCb dimuon spectrum (illustrative)")
for x, name in [(3.097, "J/$\\psi$"), (3.686, "$\\psi$(2S)"), (9.46, "$\\Upsilon$")]:
    yi = counts[np.searchsorted(edges, x) - 1]
    plt.annotate(name, (x, yi), textcoords="offset points", xytext=(0, 8),
                 ha="center", fontsize=10, color="#0f172a",
                 arrowprops=dict(arrowstyle="-", color="#64748b", lw=0.8))
plt.tight_layout()
plt.savefig(OUT / "lhcb_dimuon_spectrum.png", dpi=140)
plt.close()

# ---- Figure 2: zoomed J/psi with Gaussian + linear-background fit ----
sel = mass[(mass > 2.8) & (mass < 3.4)]
y, edges = np.histogram(sel, bins=40, range=(2.8, 3.4))
x = 0.5 * (edges[:-1] + edges[1:])
yerr = np.sqrt(np.maximum(y, 1))

def model(x, A, mu, sig, b0, b1):
    return A * gauss(x, mu, sig) + b0 + b1 * (x - 3.1)

p0 = [y.max(), 3.097, 0.03, np.median(y), 0.0]
popt, pcov = curve_fit(model, x, y, p0=p0, sigma=yerr, absolute_sigma=True)
perr = np.sqrt(np.diag(pcov))
chi2 = np.sum(((y - model(x, *popt)) / yerr) ** 2)
dof = len(x) - len(popt)

plt.figure(figsize=(7.2, 4.0))
plt.errorbar(x, y, yerr=yerr, fmt="o", ms=4, color="#0f172a", label="Data")
xf = np.linspace(2.8, 3.4, 400)
plt.plot(xf, model(xf, *popt), "-", color="#dc2626", lw=2,
         label=(f"Fit: $m$ = {popt[1]:.4f} ± {perr[1]:.4f} GeV\n"
                f"$\\chi^2$/dof = {chi2:.0f}/{dof}"))
plt.plot(xf, popt[3] + popt[4] * (xf - 3.1), "--", color="#64748b", lw=1.2, label="Background")
plt.xlabel("Dimuon invariant mass  $m_{\\mu\\mu}$  [GeV]")
plt.ylabel("Candidates / 0.015 GeV")
plt.title("Fitting the J/$\\psi$ peak (illustrative)")
plt.legend(fontsize=9, loc="upper right")
plt.tight_layout()
plt.savefig(OUT / "lhcb_jpsi_fit.png", dpi=140)
plt.close()

print("wrote lhcb_dimuon_spectrum.png and lhcb_jpsi_fit.png")
print(f"J/psi fit: m = {popt[1]:.4f} +/- {perr[1]:.4f} GeV (PDG 3.0969), chi2/dof = {chi2:.0f}/{dof}")
