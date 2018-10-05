import math

n = int(input())
sum1 = 0
sum2 = 0
for i in range(0, n):
    i = int(input())
    sum1 = sum1+i

for b in range(n, 2*n):
    b = int(input())
    sum2 = sum2+b

if sum1 == sum2:
    print("Yes, sum = " + str(sum1))
elif sum1 != sum2:
    print("No, diff = " + str(abs(sum1 - sum2)))

