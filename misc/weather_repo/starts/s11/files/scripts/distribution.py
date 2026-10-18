import numpy as np
import matplotlib.pyplot as plt

temp = np.loadtxt("data/raw/weather.csv", delimiter=",",
                  skiprows=1, usecols=1)
valid = temp[temp != -999]
print("hours", len(temp), "valid", len(valid))

m = valid.mean()
s = valid.std(ddof=1)
print(f"mean {m:.2f}, standard deviation {s:.2f}")
print("median", np.median(valid))
print("5 % and 95 %:", np.percentile(valid, [5, 95]))

fig, ax = plt.subplots()
ax.hist(valid, bins=np.arange(-17, 34, 1))
ax.set_xlabel("temp_c (°C)")
ax.set_ylabel("hours per 1 °C bin")
fig.savefig("results/temp_distribution.png", dpi=150)
