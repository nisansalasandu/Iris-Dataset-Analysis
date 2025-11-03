# Level 1 - Task 1

import pandas as pd

# Load the dataset
df = pd.read_csv('1) iris.csv')

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Get dataset info
print("\nDataset Information:")
print(df.info())

# Check for missing values
print("\nMissing Values in Each Column before cleaning:")
print(df.isnull().sum())

# No any missing values found in the dataset

# Display basic statistics of the dataset
print("\nBasic Statistics of the Dataset:")
print(df.describe())

# Check if there are any duplicate rows
duplicate_rows = df.duplicated().sum()
print(f"\nNumber of duplicate rows in the dataset: {duplicate_rows}")   

#Remove duplicate rows if any
df.drop_duplicates(inplace=True)

# Verify duplicates are removed
duplicate_rows_after = df.duplicated().sum()
print(f"Number of duplicate rows after removal: {duplicate_rows_after}")

# Save the cleaned data
df.to_csv('cleaned_iris.csv', index=False)
print("\nCleaned data saved to 'cleaned_iris.csv'")