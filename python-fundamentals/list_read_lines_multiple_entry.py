'''
2 8 30 25 40
'''

values = input()
items = values.split(' ')
nums_list = []
for i in items:
    nums_list += [int(i)]   # or nums.append(int(i))

print(type(items[1]))
print(type(nums_list[1]))



