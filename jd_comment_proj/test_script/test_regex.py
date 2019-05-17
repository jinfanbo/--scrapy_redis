import re

text = """warename: "魅族（MEIZU） V8 移动联通电信全网通4G 双卡双待 全面屏老人老年智能手机 曜黑 (4G RAM +64G ROM)",
warename: "魅族（MEIZU） 魅族16th 游戏手机 静夜黑 6+64G",
warename: "华为（HUAWEI） 荣耀 畅玩6 全网通4G 智能老人手机 双卡双待 2G+16G 金色",
warename: "华为（HUAWEI） Mate10 双卡双待 商务手机 亮黑色 全网通(6G+128G)",
warename: "三星（SAMSUNG） W2019 侧边指纹识别翻盖智能商务手机 睿金至尊版（6GB+128GB）",
warename: "华为（HUAWEI） 畅享9 移动全网通4G智能手机 幻夜黑（4G+64G）",
warename: "华为（HUAWEI） 畅享9 移动全网通4G智能手机 幻夜黑（4G+64G）", """

phones = text.split('\n')

reg = re.compile('\dG?B?\s?R?A?M?\s?\+')

for phone in phones:
    result = reg.search(phone)
    print(result.group()[0])
