import pandas as pd
data = ({
       'Column1': ['Name'],
       'Column2': ['Gender'],
       'Column3': ['Age']})

df = pd.DataFrame(data)

# Saving Data in Excel Format:

df.to_excel('data_excel.xlsx', sheet_name='Sheet1')

from google.colab import files

files.download('data_excel.xlsx')

# Export the dataframe to a JSON file

df.to_json('data_jason.json', orient='split')

files.download('data_jason.json')