# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from modelsapp.models import Author, Topic, Comment

from scrapy_djangoitem import DjangoItem
class CommentItem(DjangoItem):
    cid = scrapy.Field()
    tid = scrapy.Field()
    django_model = Comment

class AuthorItem(DjangoItem):
    django_model = Author

class TopicItem(DjangoItem):
    tid = scrapy.Field()
    django_model = Topic
