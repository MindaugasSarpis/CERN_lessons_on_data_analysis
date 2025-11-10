#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Read data from CSV
data = np.loadtxt("sample.csv", delimiter=",", skiprows=1)
print(f"Loaded {len(data)} data points")

# Create histogram for fitting
hist, bin_edges = np.histogram(data, bins=50, range=[0, 10])
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

# Define model: Gaussian + exponential background
def model(x, amp, mean, sigma, exp_norm, exp_scale):
    """Gaussian signal + exponential background"""
    gaussian = amp * np.exp(-0.5 * ((x - mean) / sigma)**2)
    exponential = exp_norm * np.exp(-x / exp_scale)
    return gaussian + exponential

# Initial parameter guesses: [amp, mean, sigma, exp_norm, exp_scale]
initial_guess = [100, 5.0, 1.0, 50, 2.0]

# Fit the model to the histogram
popt, pcov = curve_fit(model, bin_centers, hist, p0=initial_guess)
errors = np.sqrt(np.diag(pcov))

# Extract results
amp, mean, sigma, exp_norm, exp_scale = popt

print("\nFit Results:")
print(f"Gaussian mean:  {mean:.3f} ± {errors[1]:.3f}")
print(f"Gaussian sigma: {sigma:.3f} ± {errors[2]:.3f}")
print(f"Signal events:  {amp * sigma * np.sqrt(2 * np.pi):.0f}")

# Plot results
plt.figure(figsize=(10, 6))

# Plot histogram (data)
counts, bins, _ = plt.hist(data, bins=50, range=[0, 10], alpha=0.5, label="Data", edgecolor='black')

# Plot fitted curves - need to scale by bin width to match histogram
bin_width = bins[1] - bins[0]
x_smooth = np.linspace(0, 10, 500)
plt.plot(x_smooth, model(x_smooth, *popt) * bin_width, 'r-', linewidth=2, label="Fit")
plt.plot(x_smooth, amp * np.exp(-0.5 * ((x_smooth - mean) / sigma)**2) * bin_width, 'g--', label="Gaussian")
plt.plot(x_smooth, exp_norm * np.exp(-x_smooth / exp_scale) * bin_width, 'm--', label="Exponential")

plt.xlabel("x")
plt.ylabel("Entries")
plt.legend(bbox_to_anchor=(1.05, 0.5), loc='center left')
plt.grid(alpha=0.3)
# Remove background
ax = plt.gca()
ax.set_facecolor('none')
plt.gcf().patch.set_alpha(0)
plt.tight_layout()
plt.show()

