import matplotlib.pyplot as plt

from random_walk import Random

# 创建一个random实例，然后表示花粉的运动轨迹
random = Random()
random.walk()

# 绘制随机漫步点
plt.plot(random.x_values,random.y_values,linewidth=2)
plt.show()
