import numpy as np

arr = np.ones(shape=(5, 5))
# i = np.arange(1, 5, 2)
arr[0, 1] = 2
# print(arr)

# print(arr[0,1])

m = np.zeros(shape=(5, 5))
m1 = np.split(m, [1, 5])

# random matrix

rm = np.random.rand(3, 5)
print(rm)
print()
print(rm.mean(0))
print(np.mean(rm, axis=0))

# mean of each countable

print(np.mean(rm[:, [1, 3]], axis=0))


