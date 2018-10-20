# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.utils.project import get_project_settings
import os
import scrapy
from scrapy.pipelines.images import ImagesPipeline

'''下载图片'''


class ImagePipeline(ImagesPipeline):
    #获取settings.py里设置的变量值
    IMAGE_STORE = get_project_settings().get('IMAGE_STORE')

#获取图片的链接，发送Request请求，并将结果返回给it_completed 方法
    def get_media_requests(self, item, info):
        image_url = item['image_lick']
        yield scrapy.Request(image_url)

#接收响应返回的数据，重写文件保存路径及图片名称
    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        os.rename(self.IMAGE_STORE + '\\'+image_path[0],
                  self.IMAGE_STORE + '\\'+item['nickname'] + 'jpg')
        item['image_path'] = self.IMAGE_SCTRE + '\\'+item['nickname']
        yield item