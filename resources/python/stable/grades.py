import pandas as pd

# Replace 'file.csv' with your CSV file path
data = pd.read_csv('../../data/quiz_1.csv')

from plotting_functions import plot_hist

plot_hist(data['grade'], xlow=14, xup=23)