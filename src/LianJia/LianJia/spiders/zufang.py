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

    mainUrl = 'https://wh.lianjia.com/zufang'

    def start_requests(self):
        yield scrapy.Request(
            url=self.mainUrl,
            callback=self.parse
        )

    def parse(self, response):
        item = LianjiaItem()
        areaInfoList = response.xpath('//ul/li[@data-type="district"]')
        for areaInfo in areaInfoList:
            item['areaUrl'] = areaInfo.xpath('./a/@href').extract()[0]
            item['areaName'] = areaInfo.xpath('./a/text()').extract()[0]

            yield item
