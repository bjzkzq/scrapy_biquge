# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QidianspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # 书的链接
    book_url = scrapy.Field()
    # 书名
    book_name = scrapy.Field()
    # 作者名
    book_author = scrapy.Field()
    # 简介
    book_abstract = scrapy.Field()
    # 每一张的名字
    book_zhangjie_name = scrapy.Field()
    # 每一张的链接
    book_each_url = scrapy.Field()
    # 每一张的内容
    book_neirong = scrapy.Field()