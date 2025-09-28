import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, num=20)
y = np.sin(x)
lst = []
for s in y:
    # 清除数据, 放在这个位置是为了循环的清除上一次的数据
    plt.clf()
    lst.append(s)
    plt.plot(lst, marker='^', color='red')
    # 暂停0.1秒
    plt.pause(0.1)
# 保存图像到指定的路径
plt.savefig('./picture/end.jpg')