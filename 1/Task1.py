import pandas as pd
df = read_csv('stask1.xls')
df.columns
df.isnull().sum()
data = df.Names
names_data = data.dropna()
print(names_data)


