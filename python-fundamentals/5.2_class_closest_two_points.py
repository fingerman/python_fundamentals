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


points = []
count = int(input())
for i in range(count):
    points.append(build_point())

distance = float('Infinity')
last_point = len(points)
closest_points = [None, None]
for a in range(last_point):
    for b in range(a + 1, last_point):
        current_distance = points[a].calc_distance(points[b])
        if current_distance < distance:
            distance = current_distance
            closest_points = [a, b]

print(f'{distance:.3f}\n'
      f'({points[closest_points[0]].x:g}, {points[closest_points[0]].y:g})\n'
      f'({points[closest_points[1]].x:g}, {points[closest_points[1]].y:g})')
