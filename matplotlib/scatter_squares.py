# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt

# plt.scatter(2, 4, s=200)
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 8, 16, 25]
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values,cmap=plt.cm.Blues, edgecolor='none', s=40)

# 设置图表标题并给坐标轴加上标签
plt.title("square number", fontsize=24)
plt.xlabel("value", fontsize=14)
plt.ylabel("square of value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 1100, 0, 1100000])

plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()