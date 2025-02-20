!pip install pandas
from google.colab import files
files.upload()

import pandas as pd

Iris = pd.read_csv("Iris_dataset.csv")

Iris.head(5)