# - - - - - - - - - - - 
# @author like
# @since 2021-02-04 9:23
# @email 980650920@qq.com
#
import csv

with open("text.csv", "w", encoding="utf-8", newline='') as f:
    w = csv.writer(f)
    # 写一行
    w.writerow(["like", 18])
    # 写多行
    w.writerow([(), (), (), ()])
