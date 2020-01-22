import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import MeanShift

centers = [[1, 1, 1], [5, 5, 5], [3, 10, 10]]

X, y = make_blobs(n_samples=500, centers=centers, cluster_std=1)

ms = MeanShift()
ms.fit(X)

labels = ms.labels_
cluster_centers = ms.cluster_centers_

print(cluster_centers)
n_clusters = len(np.unique(labels))
print(f'Number of estimated clusters: {n_clusters}')
color_type = ['r.', 'g.', 'b.', 'c.', 'y.']

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')


for i in range(len(X)):
    ax.scatter(X[i][0], X[i][1], X[i][2], c=color_type[labels[i]])

ax.scatter(cluster_centers[:, 0],
           cluster_centers[:,1],
           cluster_centers[:,2],
            marker='x',
            color = 'k', s=150, zorder = 10, linewidths=5, alpha=0.5)

ax.scatter(cluster_centers[:, 0],
            cluster_centers[:,1],
           cluster_centers[:, 2],
           marker='x',
            color = 'k', s=150, zorder = 10, linewidths=5, alpha=0.5)

plt.show()
