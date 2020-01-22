class A():
    def a(self):
        print("A", end='')

class B(A):
    def a(self):
        print("B", end='')


a = A()
b = B()

a.a()
b.a()
