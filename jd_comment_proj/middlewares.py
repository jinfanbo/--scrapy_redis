# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class JdCommentProjSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    #     # scrapy acts as if the spider middleware does not modify the
    #     # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


import random
from jd_comment_proj.settings import USER_AGENT_LIST
from jd_comment_proj.settings import IP_PROXY_LIST
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
import logging

#首先在scrapy的middware中定义一个middware类
class RandomUserAgentMiddleware(UserAgentMiddleware):
    '''
    ua代理
    '''
    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENT_LIST)
        if user_agent:
            request.headers.setdefault('User-Agent', user_agent)
            print(f"User-Agent:{user_agent} is using.")
        return None

    def process_exception(self, request, exception, spider):
        error_info = f"spider:{spider.name} RandomUserAgentMiddleware has error with {exception}"
        print(error_info)
        logging.error(error_info)


class IPProxyMiddleWare(HttpProxyMiddleware):
    '''
    ip 代理池
    '''
    def process_request(self, request, spider):
        # 从list中选取IP，设置到request
        ip_proxy = random.choice(IP_PROXY_LIST)
        if ip_proxy:
            request.meta['proxies'] = ip_proxy  # 此处关键字proxies不能错
            print(f"IP_PROXY:{ip_proxy}")

    def process_exception(self, request, exception, spider):
        error_info = f"spider:{spider.name} MyIPProxyMiddleWare has error with {exception}"
        print(error_info)
        logging.error(error_info)