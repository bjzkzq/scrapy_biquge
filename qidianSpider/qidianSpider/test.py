# 人丑就要多学习
import requests
from lxml import etree


url = 'https://www.ybdu.com/xiaoshuo/18/18861/'
res = requests.get(url).text

html = etree.HTML(res)
a = html.xpath('//ul[@class="mulu_list"]/li/a/@href')
for i in a:
    url1 = 'https://www.ybdu.com/xiaoshuo/18/18861/'+ i
    print(url1)

    # headers = {
    #     'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    #     'If-None-Match':'W/"5a0165f3-4490"',
    #     'Cookie':'Hm_lvt_a1b17bf301c6a7aa3a0ba9cce1414f7a=1522836047; jieqiVisitId=article_articleviews%3D18861; adwinnum=1; 37cs_pidx=1; 37cs_user=37cs36914953835; Hm_lpvt_a1b17bf301c6a7aa3a0ba9cce1414f7a=1522837022; 37cs_show=253; cscpvrich8519_fidx=7',
    # }
    # session = requests.session()
    # session.headers.update(headers)
    # res1 = session.get(url1).text
    res1= requests.get(url1).text
    # print(res1)
    html1 = etree.HTML(res1)
    a1 = html1.xpath('//div[@id="htmlContent"]/text()')
    print(a1)
    for each in a1:
        print(each.replace('\xa0\xa0\xa0\xa0', ''))
    print(a1)

    break

    {'a':{}}
