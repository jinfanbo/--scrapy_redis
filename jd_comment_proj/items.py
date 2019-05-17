# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CommentItem(scrapy.Item):
    # define the fields for your item here like:
    """字段包含评论人名称，评论内容，产品颜色，产品型号，产品名称，选择内存 """
    jd_comment_id = scrapy.Field() #id
    nickname = scrapy.Field() #评论人
    content = scrapy.Field()
    color = scrapy.Field()
    sku_id = scrapy.Field() #产品 id
    warename = scrapy.Field() #名称
    model = scrapy.Field() #型号

    ram = scrapy.Field() #内存
