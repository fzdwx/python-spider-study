# - - - - - - - - - - - 
# @author like
# @since 2021-02-09 11:34
# @email 980650920@qq.com
#
from src.randomAgent import *
import requests
import re
import random

url = "http://x.fanqieip.com/index.php?s=/Api/IpManager/adminFetchFreeIpRegionInfoList&uid=13336&ukey=dcccb7a212919332c232820403ede34a&limit=10&format=0 &page={}"
h = getHeaders()


#  生成一个随机数:i（0，500）
#  爬取从i开始的后面10页
def getRawProxyList():
    proxyList = []
    p = re.compile('(((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}:\d{4})')
    i = random.randint(0, 500)

    for page in range(i, i + 3):
        reqUrl = url.format(page)
        html = requests.get(url=reqUrl, headers=h).text

        ipList = p.findall(html)
        for ip in ipList:
            proxyList.append({
                "http": "http://{}".format(ip[0]),
                "https": "https://{}".format(ip[0])
            })

    print(proxyList)
    print(len(proxyList))
    return proxyList


getRawProxyList()
