'''
1 2  3   4 5 6
1 1 2   2 1 4 7 7 8 8
 5 5 5 5
stop playing
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


