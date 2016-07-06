# -*- coding: utf-8 -*-
import scrapy
import re
from dou.items import TopicItem, AuthorItem, CommentItem


import re

from datetime import datetime
class CsvfeedSpider(scrapy.Spider):
    name = "csvfeed"
    allowed_domains = ["dou.ua"]
    start_urls = (
        'https://dou.ua/forum/',
    )
    _base_url = 'https://dou.ua'

    def parse(self, response):
        for i in range(1, 243+1):
            yield scrapy.Request('https://dou.ua/forums/page/{}/'.format(i), self.parse_next_page)

    def parse_next_page(self, response): 
        for link in response.xpath('//a[@class="g-comments-round"]/@href'):
            url = self._base_url + link.extract()
            yield scrapy.Request(url, self.parse_thread,
                    headers={'Accept-Language':'en,en-US;q=0.8,ru;q=0.6,ua;q=0.4'}, 
                    cookies={'lang': 'en'}, priority=500)

    def parse_thread(self, response):
        topic = TopicItem()
        topic['title'] = response.xpath('//title/text()').extract()[0][:-6]
        topic['url'] = response.url
        topic_id = int(re.findall('\d+', response.url)[0])
        topic['tid'] = topic_id
        date = response.xpath('//div[@class="b-post-info"]/span[@class="date"]/text()')[0].extract()
        print(date)
        try:
            topic['date'] = datetime.strptime(date, '%d %B, %H:%M')
        except Exception as e:
            print(date, 'error')
        topic['author_url'] = response.xpath('/html/body/div/div[2]/div[2]/div[2]/div[1]/div/div/a/@href')[0].extract()

        yield topic

        for link in response.xpath('//a[@class="avatar"]/@href'):
            url = self._base_url + link.extract()
            yield scrapy.Request(url, self.parse_userpage)
         
        for com in response.xpath('//div[@class="comment"]'):
            comment = CommentItem()
            author_url = com.xpath('.//a[@class="avatar"]/@href').extract()[0]
            comment['author_url'] = author_url
            comment['tid'] = topic_id 
            url = com.xpath('//a[@class="comment-link"]/@href')[0].extract()
             
            yield scrapy.Request(author_url, self.parse_userpage)


            comment['url'] = response.url + url
            comment['cid'] = url[1:]
            comment['text'] = '\n\n'.join([x for x in com.xpath('.//p/text()').extract()])
             
            date = com.xpath('.//a[@class="comment-link"]/text()')[0].extract()
            comment['date_string'] = date
            try:
                comment['date'] = datetime.strptime(date, '%d.%m.%Y %H:%M')
            except Exception as e:
                print(date)

            yield comment


    def parse_userpage(self, response):
        user = AuthorItem()
        user['url'] = response.url
        user['username'] = response.xpath('//div[@class="l-content"]/.//div[@class="head"]/h1/text()').extract()[0]
        yield user
