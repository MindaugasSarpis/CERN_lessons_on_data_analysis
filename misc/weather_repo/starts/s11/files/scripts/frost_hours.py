import numpy as np

time = np.loadtxt("data/raw/weather.csv", delimiter=",",
                  skiprows=1, usecols=0, dtype=str)
temp = np.loadtxt("data/raw/weather.csv", delimiter=",",
                  skiprows=1, usecols=1)
ok = temp != -999
frost = temp < 0
print(f"P(frost) = {frost[ok].mean():.3f}")

month = np.array([int(t[5:7]) for t in time])
for k in range(1, 13):
    print(k, f"{frost[ok & (month == k)].mean():.3f}")

f = frost[ok]
a = f[1:]       # A: frost in this hour
b = f[:-1]      # B: frost in the hour before
print(f"P(A) = {a.mean():.3f}, P(B) = {b.mean():.3f}")
print(f"P(A | B) = {a[b].mean():.3f}")
print(f"P(A and B) = {(a & b).mean():.3f}")
print(f"P(A) P(B)  = {a.mean() * b.mean():.3f}")
