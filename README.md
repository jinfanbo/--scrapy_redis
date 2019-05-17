注: 配置文件是 `jd_comment_proj/settings.py`

# 安装基本组件
- Python 3.6.8
- 安装 Pipenv, 利用目录下的 `Pipfile` 文件装依赖即可
- Redis 5.0.4 
- MongoDB 4.0.3

# 配置 redis
服务器 redis 记得配置 `protected-mode no`, 否则可能连不上
参考: https://blog.51cto.com/crfsz/1878137

配置 `settings.py` 中的 REDIS_HOST, REDIS_PORT, REDIS_PARAMS(如有密码则配置)


# 配置数据库
MONGODB_SERVER 
MONGODB_PORT
MONGODB_DB
MONGO_USER="username" #有则配置
MONGO_PASS="password" #有则配置


# ip 代理配置(默认不使用代理)
如果使用 ip 代理
    1. 把 ### ip 代理 ### 中间部分 `取消注释`
    2. 搜索 `ip proxy`, 把三行注释
    2. 全部 ip 放到 ips.txt 文件中
        ip 代理的形式:
        http://host1:port
        http://username:password@host2:port
        http://host3:port

# 运行
1. `pipenv shell` 激活虚拟环境再运行项目
## 默认 master 宿主模式
`scrapy crawl jd_comment`
## 运行 slave 子爬虫
1. 搜索 master，并注释掉
2. 搜索 slave， 取消注释，正确配置 `REDIS_URL = 'redis://@127.0.0.1:6379'`
    - redis 如有帐号密码: `REDIS_URL = 'redis://username:pass@hostIP:6379'`
    
# 添加初始 url 开始爬
当搭好开始运行，scrapy 会监控 redis 中的数据，有 url 时才会开始爬
所以运行后需要把初始 url 加入到 redis

进入 redis-cli

lpush jd_comment:start_urls https://so.m.jd.com/products/9987-653-655._m2wq_list?keyword=&datatype=1&callback=jdSearchResultBkCbZ&page=1&pagesize=10&ext_attr=no&brand_col=no&price_col=no&color_col=no&size_col=no&ext_attr_sort=no&merge_sku=yes&multi_suppliers=yes&filt_type=catid,L655M655;&area_ids=1,72,2819&qp_disable=no&fdesc=%20%2F%20%E5%8C%97%E4%BA%AC&t1=1555279488724


# 词频统计
配置 `word_counter.py` 文件头的数据库连接参数，直接运行即可 `python word_counter.py`

# 颜色， 型号 内存统计
运行 `python data_analysis.py`
生成 `result.html` 打开即可。

型号从 `warename` 中提取，难以清洗，把不想要的结果添加到 `data_analysis.py` 文件中的 excludes(搜索) 即可。
