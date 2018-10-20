# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrapy.com']
    start_urls = ['http://quotes.toscrapy.com/']

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            item = TutorialItem()
            item['text'] = quote.xpath("./span[@class='text']/text()").extract_first()
            item['author'] = quote.xpath("./span[@class='author']/text()").extract_first()
            item['tags'] = quote.xpaht("./div[@class='tags']/a/@href").extract()
            yield item
        next = response.xpath("//nav//li[@class='next']/a/href").extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url, self.parse)





