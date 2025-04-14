import pandas as pd

# Read the file
df = pd.read_csv('diabetes.csv')

# Display the first few rows of the DataFrame to confirm it's read correctly
print(df.head())

print(df.isnull().sum())

print(df.describe())

print(df.dtypes)
