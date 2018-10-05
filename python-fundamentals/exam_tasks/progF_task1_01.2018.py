'''

Input
2
10
2
3
5
5
5

Output
10 : 2 = 125 (3)
'''


num_balls = int(input())
all_lists = []
for i in range(num_balls):
    snowballSnow = int(input())
    snowballTime = int(input())
    snowballQuality = int(input())
    numberOfThrows = snowballSnow/snowballTime
    snowballValue = numberOfThrows**snowballQuality
    snowballValue = int(snowballValue)
    list_balls = snowballValue, snowballSnow, snowballTime, snowballQuality
    all_lists.append(list_balls)

all_lists.sort(reverse=True)

print(str(all_lists[0][1]) + " : " + str(all_lists[0][2]) + " = " + str(all_lists[0][0]) + " (" + str(all_lists[0][3])
      + ")")
