"""
@author like
@since 2021-01-01 20:47
@email 980650920@qq.com
"""
import requests

# 发送请求
url = "http://47.112.150.204/"
resp = requests.get(url)
print(resp.content.decode('utf-8'))
