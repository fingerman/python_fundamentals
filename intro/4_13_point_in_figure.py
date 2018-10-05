h = float(input())
x = float(input())
y = float(input())

if (x >= 0) and (x <= 3 * h) and (y >= 0) and (y <= h):
    if (x > 0) and (x < 3 * h) and (y > 0) and (y < h):
        print("inside")
    elif (x > h) and (x < 2 * h) and (y == h):
        print("inside")
    else:
        print("border")
elif (x >= h) and (x <= 2 * h) and (y >= h) and (y <= 4 * h):
    if (x > h) and (x < 2 * h) and (y > h) and (y < 4 * h):
        print("inside")
    elif (x > h) and (x < 2 * h) and (y == h):
        print("inside")
    else:
        print("border")

else:
    print("outside")

