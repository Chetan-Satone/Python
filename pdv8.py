import pandas as pd


df = pd.read_csv('data.csv')

print(df)

print(df.to_string())

print(df.tail(10))

print(df.head(10))

print(df.info)

new_df = df.dropna()

print(new_df.to_string())