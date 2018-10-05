n = int(input())

row = 1
num = 1
col = 1
while num <= n:
    column = 0
    while num <= n and column < col:
        print('{0} '.format(num), end='')
        num += 1
        column += 1
    print()
    col += 1