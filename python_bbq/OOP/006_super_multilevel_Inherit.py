#Python super() function allows us to refer to the parent class explicitly
#It’s useful in case of inheritance where we want to call super class functions.
#we have called parent class function as:
#person.__init__(self, student_name, student_age)
#We can replace this with python super function call as below.
#super().__init__(student_name, student_age)
#The output will remain the same in both the cases
#Python super function with multilevel inheritance
#Python super() will always refer the immediate superclass
#Also Python super() function not only can refer the __init__() function
#but also can call all other function of the superclass

class A:
    def __init__(self):
        print('Initializing: class A')

    def sub_method(self, b):
        print('Printing from class A:', b)


class B(A):
    def __init__(self):
        print('Initializing: class B')
        super().__init__()

    def sub_method(self, b):
        print('Printing from class B:', b)
        super().sub_method(b + 1)


class C(B):
    def __init__(self):
        print('Initializing: class C')
        super().__init__()                  # inherit the method from Class A
#       super(B)                            # use this if you want not to print

    def sub_method(self, b):
        print('Printing from class C:', b)
        super().sub_method(b + 1)            # inherit the method from Class B


c = C()
c.sub_method(1)


