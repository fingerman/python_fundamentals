n = int(input())
sumEven = float(0)
sumOdd = float(0)
maxEven = float("-inf")
maxOdd = float("-inf")
minEven = float("inf")
minOdd = float("inf")

for i in range(1, n+1):
    if i % 2 == 0:
        c = float(input())
        sumEven = sumEven + c
        if c > maxEven:
            maxEven = c
        if c < minEven:
            minEven = c
    elif i % 2 != 0:
        d = float(input())
        sumOdd = sumOdd + d
        if d > maxOdd:
            maxOdd = d
        if d < minOdd:
            minOdd = d


def check(x):
    if x.is_integer():
        decimals = 0
        return "{0:.{1}f}".format(x, decimals)
    elif x == float("-inf"):
        return "No"
    elif x == float("inf"):
        return "No"
    else:
        return x


print("OddSum=" + str(check(sumOdd)) + "\n" +
      "OddMin=" + str(check(minOdd)) + "\n" +
      "OddMax=" + str(check(maxOdd)) + "\n" +
      "EvenSum=" + str(check(sumEven)) + "\n" +
      "EvenMin=" + str(check(minEven)) + "\n" +
      "EvenMax=" + str(check(maxEven)) + "\n"
      )
'''
Input:
5
3
-2
8
11
-3

OddSum=8, 
OddMin=-3, 
OddMax=8, 
EvenSum=9, 
EvenMin=-2, 
EvenMax=11

Output:

'''
