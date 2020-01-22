'''
Special attributes:
__name__ is the class name;
__module__ is the module name in which the class was defined;
__dict__ is the dictionary containing the class’s namespace;
__bases__ is a tuple containing classes (not class names) which are direct superclasses for the class.
            The order is the same as that used inside the class definition.
__doc__ is the class’s documentation string, or None if undefined;
__annotations__ (optional) is a dictionary containing variable annotations collected during class body execution.

'''



class Animal:
    def __init__(self, race, legs, colour):
        self.race = race
        self.legs = int(legs)
        self.colour = colour


class Cat(Animal):                              # inherit from superclass, Animal
    def __init__(self, race, legs, colour, sound):
        super().__init__(race, legs, colour)
        self.sound = sound


class Dog(Animal):                              # inherit from Animal
    def __init__(self, race, legs, colour, tail):
        Animal.__init__(self, race, legs, colour)
        self.tail = tail


class Turtle(Animal):
        super(Animal)


class Pincher(Dog, Cat):
    def __init__(self, race, legs, colour, tail, sound, name):
        Dog.__init__(self, race, legs, colour, tail)
        Cat.__init__(self, race, legs, colour, sound)
        self.name = name


persian_cat = Cat("Persian", 4, "brown", "Miau")

new_pincher = Pincher("Pincher", 4, "black", "short", "BauBau", "Becky")

print(persian_cat.__dict__)

print(persian_cat.__class__.__name__)

print(persian_cat.__module__)

print(persian_cat.__class__.__bases__)
print(new_pincher.__class__.__bases__)

