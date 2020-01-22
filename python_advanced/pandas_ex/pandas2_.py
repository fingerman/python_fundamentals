import pandas as pd
import numpy as np

# build dataframe


area = pd.Series({'California': 423534,
                  'Texas': 54254,
                  'Florida': 543543,
                  'New York': 63543,
                  'Illinois': 54364}, name='area')

population = pd.Series({'California': 6763554,
                        'Texas': 654345,
                        'Florida': 123432,
                        'New York': 123243,
                        'Illinois': 13432}, name='population')

df = pd.DataFrame({'area': area, 'population': population})
print(df)

s1 = pd.Series(np.arange(5), index=np.arange(0, 10, 2), dtype='int')
s2 = pd.Series(np.arange(5)+10, index=np.arange(0, 10, 2), dtype='int')
s3 = pd.Series(np.arange(10)+20, index=np.arange(10), dtype='int')

df2 = pd.DataFrame({'s1': s1, 's2': s2, 's3' : s3})
print(df2)
print()
# via axis u can manipulate if rows, columns
print(df2.dropna())
print()
print(df2.fillna(method='bfill', axis=1))
print(df2.isnull())
