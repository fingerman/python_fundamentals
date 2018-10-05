'''Read a list of integers on the first line of the console and an integer N
from the second line of the console and print whether the item is contained
in the list. If it is, print “yes”, otherwise print “no”.
Examples
Input	            Output
1 2 3 4 5
5	            yes
8 7 7 9 6 2 2
11	                no
99 7 8 6 2314 2
2314	            yes
'''

list_nums = [int(item) for item in input().split(' ')]
token = int(input())

if token in list_nums:
    print("yes")
else:
    print("no")


