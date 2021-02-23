# - - - - - - - - - - - 
# @author like
# @since 2021-02-23 15:33
# @email 980650920@qq.com
#
from matplotlib import pyplot as  plt
from matplotlib import font_manager

y_1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y_2 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]

x = range(11, 31)

chFont = font_manager.FontProperties(family="SimHei")

plt.plot(x, y_1, label="我", color="pink",linestyle="--")
plt.plot(x, y_2, label="同桌", color="cyan")

xticks = ["{}岁".format(i) for i in x]
plt.xticks(x, xticks, fontProperties=chFont, rotation=30)

# 网格
plt.grid()

# 添加图例
plt.legend(prop=chFont)

plt.show()
