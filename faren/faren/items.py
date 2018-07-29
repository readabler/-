# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FarenItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 法人姓名
    name = scrapy.Field()

    # 法人所在公司
    company = scrapy.Field()

    # 法人联系方式
    telephone = scrapy.Field()
    pass
