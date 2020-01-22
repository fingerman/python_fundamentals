'''
We can say that Python looks for object components in the following order:

inside the object itself;
in its superclasses, from bottom to top;
if there is more than one class on a particular inheritance path, Python scans them from left to right.
'''

class Left:
    Var = 'L'
    VarL = 'LL'

    def fun(self):
        return 'left'


class Right:
    Var = 'R'
    VarR = 'RR'

    def fun(self):
        return 'right'


class Sub(Left, Right):   # first Left. If var is found, then stop searching
    pass


object = Sub()

print(object.Var, object.VarL, object.VarR, object.fun())
print(object.__dict__)
