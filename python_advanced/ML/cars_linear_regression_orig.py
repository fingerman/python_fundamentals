import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

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
X = df_n[['city-mpg']]
y = df_n['highway-mpg']
print(type(X))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=None)

# with L2 Normalization

lrT = LinearRegression(normalize=True)
lrT.fit(X_train, y_train)
print(lrT.coef_, lrT.intercept_)
print("Trainingsscore", lrT.score(X_train, y_train))
print("Test score", lrT.score(X_test, y_test))

# without normalization
lrF = LinearRegression(normalize=False)
lrF.fit(X_train, y_train)
print(lrF.coef_, lrT.intercept_)
print("Trainingsscore", lrF.score(X_train, y_train))
print("Test score", lrF.score(X_test, y_test))

# with standartization

sc = StandardScaler()
X_train_stand=sc.fit_transform(X_train)
X_test_stand=sc.fit_transform(X_test)
lrS_model=LinearRegression()
lrS_model.fit(X_train_stand, y_train)
# >> accuracy_score(Y_test,knn.predict(X_test_minmax))
print(lrS_model.coef_)
print(lrS_model.intercept_)
print("Trainingsscore", lrS_model.score(X_train, y_train))
print("Test score", lrS_model.score(X_test, y_test))




# x_new = np.linspace(X_train.min(), X_train.max(), 200)
#
# plt.scatter(X_train, y_train, color = 'b')
# plt.scatter(X_test, y_test, color = 'g')
# plt.plot(x_new, lr.predict(x_new), color = 'r')
# plt.show()