# - - - - - - - - - - -
# @author like
# @since 2021-02-24 10:53
# @email 980650920@qq.com
#
from matplotlib import pyplot as plt
from matplotlib import font_manager

y_3 = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22,
       22, 23]
y_10 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13,
        12, 13, 6]

chFont = font_manager.FontProperties(family="SimHei")

x_3 = range(1, 32)
x_10 = range(51, 82)

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)

# 绘制直方图
plt.bar(x_3, y_3,label="三月份")
plt.bar(x_10, y_10,label="十月份")

# 调整x轴的刻度
_x = list(x_3) + list(x_10)
_xtick_labels = ["3月{}日".format(i) for i in x_3]
_xtick_labels += ["10月{}日".format(i - 50) for i in x_10]
plt.xticks(_x[::3], _xtick_labels[::3], fontproperties=chFont, rotation=45)

# 描述信息
plt.xlabel("时间",fontproperties=chFont)
plt.ylabel("温度",fontproperties=chFont)
plt.title("标题",fontproperties=chFont)

plt.legend(prop=chFont)

plt.show()
