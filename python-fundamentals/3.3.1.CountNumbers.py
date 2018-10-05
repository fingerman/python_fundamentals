'''03. Count Numbers
Read a list of integers in range [0…1000] and print them in ascending order along with their number of occurrences.
Examples
Input
8 2 2 8 2 2 3 7
Output
2 -> 4
3 -> 1
7 -> 1
8 -> 2

10 8 8 10 10
8 -> 2
10 -> 3
Hints
Several algorithms can solve this problem:
•	Use a list count to count in counts[x] the occurrences of each item x.
•	Sort the numbers and count occurrences of each number.
Counting Occurrences Using List
1.	Read the input items in list of integers.
2.	Allocate a list counts.
•	It will hold for each number x its number of occurrences counts[x].
3.	Scan the input items and for each item x increase counts[x].
This algorithm has a serious drawback:
•	It depends on mapping numbers to list indexes.
•	It will work well for input values in the range [0…1000].
•	It will not work for very large and very small values, e.g. if the input holds -100 000 000 or 100 000 000.
•	It will not work for real numbers, e.g. 3.14 or 2.5.
Counting Occurrences by After Sorting
1.	Read the input items in list of integers. Example: {8, 2, 2, 8, 2, 2, 3, 7}.
2.	Sort the list in increasing order: {2, 2, 2, 2, 3, 7, 8, 8}. Now find all subsequences of equal numbers.
3.	Scan the numbers from left to right. Count how many times each number occurs.
•	Start at count = 1.
•	While the next number on the right is the same as the current number, increase count and proceed to the next number.
•	When the next number on the right is different (or there is no next number), print the current number and its count.
•	Continue scanning from the next number on the right.
This algorithm will work correctly for real numbers and very large numbers. It does not depend on mapping numbers to list indexes.
'''

list_nums = [int(item) for item in input().split(' ')]
sorted(list_nums)

d = dict((x, list_nums.count(x)) for x in set(list_nums))
for key in sorted(d):
    print(f'{key} -> {d[key]}')




