# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests, os
from lxml import etree
class QidianspiderPipeline(object):
    def process_item(self, item, spider):
        book_utl = item['book_url']
        book_each_url = item['book_each_url']
        book_zhangjie_name =item['book_zhangjie_name']
        # 对每本书的章节进行处理
        for each_url, zhang in zip(book_each_url,book_zhangjie_name):
            load_url = book_utl+each_url
            zhang_name = zhang
            res1 = requests.get(load_url).text
            html1 = etree.HTML(res1)
            text = html1.xpath('//div[@id="htmlContent"]/text()')

            path = 'F:\小说/' + item['book_name']
            if not os.path.exists(path):
                os.makedirs(path)
            for each in text:
                content = each.replace('\xa0\xa0\xa0\xa0', '')
                file = open(path+"/"  + zhang_name + ".txt", 'a')
                file.write(content)
                file.close()
            # print(text)



        return item
