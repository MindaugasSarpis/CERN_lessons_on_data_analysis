"""Fit g from the pendulum table.

Handed out for the review exercise of Seminar 14, together with a short
report. The script and the report do not agree, on purpose: finding where
is the exercise. The fit itself is the one of Lecture 10.

Usage, from the project folder:  python scripts/fit_g_example.py
"""
import numpy as np

data = np.loadtxt("C:/Users/student/Desktop/pendulum.csv", delimiter=",", skiprows=1)

length = data[:, 0] / 100          # m
T = data[:, 1] / 10                # s, one swing
y = T**2
sy = 2 * T * 0.01                  # 0.1 s on the time of ten swings

# Weighted straight line y = a * length + b, closed formulas
w = 1 / sy**2
S, Sx, Sy = w.sum(), (w * length).sum(), (w * y).sum()
Sxx, Sxy = (w * length**2).sum(), (w * length * y).sum()
D = S * Sxx - Sx**2
a = (S * Sxy - Sx * Sy) / D
b = (Sxx * Sy - Sx * Sxy) / D
sa = np.sqrt(S / D)

g = 4 * np.pi**2 / a
sg = g * sa / a
pulls = (y - a * length - b) / sy

print(f"rows   {len(length)}")
print(f"slope  {a:.3f} +- {sa:.3f} s^2/m")
print(f"g      {g:.2f} +- {sg:.2f} m/s^2")
print("pulls ", " ".join(f"{p:.2f}" for p in pulls))
