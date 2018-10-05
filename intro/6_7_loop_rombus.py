n = int(input())
r = 0
r2 = n
for i in range(0, n):
    r += 1
    print((n-r)*" " + r*"* " + (n-r)*" ")
for i in range(0, n):
    r2 -= 1
    print((n-r2)*" " + r2*"* " + (n-r2)*" ")
