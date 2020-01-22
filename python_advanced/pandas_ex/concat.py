import pandas as pd
import numpy as np
import random
import string

s1 = pd.Series(['A', 'B', 'C'])
s2 = pd.Series(['D', 'E', 'F'])

# print(pd.concat([s1, s2], ignore_index=True))

# change axis
# print(pd.concat([s1, s2], ignore_index=True, axis=1))


# two 2x2 dataframes with random numbers. Column names A, B and B, C
df_1 = pd.DataFrame({'A': [random.randint(0, 10) for i in range(0, 3)], 'B': [random.randint(100, 200) for x in range(0, 3)]})
df_2 = pd.DataFrame({'B': [random.randint(100, 200) for i in range(0, 3)], 'C': [random.randint(1000, 2000) for x in range(0, 3)]})
df_conc = pd.concat([df_1, df_2], ignore_index=True, axis=0)
df_conc1 = pd.concat([df_1, df_2], ignore_index=True, axis=0)
df_conc2 = pd.concat([df_1, df_2], join='inner', ignore_index=True, axis=0)

print(df_1)
print(df_2)
print("Concate raw \n", df_conc)
print("Concate outer join \n", df_conc1)
print("Concate inner join \n", df_conc2)

print("Append \n", df_1.append(df_2))

