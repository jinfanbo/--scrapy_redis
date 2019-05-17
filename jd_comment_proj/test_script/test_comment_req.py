import requests

headers = {
    ##一定要添加referer
    'Referer': 'https://item.m.jd.com/product',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36',
    # 'DNT': '1',
}


import demjson
import math
from utils import comment_num2code
import time
from urllib.parse import urlencode

# response = requests.get('https://so.m.jd.com/ware/search._m2wq_list?keyword=%E6%89%8B%E6%9C%BA&datatype=1&callback=jdSearchResultBkCbA&page=1&pagesize=10&ext_attr=no&brand_col=no&price_col=no&color_col=no&size_col=no&ext_attr_sort=no&merge_sku=yes&multi_suppliers=yes&area_ids=1,72,2819&qp_disable=no&fdesc=%E5%8C%97%E4%BA%AC&t1=1557837020180&traceid=641127124508556921', headers=headers)
# content = response.text
# pa_index = content.index('(') + 1
# content = content[pa_index:-2]
# json_obj = demjson.decode(content)

## all sku id in pages
# phones = json_obj['data']['searchm']['Paragraph']
# for phone in phones:
#     sku_id = phone['wareid']
#     warename = phone['Content']['warename'] #手机名称
#     model = phone['Content']['shortWarename'] #型号
#     if model == '':
#         model = warename.split()[0]
#     commentcount = phone["commentcount"]
#     if commentcount.isdigit():
#         commentcount = int(commentcount)
#     else:
#         continue
#     # yield comment page url, 主要需要 sku id, with  callback, 直接加上 comment_count
#     # 根据 comment count 来处理, 10 comment/page
#     # max pages = 100
#     pages = int(math.ceil(commentcount / 10))
#     for num in range(10):
#         page = num + 1
#         callback_code = comment_num2code(page)
#         params = (
#             ('callback', callback_code),
#             ('pagesize', '10'),
#             ('sceneval', '2'),
#             ('score', '0'),
#             ('sku', '{}'.format(sku_id)),
#             ('sorttype', '5'),
#             ('page', '{}'.format(page)),
#             ('t', '{}'.format(time.time())),
#         )
#         url = "https://wq.jd.com/commodity/comment/getcommentlist?" + urlencode(params)
#         print(url)

response = requests.get('https://wq.jd.com/commodity/comment/getcommentlist?callback=skuJDEvalI&pagesize=10&sceneval=2&score=0&sku=35050428593&sorttype=5&page=9&t=1558018539.7703946', headers=headers)
content = response.text
print(content)
with open('comment_html.txt', 'w') as f:
    f.write(content)