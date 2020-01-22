"""
    zip(iter1 [,iter2 [...]]) --> zip object

    Return a zip object whose .__next__() method returns a tuple where
    the i-th element comes from the i-th iterable argument.  The .__next__()
    method continues until the shortest iterable in the argument sequence
    is exhausted and then it raises StopIteration.
"""


coords_x = [1, 2, 3]
coords_y = [22, 14, 5]

zipped_coords = zip(coords_x, coords_y)
print(list(zipped_coords))

coords_z = [46, 22, 45]
zipped_coords = zip(coords_x, coords_y, coords_z)
print(list(zipped_coords.__next__()))
print(list(zipped_coords.__next__()))
print(list(zipped_coords))


