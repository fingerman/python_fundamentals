import math

figure = input()
area = 0
if figure == "square":
    a = float(input())
    area = math.pow(a, 2)
if figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
if figure == "circle":
    a = float(input())
    area = math.pi * a * a
if figure == "triangle":
    a = float(input())
    h = float(input())
    area = (a*h)/2

print("{0:.3f}".format(area))




