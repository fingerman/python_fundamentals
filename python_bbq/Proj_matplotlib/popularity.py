
import numpy as np
import matplotlib.pyplot as plt


objects = ('Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++')
y_pos = np.arange(len(objects))
performance = [22, 18.5, 9, 8, 7.5, 6.5]
colors = ["blue", "firebrick", "seagreen", "red", "slategrey", "lime"]


plt.bar(y_pos, performance, align='center', color=colors, zorder=100)
plt.xticks(y_pos, objects)
plt.ylabel('Popularity in %')
plt.xlabel('Languages')
plt.title('Programming language usage')
plt.minorticks_on()
plt.grid(which="major", linestyle='-', linewidth='1', color="black")
plt.grid(which="minor", linestyle=':', linewidth='0.5', color="blue")

plt.show()