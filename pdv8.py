import pandas as pd


df = pd.read_csv('data.csv')

print(df)

print(df.to_string())

print(df.tail(10))

print(df.head(10))