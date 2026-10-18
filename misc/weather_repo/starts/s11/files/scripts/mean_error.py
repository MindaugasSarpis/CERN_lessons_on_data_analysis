import numpy as np

time = np.loadtxt("data/raw/weather.csv", delimiter=",",
                  skiprows=1, usecols=0, dtype=str)
temp = np.loadtxt("data/raw/weather.csv", delimiter=",",
                  skiprows=1, usecols=1)
ok = temp != -999
valid = temp[ok]
n = len(valid)
s = valid.std(ddof=1)
print(f"mean {valid.mean():.3f} ± {s / np.sqrt(n):.3f}")

r1 = np.corrcoef(valid[:-1], valid[1:])[0, 1]
r24 = np.corrcoef(valid[:-24], valid[24:])[0, 1]
print(f"one hour apart {r1:.3f}, one day apart {r24:.3f}")

year = np.array([int(t[:4]) for t in time])
means = []
for y in range(2016, 2026):
    means.append(temp[ok & (year == y)].mean())
means = np.array(means)
print(means.round(2))
sy = means.std(ddof=1)
print(f"years scatter by {sy:.2f}")
print(f"mean {means.mean():.2f} ± {sy / np.sqrt(10):.2f}")

rng = np.random.default_rng(1)
random_means = []
row_means = []
for i in range(2000):
    random_means.append(rng.choice(valid, 1000).mean())
    k = rng.integers(0, n - 1000)
    row_means.append(valid[k:k + 1000].mean())
print(f"s / sqrt(1000)      {s / np.sqrt(1000):.2f}")
print(f"1000 random hours   {np.std(random_means):.2f}")
print(f"1000 hours in a row {np.std(row_means):.2f}")
