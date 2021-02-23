# - - - - - - - - - - - 
# @author like
# @since 2021-02-23 11:43
# @email 980650920@qq.com
# x years
# y size
from matplotlib import pyplot as  plt
from matplotlib import font_manager

y = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
x = range(11, 31)

chFont = font_manager.FontProperties(family="SimHei")
plt.plot(x, y)
xticks = ["{}岁".format(i) for i in x]
plt.xticks(x, xticks, fontProperties=chFont, rotation=30)

# 网格
plt.grid()

plt.show()
