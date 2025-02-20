
# Exo4
import pandas as pd
import numpy as np

# Sample data
data = {
    'Fare': [7.25, 71.83, 8.05, 53.1, 8.05, 51.86, 21.07, 11.13, 30.07, 16.7, 7.92, 39.6, 31.28, 7.75, 21.0, 18.0, 26.0, 13.0, 8.0, 35.5],
    'Age': [22, 38, 26, 35, 35, 54, 2, 27, 14, 4, 58, 20, 39, 14, 55, 2, 31, 30, 34, 15]
}
df = pd.DataFrame(data)

# Detecting outliers using IQR
def detect_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers

# Detecting outliers using Z-score
def detect_outliers_zscore(df, column, threshold=3):
    mean = np.mean(df[column])
    std = np.std(df[column])
    z_scores = [(y - mean) / std for y in df[column]]
    outliers = df[np.abs(z_scores) > threshold]
    return outliers

# Handling outliers by capping
def cap_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df[column] = np.where(df[column] < lower_bound, lower_bound, df[column])
    df[column] = np.where(df[column] > upper_bound, upper_bound, df[column])
    return df

# Detect outliers in 'Fare' and 'Age' columns
fare_outliers_iqr = detect_outliers_iqr(df, 'Fare')
age_outliers_iqr = detect_outliers_iqr(df, 'Age')
fare_outliers_zscore = detect_outliers_zscore(df, 'Fare')
age_outliers_zscore = detect_outliers_zscore(df, 'Age')

print("Fare outliers detected using IQR:\n", fare_outliers_iqr)
print("Age outliers detected using IQR:\n", age_outliers_iqr)
print("Fare outliers detected using Z-score:\n", fare_outliers_zscore)
print("Age outliers detected using Z-score:\n", age_outliers_zscore)

# Handle outliers by capping
df_capped = df.copy()
df_capped = cap_outliers(df_capped, 'Fare')
df_capped = cap_outliers(df_capped, 'Age')

print("\nData after capping outliers:\n", df_capped)



# Exo_5

import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Sample data
data = {
    'Fare': [7.25, 71.83, 8.05, 53.1, 8.05, 51.86, 21.07, 11.13, 30.07, 16.7, 7.92, 39.6, 31.28, 7.75, 21.0, 18.0, 26.0, 13.0, 8.0, 35.5],
    'Age': [22, 38, 26, 35, 35, 54, 2, 27, 14, 4, 58, 20, 39, 14, 55, 2, 31, 30, 34, 15]
}
df = pd.DataFrame(data)

# Evaluate the scale and distribution of numerical columns
print("Original Data:")
print(df.describe())

# Apply StandardScaler
scaler = StandardScaler()
df_standard_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

print("\nStandard Scaled Data:")
print(df_standard_scaled.describe())

# Apply MinMaxScaler
min_max_scaler = MinMaxScaler()
df_min_max_scaled = pd.DataFrame(min_max_scaler.fit_transform(df), columns=df.columns)

print("\nMin-Max Scaled Data:")
print(df_min_max_scaled.describe())

# Exo 4

import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np

# Sample data
data = {
    'Fare': [7.25, 71.83, 8.05, 53.1, 8.05, 51.86, 21.07, 11.13, 30.07, 16.7, 7.92, 39.6, 31.28, 7.75, 21.0, 18.0, 26.0, 13.0, 8.0, 35.5],
    'Age': [22, 38, 26, 35, 35, 54, 2, 27, 14, 4, 58, 20, 39, 14, 55, 2, 31, 30, 34, 15]
}
df = pd.DataFrame(data)

# Evaluate the scale and distribution of numerical columns
print("Original Data:")
print(df.describe())

# Apply StandardScaler
scaler = StandardScaler()
df_standard_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

print("\nStandard Scaled Data:")
print(df_standard_scaled.describe())

# Apply MinMaxScaler
min_max_scaler = MinMaxScaler()
df_min_max_scaled = pd.DataFrame(min_max_scaler.fit_transform(df), columns=df.columns)

