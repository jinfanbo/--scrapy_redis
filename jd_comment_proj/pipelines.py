# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import redis
from scrapy.conf import settings
from scrapy.exceptions import DropItem
# Define your item pipelines here
from scrapy_redis.pipelines import RedisPipeline
from .db import init_mongodb


class MongoDBPipeline(object):
    def __init__(self):
        self.db = init_mongodb()

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            try:
                # 防止重复插入
                # self.db['comments'].insert(dict(item))
                item = dict(item)
                self.db['comments'].update_one(item, {'$set': item}, upsert=True)
            except (pymongo.errors.WriteError, KeyError) as err:
                raise DropItem(
                    "Duplicated comment Item: {}".format(item['good_name']))
        return item


# class RedisPipeline(object):
#     def __init__(self):
#         self.redis_table = settings.MY_REDIS  # 选择表
#         self.redis_db = redis.Redis(host=settings.REDIS_SERVER, port=settings.REDIS_PORT)  # redis数据库连接信息
#
#     def process_item(self, item, spider):
#         if self.redis_db.exists(item['url']):
#             raise DropItem('%s id exists!!' % (item['url']))
#         else:
#             self.redis_db.lpush(self.redis_table, item['url'])
#         return item