# - - - - - - - - - - - 
# @author like
# @since 2021-02-05 10:42
# @email 980650920@qq.com
#
import random
import re
from urllib import request
from randomAgent import *
import time


class FilmSkyData(object):
    p1 = re.compile('<table width="100%".*?<td height="26">.*?<a href="(.*?)".*?>(.*?)</a>', re.S)
    p2 = re.compile('<a href="(.*?)" target="_blank"><strong>')

    def __init__(self):
        self.url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'

    # 获取页面数据
    def getPage(self, url):
        req = request.Request(
            url=url,
            headers=getHeaders()
        )
        res = request.urlopen(req)
        html = res.read().decode('gbk', 'ignore')
        return html

    # 解析提取数据
    def parsePage(self, html):

        fileList = self.p1.findall(html)
        for f in fileList:
            fileName = f[1]
            fileLink = f[0]

            # 打开二级页面
            h2Url = 'https://www.dytt8.net' + fileLink
            h2 = self.getPage(h2Url)
            downloadLink = self.p2.findall(h2)
            print({
                'name': fileName,
                '磁力链接地址': downloadLink
            })

    def start(self):
        for no in range(1, 11):
            h1Url = self.url.format(no)
            h1 = self.getPage(h1Url)
            self.parsePage(h1)


# f = FilmSkyData()
# f.start()
if __name__ == '__main__':
    s = FilmSkyData()
    s.start()
