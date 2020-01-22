def makeclosure(par):
    loc = par

    def power(p):
        return p ** loc

    return power


fsqr = makeclosure(2)
fcub = makeclosure(3)
print(fsqr(3))

for i in range(5):
     print(i, fsqr(i), fcub(i))     # fsqr(i) invoces the inner var, fsqr has already one argument with makeclosure(2)


'''
closure not only makes use of the frozen environment
it can also modify its behavior by using values taken from the outside.
'''