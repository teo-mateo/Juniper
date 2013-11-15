__author__ = 'teo'

from mongoengine import *

connect('linksdb')

class LinkTag(Document):
    tag = StringField(required=True)

class Link(Document):
    url = StringField(required=True)
    date = DateTimeField(required=False)
    title = StringField(required=False)
    comment = StringField(required=False)
    tags = ListField(ReferenceField(LinkTag))

class Page(Document):
    title = StringField(required=True)
    content = StringField(required=False)
    lastModified = DateTimeField(required=True)

class Contraption(Document):
    title = StringField(required=True)
    description = StringField(required=False)
    visible = BooleanField(required=True)
    pages = ListField(ReferenceField(Page))