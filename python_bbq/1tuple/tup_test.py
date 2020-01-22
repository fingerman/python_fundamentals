"""
tuples may be stored inside tuples and lists

"""


myTuple = ("Banane", "Orange", "Apfel")
myTuple2 = ("Banane1", "Orange1", "Apfel1")

print(myTuple + myTuple2)
print(myTuple2[2])

tuple_nested = ("Banane", ("Orange", "Strawberry"), "Apfel")
print(tuple_nested)
print(tuple_nested[1])
print(type(tuple_nested[1]))

tuple_list = ("Banane", ["Orange", "Strawberry"], "Apfel")
print(tuple_list)
print(type(tuple_list))
print(tuple_list[1])
print(type(tuple_list[1]))

list_tuple = ["Banane", ("Orange", "Strawberry"), "Apfel"]
print(type(list_tuple))
print(type(list_tuple[1]))