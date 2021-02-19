# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from .settings import *


class MaoyanPipeline:
    def process_item(self, item, spider):
        # print(item['name'], item['star'], item['time'])
        return item


class MysqlPipeline(object):
    def __init__(self):
        pass

    def open_spider(self, spider):
        self.db = pymysql.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            db=MYSQL_DB)
        self.cursor = self.db.cursor()
        pass

    def process_item(self, item, spider):
        sql = 'insert into maoyan(`name`,`star`,`time`) values(%s,%s,%s)'
        data = [item['name'], item['star'], item['time']]
        self.cursor.execute(sql, data)
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()
