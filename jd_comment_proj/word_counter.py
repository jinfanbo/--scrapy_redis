import jieba
from collections import Counter
import pymongo

MONGODB_SERVER = ""
MONGODB_PORT = 27017
MONGODB_DB = ""


def connect_db():
    """返回 collection cursor"""
    connection = pymongo.MongoClient(MONGODB_SERVER, MONGODB_PORT)
    db = connection[MONGODB_DB]
    return db['comments']


def word_count():
    """计算词频"""
    c = Counter()
    cur = connect_db()
    for g in cur.find({'content': {'$ne': "此用户未填写评价内容"}}, {'content': 1, '_id': 0}):
        text = g['content']
        seg_list = jieba.cut(text)
        for x in seg_list:
            if len(x) > 1 and x != '\r\n':
                c[x] += 1

    # 出现最多的一百个词
    for (k, v) in c.most_common(100):
        print(k, v)


word_count()
