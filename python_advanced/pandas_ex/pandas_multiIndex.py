import pandas as pd
import numpy as np

ar = pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'], [1, 2, 1, 2]])
# print(ar)


index = [('California', 2000), ('California', 2010), ('New York', 2000), ('New York', 2010), ('Texas', 2000),
         ('Texas', 2010)]
population = [33543543, 35543741, 5435435, 5935435, 2432432, 3333453]
pop_s = pd.Series(population, index)

# print from to
# print(pop_s[('California', 2010):('Texas', 2000)])

# show just 2000 - list comprehension
# print(pop_s[[i for i in pop_s.index if i[1] == 2000]])

mindex = pd.MultiIndex.from_tuples(
    [('California', 2000), ('California', 2010), ('New York', 2000), ('New York', 2010), ('Texas', 2000),
     ('Texas', 2010)])
pop_mindex = pd.Series(population, mindex)

print(pop_mindex)
print(type(pop_mindex))

# take one subindex and put it as column index
print(pop_mindex.unstack())

pop_df = pd.DataFrame({'all': pop_mindex, 'u_18': [432432, 432432, 876876, 5765765, 1232143, 987987]})
print(pop_df)
# with two sublevels
print(pop_df.unstack())
