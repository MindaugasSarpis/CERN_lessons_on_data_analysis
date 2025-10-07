import numpy as np
import csv
import matplotlib.pyplot as plt

# Parameters for the Gaussian signal
signal_mean = 5.0  # Center of Gaussian
signal_std_dev = 1.0  # Standard deviation of Gaussian
num_sig_points = 10000  # Number of data points for the signal

# Parameters for the exponential background
num_background_points = 100000  # Number of data points for the background

# Generate Gaussian signal data
gaussian_signal = np.random.normal(signal_mean, signal_std_dev, num_sig_points)

# Generate exponential background data
exponential_background = np.random.exponential(scale=2.0, size=num_background_points)

# Combine signal and background data
all_data = np.concatenate([gaussian_signal, exponential_background])

# Plot the combined data
plt.hist(
    exponential_background,
    bins=50,
    alpha=0.5,
    label="Background (exp)",
    color="tab:blue",
)

plt.hist(
    gaussian_signal, bins=50, alpha=0.5, label="Signal (gauss)", color="tab:orange"
)

plt.hist(all_data, bins=50, histtype="step", linewidth=2, color="black", label="Total")
plt.show()
