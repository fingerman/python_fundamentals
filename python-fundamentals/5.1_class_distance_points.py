from math import sqrt

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc_distance(self, other_point):
        x = abs(self.x - other_point.x)
        y = abs(self.y - other_point.y)
        return sqrt(x ** 2 + y ** 2)



def build_point():
    coordinates = list(map(float, input().split(' ')))
    return Point(*coordinates)


a = build_point()
b = build_point()
distance = a.calc_distance(b)

print(f'{distance:.3f}')