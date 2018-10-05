'''

Write a program, which reads a list of integers, calculates its sum and prints it.
The input consists of a number n (the number of items) + n integers, each as a separate line.
Examples
Input	Output
4
1
2
3
4
            10
5
1
1
1
1
1
	        5
4
2
-1
-2
8	        7
'''

n = int(input())

list = []

for i in range(n):
    list += [int(input())]

print(sum(list))
