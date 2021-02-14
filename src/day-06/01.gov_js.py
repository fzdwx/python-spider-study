# - - - - - - - - - - - 
# @author like
# @since 2021-02-13 9:32
# @email 980650920@qq.com
# 政府网站通过js跳转页面 反爬
from asyncio import Lock

import requests
import pymysql
import re
from lxml import etree
from src.randomAgent import *


class Gov(object):
    def __init__(self):
        self.oneUrl = 'http://preview.www.mca.gov.cn/article/sj/xzqh/2020/'
        self.rawUrl = 'http://www.mca.gov.cn'
        self.headers = getHeaders()
        self.db = pymysql.connect(
            host='47.115.115.226', user='root', password='root', database='mall2', charset='utf8'
        )
        self.c = self.db.cursor()

    def getFalseLink(self):
        html = requests.get(url=self.oneUrl, headers=self.headers).content.decode('utf-8', 'ignore')
        p = etree.HTML(html)
        aList = p.xpath('//a[@class="artitlelist"]')
        for a in aList:
            title = a.get('title')
            if re.findall('.县以上', title, re.S):
                href = a.get('href')
                twoUrl = self.rawUrl + href

                self.getTrueLink(twoUrl)

    def getTrueLink(self, url):
        html = requests.get(url=url, headers=self.headers).content.decode('utf-8', 'ignore')
        p = re.compile(r'window.location.href="(.*?)"', re.S)
        url = p.findall(html)[0]

        print(url)

    def getData(self):
        pass

    def start(self):
        pass


if __name__ == '__main__':
    gov = Gov()
