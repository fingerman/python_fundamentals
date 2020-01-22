import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split


car_data = pd.read_csv('data/Automobile_data.csv', na_values='?', sep=",")

cols = ['length', 'width', 'height', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price', 'horsepower']

car_data = car_data[cols]
#print(car_data.head())
# missings in each column
#print(car_data.isna().sum())
# remove missiongs
car_data = car_data.dropna()
#print(car_data.isna().sum())
#print(car_data.describe())

color = car_data['price']
scatterMat = pd.plotting.scatter_matrix(car_data, c=color)
plt.show()

df_n = car_data[['city-mpg', 'highway-mpg']].copy()

scaler = StandardScaler()
cols = ['city-mpg', 'highway-mpg']
df_n[cols] = scaler.fit_transform(car_data[cols])

X = df_n[['city-mpg']]
y = df_n['highway-mpg']
print(type(X))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=None)

# with and without normaliy
lr = LinearRegression()

lr.fit(X_train, y_train)

print(lr.coef_)
print(lr.intercept_)
print("Trainingsscore", lr.score(X_train, y_train))
print("Test score", lr.score(X_test, y_test))

