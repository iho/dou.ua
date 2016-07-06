# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Author, Topic, Comment


class AuthorAdmin(admin.ModelAdmin):
    list_display = (u'id', 'created', 'modified', 'login', 'username')
    list_filter = ('created', 'modified')
admin.site.register(Author, AuthorAdmin)


class TopicAdmin(admin.ModelAdmin):
    list_display = (
        u'id',
        'created',
        'modified',
        'url',
        'title',
        'text',
        'date',
        'author_url',
        'author',
    )
    list_filter = ('created', 'modified', 'date', 'author')
admin.site.register(Topic, TopicAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        u'id',
        'created',
        'modified',
        'date',
        'date_string',
        'url',
        'author_url',
        'author',
    )
    list_filter = ('created', 'modified', 'date', 'author', 'topic')
admin.site.register(Comment, CommentAdmin)

