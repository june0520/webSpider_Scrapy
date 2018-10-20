# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    #职位名称
    title = scrapy.Field()
    #详情链接
    link = scrapy.Field()
    #职位类别
    type = scrapy.Field()
    #招聘人数
    num = scrapy.Field()
    #工作地址
    location = scrapy.Field()
    #发布时间
    publish = scrapy.Field()
