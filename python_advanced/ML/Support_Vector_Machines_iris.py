import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn import svm, datasets

data = datasets.load_iris()


features = np.array(data.data)
labels = np.array(data.target)


# try it out with different kernels
def plot_data(X, y, kernel_fn='linear', C=1.0, degree=3, gamma='auto'):
    fig, (ax1, ax2) = plt.subplots(ncols=2)

    for i in range(2):
        ax = [ax1, ax2][i]

        svm = SVC(kernel=kernel_fn, C=C, degree=degree, gamma=gamma)
        svm.fit(X[:, 2 * i:2 * i + 2], y)

        # min and max values in X
        x_min = X[:, 0 + (2 * i)].min() - 1
        x_max = X[:, 0 + (2 * i)].max() + 1

        y_min = X[:, 1 + (2 * i)].min() - 1
        y_max = X[:, 1 + (2 * i)].max() + 1

        # matrix with all coordinates btw min and max
        # C = 0.05

        xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.05),
                             np.arange(y_min, y_max, 0.05))

        Z = svm.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        ax.contourf(xx, yy, Z, cmap=plt.cm.summer, edgecolors = 'k')
        ax.scatter(X[:, 0+(2*i)], X[:, 1+(2*i)], c=y, cmap = plt.cm.summer, edgecolors='k')
        ax.get_xaxis().set_ticks([])
        ax.get_yaxis().set_ticks([])

    ax1.set(ylabel='Sepalum Plot', title=f'Kernel Function: {kernel_fn}, C: {C}, gamma: {gamma}')
    ax2.set(ylabel='Pepalum Plot', title=f'Kernel Function: {kernel_fn}, C: {C}, gamma: {gamma}')

    plt.show()




plot_data(features, labels)
