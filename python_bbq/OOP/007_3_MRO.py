class A:
    def __init__(self):
        super().__init__()
        self.name = 'John'
        self.__age = 23

    def getName(self):
        return self.name


class B:
    def __init__(self):
        super().__init__()
        self.name = 'Richard'
        self.id = '32'

    def getName(self):
        return self.name

    def getHisAge(self):
        return self.age

    def getID(self):
        return self.id


class C(B, A):
    def __init__(self):
        super().__init__()

    def getName(self):
        return self.name

C1 = C()
print(C1.getName())
print(C1.getHisAge())
#print(C1.getId())
print()


#Method Resolurtion Order
#MRO works in a depth first left to right way.
#super() in the __init__ method indicates the class that is
#in the next hierarchy. At first the the super() of C indicates A.
#Then super in the constructor of A searches for its superclass.
#If it doesn’t find any, it executes the rest of the code and returns.
#So the order in which constructors are called here is:
#C -> A -> B
#If we call
print(C.__mro__)
#, then we can see the MRO traceroute.
