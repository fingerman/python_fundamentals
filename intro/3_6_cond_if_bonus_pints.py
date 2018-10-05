a = int(input())
b = 0
if a <= 100:
    b = 5
if a > 100:
    b = 0.2*a
if a > 1000:
    b = 0.1*a
if a % 2 == 0:
    b += 1
if a % 10 == 5:
    b += 2
print(b)
print(a+b)

























