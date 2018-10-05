n = int(input())
sum = 0
max = -1000
for i in range(1, n+1):
    i = int(input())
    sum = sum+i
    if i > max:
        max = i

if (sum - max) == max:
    print("Yes" + "\n" + "Sum = " + str(max))
if (sum - max) != max:
    print("No" + "\n" + "Diff = " + str(abs(max - (sum-max))))

