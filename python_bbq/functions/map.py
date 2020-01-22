'''
map(func, *iterables) --> map object

    Make an iterator that computes the function using arguments from
    each of the iterables.  Stops when the shortest iterable is exhausted.
    -> returns iterator
'''

def myfunc(a, b):
    return a + b


x = list(map(myfunc, 'apple', 'orange'))
print(x)

l = list(map(myfunc, ['apple'], ['orange']))
print(l)



#========================

lst1 = [10, 11, 12, 13, 14, 15, 23, 55, 90]
lst2 = [10, 11, 15, 20, 33, 15, 16]
lst_neu = list(map(lambda x: x%5, lst1))
print(lst_neu)











