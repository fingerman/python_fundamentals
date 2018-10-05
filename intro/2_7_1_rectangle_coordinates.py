x1 = input()
y1 = input()
x2 = input()
y2 = input()
a = max(float(x1), float(x2)) - min(float(x1), float(x2))
b = max(float(y2), float(y1)) - min(float(y1), float(y2))
area = a*b
perimeter = 2 * (a+b)
print(area)
print(perimeter)

