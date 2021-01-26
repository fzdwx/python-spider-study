# - - - - - - - - - - - 
# @author like
# @since 2021-01-26 15:07
# @email 980650920@qq.com
#
# 純數字二點正則 \d 0-9之間的一個數
import re

pattern = re.compile("^\d")

one = '1234'

# match 方法 是否匹配成功，從頭開始 匹配一次
res = pattern.match(one)
print(res.group())
