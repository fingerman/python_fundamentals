from math import sqrt

class Rectangle:

    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.right = left + width
        self.bottom = top + height

    def is_inside(self, r2):
        is_in_left = self.left >= r2.left
        is_in_right = self.right <= r2.right
        is_in_top = self.top <= r2.top
        is_in_bottom = self.bottom <= r2.bottom
        return is_in_left and is_in_right and is_in_top and is_in_bottom


def read_rectangle():
    coordinates = list(map(float, input().split(' ')))
    return Rectangle(*coordinates)


rectangle1 = read_rectangle()
rectangle2 = read_rectangle()

print('Inside' if rectangle1.is_inside(rectangle2) else 'Not inside')
