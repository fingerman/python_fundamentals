h = int(input())
m = int(input()) + 15

if m > 59:
    m = m-60
    h = h + 1
if h > 23:
    h = h - 24
if m < 10:
    print(str(h) + ":" + "0" + str(m))
else:
    print(str(h) + ":" + str(m))
