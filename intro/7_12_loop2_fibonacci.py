n = int(input())

prev = 1
curr = 1

if n < 2:
    print(1)
else:
    for i in range(0, n - 1):
        next = prev + curr
        prev = curr
        curr = next
    print(curr)