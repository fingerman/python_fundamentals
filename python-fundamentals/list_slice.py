>>> a = [1,2,3,4]
>>> a[0:2] # take items 0-2, upper bound noninclusive
[1, 2]
>>> a[0:-1] #take all but the last
[1, 2, 3]
>>> a[1:4]
[2, 3, 4]
>>> a[::-1] # reverse the list
[4, 3, 2, 1]
>>> a[::2] # skip 2
[1, 3]