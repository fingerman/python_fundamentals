import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import MeanShift, KMeans

centers = [[1, 1], [5, 5], [3, 10]]

X, y = make_blobs(n_samples=500, centers=centers)

kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

labels = kmeans.labels_
cluster_centers = kmeans.cluster_centers_
color_type = ['r.', 'g.', 'b.', 'c.', 'y.']

plt.scatter(cluster_centers[:, 0], cluster_centers[:,1], marker='x', color= 'k', s=150, zorder = 10, linewidths=5, alpha=0.5)
# plt.show()
