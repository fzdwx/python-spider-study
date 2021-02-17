# - - - - - - - - - - - 
# @author like
# @since 2021-02-17 13:47
# @email 980650920@qq.com
#
from selenium import webdriver
from lxml import etree
import pymysql, time


class GovSpider(object):
    def __init__(self):
        self.chrome = webdriver.Chrome()
        self.oneUrl = 'http://preview.www.mca.gov.cn/article/sj/xzqh/2020/'
        self.rawUrl = 'http://www.mca.gov.cn'
        # self.db = pymysql.connect()

    def getFalseUrl(self):
        self.chrome.get(self.oneUrl)

        tdList = self.chrome.find_elements_by_xpath('//td[@class="arlisttd"]/a[contains(@title,"代码")]')
        if tdList:
            twoUrlElement = tdList[0]
            # todo 增量爬取 取出链接和 数据库对比
            towUrl = twoUrlElement.get_attribute('href')
            # sql = "select * from version where link = '%s' "
            # res = self.cursor.excute(sql, [towUrl])
            # if res:
            #     print("数据已经是最新，无需爬取")
            # else
            # 点击
            twoUrlElement.click()
            time.sleep(3)
            # 切换browser
            allHandler = self.chrome.window_handles
            self.chrome.switch_to_window(allHandler[1])
            # 数据抓取
            self.getData()

    def getData(self):
        trList = self.chrome.find_elements_by_xpath('//tr[@height="19"]')
        for tr in trList:
            code = tr.find_element_by_xpath('./td[2]').text.strip()
            name = tr.find_element_by_xpath('./td[3]').text.strip()
            print(name, code)

    def main(self):
        self.getFalseUrl()


if __name__ == '__main__':
    gov = GovSpider()
    gov.main()
