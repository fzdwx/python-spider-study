import scrapy

from src.MAOYAN.MAOYAN.items import MaoyanItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['www.maoyan.com']
    offset = 0
    start_urls = ['https://maoyan.com/board/4']

    def parse(self, response):
        ddList = response.xpath('//dl[@class="board-wrapper"]/dd')
        item = MaoyanItem()
        for dd in ddList:
            item['name'] = dd.xpath('./a/@title').extract_first().strip()
            item['star'] = dd.xpath('.//p[@class="star"]/text()').extract_first().strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').extract_first().strip()
            # 把爬取的数据交给pipeLine
            yield item

        # 拼接url 交给调度器入队列
        self.offset += 10
        if self.offset <= 90:
            url = 'https://maoyan.com/board/4?offset={}'.format(self.offset)
            print(url)
            yield scrapy.Request(
                url=url,
                callback=self.parse
            )
