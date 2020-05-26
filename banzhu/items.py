# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BanzhuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ArticleCatalogItem(scrapy.Item):
    #文章名
    articleName = scrapy.Field()

    #链接
    link = scrapy.Field()
    pass

class TitleItem(scrapy.Item):
    #文章名
    articleName = scrapy.Field()

    #标题
    title = scrapy.Field()

    #链接
    link = scrapy.Field()

    pass


class ContentItem(scrapy.Item):
    #文章名
    articleName = scrapy.Field()

    #内容
    content = scrapy.Field()

    #章节名称
    title = scrapy.Field()

    pass
