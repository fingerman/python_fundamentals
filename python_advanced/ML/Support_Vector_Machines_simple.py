import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.svm import SVC

import numpy as np

X = np.array([[-1, -1],
              [-2, -1],
              [1, 1],
              [2, 1]])
y = np.array([1, 1, 2, 2])
from sklearn.svm import SVC

clf = SVC(gamma='auto')
clf.fit(X, y)
SVC(kernel='linear')
print(clf.predict([[0.8, 1]]))
