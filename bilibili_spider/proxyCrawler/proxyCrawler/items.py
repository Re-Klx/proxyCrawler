# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProxycrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ip_name = scrapy.Field()
    # ip地址
    port_name = scrapy.Field()
    # 端口号
    type_name = scrapy.Field()
    # 类型 http / https
