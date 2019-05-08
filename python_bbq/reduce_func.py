from functools import reduce

myNums = [92, 27, 63, 43, 88, 8, 38, 91, 47, 74, 18, 16, 20, 21, 59, 65]

p = reduce(lambda x, y: x/y, myNums)
print(p)