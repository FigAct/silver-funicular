import requests,re
import lxml
# http://exercise.kingname.info/exercise_requests_get.html
web = "https://www.ddyveshu.cc/98288_98288020/21101683.html"
html_txt = requests.get(web).content.decode('gbk')

tree = lxml.html.fromstring(html_txt)
#print(html_txt)
with open('html.txt','w',encoding='utf-8') as f:
    f.write(html_txt)
patt = "<div id=\"content\"><br />(.*)<br />"
lis = re.findall(patt, html_txt)
print(lis)
pat = "<br />(.*?)<br />"
if lis:
    l = re.findall(pat, lis[0])
    if l:
        with open('content.txt','w',encoding='utf-8') as f:
            f.write(l[0])
            for i in l:
                f.write(i)
                f.write('\n')
    else:
        print("pat")
else:
    print("list为空")