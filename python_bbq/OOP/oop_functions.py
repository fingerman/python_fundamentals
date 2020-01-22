class Animal:
    def __init__(self, race, legs, colour):
        self.race = race
        self.legs = int(legs)
        self.colour = colour


class Cat(Animal):
    def __init__(self, race, legs, colour, sound):
        Animal.__init__(self, race, legs, colour)
        self.sound = sound


class Dog(Animal):

    owner = 0

    def __init__(self, race, legs, colour, tail):
        Animal.__init__(self, race, legs, colour)
        self.tail = tail


class Turtle(Animal):
        super(Animal)


dog = Dog("Pincher", 4, "white", "long")

print('-----  hasattr(obj, attr_name)   --------')
'''hasattr(obj, attr_name) -  returns true if an object has the given named attribute and false if it does not.
                            - You can use it also to find out if a class variable is available  '''
print(hasattr(dog, 'tail'))
print(hasattr(dog, 'ownerr'))

print('----type()-------------------------------')
print(type(dog))

print('-----  isubclass(object, classinfo)  -----')
'''issubclass(object, classinfo) -  checks if the object argument (first argument) 
is a subclass of classinfo class (second argument).
* True if object is subclass of a class, or ANY element of the tuple
* False otherwise
'''
print(issubclass(Turtle, Dog))              # False
print(issubclass(Turtle, (list, Animal)))   # True
print(issubclass(Animal, Animal))           # True
print(issubclass(Animal, (list, Animal)))   # True
print(issubclass(Animal, list))             # False, list is obj of class "list"
print(list.__class__.__name__)
print(issubclass(Animal, (Animal, Dog)))  # True


print('-----  isinstance(object, classinfo)  -----')
'''
checks if the object (first argument) is an instance or subclass of classinfo class (second argument).
        - or has the same properties
'''

print(isinstance(dog, Dog))                 # True
print(isinstance(dog, Animal))              # True
print(isinstance(dog, Turtle))              # False
print(isinstance(dog, (Cat, Turtle)))       # False
print(isinstance(dog, (Cat, Turtle, Animal)))       # True -> if one is True, then return is True
print(issubclass(list, type))
