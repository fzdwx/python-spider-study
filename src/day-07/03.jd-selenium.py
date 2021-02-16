# - - - - - - - - - - - 
# @author like
# @since 2021-02-15 13:40
# @email 980650920@qq.com
#
from selenium import webdriver
import time
import scrapy

class JdSpider(object):
    def __init__(self):
        self.chrome = webdriver.Chrome()
        self.indexUrl = "http://www.jd.com"

    # 获取商品页面
    def getPage(self, keywords):
        # 打开京东首页
        self.chrome.get(self.indexUrl)
        # 找到搜索框
        self.chrome.find_element_by_xpath('//*[@id="key"]').send_keys(keywords)
        self.chrome.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()

        # 页面加载时间
        time.sleep(2)

    # 解析页面
    def parsePage(self):
        pass
        # 把滑轮拉到页面底
        self.chrome.execute_script(
            'window.scrollTo(0,document.body.scrollHeight)'
        )

        # 匹配 所有商品节点对象
        liList = self.chrome.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
        for li in liList:
            print(li.text)
            print('*' * 50)

    def start(self):
        keywords = input("请输入你要搜索的关键字:")
        self.getPage(keywords)
        while True:
            self.parsePage()
            if self.chrome.page_source.find('pn-next disable') == -1:
                self.chrome.find_element_by_class_name('pn-next').click()
                time.sleep(1)
            else:
                break

        self.chrome.quit()


if __name__ == '__main__':
    jd = JdSpider()
    jd.start()
