__author__ = 'teo'

from mongoengine import *

connect('linksdb')

class Link(Document):
    url = StringField(required=True)
    date = DateTimeField(required=False)
    title = StringField(required=False)
    comment = StringField(required=False)

