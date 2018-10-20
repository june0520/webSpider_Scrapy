# -*- coding: utf-8 -*-
import scrapy
import json
from douyu.items import DouyuItem

"""爬取斗鱼APP的spider"""
class DouyupicSpider(scrapy.Spider):
    name = 'douyupic'
    allowed_domains = ['douyu.com']
    url = 'https://capi.douyucdn.cn/api/vi'
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        '''app上的数据格式是json格式，需要转换为Python格式'''
        text = json.loads(response.text)
        for each in text.get('data'):
            item = DouyuItem()
            item['nick_name'] = each['nickname']
            item['image'] = each['vertical_scr']
            yield item
        if self.offset < 500:
            self.offset += 20

        url = self.url + str(self.offset)
        yield scrapy.Request(url, callback=self.parse)




