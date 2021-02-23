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

chFont = font_manager.FontProperties(fname="C:/Windows/Fonts/SIMHEI.TTF")

# 跳转x轴的刻度
step = 10
xLabels = ["10点,{}分".format(i) for i in range(60)]
xLabels += ["11点,{}分".format(i) for i in range(60)]
plt.xticks(list(x)[::step], xLabels[::step], rotation=25, fontProperties=chFont)

plt.show()
