import requests
import lxml.html

def save_html(_html,_name):
    with open(_name, "w", encoding='utf-8') as f:
        for i in _html:
            f.write(str(i))
            f.write('\n')
    print(f"已经写入{_name}")
    #print(_html)

if __name__ == '__main__':
    # response = requests.get("https://www.m.xiaoxiaoshuo8.com/0_4/2223.html")
    # encoding_html = response.encoding
    # html_txt = response.content.decode("utf-8").replace("&nbsp;","")
    # selector = lxml.html.fromstring(html_txt)
    # info = selector.xpath("/html/body/div[2]/text()")
    # save_html(info,"ccontext.txt")
    # title = selector.xpath("/html/body/header/span/text()")
    # print(title[0].replace(" ","_"))
    def get_url():
        """从文件中得到章节网址"""
        _url_ = []
        _name_ = []
        with open("TheSecond/url_txt.txt", "r", encoding="utf-8") as f:
            for line in f.readlines():
                #if line != "\n":
                    _url_.append(line.strip())

        return _url_
    url = get_url()
    print(url)
    for i in url:
        print(i)