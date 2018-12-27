'''

Problem 2. Lists
Input / Constraints
You will be given a single lines of elements(integers), separated with one or more spaces. You should check if all elements in the line are unique. If they are you should increase the value of every even element with the number of 2 and print the list on single row in ascending order separated by ",".
If they are not unique you should increase every odd element with the number of 3 and print them on single row, separated with ":"
On the next line you should print sum of the all elements divided by the count of the elements in the list. You should do that until you receive the command "stop playing"
Output
If the elements are unique
Unique list: {elements in the list, separated by “,”}
Output: {sum of all elements divided by the length of the list}
Else
Non-unique list: {elements in the list, separated by “:”}
Output: {sum of all elements divided by the length of the list}


Input
1 2  3   4 5 6
1 1 2   2 1 4 7 7 8 8
 5 5 5 5
stop playing

Output
Unique list: 1,3,4,5,6,8
Output: 4.50
Non-unique list: 2:2:4:4:4:4:8:8:10:10
Output: 5.60
Non-unique list: 8:8:8:8
Output: 8.00

'''

list_nums = []

line = input()
while line != "stop playing":
    tokens = [int(x.strip()) for x in line.split()]
    list_nums.append(tokens)
    line = input()

for row in list_nums:
    if len(row) == len(set(row)):
        row_increased = [x if x % 2 != 0 else x+2 for x in row]
        row_increased.sort()
        print(f'Unique list: {",".join(map(str, row_increased))}')
        output = (sum(row_increased) / len(row_increased))
        print(f'Output: {output:.2f}')
    else:
        row_odd_increased = [x if x % 2 == 0 else x+3 for x in row]
        row_odd_increased.sort()
        print(f'Non-unique list: {":".join(map(str, row_odd_increased))}')
        output2 = sum(row_odd_increased) / len(row_odd_increased)
        print(f'Output: {output2:.2f}')


