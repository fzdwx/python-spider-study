import scrapy


class ZufangSpider(scrapy.Spider):
    name = 'zufang'
    allowed_domains = ['wh.lianjia.com']
    start_urls = ['http://wh.lianjia.com/']

    def parse(self, response):
        pass
