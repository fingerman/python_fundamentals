import itertools as it

### endlos

# counter = it.count(start=5, step=-0.5)
#
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
#
# cyc = it.cycle([1,2,3])

#
# print(next(cyc))
# print(next(cyc))
# print(next(cyc))
# print(next(cyc))
# print(next(cyc))
# print(next(cyc))
# print(next(cyc))
# print(next(cyc))
# print(next(cyc))
#
# rep = it.repeat([1,2,3], times=5)
#
# for i in rep:
#     print(i)

#### comb + perm

# comb = it.combinations([1,2,3], 2)
# print(list(comb))
#
# c_w_r = it.combinations_with_replacement([1,2,3], 2)
# print(list(c_w_r))
#
#
# per = it.permutations([1,2,3], 2)
# print(list(per))
#
# prod = it.product([1,2,3], repeat=2)
# print(list(prod))


# Aufgabe:
# Wirf zwei 6-seitige Würfel und gib alle möglichen Augenpaare an. Wieviele Möglichkeiten gibt es.

# # Möglichkeiten
# print(list(it.combinations_with_replacement(range(1,7), 2)))
# # Anzahl der Möglichkeiten
# print(len(list(it.combinations_with_replacement(range(1,7), 2))))


# Aufgabe: Welche Augenzahl insgesamt kommt wie häufig vor?
# Wurf mit zwei 6-seitgen Würfeln.
# Nutze modul 'itertools'.

# augen = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}

# augen = {}
#
# wurf = list(it.product([1, 2, 3, 4, 5, 6], repeat=2))
#
# for w in wurf:
#     augen[w[0]+w[1]] = 0
#
# for w in wurf:
#     augen[w[0]+w[1]] += 1
#
#
# for key, value in augen.items():
#     print(key, (value/len(wurf))*100)

# import numpy as np
#
# ch = it.chain([1, 2, 3], np.asarray((4, 5 , 6)))
#
# for c in ch:
#     print(c)

#
# result = it.islice(range(10), 2,  8, 2)
#
# for r in result:
#     print(r)

# l = (1, 2, 3, 4)
# b = [0, 1]
# b2 = [True, True, False, True, True]
#
# comp = it.compress(l, b)
# print(list(comp))
#
# comp = it.compress(l, b2)
# print(list(comp))

# def lt2(n):
#     if n<2:
#         return True
#     return False
#
# nums = [0, 2, 5, 1, 0, 3]
#
# # bei filter erst funktion, dann iterable
# result = filter(lt2, nums)
#
# print(list(result))
# # bei filterfalse erst funktion, dann iterable
# result = it.filterfalse(lt2, nums)
#
# print(list(result))

# nums = [0, 1, 1, 2, 5, 1, 0, 3]
# x = 5
# def lt5(n):
#     if n<x:
#         return True
#     return False
#
# take = it.takewhile(lt5, nums)
#
# print(list(take))
# x = 2
# drop = it.dropwhile(lt5, nums)
# print(list(drop))

# nums = [1, 1, 2, 5, 1, 0, 3]
#
# def mul(a, b):
#     return a*b
#
# # !!! bei accumulate ist das zweite argument die funktion
# acc = it.accumulate(nums, mul)
# print(nums)
# print(list(acc))

# def get_state(person):
#     return person['state']
#
# people = [
#         {'name': 'John Doe', 'state': 'NY'},
#         {'name': 'Jane Doe', 'state': 'WY'},
#         {'name': 'Jon Doe', 'state': 'WY'},
#         {'name': 'Jeremy Doe', 'state': 'NY'},
#         {'name': 'Jason Doe', 'state': 'NY'},
#         {'name': 'Jacob Doe', 'state': 'NY'},
# ]
#
# person_group = it.groupby(people, get_state)
#
# for key, group in person_group:
#     print(key, group)
#     for person in group:
#         print(person)
#     print('---------')
#

#
# nums = [1, 1, 2, 5, 1, 0, 3]
#
# def lt2(n):
#     if n<2:
#         return True
#     return False
#
# l2 = it.groupby(nums, lt2)
#
# for key, group in l2:
#     print(key)
#     for value in group:
#         print(value)
#     print('---------')

# l = [1, 1, 2, 5, 1, 0, 3]
#
# # l1  = it.tee(l, 3)
#
# l1, l2, l3 = it.tee(l, 3)
#
# print(l1)
# for e in l1:
#     print(e)
# # die iterable kopien verbrauchen sich beim aufrufen
# print(list(l1))
# # print(list(l2))
# # print(list(l3))

# l1 = [1, 2, 3]
# l2 = [4, 5, 6, 7]
#
# z = zip(l2, l1)
#
# for i in z:
#     print(i)
#
# zl = it.zip_longest(l2, l1, fillvalue=0)
#
# for i in zl:
#     print(i)

def func(x):
    return x*x

nums = [1, 2, 3]
def func2(x, y, z):
    return x*y*z
quad = map(func, nums)
print(list(quad))
nums2 = [(2,2, 3), (4,1, 1), (23,2, 5), (2,5, 0)]
starquad = it.starmap(func2, nums2)

print(list(starquad))
