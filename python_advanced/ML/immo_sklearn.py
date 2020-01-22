from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/Immobilien.txt', delimiter='\t', index_col='Immobilie')

scaler = MinMaxScaler(feature_range=(0,1))

# normalize the columns
df_norm = df.copy()

cols = ['Quadratmeter', 'Wandhoehe', 'IA_Ratio']
df_norm[cols] = scaler.fit_transform(df[cols])
print(df_norm.head())

# take a sample
df_test = df_norm.sample(200)
print(df_test.head())
