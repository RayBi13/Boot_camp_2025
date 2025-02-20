from google.colab import files
files.upload()

import pandas as pd
post = pd.read_json("posts.json")

post.head(5)