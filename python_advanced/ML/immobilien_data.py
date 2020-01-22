import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv('data/Immobilien.txt', delimiter='\t')

# erstellen der Color spalte
color = {'Buero':'b', 'Wohnung':'r', 'Haus':'y'}

fig = plt.figure()
graph3d = fig.add_subplot(111, projection = '3d')

# graph3d.scatter(df['Quadratmeter'], df['Wandhoehe'], df['IA_Ratio'], color=df['Color'], s=3)

graph3d.set_xlabel('Quadratmeter')
graph3d.set_ylabel('Wandhoehe')
graph3d.set_zlabel('IA_Ratio')
graph3d.set_xlim(left=0)
graph3d.set_ylim(bottom=0)
graph3d.set_zlim(bottom=0)
#plt.show()

#print(df.head())

# normalizing a single vector
quad_min = df['Quadratmeter'].min()
print(quad_min)
quad_max = df['Quadratmeter'].max()
print(quad_max)
quad_range = quad_max - quad_min
print(quad_range)

df_n = df.copy()
df_n['Quadratmeter'] = (df['Quadratmeter'] - quad_min)/quad_range
# print(df_n['Quadratmeter'])
cols = ['Wandhoehe', 'IA_Ratio']
for col in cols:
    col_min = df[col].min()
    col_max = df[col].max()
    col_range = col_max - col_min
    df_n[col] = (df[col] - col_min)/col_range

print(df.head())
print(df_n.head())