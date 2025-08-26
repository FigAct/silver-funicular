import os, re, time
import random

import requests

pat = "<br />(.*?)<br />"
patt = "<div id=\"content\"><br />(.*)<br />"
web_patt = "章节目录</a> &rarr; <a href=\"(.*?)\">下一章</a>"
title_patt_1 = "<div class=\"bookname\">(.*?)</div>"
title_patt_2 = "<h1>(.*?)</h1>"
root = "https://www.ddyveshu.cc"
# web = "https://www.ddyveshu.cc/98288_98288020/21101683.html"  start
web = "https://www.ddyveshu.cc/98288_98288020/19274976.html"  # end
NUM = 2022


def save_cont(_path, _l):
    """保存章节"""
    with open(_path, 'w', encoding='utf-8') as _f:
        for _t in _l:
            _f.write(_t)
            _f.write('\n')


os.makedirs('斩神', exist_ok=True)

for i in range(1684, NUM):
    try:
        response = requests.get(web)
    except requests.exceptions.ConnectionError:
        time.sleep(1)
        print("失败--")
        response = requests.get(web)
    con = response.encoding
    html_txt = response.content.decode('GB18030')
    title = re.findall(title_patt_1, html_txt, re.S)
    title = re.findall(title_patt_2, title[0], re.S)
    title = title[0].strip()
    title.replace(" ", "_")

    lis = re.findall(patt, html_txt)  # 正文
    web_list = re.findall(web_patt, html_txt)  # 下一章链接
    web = root + web_list[0]
    print(i, end='----')
    # print(web_list,end='----')
    print(web)
    path = '斩神' + '//' + title + '.txt'
    if lis:
        l = re.findall(pat, lis[0])
        if l:
            save_cont(path, l)
        else:
            print("pat")
    else:
        print("list为空")
    time.sleep(random.randint(1, 3))
