# - - - - - - - - - - - 
# @author like
# @since 2021-02-03 9:35
# @email 980650920@qq.com
#
from urllib import request, parse
import time
import random


class BaiduSpider(object):
    def __init__(self):
        self.url = 'https://tieba.baidu.com/f?kw={}&pn={}'
        self.headers = {'user-agent': 'mozilla/5.0'}

    # 获取页面
    def getPage(self, url, headers):
        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req)
        html = res.read().decode("utf-8")
        return html

    # 提取数据
    def parseData(self):
        pass

    # 保存数据
    def saveData(self, html, fileName):
        with open(fileName, 'w', encoding='utf-8') as f:
            f.write(html)

    # 主函数
    def start(self):
        tieBaName = input("请输入贴吧名字：")
        startPage = int(input("请输入起始页："))
        endPage = int(input("请输入终止页："))

        for page in range(startPage, endPage + 1):
            pn = (page - 1) * 50
            kw = parse.quote(tieBaName)
            url = self.url.format(kw, pn)
            html = self.getPage(url, self.headers)
            fileName = "{}-第{}页.html".format(tieBaName, page)
            self.saveData(html, fileName)

            print("第{}页爬取成功".format(page))

            time.sleep(random.randint(0, 3))  # 随机休眠


if __name__ == '__main__':
    spider = BaiduSpider()
    spider.start()
