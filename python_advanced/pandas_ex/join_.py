import pandas as pd

df_1 = pd.DataFrame({'employee': ['Bob', 'Gretel', 'Erna', 'Hilde'], 'Dept': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df_2 = pd.DataFrame({'employee': ['Lisa', 'Gretel', 'Erna', 'Hilde'], 'hire-date': ['2000', '2002', '2004', '2010']})

df = df_1.set_index('employee').join(df_2, lsuffix='_caller', rsuffix='_other')
df2 = df_1.set_index('employee').join(df_2.set_index('employee'))

print(df2)
# check missings in columns
print(df2.isnull().any(axis=0))
