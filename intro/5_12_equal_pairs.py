import math

n = int(input())
currSum = 0
prevSum = 0
diff = 0
maxDiff = 0
for i in range(0, n):
    prevSum = currSum
    currSum = 0
    currSum += int(input())
    currSum += int(input())
    if i != 0:
        diff = abs(currSum - prevSum)
        if diff != 0 and diff > maxDiff:
            maxDiff = diff
if maxDiff == 0 or n == 1:
    print("Yes, value=" + str(currSum))
else:
    print("No, maxdiff=" + str(maxDiff))


'''
Дадени са 2*n-на брой числа. Първото и второто формират двойка, третото и четвъртото също и т.н. Всяка двойка има стойност –
 сумата от съставящите я числа. Напишете програма, която проверява дали всички двойки имат еднаква стойност или печата максималната
  разлика между две последователни двойки. Ако всички двойки имат еднаква стойност, отпечатайте "Yes, value={Value}" (стойността). 
  В противен случай отпечатайте "No, maxdiff={Difference}" (максималната разлика). 
'''