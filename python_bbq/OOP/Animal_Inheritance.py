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
    def __init__(self, race, legs, colour, tail):
        super().__init__(race, legs, colour)
        self.tail = tail


class Turtle(Animal):
        super(Animal)


# something = Animal("General", 4, "all_colours")
# print(something.give_properties())
# print()
persian_cat = Cat("Persian", 4, "brown", "Miau")
print(persian_cat.__dict__)
# print()
# pitbull = Dog("Pitbull Terrier", 4, "black-white", "short")
# print(pitbull.__dict__)

turtle = Turtle("Sethose", 150, "standard colors")
print(turtle.__dict__)
print(turtle.__class__.__name__)
print(turtle.__class__.__bases__)

print(hasattr(turtle, 'race'))
