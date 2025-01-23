import pandas as pd

from plotting_functions import *

# Replace 'file.csv' with your CSV file path
# data = pd.read_csv('../../data/quiz_1.csv')
data = pd.read_csv('resources\data\quiz_1.csv')
grade_chart(data['grade'])
# plot_hist(data['score'], xlow=14, xup=22)
# plot_hist(data['grade'], xlow=0, xup=10)

# plot_bar_chart(data['score'], xlow=13, xup=23)


