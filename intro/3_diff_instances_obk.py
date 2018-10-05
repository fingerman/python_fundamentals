a = 5
b = 5
print(id(a))
print(id(b))
print(a is b)
print(type(a))

c = [1, 2]
d = [2, 2]
print(id(c))
print(id(d))
print(type(c))

# is compares the value of the objects/instances, not values
print(c == d)
print(c is d)