print("\nMin-Max Scaled Data:")
print(df_min_max_scaled.describe())

# Detecting outliers using IQR
def detect_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers

# Handling outliers by capping
def cap_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df[column] = np.where(df[column] < lower_bound, lower_bound, df[column])
    df[column] = np.where(df[column] > upper_bound, upper_bound, df[column])
    return df

# Detect outliers in 'Fare' and 'Age' columns
fare_outliers_iqr = detect_outliers_iqr(df, 'Fare')
age_outliers_iqr = detect_outliers_iqr(df, 'Age')

print("\nFare outliers detected using IQR:\n", fare_outliers_iqr)
print("\nAge outliers detected using IQR:\n", age_outliers_iqr)

# Handle outliers by capping
df_capped = df.copy()
df_capped = cap_outliers(df_capped, 'Fare')
df_capped = cap_outliers(df_capped, 'Age')


# Exo6 

import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder

# Sample data
data = {
    'Fare': [7.25, 71.83, 8.05, 53.1, 8.05, 51.86, 21.07, 11.13, 30.07, 16.7, 7.92, 39.6, 31.28, 7.75, 21.0, 18.0, 26.0, 13.0, 8.0, 35.5],
    'Age': [22, 38, 26, 35, 35, 54, 2, 27, 14, 4, 58, 20, 39, 14, 55, 2, 31, 30, 34, 15],
    'Sex': ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'male', 'male', 'female'],
    'Embarked': ['S', 'C', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']
}
df = pd.DataFrame(data)

# Evaluate the scale and distribution of numerical columns
print("Original Data:")
print(df.describe())

# Apply StandardScaler
scaler = StandardScaler()
df_standard_scaled = pd.DataFrame(scaler.fit_transform(df[['Fare', 'Age']]), columns=['Fare', 'Age'])

print("\nStandard Scaled Data:")
print(df_standard_scaled.describe())

# Apply MinMaxScaler
min_max_scaler = MinMaxScaler()
df_min_max_scaled = pd.DataFrame(min_max_scaler.fit_transform(df[['Fare', 'Age']]), columns=['Fare', 'Age'])

print("\nMin-Max Scaled Data:")
print(df_min_max_scaled.describe())

# Detecting outliers using IQR
def detect_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers

# Handling outliers by capping
def cap_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df[column] = np.where(df[column] < lower_bound, lower_bound, df[column])
    df[column] = np.where(df[column] > upper_bound, upper_bound, df[column])
    return df

# Detect outliers in 'Fare' and 'Age' columns
fare_outliers_iqr = detect_outliers_iqr(df, 'Fare')
age_outliers_iqr = detect_outliers_iqr(df, 'Age')

print("\nFare outliers detected using IQR:\n", fare_outliers_iqr)
print("\nAge outliers detected using IQR:\n", age_outliers_iqr)

# Handle outliers by capping
df_capped = df.copy()
df_capped = cap_outliers(df_capped, 'Fare')
df_capped = cap_outliers(df_capped, 'Age')

print("\nData after capping outliers:\n", df_capped.describe())

# Exo:
# Identifier les colonnes catégorielles dans l'ensemble de données Titanic, telles que Sex et Embarked.
# Utiliser un codage à un coupon pour les variables nominales et le codage de l'étiquette pour les variables ordinales.
# Intégrer les caractéristiques codées dans l'ensemble de données principal.

# Handle categorical columns
# One-hot encoding for nominal variables
df_encoded = pd.get_dummies(df_capped, columns=['Sex', 'Embarked'])

print("\nData after one-hot encoding:\n", df_encoded.head())

# Label encoding for ordinal variables (if any)
# Example: Assuming 'Embarked' is ordinal (which it is not in this case)
# label_encoder = LabelEncoder()
# df['Embarked'] = label_encoder.fit_transform(df['Embarked'])

# Note: In this dataset, 'Embarked' is not ordinal, so we use one-hot encoding instead.