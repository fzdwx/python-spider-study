# - - - - - - - - - - - 
# @author like
# @since 2021-02-26 9:11
# @email 980650920@qq.com
#
import pandas as pd
from matplotlib import pyplot as plt

lj = pd.read_csv("链家数据.csv", encoding="gbk")

df = pd.DataFrame(lj).drop_duplicates()

data1 = df.groupby(by="区域")
for i,j in data1:
    print(j.sort_values(by="租金")[:10])
