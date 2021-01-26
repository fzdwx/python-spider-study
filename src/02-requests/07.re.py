# - - - - - - - - - - - 
# @author like
# @since 2021-01-26 14:54
# @email 980650920@qq.com
#
#  正則表達式

import re

one = 'mdasdasgasd123456135n'

pattern = re.compile('m(.*?)n')  # 匹配以m開頭n結尾的多個字符

print(pattern.findall(one))
