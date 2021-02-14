# - - - - - - - - - - - 
# @author like
# @since 2021-02-14 9:34
# @email 980650920@qq.com
# 多线程爬取
import json, time, requests
from queue import Queue
from threading import Thread
from src.randomAgent import *


class Xiaomi:
    def __init__(self):
        self.url = 'https://app.mi.com/categotyAllListApi?page={}&categoryId=2&pageSize=30'
        self.headers = getHeaders()
        self.queue = Queue()
        self.n = 0

    def urlEnQueue(self):
        for i in range(10):
            trueUrl = self.url.format(i)
            self.queue.put(trueUrl)

    def getData(self):
        while True:
            if self.queue.empty():
                break
            url = self.queue.get()
            html = requests.get(url=url, headers=self.headers).content.decode('utf-8', 'ignore')
            html = json.loads(html)
            for app in html['data']:
                appName = app['displayName']
                appLink = 'http://app.mi.com/details?id=' + app['packageName']
                print(appName + ":" + appLink)
                self.n = self.n + 1

    def start(self):
        self.urlEnQueue()

        tList = []
        for i in range(20):  # 启动n个线程
            t = Thread(target=self.getData())
            tList.append(t)
            t.start()

        for t in tList:
            t.join()

        print(self.n)


if __name__ == '__main__':
    start = time.time()

    c = Xiaomi()
    c.start()

    end = time.time()
