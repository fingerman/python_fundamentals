class A:
    X = 0 # X will be overwritten at each object creation

    def __init__(self, v=0):
        self.v = v
        A.X += v


a = A()
b = A(1)
c = A(2)

print(c.X)