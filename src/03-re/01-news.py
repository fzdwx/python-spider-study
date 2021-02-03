# - - - - - - - - - - - 
# @author like
# @since 2021-01-30 15:24
# @email 980650920@qq.com
#
import re
import requests

url = "http://news.baidu.com"
header = {
    # 浏览器的版本
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/87.0.4280.66 Safari/537.36 ",
}
get = requests.get(url, headers=header).content.decode("utf-8")

"""
    正则解析数据
        <a href="http://wenku.baidu.com/" data-path="search?ie=utf-8&word=">文库</a>
        每个新闻的url title
        <a href="(.*)">(.*)</a>
"""

p = re.compile('<a href="(.*?)" title="(.*?)">(.*?)</a>')
titleAndUrlList = p.findall(get)
print(titleAndUrlList)

with open("01-news.html", "w", encoding="utf-8") as f:
    f.write(get)
