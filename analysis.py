# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
try:
    df = pd.read_csv("c:\Users\user\Downloads\greenhouse-gas-emissions-industry-and-household-december-2024-quarter.csv")
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: File not found. Ensure the dataset is in the correct path.")
    exit()

# Display first few rows
print("\nFirst five rows of the dataset:")
print(df.head())

# Explore the dataset structure
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Cleaning the dataset
df.dropna(inplace=True)  # Remove rows with missing values
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Compute basic statistics
print("\nBasic Statistics:")
print(df.describe())

# Group data by a categorical column
group_column = 'Anzsic_descriptor'  
numeric_column = 'Data_value'  
if group_column in df.columns and numeric_column in df.columns:
    grouped_df = df.groupby(group_column)[numeric_column].mean()
    print("\nMean value per category:")
    print(grouped_df)
else:
    print("\nError: Column names for grouping do not match dataset.")

# Visualization

# Line Chart: Time trends
if 'Period' in df.columns and 'Data_value' in df.columns:
    plt.figure(figsize=(8, 5))
    df.plot(x='Period', y='Data_value', kind='line')
    plt.title('Time Trends')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.show()
else:
    print("\nError: Column names for line chart do not match dataset.")

# Bar Chart: Comparing categories
if group_column in df.columns and numeric_column in df.columns:
    plt.figure(figsize=(8, 5))
    sns.barplot(x=group_column, y=numeric_column, data=df)
    plt.title('Category Comparison')
    plt.show()
else:
    print("\nError: Column names for bar chart do not match dataset.")

# Histogram: Distribution of numerical data
if numeric_column in df.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df[numeric_column], bins=30, kde=True)
    plt.title('Numerical Column Distribution')
    plt.show()
else:
    print("\nError: Column name for histogram does not match dataset.")

# Scatter Plot: Relationship between two numerical variables
num_col1 = 'numerical_column1'  # Replace with actual numerical column name
num_col2 = 'numerical_column2'  # Replace with actual numerical column name
if num_col1 in df.columns and num_col2 in df.columns:
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=num_col1, y=num_col2, data=df)
    plt.title('Scatter Plot: Relationship Between Variables')
    plt.show()
else:
    print("\nError: Column names for scatter plot do not match dataset.")
