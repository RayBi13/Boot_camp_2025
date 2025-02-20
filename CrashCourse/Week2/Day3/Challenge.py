from google.colab import files
files.upload()

# Normalize the ‘salary’ column using Min-Max normalization
from sklearn.preprocessing import MinMaxScaler

import pandas as pd
data = pd.read_csv("datascience_salaries.csv")
data.head()

print(data.columns)

scaler = MinMaxScaler()
data['salary'] = scaler.fit_transform(data[['salary']])
print(data.describe())

print(data.dtypes)

# dimensionality reduction (PCA) to reduce the number of features (columns) in the dataset.
# first import
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Convert categorical columns into numeric using one-hot encoding, This replaces text with binary columns
data_numeric = pd.get_dummies(data)

# to standardize the numerical values (PCA needs scaled data)
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_numeric)

# to apply PCA
pca = PCA(n_components=2)  # Reduce to 2 principal components
reduced_data = pca.fit_transform(data_scaled)

# To convert PCA result into DataFrame
reduced_df = pd.DataFrame(reduced_data, columns=["PC1", "PC2"])

print(reduced_df.head())

# To group by experience level and calculate mean & median salary
salary_stats = data.groupby("experience_level")["salary"].agg(["mean", "median"])

# Renaming columns for clarity
salary_stats.columns = ["Average Salary", "Median Salary"]

print(salary_stats)