# Importation des librairies
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Chargement de Iris dataset
iris = sns.load_dataset('iris')

# rows
print("Iris Dataset:")
print(iris.head())

# Identifier les colonnes qualitatives et quantitatives
qualitative_columns = ['species']
quantitative_columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

print("\nQualitative Columns:", qualitative_columns)
print("Quantitative Columns:", quantitative_columns)

# classification qualitative ou quantitative
print("\nDescription:")
print("Qualitative Columns:")
print(" - species: Categorical variable representing the species of the iris flower.")

print("\nQuantitative Columns:")
print(" - sepal_length: Numerical variable representing the length of the sepal.")
print(" - sepal_width: Numerical variable representing the width of the sepal.")
print(" - petal_length: Numerical variable representing the length of the petal.")
print(" - petal_width: Numerical variable representing the width of the petal.")


mean_sepal_length = iris['sepal_length'].mean()
median_sepal_length = iris['sepal_length'].median()
mode_sepal_length = stats.mode(iris['sepal_length'])[0][0]

print("\nBasic Data Analysis:")
print(f"Mean of sepal_length: {mean_sepal_length}")
print(f"Median of sepal_length: {median_sepal_length}")
print(f"Mode of sepal_length: {mode_sepal_length}")

# plots
plt.figure(figsize=(10, 6))
sns.histplot(iris['sepal_length'], kde=True)
plt.title('Histogram of Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()

