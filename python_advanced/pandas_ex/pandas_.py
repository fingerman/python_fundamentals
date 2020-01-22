import pandas as pd
import numpy as np

ind = pd.Index(list('abc'))

# build dataframe
data = pd.DataFrame(np.random.rand(3, 2), columns=['col1', 'col2'],
                    index=['a', 'b', 'c'])

# series from iterable
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict2 = {
    "brand": "Ford",
    "model": "Mustang",
    "PS": 30
}

s6 = pd.Series(thisdict)
s7 = pd.Series(thisdict2)
# print(s6 + s7)


# data frame from series data frame
df = pd.DataFrame({'col1': s6, 'col2': s7})
# data frame from series array
str_arr = np.zeros(3, dtype=[('col1', 'i'), ('col2', 'f')])
df3 = pd.DataFrame(str_arr)

area = pd.Series({'California': 423534,
                  'Texas': 54254,
                  'Florida': 543543,
                  'New York': 63543,
                  'Illinois': 54364}, name='area')

population = pd.Series({'California': 6763554,
                        'Texas': 654345,
                        'Florida': 123432,
                        'New York': 123243,
                        'Illinois': 13432}, name='polulation')

df_comb = pd.DataFrame({'area': area, 'population': population})
# print(df_comb)

df_comb2 = pd.DataFrame([area, population])
# transpose the DF
df_comb_transposed = pd.DataFrame([area, population]).T
# print(df_comb2)


# add column density = population/area
df_comb['density'] = df_comb['population'] / df_comb['area']
print(df_comb)
print(type(df_comb))

print('--- each second row ---')
print(df_comb.iloc[::2, :2])
print()

print('certain values')
print(df_comb.loc['California', :'area'])

# take the index which has upper I
print(df_comb[df_comb.index.str.contains('I')])
print('-------------')
print(df_comb.loc[(df_comb['area'] > 553243) | (df_comb['population'] > 1980934), ['area', 'population']])


