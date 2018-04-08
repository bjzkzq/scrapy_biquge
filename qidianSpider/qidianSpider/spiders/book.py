# -*- coding: utf-8 -*-
import scrapy
from qidianSpider.items import QidianspiderItem

"""
每本书的
//div[@class="clearfix rec_rullist"]/ul

每本书的链接
./li[@class="two"]/a/@href

书名
./li[@class="two"]/a/text()

作者
./li[@class="four"]/text()
"""


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['ybdu.com']
    url = 'https://www.ybdu.com/book1/0/'
    offset =1
    start_urls = [url+ str(offset)+'/']

    def parse(self, response):

        book = response.xpath('//div[@class="clearfix rec_rullist"]/ul')
        book_url_list = book.xpath('./li[@class="two"]/a/@href').extract()
        book_name_list = book.xpath('./li[@class="two"]/a/text()').extract()
        book_author_lsit = book.xpath('./li[@class="four"]/text()').extract()

        for each_url,name,author in zip(book_url_list,book_name_list,book_author_lsit):
            item = QidianspiderItem()
            text = each_url
            item['book_url'] = each_url
            item['book_name'] = name[:len(name)-4]
            item['book_author'] = author
            yield scrapy.Request(text, callback=self.book_sovle, meta={'item': item})
            # yield item

    # 每本书的处理，章节名，链接
    def book_sovle(self,response):
        item = response.meta['item']
        # print(item)
        book_abstract_list = response.xpath('//div[@class="mu_contain"]/p/text()').extract()
        book_each_url_list = response.xpath('//div[@class="mu_contain"]/ul/li/a/@href').extract()
        book_zhangjie_name_list = response.xpath('//div[@class="mu_contain"]/ul/li/a/text()').extract()
        # print(all)
        item['book_zhangjie_name'] = book_zhangjie_name_list

        item['book_abstract'] = book_abstract_list
        item['book_each_url'] = book_each_url_list
        yield item
        # for load_book_url,zhang in zip(book_each_url_list, book_zhangjie_name_list):
        #     item['book_zhangjie_name'] = zhang
        #     item['book_each_url'] = load_book_url
        #     # yield scrapy.Request(item['book_url']+load_book_url,callback=self.load,meta={'item': item})
        #     print(item)
        #     yield item

    # def load(self,response):
    #     item = response.meta['item']
    #     book_neirong_list = response.xpath('//div[@id="htmlContent"]/text()').extract()
    #     item['book_neirong'] = book_neirong_list
    #     print(item['book_neirong'])
    #     yield item