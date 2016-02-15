# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XueersiXiaoChuScore2009Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    xiao = scrapy.Field()
    chu = scrapy.Field()
    teacher = scrapy.Field()
    clazz = scrapy.Field()
    
