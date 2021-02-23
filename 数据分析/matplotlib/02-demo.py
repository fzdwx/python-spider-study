# - - - - - - - - - - - 
# @author like
# @since 2021-02-23 9:51
# @email 980650920@qq.com
# x:一天的24个小时，间隔为2个小时
# y:每个小时的温度
from matplotlib import pyplot as plt

x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)

# 绘图
plt.plot(x, y)

# 设置x轴的刻度
x_labels = [i / 2 for i in range(4, 49)]
plt.xticks(x_labels[::3])
plt.yticks(range(min(y), max(y) + 1))

# 保存图片
# plt.savefig("02-demo.svg")

# 展示图形
plt.show()
