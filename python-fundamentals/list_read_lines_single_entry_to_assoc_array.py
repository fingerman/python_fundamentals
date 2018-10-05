'''
2
1
2
3
4
5
6
'''

n = int(input())
all_lists = []
for i in range(n):
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    list_num = [num1, num2, num3]
    all_lists.append(list_num)

print(all_lists[1])

