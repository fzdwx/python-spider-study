# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SoItem(scrapy.Item):
    # define the fields for your item here like:
    # 图片连接
    img_link = scrapy.Field()
    pass
