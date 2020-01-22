str1 = "abcd"
str2 = str1[:]
str3 = str1

print(id(str1))
print(id(str2))
print(id(str3))

lst1 = ['a', 'b', 'c', 'd']
lst2 = lst1[:]                  # copy
lst3 = lst1


print(id(lst1))
print(id(lst2))
print(id(lst3))