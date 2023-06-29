import pandas as pd
df = pd.read_csv('housing.csv')
print(df.head())
# df = pd.read_csv('file.csv', header=None) first row as data and
# as column names