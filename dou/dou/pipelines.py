# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import items

from items import AuthorItem, CommentItem, TopicItem
ids = []
class DouPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, TopicItem): 
            topic = item.save(commit=False)
            topic.id = item['tid']
            topic.save()
        elif isinstance(item, CommentItem): 
            comment = item.save(commit=False)
            comment.id = item['cid']
            comment.topic_id = item['tid']
            try:
                comment.save()
            except Exception as e:
                import ipdb
                ipdb.set_trace()
            ids.append(comment.id)
        else:
            item.save()
        return item
