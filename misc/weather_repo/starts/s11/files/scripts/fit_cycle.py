import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

temp = np.loadtxt("data/raw/weather.csv", delimiter=",",
                  skiprows=1, usecols=1)
days = temp.reshape(-1, 24)
good = (days != -999).all(axis=1)
T = days[good].mean(axis=1)
d = np.arange(len(days))[good]
print("days", len(days), "with 24 hours", len(T))

fig, ax = plt.subplots(figsize=(8, 3))
ax.plot(d, T, ".", ms=2)
ax.set_xlabel("day since 2016-01-01")
ax.set_ylabel("daily mean (°C)")
fig.savefig("results/daily_means.png", dpi=150, bbox_inches="tight")

om = 2 * np.pi / 365.25
A = np.column_stack([np.ones(len(d)), np.cos(om * d), np.sin(om * d)])
theta, *rest = np.linalg.lstsq(A, T, rcond=None)
c, a, b = theta
print(f"c = {c:.3f}, a = {a:.3f}, b = {b:.3f}")

amp = np.hypot(a, b)
d0 = (np.arctan2(b, a) + np.pi) / om
print(f"amplitude {amp:.2f} °C, coldest on day {d0:.1f}")

def cycle(d, c, amp, d0):
    return c - amp * np.cos(om * (d - d0))

popt, pcov = curve_fit(cycle, d, T, p0=[7, 11, 15])
err = np.sqrt(np.diag(pcov))
print(f"c   = {popt[0]:.3f} ± {err[0]:.3f}")
print(f"amp = {popt[1]:.3f} ± {err[1]:.3f}")
print(f"d0  = {popt[2]:.2f} ± {err[2]:.2f}")

res = T - cycle(d, *popt)
print(f"residuals: std {res.std(ddof=3):.2f}, "
      f"next day {np.corrcoef(res[:-1], res[1:])[0, 1]:.3f}")
fig, (top, bottom) = plt.subplots(2, 1, figsize=(8, 5), sharex=True)
top.plot(d, T, ".", ms=2)
top.plot(d, cycle(d, *popt), "-")
top.set_ylabel("daily mean (°C)")
bottom.plot(d, res, ".", ms=2)
bottom.axhline(0, color="black")
bottom.set_xlabel("day since 2016-01-01")
bottom.set_ylabel("residual (°C)")
fig.savefig("results/cycle_fit.png", dpi=150, bbox_inches="tight")
