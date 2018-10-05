'''

Write a program to read a list of integers, an integer p, multiply each item by p and print the resulting list.
Examples
Input	    Output
1 3 12 4
4
            4 12 48 16

6 8 1 -9
3
            18 24 3 -27
'''


values = input()
p = int(input())
items = values.split(' ')
nums_list = []
for i in items:
    nums_list += [int(i)] # or nums.append(int(i))


new_list = [i * p for i in nums_list]


for i in new_list:
    print(i, end=' ')
