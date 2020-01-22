import pandas as pd


df_1 = pd.DataFrame({'employee': ['Bob', 'Gretel', 'Erna', 'Hilde'], 'Dept': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df_2 = pd.DataFrame({'employee': ['Lisa', 'Gretel', 'Erna', 'Hilde'], 'hire-date': ['2000', '2002', '2004', '2010']})

df_conc = pd.concat([df_1, df_2], axis=1)
# print("Concate raw \n", df_conc)

# merge
df_merge = pd.merge(df_1, df_2)
print("Inner merge \n", df_merge)
print()
df_merge_out = pd.merge(df_1, df_2, how='inner', validate='m:m')
print("Outer merge \n", df_merge_out)