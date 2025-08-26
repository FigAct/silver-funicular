import requests,os,time,random
import lxml.html

PATH_URL = "url"
def get_url():
    """从文件中得到章节网址"""
    _url = []
    _name = []
    with open("url_txt.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            if line != "":
                _url.append(line.strip())
    with open("name_txt.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            if line != "":
                _name.append(line.strip())
    return _url, _name


def save_html(_html,_name):
    with open(_name, "w", encoding='utf-8') as f:
        for i in _html:
            f.write(str(i))
            f.write('\n')
    print(f"已经写入{_name}")
    #print(_html)



if __name__ == '__main__':
    os.makedirs('血姬与骑士', exist_ok=True)
    url_list, name_list = get_url() #章节名的获得
    n = 0
    for url in url_list:
        n += 1
        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError:
            time.sleep(1)
            print("失败--")
            response = requests.get(url)
        #encoding_html = response.encoding

        html_txt = response.content.decode("utf-8").replace("&nbsp;", "")#替换&nbsp防止通过xpath提取的内容出现乱码
        selector = lxml.html.fromstring(html_txt)   # 生成一个特殊对象
        info = selector.xpath("/html/body/div[2]/text()")   # 提取章节内容
        title = selector.xpath("/html/body/header/span/text()")[0].replace(" ", "_")    # 提取题目
        path = '血姬与骑士' + '//' + title + '.txt'  # 保存txt文件的文件名

        print(n,end="---")
        print(title,end="    ")
        print(url,end="---")    # 标明在爬取过程中的错误url
        save_html(info, path)

        time.sleep(random.randint(1, 3))