import requests
import re
import lxml.html



URL = "https://www.m.xiaoxiaoshuo8.com/0_4/all.html"
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
    html_txt = response.content.decode("utf-8")

    url_txt_start = re.findall(r'<p>(.*?)</p>', html_txt)
    url = []

    for t_url in url_txt_start[1:]:
        t = re.findall(r"<a href='(.*?)'>", t_url)
        url.append(f"{URL}{t[0]}")

    selector = lxml.html.fromstring(html_txt)
    info = selector.xpath("/html/body/div/p/a/text()")

    save_html(info[1:], "name_txt.txt")
    save_html(url[0:], "url_txt.txt")
