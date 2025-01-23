import numpy as np
import pandas as pd

# Parameters for the Gaussian signal
mean_signal = 5.0  # Center of Gaussian
std_dev_signal = 1.0  # Standard deviation of Gaussian
num_signal_points = 10000  # Number of data points for the signal

# Parameters for the exponential background
scale_background = 2.0  # Scale parameter for exponential distribution
num_background_points = 15000  # Number of data points for the background

# Generate Gaussian signal data
gaussian_signal = np.random.normal(mean_signal, std_dev_signal, num_signal_points)

# Generate exponential background data
exponential_background = np.linspace(0, 20, num_background_points)

# Combine signal and background into a single dataset
data = np.concatenate((gaussian_signal, exponential_background))
labels = np.concatenate((['signal'] * num_signal_points, ['background'] * num_background_points))

# Create a DataFrame and save it to a CSV file
df = pd.DataFrame({'value': data, 'type': labels})
df.to_csv('data2.csv', index=False)

print("CSV file 'gaussian_signal_exponential_background.csv' has been created.")
