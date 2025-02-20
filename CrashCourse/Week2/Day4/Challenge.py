import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

from google.colab import files
files.upload()

data = pd.read_csv("2019.csv")
print (data.head())

# verif oubliés
df = pd.DataFrame(data)
missing_data = df.isnull()

print(missing_data.head())

# compter les val de chaques colones
missing_counts = df.isnull().sum()
print(missing_counts)


sns.lmplot(x='Social support', y='Score', data=data, aspect=1.5, height=5)
plt.title('Social Support and Happiness')
plt.show()


import matplotlib.pyplot as plt
import seaborn as sns

print(df.columns)


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

sns.boxplot(x="Country or region", y="GDP per capita", data=df, ax=ax1)
ax1.set_title('GDP per Capita by Region')
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)


sns.boxplot(x="Country or region", y="Healthy life expectancy", data=df, ax=ax2)
ax2.set_title('Healthy Life Expectancy by Region')
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45)

plt.tight_layout()
plt.show()

