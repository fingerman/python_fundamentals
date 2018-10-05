n = int(input())
i = '*'
s = ' '
print(i*n)
for rows in range(0, n-2):
    print(i + (s*(n-2)) + i)
print(i*n)
