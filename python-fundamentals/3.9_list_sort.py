'''
Read a list of integers and sort them in ascending order. Print the output as shown in the examples below.
Examples
Input	Output
8 2 7 3	    2 <= 3 <= 7 <= 8
2 4 -9	    -9 <= 2 <= 4
'''

data = list(map(int, input().split()))
data.sort()
for i in data:
    print(i, end=" <= ", flush=False)
