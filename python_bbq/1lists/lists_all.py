thislist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
print(thislist)

print("append()    -add an item to the end of the list")
thislist.append('i')
print(thislist)


print("list.copy() - returns copy of the list: ")
second_list = thislist.copy()
print(id(thislist))
print(id(second_list))

print("list.count('a') - eturn the number of times the value in list: ")
print(thislist.count('a'))

print("Add the elements of a list (or any iterable), to the end of the current list. No return:  ")
add_list = ['w', 'x', 'y', 'z']
second_list.extend(add_list)
print(second_list)

print("the index(i) method returns THE POSITION OF THE FIRST OCCURRENCE of the specified value.")
print(thislist.index("f"))

print("insert(i, x)    -insert an item at a certain position .insert(1, b)")
thislist.insert(1, 'b')
print(thislist)

print("replace the second item:")
thislist[1] = "a"
print(thislist)

print("len()")
print(len(thislist))


print("remove()      - removes the first item with that value:")
thislist.remove('a')
print(thislist)

print("pop()- remove last element, pop(i) -remove element at index:  pop.(-1) - last element")
thislist.pop(-1)
print(thislist)

print('reverse() - No return')
print(thislist.reverse())
print(thislist)

print('list.sort() - No return')
print(thislist.sort())
print(thislist)
