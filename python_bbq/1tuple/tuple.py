"""A tuple is a collection which is ordered and unchangeable.
In Python tuples are written with round brackets."""


myTuple = ("Banane", "Orange", "Apfel")
myTuple2 = ("Banane", "Orange", "Apfel")
print("tuple([]) vls tuple() constructor")
tuple_constructor = tuple(["Banane", "Orange", "Apfel"])
tuple_constructor2 = tuple("Banane")
print(myTuple)
print(tuple_constructor)
print(tuple_constructor2)

print("-- len(tuple) - number of elements")
print(len(myTuple))

print("---count()  - counts elements equal to attribute  ")
print(myTuple.count("Banane"))

print(" ---  index()	Searches the tuple for a specified value and returns the position of where it was found")
print(myTuple.index("Banane"))

print("---  Tuple of one element")
t = ('tup')
t1 = ('tup', )
t2 = ('a', 'b')
print(t, type(t))
print(t1, type(t1))
print(t2, type(t2))
