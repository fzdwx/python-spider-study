# - - - - - - - - - - - 
# @author like
# @since 2021-02-25 11:38
# @email 980650920@qq.com
#

import pandas as pd
from matplotlib import pyplot as plt

lj = pd.read_csv("链家数据.csv", encoding="gbk")

t = pd.DataFrame(lj).drop_duplicates()
print(t.sort_values(by="租金").head(20))
# 获取当前读取数据的信息
print(t.info())

# 获取平均租金
print(t["租金"].mean())
# 获取户型的类型的个数
print(t["户型"].unique())
# 获取区域类型
print(t["区域"].unique())
print(i for i in t.loc)
#
# t_qy = t['区域'].values
# t_title = t['标题'].values
# t_zj = t['租金'].values
#
# zj_max = t_zj.max()
# zj_min = t_zj.min()
#
# numBin = (zj_max - zj_min) // 10
# plt.figure(figsize=(20, 8), dpi=80)
#
# plt.hist(t_zj, numBin)
#
# plt.show()
