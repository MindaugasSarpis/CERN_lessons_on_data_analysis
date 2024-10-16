from cool_plotting_functions import super_function
import numpy as np

# Create a random number generator with a fixed seed for reproducibility
rng = np.random.default_rng(19680801)
N_points = 10000000  # You can change this, and the y-limits will adjust automatically
n_bins = 1000

distribution = rng.standard_normal(N_points)

super_function(distribution, n_bins, width=1, height=1)