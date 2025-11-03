# Level 1 - Task 2

# Import libraries and Load data set
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv('cleaned_iris.csv')

# Display the first few rows of the cleaned dataset
print("First 5 rows of the cleaned dataset:")
print(df.head())

# Summary staticstics for numerical columns
print("\nSummary Statistics for Numerical Columns:")

print(df.describe())

# Mean, Median, Mode, Standard Deviation for each numerical column
print("\nMean values:\n", df.mean(numeric_only=True))
print("\nMedian values:\n", df.median(numeric_only=True))
print("\nMode values:\n", df.mode().iloc[0])
print("\nStandard Deviation:\n", df.std(numeric_only=True))

# Visualizations

# Histograms for each numerical column
df.hist(figsize=(10,6), color='skyblue', edgecolor='black') 
plt.suptitle('Histograms of Numerical Columns', fontsize=14)
plt.show()

# Box plots for each numerical column
plt.figure(figsize=(10,6))
sns.boxplot(df, palette='Set2')
plt.title('Box Plots of Numerical Columns', fontsize=14)
plt.show()

# Scatterplots to show relationships between numerical columns
sns.scatterplot(df, x='sepal_length', y='sepal_width', hue='species')
plt.title("Sepal Length vs Sepal Width by Species")
plt.show()

sns.scatterplot(df, x='petal_length', y='petal_width', hue='species')
plt.title("Petal Length vs Petal Width by Species")
plt.show()

# Correlation matrix
corr = df.corr(numeric_only=True)
print("\nCorrelation Matrix:\n", corr)  
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix Heatmap')


plt.savefig('correlation_matrix_heatmap.png')
print("\nCorrelation matrix heatmap saved as 'correlation_matrix_heatmap.png'") 

plt.show()




