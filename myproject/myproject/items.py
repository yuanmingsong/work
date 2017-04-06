# -*- coding: utf-8 -*-

import scrapy


class MyprojectItem(scrapy.Item):
    mytitle = scrapy.Field()
    mydata = scrapy.Field()
    myurl = scrapy.Field()
    pass