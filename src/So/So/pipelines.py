# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 导入scrapy的图片管道类
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from PIL import Image


class SoPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        yield scrapy.Request(
            url=item['img_link']
        )

    # def process_item(self, item, spider):
    #     print(item['img_link'])
    #     print("开始下载")
    #     return item
