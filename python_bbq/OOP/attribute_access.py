class Class:
    counter = 0 # class var
    def __init__(self, val=1):
        self.__first = val
        Class.counter += 1

    def set_second(self, val=2):
        self.__second = val


object1 = Class()
object2 = Class(2)
object2.set_second(3)
object3 = Class(4)
object3.__third = 5

print(object1.__dict__)
print(object2.__dict__)
print(object3.__dict__)

# class vars
print(object1.counter)
print(object2.counter)
print(object3.counter)