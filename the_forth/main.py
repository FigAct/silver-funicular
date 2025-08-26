import requests, os, time, random
from fake_useragent import UserAgent
import re

dir_name = '粒米洛'
ua = UserAgent()
headers = {
    "User-Agent": ua.random,
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Referer": "https://www.baidu.com/"
}


def get_url():
    """从文件中得到章节网址"""
    _url = []
    _name = []
    with open("url_list.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            if line != "":
                _url.append(line.strip())
    return _url


def save_html(_html, _name):
    with open(_name, "w", encoding='utf-8') as f:
        for _i in _html:
            _i = _i.replace("\r\r", "\n")
            f.write(_i)
            f.write('\n')
    print(f"已经写入--{_name}")
    # print(_html)


if __name__ == '__main__':
    os.makedirs(f'{dir_name}', exist_ok=True)
    url_list = get_url()  # 章节名的获得
    n = 0
    for url in url_list:
        n += 1
        try:
            response = requests.get(url, headers=headers)
        except requests.exceptions.ConnectionError:
            time.sleep(1)
            print("失败--")
            response = requests.get(url, headers=headers)
        # encoding_html = response.encoding

        html_txt = response.content.decode("GBK").replace("&nbsp;", "")  # 替换&nbsp防止通过xpath提取的内容出现乱码
        html_txt = html_txt.replace("\n", "")
        html_txt = html_txt.replace("<br />", "")
        info = re.findall("<div id=\"content\">(.*?)</div>", html_txt)

        title = re.findall("<div class=\"bookname\">(.*?)</div>", html_txt, re.S)  # 提取题目
        title = re.findall("<h1>(.*?)</h1>", title[0], re.S)[0]
        # 剔除特殊字符
        title = title.replace(" ", "_")
        title = title.replace("/", ":")
        title = title.replace("?", "")
        title = title.replace("\\", "")
        title = title.replace("*", "")
        title = title.replace("<", "")
        title = title.replace(">", "")
        title = title.replace("|", "")

        path = f'{dir_name}' + '//' + title + '.txt'  # 保存txt文件的文件名

        print(n, end="---")
        print(title, end="    ")
        print(url, end="---")  # 标明在爬取过程中的错误url
        save_html(info, path)
        # print(info,end="--info")

        time.sleep(random.randint(1, 2))
    print("完成！！！")
