

class A:
    def __init__(self):
        self.name = 'John'
        self.age = 23

    def getName(self):
        return self.name


class B:
    def __init__(self):
        self.name = 'Richard'
        self.id = '32'

    def getName(self):
        return self.name


class C(B,A):
    def __init__(self):
        #B.__init__(self)
        #A.__init__(self)
        super().__init__()


    def getName(self):
        return self.name

C1 = C()
print(C1.getName())

#The hierarchy becomes completely depended on the order of
# __init__() calls inside the subclass.
# super() looks at the sequence order of super classes A, B, etc.
