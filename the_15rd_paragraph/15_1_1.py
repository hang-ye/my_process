import matplotlib.pyplot as plt

x_value = list(range(1, 5001))
y_value = [x**3 for x in x_value]

plt.scatter(x_value, y_value,c=y_value, cmap=plt.cm.Blues, edgecolors='none', s=40)

# 设置图表标题并给坐标轴加上标签
plt.title("square number", fontsize=24)
plt.xlabel("value", fontsize=14)
plt.ylabel("square of value", fontsize=14)

# 设置每个坐标轴的取值范围
max = 5100**3
plt.axis([0,6000,0,max])

plt.show()