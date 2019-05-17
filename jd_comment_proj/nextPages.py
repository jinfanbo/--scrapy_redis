# -*- coding: utf-8 -*-
import demjson
from urllib.parse import urlencode
import requests
import time
import redis
from utils import num2code
from jd_comment_proj.settings import REDIS_HOST
identity='master'


class nextPagesSpider(object):
    def __init__(self, url):
        self.r = redis.Redis(host=REDIS_HOST, port=6379)
        self.url = url
        self.headers = {
            'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        }

    def parse(self):
        self.r.lpush('jd_comment:start_urls', self.url)
        response = requests.get(self.url, headers=self.headers)
        content = response.text
        pa_index = content.index('(') + 1
        content = content[pa_index:-2]
        json_obj = demjson.decode(content)


        # yield next page
        page_count = int(json_obj['data']['searchm']['Head']['Summary']['Page']['PageCount'])
        current_page = int(json_obj['data']['searchm']['Head']['Summary']['Page']['PageIndex'])
        for i in range(current_page, 251):
            next_page = i + 1
            params = (
                ('keyword', '手机'),
                ('datatype', '1'),
                ('callback', '{}'.format(num2code(next_page))),
                ('page', '{}'.format(next_page)),
                ('pagesize', '10'),
                ('ext_attr', 'no'),
                ('brand_col', 'no'),
                ('price_col', 'no'),
                ('color_col', 'no'),
                ('size_col', 'no'),
                ('ext_attr_sort', 'no'),
                ('merge_sku', 'yes'),
                ('multi_suppliers', 'yes'),
                ('area_ids', '1,72,2819'),
                ('qp_disable', 'no'),
                ('fdesc', '北京'),
                ('t1', '{}'.format(int(time.time())*1000)),
                ('traceid', '641129632769461602')
            )
            url = "https://so.m.jd.com/ware/search._m2wq_list?" + urlencode(params)
            self.r.lpush('jd_comment:start_urls', url)

if __name__ == '__main__':
    start = nextPagesSpider('https://so.m.jd.com/ware/search._m2wq_list?keyword=%E6%89%8B%E6%9C%BA&datatype=1&callback=jdSearchResultBkCbA&page=1&pagesize=10&ext_attr=no&brand_col=no&price_col=no&color_col=no&size_col=no&ext_attr_sort=no&merge_sku=yes&multi_suppliers=yes&area_ids=1,72,2819&qp_disable=no&fdesc=%E5%8C%97%E4%BA%AC&t1=1558015317044&traceid=642658684076502161')
    start.parse()