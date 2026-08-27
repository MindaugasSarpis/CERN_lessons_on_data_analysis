#!/usr/bin/env python3
"""Generate LHCb seminar-dataset demo figures (synthetic but realistic), matching
the real LHCb open-data masterclass channel D0 -> K- pi+.

Outputs to lectures/content/public/figures/:
  lhcb_d0_spectrum.png  — K-pi invariant-mass spectrum with the D0 peak
  lhcb_d0_fit.png       — the D0 peak fitted with a Gaussian + linear background
Clean light background to sit in the deck's white figure cards.
Reference: CERN Open Data Portal, LHCb masterclass D0->Kpi (record 401).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.optimize import curve_fit

OUT = Path(__file__).resolve().parents[1] / "lectures/content/public/figures"
rng = np.random.default_rng(1865)
MD0 = 1.86484  # D0 mass, GeV
LO, HI = 1.80, 1.94

def gauss(x, mu, sig):
    return np.exp(-0.5 * ((x - mu) / sig) ** 2)

# ---- Simulate the K-pi invariant mass of ~60k pre-selected candidates ----
signal = rng.normal(MD0, 0.0085, 22000)                 # D0 peak (detector resolution)
background = rng.uniform(LO, HI, 40000)                  # combinatorial background
mass = np.concatenate([signal, background])
mass = mass[(mass > LO) & (mass < HI)]

# ---- Figure 1: full spectrum ----
plt.figure(figsize=(7.2, 4.0))
counts, edges, _ = plt.hist(mass, bins=70, range=(LO, HI),
                            histtype="stepfilled", color="#2563eb", alpha=0.85,
                            edgecolor="#1e3a8a", linewidth=0.4)
plt.xlabel(r"$K^-\pi^+$ invariant mass  [GeV]")
plt.ylabel("Candidates / 2 MeV")
plt.title("LHCb $D^0 \\to K^-\\pi^+$ spectrum (illustrative)")
ypk = counts[np.searchsorted(edges, MD0) - 1]
plt.annotate(r"$D^0$", (MD0, ypk), textcoords="offset points", xytext=(14, -6),
             ha="left", fontsize=11, color="#0f172a",
             arrowprops=dict(arrowstyle="-", color="#64748b", lw=0.8))
plt.tight_layout()
plt.savefig(OUT / "lhcb_d0_spectrum.png", dpi=140)
plt.close()

# ---- Figure 2: fit the D0 peak (Gaussian + linear background) ----
y, edges = np.histogram(mass, bins=70, range=(LO, HI))
x = 0.5 * (edges[:-1] + edges[1:])
yerr = np.sqrt(np.maximum(y, 1))

def model(x, A, mu, sig, b0, b1):
    return A * gauss(x, mu, sig) + b0 + b1 * (x - MD0)

p0 = [y.max(), MD0, 0.009, np.median(y), 0.0]
popt, pcov = curve_fit(model, x, y, p0=p0, sigma=yerr, absolute_sigma=True)
perr = np.sqrt(np.diag(pcov))
chi2 = np.sum(((y - model(x, *popt)) / yerr) ** 2)
dof = len(x) - len(popt)

plt.figure(figsize=(7.2, 4.0))
plt.errorbar(x, y, yerr=yerr, fmt="o", ms=4, color="#0f172a", label="Data")
xf = np.linspace(LO, HI, 400)
plt.plot(xf, model(xf, *popt), "-", color="#dc2626", lw=2,
         label=(f"Fit: $m(D^0)$ = {popt[1]*1000:.1f} ± {perr[1]*1000:.1f} MeV\n"
                f"$\\chi^2$/dof = {chi2:.0f}/{dof}"))
plt.plot(xf, popt[3] + popt[4] * (xf - MD0), "--", color="#64748b", lw=1.2, label="Background")
plt.xlabel(r"$K^-\pi^+$ invariant mass  [GeV]")
plt.ylabel("Candidates / 2 MeV")
plt.title(r"Fitting the $D^0$ peak (illustrative)")
plt.legend(fontsize=9, loc="upper right")
plt.tight_layout()
plt.savefig(OUT / "lhcb_d0_fit.png", dpi=140)
plt.close()

# remove the old dimuon figures if present
for old in ("lhcb_dimuon_spectrum.png", "lhcb_jpsi_fit.png"):
    p = OUT / old
    if p.exists():
        p.unlink()

print(f"wrote lhcb_d0_spectrum.png and lhcb_d0_fit.png")
print(f"D0 fit: m = {popt[1]*1000:.1f} +/- {perr[1]*1000:.1f} MeV (PDG 1864.84), chi2/dof = {chi2:.0f}/{dof}")
