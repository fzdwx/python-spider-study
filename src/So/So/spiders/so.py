import json

import scrapy
from ..items import *


class SoSpider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['image.so.com']

    # start_urls = ['http://image.so.com/']

    def parse(self, response):
        item = SoItem()
        html = json.loads(response.text)
        for info in html['list']:
            item['img_link'] = info['qhimg_url']
            yield item

    def start_requests(self):
        url = 'https://image.so.com/zjl?ch=beauty&sn={}'
        for i in range(5):
            sn = i * 30
            queryUrl = url.format(sn)
            yield scrapy.Request(
                url=queryUrl,
                callback=self.parse
            )
