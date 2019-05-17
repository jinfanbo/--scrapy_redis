from collections import Counter
import pymongo
from pyecharts import Pie, Style, Page
from db import init_mongodb


def analyst():
    """颜色，型号，内存"""
    color_c = Counter()
    model_c = Counter()
    ram_c = Counter()

    db = init_mongodb()
    cur = db['comments']

    for g in cur.find({}, {'color': 1, 'model': 1, 'ram': 1, '_id': 0}):
        # 颜色清洗
        color = g['color']
        if ' ' in color:
            color = color.split()[0]
        color_c[color] += 1

        # ram 清洗
        ram = g['ram']
        if ram:
            ram_c[ram] += 1

        # model 清洗
        model = g['model']
        excludes = ['手机', '白条免息', '电信老人机']
        if model not in excludes:
            model_c[model] += 1

    # for (k, v) in c.most_common(100):
    #     print(k, v)
    # 饼图
    page = Page()
    style = Style(
        width=800, height=800
    )
    ## color
    attr = color_c.keys()
    v1 = color_c.values()

    chart = Pie("颜色", **style.init_style)
    chart.add("", attr, v1, is_label_show=True)
    page.add(chart)

    ## model
    attr = model_c.keys()
    v1 = model_c.values()
    chart = Pie("型号", title_pos='center', **style.init_style)
    chart.add("", attr, v1, radius=[40, 75], label_text_color=None,
              is_label_show=True, legend_orient='vertical', legend_pos='left')
    page.add(chart)

    ## ram
    attr = ram_c.keys()
    v1 = ram_c.values()
    chart = Pie("内存", title_pos='center', **style.init_style)
    chart.add("", attr, v1, radius=[40, 75], label_text_color=None,
              is_label_show=True, legend_orient='vertical', legend_pos='right')
    page.add(chart)

    page.render(path="result.html")


analyst()
