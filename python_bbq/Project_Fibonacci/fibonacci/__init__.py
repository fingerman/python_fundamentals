def fibo_n(n):
    """return the n-th fibonacci element"""
    a = 0
    b = 1
    if n == 0:
        return 0
    for i in range(1, n):
        c = a + b
        a = b
        b = c
    return b


def fibo_list(n):
    """delivers a list with fibonacci numbers btw the first element
    and n-th element as input"""
    lst = []
    for i in range(0, n+1):
        lst.append(fibo_n(i))
    return lst



