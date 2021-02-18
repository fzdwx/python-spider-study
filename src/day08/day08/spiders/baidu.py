import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫名字
    name = 'baidu'
    # 爬取的域名
    allowed_domains = ['www.baidu.com']
    # 起始的url地址
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        with open('baidu.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
        print('ok')
