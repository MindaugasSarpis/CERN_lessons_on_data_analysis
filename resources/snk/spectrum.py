import pandas as pd
import matplotlib.pyplot as plt

import argparse

# Parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument("--output", type=str,     default = "output.png")
parser.add_argument("--color")
parser.add_argument("--line_style", type=str, default = "-")
args = parser.parse_args()

# Read the dataset
df = pd.read_csv("data.csv")

# Create a color map with 100 different colors
cmap = plt.get_cmap('viridis', 100)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(df['x'], df['y'], color=args.color, linestyle=args.line_style, label=f"Plot ")

# Customize the plot
plt.title(f"Wavy Spectrum - Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)

# Ensure output directory exists

# Save the plot to a file
plt.savefig(args.output)
plt.close()
