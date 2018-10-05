n = int(input())
sumEven = 0
sumOdd = 0

for i in range(1, n+1):
    if i % 2 == 0:
        c = int(input())
        sumEven = sumEven + c
    elif i % 2 != 0:
        d = int(input())
        sumOdd = sumOdd + d


if sumEven == sumOdd:
    print("Yes" + "\n" + "Sum = " + str(sumOdd))
elif sumEven != sumOdd:
    print("No" + "\n" + "Diff = " + str(abs(sumEven - sumOdd)))
