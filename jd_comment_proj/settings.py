# -*- coding: utf-8 -*-

# Scrapy settings for jd_comment_proj project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import os

BOT_NAME = 'jd_comment_proj'

SPIDER_MODULES = ['jd_comment_proj.spiders']
NEWSPIDER_MODULE = 'jd_comment_proj.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'jd_comment_proj.middlewares.JandanRedisSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'jd_comment_proj.middlewares.JandanRedisDownloaderMiddleware': 543,
    'jd_comment_proj.middlewares.RandomUserAgentMiddleware': 400,
    'jd_comment_proj.middlewares.IPProxyMiddleWare': 405,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    # 'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,  # 开启
    # 'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,  # ip proxy
    # 'scrapy_proxies.RandomProxy': 100,  # ip proxy
    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,  # ip proxy
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'jd_comment_proj.pipelines.MongoDBPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Enables scheduling storing requests queue in redis.
#使用Scrapy-Redis的调度器
SCHEDULER = 'scrapy_redis.scheduler.Scheduler'

#利用Redis的集合实现去重
# Ensure all spiders share same duplicates filter through redis.
DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'

#允许继续爬取
# Don't cleanup redis queues, allows to pause/resume crawls.
SCHEDULER_PERSIST = True

#设置优先级
# Default QUENE FIFO
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'

# QUENE LIFO
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderStack'

# QUENE PRIORITY
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'

FEED_EXPORT_ENCODING = 'utf-8'

### master ###
REDIS_HOST = '10.51.188.138'
REDIS_PORT = 6379
MY_REDIS='jd_comment:start_urls'
# REDIS_PARAMS = {
#    'password': '123456',
# }
### master ###

# ### slave ###
# REDIS_URL = 'redis://@127.0.0.1:6379'
# ### slave ###

# mongodb
MONGODB_SERVER = '10.51.188.138'
MONGODB_PORT = 27017
MONGODB_DB = 'jindong_test_final_3'

##################### 代理 ip ##############################
# # random ips
# RETRY_TIMES = 3   #重试请求次数
# RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]  #遇到什么http code时需要重试
# # 存放代理IP列表的位置
# from scrapy.utils.conf import closest_scrapy_cfg
# #closest_scrapy_cfg()函数做的工作是在当前文件夹下，寻找有没有scrapy.cfg文件，
# # 如果没有找到，则递归遍历父文件夹，直到遍历到根目录。
# # 如果找到了scrapy.cfg文件，则返回scrapy.cfg的绝对路径。
# dirpath = os.path.dirname(closest_scrapy_cfg())
# PROXY_LIST = 'E:\\spider\\spider\\京东\\jd_comment_proj\\ips.txt'
# #代理模式
# # 0 每个请求随机 ip，1 全部请求一个 ip， 2 使用设置中的 ip
# PROXY_MODE = 0
##################### 代理 ip ##############################


USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit /537.36 (KHTML, like Gecko) Chrome /39.0.2171.95 Safari /537.36',
    'OPR / 26.0.1656.60 Opera / 8.0(Windows NT 5.1; U; en)',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17 SE 2.X MetaSr 1.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1',
    'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
    'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24',
    'Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17',
    'Mozilla/5.0 (Linux; U; Android 3.0.1; fr-fr; A500 Build/HRI66) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.3 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36 TheWorld 7',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1',
    'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
    'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1',
    'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
    'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
    'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12',
    'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.302.2 Safari/532.8',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.15 Safari/534.13',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.186 Safari/535.1',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
    'Mozilla/5.0 (Macintosh; U; Mac OS X Mach-O; en-US; rv:2.0a) Gecko/20040614 Firefox/3.0.0 ',
    'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.0.3) Gecko/2008092414 Firefox/3.0.3',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1) Gecko/20090624 Firefox/3.5',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.14) Gecko/20110218 AlexaToolbar/alxf-2.0 Firefox/3.6.14',
    'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'
]

