# pandas_matplotlib_extended_tutorial.py
"""
Extended Pandas & Matplotlib Tutorial
Duration: ~3 hours
Dataset: dating_app.csv

This script covers:
 1) Data loading & inspection
 2) Data cleaning & feature engineering
 3) Exploratory data analysis (EDA)
 4) Visualization with matplotlib
 5) Advanced grouping & pivot tables
 6) Parsing list-like columns
 7) Saving outputs

Run each section sequentially and review comments for guidance.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Configure pandas display options
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

DATA_PATH = './dating_app.csv'
OUTPUT_DIR = './outputs'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Section 1: Load & Inspect Data (20 min)
def load_and_inspect(path):
    df = pd.read_csv(path)
    print("Dataset loaded. Shape:", df.shape)
    print("\nColumn Types and Non-Null Counts:")
    print(df.info())
    print("\nSummary Statistics:")
    print(df.describe(include='all'))
    return df

# Section 2: Data Cleaning & Feature Engineering (30 min)
def clean_and_transform(df):
    # Convert 'Interests' from string to list
    df['Interests'] = df['Interests'].str.strip('[]').str.replace("'", "").str.split(', ')    

    # Convert Frequency of Usage to ordered categorical
    freq_order = ['Daily', 'Weekly', 'Monthly']
    df['Frequency of Usage'] = pd.Categorical(df['Frequency of Usage'], categories=freq_order, ordered=True)

    # Convert Height from feet to cm
    df['Height_cm'] = df['Height'] * 30.48

    # Handle missing values
    missing = df.isnull().sum()
    print("\nMissing Values per Column:\n", missing)
    return df

# Section 3: Exploratory Data Analysis (45 min)
def exploratory_analysis(df):
    # Value counts for categorical features
    print("\nGender Counts:\n", df['Gender'].value_counts())
    print("\nLooking For Counts:\n", df['Looking For'].value_counts())

    # Grouped aggregations
    agg_gender = df.groupby('Gender').agg({'Age': ['mean', 'median'], 'Swiping History': 'mean'})
    print("\nAggregated Stats by Gender:\n", agg_gender)

    # Crosstab: Gender vs Looking For
    crosstab = pd.crosstab(df['Gender'], df['Looking For'], normalize='index')
    print("\nGender vs Looking For (Proportions):\n", crosstab)
    return agg_gender, crosstab

# Section 4: Visualization (60 min)
def create_visualizations(df):
    # Age distribution histogram
    plt.figure()
    plt.hist(df['Age'], bins=15)
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.savefig(os.path.join(OUTPUT_DIR, 'age_histogram.png'))
    plt.close()

    # Bar chart: users by Gender
    counts = df['Gender'].value_counts()
    plt.figure()
    plt.bar(counts.index, counts.values)
    plt.title('Users by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.savefig(os.path.join(OUTPUT_DIR, 'gender_counts.png'))
    plt.close()

    # Boxplot: Swiping History by Frequency of Usage
    plt.figure()
    df.boxplot(column='Swiping History', by='Frequency of Usage')
    plt.title('Swiping History by Frequency')
    plt.suptitle('')
    plt.xlabel('Frequency of Usage')
    plt.ylabel('Swipes')
    plt.savefig(os.path.join(OUTPUT_DIR, 'swipes_boxplot.png'))
    plt.close()

    # Scatter: Height_cm vs Swiping History
    plt.figure()
    plt.scatter(df['Height_cm'], df['Swiping History'])
    plt.title('Height (cm) vs Swiping History')
    plt.xlabel('Height (cm)')
    plt.ylabel('Swiping History')
    plt.savefig(os.path.join(OUTPUT_DIR, 'height_vs_swipes.png'))
    plt.close()

# Section 5: Advanced Grouping & Pivot Tables (30 min)
def advanced_grouping(df):
    pivot = df.pivot_table(index='Education Level', columns='Frequency of Usage', values='Swiping History', aggfunc='mean')
    print("\nPivot Table - Avg Swiping History by Education & Frequency:\n", pivot)
    return pivot

# Section 6: Parse Interests (15 min)
def analyze_interests(df):
    interests_exploded = df.explode('Interests')
    interest_counts = interests_exploded['Interests'].value_counts()
    print("\nTop Interests:\n", interest_counts.head(10))

    plt.figure()
    plt.bar(interest_counts.index[:10], interest_counts.values[:10])
    plt.title('Top 10 Interests')
    plt.xlabel('Interest')
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'top_interests.png'))
    plt.close()
    return interest_counts

# Section 7: Save Clean Data & Results (10 min)
def save_outputs(df, agg_gender, crosstab, pivot, interest_counts):
    df.to_csv(os.path.join(OUTPUT_DIR, 'cleaned_dating_app.csv'), index=False)
    agg_gender.to_csv(os.path.join(OUTPUT_DIR, 'agg_gender.csv'))
    crosstab.to_csv(os.path.join(OUTPUT_DIR, 'gender_looking_crosstab.csv'))
    pivot.to_csv(os.path.join(OUTPUT_DIR, 'pivot_swiping.csv'))
    interest_counts.to_csv(os.path.join(OUTPUT_DIR, 'interest_counts.csv'))
    print("\nAll outputs saved to", OUTPUT_DIR)

# Main execution
if __name__ == '__main__':
    df = load_and_inspect(DATA_PATH)
    df = clean_and_transform(df)
    agg_gender, crosstab = exploratory_analysis(df)
    create_visualizations(df)
    pivot = advanced_grouping(df)
    interest_counts = analyze_interests(df)
    save_outputs(df, agg_gender, crosstab, pivot, interest_counts)

