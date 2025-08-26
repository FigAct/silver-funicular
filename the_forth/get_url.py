import requests
import lxml.html

URL = "https://www.xslca.net/girl/146331.html"
URL_t = "https://www.xslca.net"
def save_html(_html,_name):
    with open(_name, "w", encoding='utf-8') as f:
        for _i in _html:
            f.write(str(_i))
            f.write('\n')
    print(f"已经写入{_name}")
    #print(_html)

if __name__ == '__main__':
    n = 1

    response = requests.get(URL)
    encoding_html = response.encoding
    html_txt = response.content.decode("gbk")
    selector = lxml.html.fromstring(html_txt)
    url = selector.xpath("//*[@id=\"list\"]/dl/dd/a/@href")
    url_txt = []
    if url:
        for t_url in url:
            url_txt.append(f"{URL_t}{t_url}")
    else:
        print("找不到章节url")
    print(n, end=f'{URL}--')
    n += 1
    save_html(url_txt, "url_list.txt")