IP_PROXY_LIST = [
    'https://145.239.169.42:8080',
    'https://103.249.182.18:80',
    'https://186.24.11.165:8080',
    'https://180.168.13.26:8000',
    'https://221.126.249.100:8080',
    'https://176.31.69.179:8080',
    'https://196.13.208.22:8080',
    'https://1.10.189.119:58040',
    'https://50.73.137.241:3128',
    'https://81.91.144.53:3128',
    'https://221.14.153.189:9999',
    'https://139.129.236.194:80',
    'https://74.208.83.188:80',
    'https://14.104.178.176:9999',
    'https://179.106.88.162:80',
    'https://151.233.32.62:3128',
    'https://197.216.2.11:8080',
    'https://114.55.236.62:3128',
    'https://145.239.169.45:8080',
    'https://201.48.194.210:80',
    'https://47.90.73.118:3128',
    'https://58.8.110.16:8080',
    'https://167.114.203.141:80',
    'https://204.191.85.34:8080',
    'https://217.9.95.24:8080',
    'https://93.39.228.188:3128',
    'https://82.179.134.236:8080',
    'https://103.47.66.2:39804',
    'https://194.8.71.9:8080',
    'https://2.188.164.58:8080',
    'https://37.59.32.112:8080',
    'https://1.10.189.74:45481',
    'https://52.5.253.10:80',
    'https://178.62.111.19:8080',
    'https://223.27.212.41:8080',
    'https://176.31.69.177:8080',
    'https://222.74.237.246:808',
    'https://221.126.249.102:8080',
    'https://94.206.19.242:34561',
    'https://104.196.41.69:80',
    'https://163.172.175.210:3128',
    'https://95.167.213.27:8080',
    'https://85.93.47.137:8080',
    'https://218.60.8.83:3129',
    'https://103.249.182.20:80',
    'https://198.27.67.35:3128',
    'https://196.13.208.23:8080',
    'https://145.239.169.40:8080',
    'https://151.80.36.115:1080',
    'https://139.196.73.1:80',
    'https://51.38.71.101:8080',
    'https://119.28.87.177:808',
    'https://197.216.2.14:8080',
    'https://221.126.249.101:8080',
    'https://172.106.33.48:80',
    'https://119.28.118.116:1080',
    'https://176.31.69.180:8080',
    'https://37.79.244.120:3128',
    'https://202.142.221.131:80',
    'https://85.47.31.179:3128',
    'https://118.190.94.224:9001',
    'https://151.80.36.115:8080',
    'https://145.239.169.47:8080',
    'https://52.83.146.11:3128',
    'https://201.64.22.50:8081',
    'https://120.77.213.119:80',
    'https://193.93.78.242:32231',
    'https://118.190.95.35:9001',
    'https://221.126.249.99:8080',
    'https://203.113.10.153:8080',
    'https://103.227.255.175:80',
    'https://35.181.36.31:3128',
    'https://45.113.69.177:1080',
    'https://171.255.192.118:8080',
    'https://145.239.169.46:8080',
    'https://118.190.145.138:9001',
    'https://203.115.97.106:31070',
    'https://119.28.118.116:1080',
    'https://118.140.151.98:3128',
    'https://74.208.83.188:80',
    'https://104.196.41.69:80',
    'https://120.77.213.119:80',
    'https://218.60.8.83:3129',
    'https://197.216.2.12:8080',
    'https://120.83.122.224:9999',
    'https://52.5.253.10:80',
    'https://171.255.192.118:8080',
    'https://103.227.255.175:80',
    'https://119.28.87.177:808',
    'https://221.126.249.100:8080',
    'https://202.142.221.131:80',
    'https://179.106.88.162:80',
    'https://118.190.94.224:9001',
    'https://183.88.195.128:8080',
    'https://181.129.183.19:53281',
    'https://37.79.244.120:3128',
    'https://167.114.203.141:80',
    'https://40.114.109.214:3128',
    'https://103.249.182.20:80',
    'https://151.80.36.115:1080',
    'https://1.2.169.44:48545',
    'https://46.151.248.1:53281',
    'https://51.255.198.111:9999',
    'https://163.172.175.210:3128',
    'https://185.146.112.142:8080',
    'https://197.216.2.11:8080',
    'https://203.113.10.153:8080',
    'https://198.27.67.35:3128',
    'https://178.62.111.19:8080',
    'https://176.31.69.179:8080',
    'https://196.13.208.23:8080',
    'https://14.104.178.176:9999',
    'https://93.39.228.188:3128',
    'https://221.126.249.102:8080',
    'https://139.129.236.194:80',
    'https://114.55.236.62:3128',
    'https://221.126.249.99:8080',
    'https://186.24.11.165:8080',
    'https://196.13.208.22:8080',
    'https://118.190.95.35:9001',
    'https://45.113.69.177:1080',
    'https://118.190.145.138:9001',
    'https://164.132.92.16:9999',
    'https://81.91.144.53:3128',
    'https://139.196.22.147:80',
    'https://201.64.22.50:8081',
    'https://180.168.13.26:8000',
    'https://221.14.153.189:9999',
    'https://139.196.73.1:80',
    'https://103.249.182.18:80',
    'https://118.190.94.254:9001',
    'https://58.8.110.16:8080',
    'https://165.227.68.33:8118',
    'https://197.216.2.9:8080',
    'https://124.81.99.30:3128',
    'https://115.79.63.188:8081',
    'https://221.126.249.101:8080',
    'https://45.119.90.23:42458',
    'https://197.216.2.14:8080',
    'https://197.216.2.13:8080',
    'https://36.76.94.129:8080',
    'https://159.69.211.173:3128',
    'https://201.48.194.210:80',
    'https://41.60.237.20:8080',
    'https://47.90.73.118:3128',
    'https://80.78.70.30:53281'
]