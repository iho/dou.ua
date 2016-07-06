from __future__ import unicode_literals
from django.db import models

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)
    class Meta:
        abstract = True

class Author(TimeStampedModel):
    login = models.TextField(unique=True, db_index=True)

    username = models.CharField(max_length=256, null=True)


class Topic(TimeStampedModel):
    url = models.TextField()

    title = models.CharField(max_length=256)
    text = models.TextField()

    date = models.DateTimeField(null=True, blank=True)

    author_url = models.TextField(null=True, blank=True)
    author = models.ForeignKey('Author', null=True, 
            related_name='topic'
            )


class Comment(TimeStampedModel):

    text = models.TextField()
    date = models.DateTimeField(null=True, blank=True)
    date_string = models.TextField(null=True, blank=True)

    url = models.TextField()
    author_url = models.TextField(null=True, blank=True)

    author = models.ForeignKey('Author', null=True, related_name="comments")
    topic = models.ForeignKey('Topic', null=True)
