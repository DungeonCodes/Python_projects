import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('500hits.csv', encoding='latin-1')

print(df.head())

X = df.drop(columns=['PLAYER', 'HOF'])
Y = df['HOF']

print(X.head)