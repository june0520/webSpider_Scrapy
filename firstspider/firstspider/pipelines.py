# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


class FirstspiderPipeline(object):
    # 可选值，作为类的初始化方法
    def __init__(self):
        self.filename = open('teacher.json', 'wb')

    #以json格式写入文件
    def process_item(self, item, spider):
        text = dict(item)
        item = json.dumps(text, ensure_ascii=False)
        self.filename.write(item.encode('utf8'))
        return item

    #关闭文件
    def close_spider(self, spider):
        self.filename.close()