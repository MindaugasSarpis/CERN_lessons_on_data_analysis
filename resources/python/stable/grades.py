import pandas as pd

# Replace 'file.csv' with your CSV file path
data = pd.read_csv('../data/quiz_1.csv')

from resources.python.stable.plotting_functions import plot_hist

plot_hist(data['grade'], n_bins=22)