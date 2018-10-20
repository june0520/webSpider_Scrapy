# -*- coding: utf-8 -*-
import scrapy
from firstspider.items import FirstspiderItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://itcast.cn/channel/teacher.shtml#']

    def parse(self, response):

        results = response.xpath("//div[@class='li_txt']")
        for result in results:
            item = FirstspiderItem()
            name = result.xpath('./h3/text()').extract()
            title = result.xpath('./h4/text()').extract()
            info = result.xpath('./p/text()').extract()

            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            yield item

