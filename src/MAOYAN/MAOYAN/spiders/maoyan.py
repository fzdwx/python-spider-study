import scrapy

from src.MAOYAN.MAOYAN.items import MaoyanItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['www.maoyan.com']
    offset = 0
    start_urls = ['https://maoyan.com/board/4?offset=0']

    def parse(self, response):
        for offset in range(0, 91, 10):
            url = 'https://maoyan.com/board/4?offset={}'.format(offset)
            yield scrapy.Request(
                url=url,
                callback=self.parse_html,
                dont_filter=True  # 很关键
            )
        print("start")

    def parse_html(self, response):
        print("123")
        ddList = response.xpath('//dl[@class="board-wrapper"]/dd')
        item = MaoyanItem()
        for dd in ddList:
            item['name'] = dd.xpath('./a/@title').extract_first().strip()
            item['star'] = dd.xpath('.//p[@class="star"]/text()').extract_first().strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').extract_first().strip()

            print(item['name'], item['star'], item['time'])
            # 把爬取的数据交给pipeLine
            yield item
