
import pandas as pd

Iris = pd.read_csv("Iris.csv")

Iris.head()
Iris.describe()

import matplotlib.pyplot as plt

data = pd.read_csv("Iris.csv")
plt.plot(data['SepalLengthCm'], data['SepalWidthCm'])
plt.show()