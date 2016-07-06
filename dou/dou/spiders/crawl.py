# -*- coding: utf-8 -*-
import scrapy


class CrawlSpider(scrapy.Spider):
    name = "crawl"
    allowed_domains = ["dou.ua"]
    start_urls = (
        'http://www.dou.ua/',
    )

    def parse(self, response):
        pass
