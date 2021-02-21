import scrapy
from ..items import LianjiaItem

"""
@author Like 
@since 2021/02/21
"""


class ZufangSpider(scrapy.Spider):
    name = 'zufang'
    allowed_domains = ['wh.lianjia.com']

    # start_urls = ['http://wh.lianjia.com/']

    # 主路径
    mainUrl = 'https://wh.lianjia.com{}'
    # 保存各个地区的名称
    areaNameList = []
    # 保存各个地区名字以及对应的跳转url
    areaInfoMap = {}
    # 各个区域房源总数量
    areaMapHouseCount = {}

    def start_requests(self):
        yield scrapy.Request(
            url=self.mainUrl.format('/' + self.name),
            callback=self.parse
        )

    def parse(self, response):
        #
        areaInfoListXpath = response.xpath('//ul/li[@data-type="district"]')
        for areaInfo in areaInfoListXpath:
            areaName = areaInfo.xpath('./a/text()').extract()[0]
            areaUrl = self.mainUrl.format(areaInfo.xpath('./a/@href').extract()[0])

            self.areaInfoMap[areaUrl] = areaName
            self.areaNameList.append(areaName)

            yield scrapy.Request(
                url=areaUrl,
                callback=self.parseAreaHouseCount
            )

    def parseAreaHouseCount(self, response):
        # //span[@class="content__title--hl"]/text()
        count = response.xpath('//span[@class="content__title--hl"]/text()').extract()[0]
        print(response.url, count)
