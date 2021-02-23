# - - - - - - - - - - - 
# @author like
# @since 2021-02-23 11:08
# @email 980650920@qq.com
# 十点到十二点的气温变化

from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib import font_manager

import random

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

plt.figure(figsize=(20, 8), dpi=80)

plt.plot(x, y)

# 中文字体
chFont = font_manager.FontProperties(family="SimHei")  # SimHei
# chFont = font_manager.FontProperties(fname="C:/Windows/Fonts/SIMHEI.TTF")

# 刻度相关设置
step = 10
xLabels = ["10点,{}分".format(i) for i in range(60)]
xLabels += ["11点,{}分".format(i) for i in range(60)]
plt.xticks(list(x)[::step], xLabels[::step], rotation=25, fontProperties=chFont)

# 添加描述信息
plt.xlabel("时间", fontProperties=chFont)
plt.ylabel("温度 单位(℃)", fontProperties=chFont)
plt.title("10点到12点每分钟的气温变化", fontProperties=chFont)

plt.show()
