# Wenn eine Methode versucht, ein Object als Argument zu bearbeiten,
# schaut sie sich zunächst, um welche Objektinstanz es sich handelt

class Dog():
    def talk(self):
        return "bark"
class Cat():
    def talk(self):
        return "meow"

my_dog=Dog()
my_cat=Cat()
print(my_dog.talk())
print(my_cat.talk())

