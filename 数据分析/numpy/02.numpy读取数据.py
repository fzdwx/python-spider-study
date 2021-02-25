# - - - - - - - - - - - 
# @author like
# @since 2021-02-25 10:25
# @email 980650920@qq.com
#
import numpy as np

filePath1 = "链家数据.csv"
filePath2 = "01.csv"

print(np.nan)
t1 = np.loadtxt(filePath2, delimiter=",", dtype=int)

print(t1)

print("切片")

print(t1[:, 2:4])
