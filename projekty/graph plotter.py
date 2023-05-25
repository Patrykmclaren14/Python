import matplotlib.pyplot as plt


x = [0, 1000, -1000, 0, 0]
y = [0, 0, 0, 1000, -1000]

plt.plot(x, y, color='Green', linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor='blue', markersize=12)
plt.ylim(1, 8)
plt.xlim(1, 8)
plt.xlabel('X Axis')

plt.ylabel('Y Axis')

plt.title('Demo Graph - Custimization')

plt.legend()

plt.show()
