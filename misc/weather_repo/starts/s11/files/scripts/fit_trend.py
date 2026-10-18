import numpy as np

time = np.loadtxt("data/raw/weather.csv", delimiter=",",
                  skiprows=1, usecols=0, dtype=str)
temp = np.loadtxt("data/raw/weather.csv", delimiter=",",
                  skiprows=1, usecols=1)
year = np.array([int(t[:4]) for t in time])
ok = temp != -999
x = np.arange(10)              # years since 2016
y = np.array([temp[ok & (year == 2016 + k)].mean() for k in x])
sy = np.full(10, 0.70)         # the scatter of the years, Seminar 9
print(y.round(2))

def chi2_of(a, b):
    return (((y - a * x - b) / sy)**2).sum()

print(f"flat line at 7.16: chi2 {chi2_of(0, 7.16):.2f}")
print(f"slope 0.1 per year: chi2 {chi2_of(0.1, 6.7):.2f}")

w = 1 / sy**2
S, Sx, Sy = w.sum(), (w * x).sum(), (w * y).sum()
Sxx, Sxy = (w * x * x).sum(), (w * x * y).sum()
print(f"S {S:.2f}, Sx {Sx:.2f}, Sy {Sy:.2f}, Sxx {Sxx:.2f}, Sxy {Sxy:.2f}")
D = S * Sxx - Sx**2
a = (S * Sxy - Sx * Sy) / D
b = (Sxx * Sy - Sx * Sxy) / D
print(f"a = {a:.4f} °C per year, b = {b:.3f} °C")

sa = np.sqrt(S / D)
sb = np.sqrt(Sxx / D)
chi2 = (((y - a * x - b) / sy)**2).sum()
print(f"a = {a:.3f} ± {sa:.3f}, b = {b:.2f} ± {sb:.2f}, cov {-Sx / D:.4f}")
print(f"chi2 = {chi2:.2f} for {len(x) - 2} degrees of freedom")
print(f"per decade: {10 * a:.1f} ± {10 * sa:.1f} °C")
