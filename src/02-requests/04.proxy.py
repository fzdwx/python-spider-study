"""
@author like
@since 2021-01-04 20:27
@email 980650920@qq.com
"""

import requests

url = "https://www.baidu.com"
# 自定义请求头
header = {
    # 浏览器的版本
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/87.0.4280.66 Safari/537.36 ",
}
freeProxy = {
    'http': '115.53.37.35:9999'
}

getReq =  requests.get(url, headers=header, proxies=freeProxy)
print(getReq.status_code)