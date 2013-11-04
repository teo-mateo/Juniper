__author__ = 'teo'

from mongoengine import *

connect('linksdb')

class Link(Document):
    url = StringField(required=True)
    comment = StringField(required=False)

