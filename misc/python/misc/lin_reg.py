import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Example data: y = 2.5x + 1.3 + noise
x = np.linspace(0, 10, 20)
y = 2.5 * x + 1.3 + np.random.normal(scale=2.0, size=len(x))

# Model function
def linear(x, a, b):
    return a * x + b

# Fit
params, covariance = curve_fit(linear, x, y)
a_fit, b_fit = params
print(f"a = {a_fit:.3f}, b = {b_fit:.3f}")

# Plot
plt.scatter(x, y, label="Data")
plt.plot(x, linear(x, a_fit, b_fit), label=f"Fit: y = {a_fit:.2f}x + {b_fit:.2f}", lw=2)
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()

