# 01-urllib.requst 提示错误 httpError UrlError

import urllib.request

url = "http://www.baidu.com"
response = urllib.request.urlopen(url)

date = response.read().decode('utf-8')
with open("baidu.html", "w", encoding='utf-8') as f:
    f.write(date)
