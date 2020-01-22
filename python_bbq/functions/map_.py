import math

standorte = [(2, 1, 3), (5, 7, -3), (2, 4, 0), (9, 6, 8)]

p = list(map(lambda input : math.sqrt(sum(x*x for x in input)), standorte))
print(p)
