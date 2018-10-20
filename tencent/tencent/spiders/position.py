# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem


class PositionSpider(scrapy.Spider):
    name = 'position'
    allowed_domains = ['tencent.com']

    offset = 0
    url = 'https://hr.tencent.com/position.php?&start='
    start_urls = [url + str(offset)]

    def parse(self, response):
        #实例化模型
        item = TencentItem()
        for result in response.xpath("//tr[@class='even']| //tr[@class='odd']"):
            item['title'] = result.xpath("./td[1]/a/text()").extract_first()
            item['link'] = result.xpath("./td[1]/a/@href").extract_first()
            item['type'] = result.xpath("./td[2]/text()").extract_first()
            item['num'] = result.xpath("./td[3]/text()").extract_first()
            item['location'] = result.xpath("./td[4]/text()").extract_first()
            item['publish'] = result.xpath("./td[5]/text()").extract_first()
            yield item

        if self.offset < 3010:
            self.offset += 10
        url = self.url + str(self.offset)
        yield scrapy.Request(url, callback=self.parse)






