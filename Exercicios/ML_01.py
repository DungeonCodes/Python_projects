import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split

df = pd.read_csv('heart-disease.csv')

#print(df.head())

print(df["target"].value_counts())
print(df["target"].value_counts(normalize=True))
df["target"].value_counts().plot(kind="bar", color=["salmon", "lightblue"])