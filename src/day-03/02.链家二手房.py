# - - - - - - - - - - - 
# @author like
# @since 2021-02-07 9:17
# @email 980650920@qq.com
#
from src.randomAgent import *
import requests
from lxml import etree
import time
import random


class LianJiaSpider(object):
    def __init__(self):
        self.url = "https://bj.lianjia.com/ershoufang/pg{}/"
        self.headers = getHeaders()

    def getPage(self, url):
        res = requests.get(url=url, headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        return html

    def parsePage(self, html):
        houseMap = {}
        p = etree.HTML(html)
        liList = p.xpath('//ul[@class="sellListContent"]/li[@data-lj_action_source_type="链家_PC_二手列表页卡片"]')
        for i in liList:
            # 名称
            houseMap['houseName'] = i.xpath('.//a[@data-el="region"]/text()')[0].strip()
            # 总价
            houseMap['totalPrice'] = i.xpath('.//div[@class="totalPrice"]/span/text()')[0].strip()
            # 单价
            houseMap['unitPrice'] = i.xpath('.//div[@class="unitPrice"]/@data-price')[0].strip()
            print(houseMap)

    def start(self):
        for pg in range(1, 11):
            u = self.url.format(pg)
            print(u)
            # 1.获取页面
            html = self.getPage(u)
            # 2.解析页面
            self.parsePage(html)
            time.sleep(random.uniform(0, 1))


if __name__ == '__main__':
    s = LianJiaSpider()
    s.start()
