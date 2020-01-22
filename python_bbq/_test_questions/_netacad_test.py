def I(n):
    s = ''
    for i in range(n):
        s += '*'
        yield s


for x in I(4):
    print(x,end='')