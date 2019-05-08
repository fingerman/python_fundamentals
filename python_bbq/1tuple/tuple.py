myTuple = ("Banane", "Orange", "Apfel")

print("-- len(tuple) - number of elements")
print(len(myTuple))

print("---count()  - counts elements equal to attribute  ")
print(myTuple.count("Banane"))

print(" ---  index()	Searches the tuple for a specified value and returns the position of where it was found")
print(myTuple.index("Banane"))

print("---  Tuple of one element")
t = ("tup")
t1 = ("tup", )
print(type(t))
print(type(t1))
