import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv('cleaned_iris.csv')

# Display the first few rows of the cleaned dataset
print("First 5 rows of the cleaned dataset:")
print(df.head())

# Create a barplot for the count of each species
plt.figure(figsize=(8,6))
sns.countplot(df, x='species', palette='Set3')
plt.title('Count of Each Iris Species', fontsize=14)
plt.xlabel('Species', fontsize=12)
plt.ylabel('Count', fontsize=12)

# Save the barplot
plt.savefig('species_count_barplot.png')
print("\nSpecies count barplot saved as 'species_count_barplot.png'")

plt.show()



# Create a line chart for sepal length across different species
plt.figure(figsize=(10,6))
sns.lineplot(data=df, x=df.index, y='sepal_length', hue='species', marker='o', palette='Set2')
plt.title('Sepal Length across Different Species', fontsize=14)
plt.xlabel('Index', fontsize=12)
plt.ylabel('Sepal Length', fontsize=12)
plt.legend(title='Species')

# Save the line chart
plt.savefig('sepal_length_line_chart.png')
print("\nSepal length line chart saved as 'sepal_length_line_chart.png'")

plt.show()


# Create a line chart for petal length across different species
plt.figure(figsize=(10,6)) 
sns.lineplot(data=df, x=df.index, y='petal_length', hue='species', marker='o', palette='Set2')
plt.title('Petal Length across Different Species', fontsize=14)
plt.xlabel('Index', fontsize=12)
plt.ylabel('Petal Length', fontsize=12)
plt.legend(title='Species')

# Save the line chart
plt.savefig('petal_length_line_chart.png')
print("\nPetal length line chart saved as 'petal_length_line_chart.png'")

plt.show()



# Create a line chart for sepal width across different species
plt.figure(figsize=(10,6))
sns.lineplot(data=df, x=df.index, y='sepal_width', hue='species', marker='o', palette='Set2')
plt.title('Sepal Width across Different Species', fontsize=14)  
plt.xlabel('Index', fontsize=12)
plt.ylabel('Sepal Width', fontsize=12)
plt.legend(title='Species')

# Save the line chart
plt.savefig('sepal_width_line_chart.png')
print("\nSepal width line chart saved as 'sepal_width_line_chart.png'")

plt.show()


# Create a line chart for petal width across different species
plt.figure(figsize=(10,6))
sns.lineplot(data=df, x=df.index, y='petal_width', hue='species', marker='o', palette='Set2')
plt.title('Petal Width across Different Species', fontsize=14)
plt.xlabel('Index', fontsize=12)
plt.ylabel('Petal Width', fontsize=12)
plt.legend(title='Species')

# Save the line chart
plt.savefig('petal_width_line_chart.png')
print("\nPetal width line chart saved as 'petal_width_line_chart.png'")

plt.show()



# Create a combined line chart for all numerical features

# List of numerical columns
numeric_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

# Create line chart
plt.figure(figsize=(10,6))

# Plot each column
for col in numeric_cols:
    plt.plot(df.index, df[col], label=col)   # label for legend

# Add title and labels
plt.title("Changes in Iris Flower Measurements Across Dataset")
plt.xlabel("Sample Index")
plt.ylabel("Measurement (cm)")

# Add legend
plt.legend(title="Features")


# Save the combined line chart
plt.savefig('combined_line_chart.png')
print("\nCombined line chart saved as 'combined_line_chart.png'")

# Show the chart
plt.show()



# Create a Scatter plot for sepal length vs sepal width
plt.figure(figsize=(10,6))
sns.scatterplot(df, x='sepal_length', y='sepal_width', hue='species', palette='Set1')
plt.title("Sepal Length vs Sepal Width by Species", fontsize=14)
plt.xlabel('Sepal Length', fontsize=12)
plt.ylabel('Sepal Width', fontsize=12)
plt.legend(title='Species')

# Save the scatter plot
plt.savefig('sepal_scatter_plot.png')
print("\nSepal scatter plot saved as 'sepal_scatter_plot.png'")

plt.show()


# Create a Scatter plot for petal length vs petal width
plt.figure(figsize=(10,6))
sns.scatterplot(df, x='petal_length', y='petal_width', hue='species', palette='Set1')
plt.title("Petal Length vs Petal Width by Species", fontsize=14)
plt.xlabel('Petal Length', fontsize=12)
plt.ylabel('Petal Width', fontsize=12)
plt.legend(title='Species')

# Save the scatter plot
plt.savefig('petal_scatter_plot.png')
print("Petal scatter plot saved as 'petal_scatter_plot.png'") 

plt.show()

  

# Create combined scatter plot for all numerical features
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='sepal_length', y='sepal_width', hue='species', style='species', s=100)
sns.scatterplot(data=df, x='petal_length', y='petal_width', hue='species', style='species', s=100, marker='X')
plt.title("Combined Scatter Plot of Iris Features by Species", fontsize=14)
plt.xlabel('Length (cm)', fontsize=12)
plt.ylabel('Width (cm)', fontsize=12)   
plt.legend(title='Species and Features') 

# Save the combined scatter plot
plt.savefig('combined_scatter_plot.png')
print("\nCombined scatter plot saved as 'combined_scatter_plot.png'")

plt.show() 



