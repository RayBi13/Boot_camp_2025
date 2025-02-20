

# Import necessary libraries
import pandas as pd

# chargement datasets
sleep_data = pd.read_csv('Time Americans Spend Sleeping.csv')
mental_health_data = pd.read_csv('clean_dataset.csv')
credit_card_data = pd.read_csv('Mental health Depression disorder Data.csv')


print("Sleep Data:")
print(sleep_data.head())

print("\nMental Health Data:")
print(mental_health_data.head())

print("\nCredit Card Data:")
print(credit_card_data.head())

# breve dataset description
print("\nSleep Data Description:")
print(sleep_data.describe(include='all'))

print("\nMental Health Data Description:")
print(mental_health_data.describe(include='all'))

print("\nCredit Card Data Description:")
print(credit_card_data.describe(include='all'))

def categorize_columns(df):
    quantitative = []
    qualitative = []
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            quantitative.append(column)
        else:
            qualitative.append(column)
    return quantitative, qualitative

sleep_quantitative, sleep_qualitative = categorize_columns(sleep_data)
mental_health_quantitative, mental_health_qualitative = categorize_columns(mental_health_data)
credit_card_quantitative, credit_card_qualitative = categorize_columns(credit_card_data)

print("\nSleep Data Columns:")
print("Quantitative:", sleep_quantitative)
print("Qualitative:", sleep_qualitative)

print("\nMental Health Data Columns:")
print("Quantitative:", mental_health_quantitative)
print("Qualitative:", mental_health_qualitative)

print("\nCredit Card Data Columns:")
print("Quantitative:", credit_card_quantitative)
print("Qualitative:", credit_card_qualitative)