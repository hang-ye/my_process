import matplotlib.pyplot as plt

from random_walk import Random

# 创建一个random实例，然后表示花粉的运动轨迹
random = Random()
random.walk()

# 生成数字列表
point_number = list(range(random.num_point))
# 绘制随机漫步点
plt.scatter(random.x_values,random.y_values,c=point_number,cmap=plt.cm.Blues,
         edgecolor='none',s=1)
plt.show()