# - - - - - - - - - - - 
# @author like
# @since 2021-02-26 8:28
# @email 980650920@qq.com
#
import pandas as pd
from matplotlib import pyplot as plt

lj = pd.read_csv("链家数据.csv", encoding="gbk")

df = pd.DataFrame(lj).drop_duplicates()

# 根据单个分组
grb_1 = df.groupby(by='区域')

for i, j in grb_1:  # i标题,j 是一个dataFrame
    print(i)
    print('*' * 100)
    print(j, type(j))
    print('=' * 100)

# 按照多个条件进行分组
grb_2 = df['区域'].groupby(by=[df['小区名字'], df['户型']])
for i, j in grb_2:
    print(i)
    print('*' * 100)
    print(j, type(j))
    print('=' * 100)