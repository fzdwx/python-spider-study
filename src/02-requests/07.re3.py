# - - - - - - - - - - - 
# @author like
# @since 2021-01-26 15:07
# @email 980650920@qq.com
#
# 純數字二點正則 \d 0-9之間的一個數
import re
one = '123abc'
pattern = re.compile('\d+')
# match 從頭匹配 匹配一次
res = pattern.match(one)
# search 從任意位 匹配一次
res = pattern.search(one)
# findall 查找符合正則的内容
res = pattern.findall(one)
# sub 替換字符串
res = pattern.sub('hello',one)
# split 拆分
res = pattern.split()

print(res)