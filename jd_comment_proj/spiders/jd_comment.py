# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
from jd_comment_proj.items import CommentItem
import demjson
from urllib.parse import urlencode
import time
from scrapy.http import Request
from ..utils import comment_num2code
identity='slave'


class JdCommentSpider(RedisCrawlSpider):
    name = 'jd_comment'
    redis_key = 'jd_comment:start_urls'

    def __init__(self, *args, **kwargs):
        super(JdCommentSpider, self).__init__(*args, **kwargs)
        self.base_comment_url = ""

    def parse(self, response):
        content = response.text
        pa_index = content.index('(') + 1
        content = content[pa_index:-2]
        json_obj = demjson.decode(content)

        # all sku id in pages
        phones = json_obj['data']['searchm']['Paragraph']
        for phone in phones:
            sku_id = phone['wareid']
            warename = phone['Content']['warename'] #手机名称
            model = phone['Content']['shortWarename'] #型号
            if model == '':
                model = warename.split()[0]

            #构造手机评论url
            callback_code = comment_num2code(1)
            params = (
                ('callback', callback_code),
                ('pagesize', '10'),
                ('sceneval', '2'),
                ('score', '0'),
                ('sku', '{}'.format(sku_id)),
                ('sorttype', '5'),
                ('page', '1'),
                ('t', '{}'.format(time.time())),
            )
            # https://wq.jd.com/commodity/comment/getcommentlist?callback=skuJDEvalC&pagesize=10&sceneval=2&score=0&sku=18029072858&sorttype=5&page=3&t=1557926697.4126072
            url = "https://wq.jd.com/commodity/comment/getcommentlist?" + urlencode(params)
            yield Request(url=url, callback=self.get_phone_comments_maxpage, meta={
                'skuJDEval_code': callback_code,
                'sku_id': sku_id,
                'warename': warename,
                'model': model,
            })

    def get_phone_comments_maxpage(self, response):

        skuJDEval_code = response.meta['skuJDEval_code']
        sku_id = response.meta['sku_id']
        warename = response.meta['warename']
        model = response.meta['model']

        content = response.text
        content = content.replace(r"{}(".format(skuJDEval_code), "")
        content = content[:-1]
        json_obj = demjson.decode(content)
        maxpage = int(json_obj['result']['maxPage'])
        for page in range(1, maxpage):
            callback_code = comment_num2code(page)
            params = (
                ('callback', callback_code),
                ('pagesize', '10'),
                ('sceneval', '2'),
                ('score', '0'),
                ('sku', '{}'.format(sku_id)),
                ('sorttype', '5'),
                ('page', '{}'.format(page)),
                ('t', '{}'.format(time.time())),
            )
            # https://wq.jd.com/commodity/comment/getcommentlist?callback=skuJDEvalC&pagesize=10&sceneval=2&score=0&sku=18029072858&sorttype=5&page=3&t=1557926697.4126072
            url = "https://wq.jd.com/commodity/comment/getcommentlist?" + urlencode(params)
            yield Request(url=url, callback=self.parse_phone_comments, meta={
                'skuJDEval_code': callback_code,
                'sku_id': sku_id,
                'warename': warename,
                'model': model,
            })

    def parse_phone_comments(self, response):
        """字段包含评论人名称，评论内容，产品颜色，产品型号，产品名称，选择内存 """

        skuJDEval_code = response.meta['skuJDEval_code']
        sku_id = response.meta['sku_id']
        warename = response.meta['warename']
        model = response.meta['model']

        content = response.text
        content = content.replace(r"{}(".format(skuJDEval_code), "")
        content = content[:-1]
        json_obj = demjson.decode(content)
        comments = json_obj['result']['comments']

        for cm in comments:
            comment_item = CommentItem()
            comment_item['jd_comment_id'] = cm['id']
            comment_item['sku_id'] = sku_id
            comment_item['content'] = cm['content']
            comment_item['nickname'] = cm['nickname']
            comment_item['color'] = cm['productColor']
            comment_item['warename'] = warename
            comment_item['model'] = model
            comment_item['ram'] = cm['productSize']
            yield comment_item