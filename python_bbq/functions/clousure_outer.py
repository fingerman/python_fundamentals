def outer(par):
    loc = par

    def inner():
        return loc

    return inner


var = 1
fun = outer(var)  # func is a closure
print(fun())
