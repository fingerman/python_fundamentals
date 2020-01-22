# Static methods in Python are extremely similar to python class level methods.
# the difference being that a static method is bound to a class rather than the
# objects for that class.
# This means that a static method can be called without an object for that class

# the difference between a static method and a class method is:
#
# Static method knows nothing about the class and just deals with the parameters.
# Class method works with the class since its parameter is always the class itself.

# Python Static methods can be created in two ways.
# staticmethod():

class Calculator:

    def multiplyNums(x, y):
        return x + y

# create addNumbers static method
Calculator.multiplyNums = staticmethod(Calculator.multiplyNums)

print('Product:', Calculator.multiplyNums(15, 110))

#@staticmethod
class Calculator:

    # create addNumbers static method
    @staticmethod
    def multiplyNums(x, y):
        return x + y

print('Product:', Calculator.multiplyNums(15, 110))

#Advantages of Python static method
#Static methods have a very clear use-case
#When we need some functionality not w.r.t an Object but w.r.t the complete class
#we don’t need the self to be passed as the first argument.
