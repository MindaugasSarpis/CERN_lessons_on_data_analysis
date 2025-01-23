import pandas as pd
from plotting_functions import plot_hist 

# Load the CSV file
df = pd.read_csv('data2.csv')

# # Separate the signal and background for plotting
# signal_data = df[df['type'] == 'signal']['value']
# background_data = df[df['type'] == 'background']['value']

combined = df['value']

# Plot the signal and background data
plot_hist(combined,n_bins= 50, xup=12)