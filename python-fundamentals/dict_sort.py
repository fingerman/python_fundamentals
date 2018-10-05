import collections

d = {'Pierre': 42, 'Anne': 33, 'Mandrigon': 55, 'Samuel': 27, 'Wolfgang': 29}
print(d, '\n')
print('Sort by value in descending order')
dict_key_list = sorted(d.items(), key=lambda kv: -kv[1])    # returns a list fo tuples
print(dict_key_list)
print('Type: ' + str(type(dict_key_list)))
print('Type of list element: ' + str(type(dict_key_list[1])))
dict_key_new = dict(sorted(d.items(), key=lambda kv: -kv[1]))
print('Type: ' + str(type(dict_key_new)) + '\n')
# this abouve makes new dictionary and keeps the original unsorted
# if u want to sort the dict then:

dict_key = collections.OrderedDict(sorted(d.items(), key=lambda kv: -kv[1]))
print(dict_key)
print('Type: ' + str(type(dict_key)) + '\n')
# Ordered dict preserves the order the elements have been insered:
d['Maria'] = 56
d['Johan'] = 13
d['Ben'] = 22
d['Emily'] = 14
for k, v in d.items():
    print(k, v)



# key=lambda kvp: (-kvp[1], kvp[0])))

'''
print(d)
print(sorted_d)             # list of tuples sorted by the second element in each tuple
print(dict(sorted_d))       # print it as dictionary

# sort by name in ascending order
sorted_letters = dict(sorted(d.items(), key=lambda x: x[0]))
print("sorted by name (key)")
print(sorted_letters)
# sort by name in descending order
sorted_letters = dict(sorted(d.items(), key=lambda x: x[0], reverse=True))




# sort first by value then by key(name)
sorted_letters_mult = dict(sorted(d.items(), key=lambda x: (x[1], x[0])))
print(sorted_letters_mult)

'''

