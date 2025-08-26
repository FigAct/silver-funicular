import requests
import re
import lxml.html



URL = "https://www.biquinfo.com/book/49860/"
def save_html(_html,_name):
    with open(_name, "w", encoding='utf-8') as f:
        for i in _html:
            f.write(str(i))
            f.write('\n')
    print(f"已经写入{_name}")
    #print(_html)

if __name__ == '__main__':
    response = requests.get(URL)
    encoding_html = response.encoding
    html_txt = response.content.decode("gbk")

    selector = lxml.html.fromstring(html_txt)
    info = selector.xpath("/html/body/div/p/a/text()")
    url_txt_start = selector.xpath("/html/body/div[3]/div[2]/div/div[2]/ul/li/a/@href")

    url = []
    for t_url in url_txt_start:
        url.append(f"https://www.biquinfo.com/book/49860/{t_url}")


    save_html(info, "name_txt.txt")
    save_html(url, "url_txt.txt")
