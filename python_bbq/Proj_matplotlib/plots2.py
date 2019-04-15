import matplotlib.pyplot as plt

########## Page 2 ############

plt.title("Two or more lines on same plot with suitable legends")
plt.plot([10, 20, 30], [20, 40, 10], label="line1-width-3", linewidth=3) # x axis against y axis
plt.plot([10, 20, 30], [40, 10, 30], label="line2-width-5", linewidth=5)
plt.xlabel("x-axis")
plt.ylabel('y-axis')
plt.legend()
plt.show()
