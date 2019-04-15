thislist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

the_list = list()
print(the_list)

# replace the second item:
thislist[1] = "a"
print(thislist)

# len()
print(len(thislist))

# append()    -add an item to the end of the list
thislist.append('i')
print(thislist)

# insert(i, x)    -insert an item at a certain position
thislist.insert(1, 'b')
print(thislist)

# remove()      - removes the first item with that value:
thislist.remove('a')
print(thislist)

# pop(i)
thislist.pop(0)
print(thislist)
