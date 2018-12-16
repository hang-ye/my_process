import matplotlib.pyplot as plt

x_number = [1, 2, 3, 4, 5]
squares = [1, 2**3, 3**3, 4**3, 5**3]
plt.plot(x_number,squares, linewidth=5)

# 设置图表标题并给坐标轴加上标签
plt.title("square number", fontsize=24)
plt.xlabel("value", fontsize=14)
plt.ylabel("square of value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both',labelsize=14)

# 显示
plt.show()

