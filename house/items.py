# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    area = scrapy.Field()
    location = scrapy.Field()
    totalPrice = scrapy.Field()
    unitPrice = scrapy.Field()
    flood = scrapy.Field()
    follow = scrapy.Field()
    tag1 = scrapy.Field()
    tag2 = scrapy.Field()
    pass
