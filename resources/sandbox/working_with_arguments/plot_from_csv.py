# Import data from csv 
import pandas as pd
from plotting_functions import plot_data

df = pd.read_csv('data.csv')

value1 = df['value_1']

plot_data(value1)