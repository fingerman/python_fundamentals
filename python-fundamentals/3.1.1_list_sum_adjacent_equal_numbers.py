'''
Write a program to sum all adjacent equal numbers in a list of decimal numbers, starting from left to right.
	After two numbers are summed, the obtained result could be equal to some of its neighbors and should be summed as well (see the examples below).
	Always sum the leftmost two equal neighbors (if several couples of equal neighbors are available).
Examples
Input	        Output	Explanation
3 3 6 1	        12 1	3 3 6 1  6 6 1  12 1
8 2 2 4         8 16	16 8 16	8 2 2 4 8 16  8 4 4 8 16  8 8 8 16  16 8 16
5 4 2 1 1 4	    5 8 4	5 4 2 1 1 4  5 4 2 2 4  5 4 4 4  5 8 4
'''

list_nums = [float(item) for item in input().split(' ')]

i = 0
while i in range(len(list_nums)-1):
    if list_nums[i] == list_nums[i+1]:
        list_nums[i] = list_nums[i] + list_nums[i+1]
        del(list_nums[i+1])
        i = i-1
        if i < 0:
            i = 0   # if very left were equal start from the beginning
    else:
        i = i+1     # move forward the very left are not equal


print(" ".join(map(str, list_nums)))

