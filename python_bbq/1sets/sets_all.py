vowels = {'a', 'e', 'e', 'i', 'o', 'u', 'u'}
print(vowels)

print("-----  set()")
vow2 = set('aaaeeeiouuuu')
print(vow2)

print(" --  add() method adds an element to the set if it does not exists")
vow2.add('y')
vow2.add('z')
print(vow2)

print(" --- difference(set2)	returns a set containing the difference between two or more sets")
s = vow2.difference(vowels)
print(s)

print(" intersection(set2)")
i = vow2.intersection(vowels)
print(i)

print(" ---- pop()	Removes an element from the set (random)")
i.pop()
print(i)
i.pop()
print(i)

print(" -------  remove('element')	Removes the specified element")
vowels.remove('a')
print(vowels)