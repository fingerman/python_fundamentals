'''
Read a list of integers on the first line of the console. After that, find the smallest item in the list and print it on the console.
Examples
Input	Output
1 2 3 4 5	1
9 8 7 82 78 13	7
78 77 1268 43 9	9

'''

list_nums = [int(item) for item in input().split(' ')]

a = 99999
for i in list_nums:
    if i < a:
        a = i
print(a)



