__author__ = 'teo'

from mongoengine import *
import markdown
from django.utils.safestring import mark_safe

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
    order = IntField(required=True)
    title = StringField(required=True)
    content = StringField(required=False)
    lastModified = DateTimeField(required=True)

class Contraption(Document):
    order = IntField(required=True)
    title = StringField(required=True)
    description = StringField(required=False)
    visible = BooleanField(required=True)
    pages = ListField(ReferenceField(Page))

class ContraptionHtml:
    def __init__(self, contraption):
        self.source = contraption
        self.order = contraption.order
        self.title = contraption.title
        self.description = mark_safe(markdown.markdown(contraption.description))
        self.pages = []
        for p in contraption.pages:
            self.pages.append(PageHtml(p))

class PageHtml:
    def __init__(self, page):
        self.source = page
        self.order = page.order
        self.title = page.title
        self.content = mark_safe(markdown.markdown(page.content))
        self.lastModified = page.lastModified

if __name__ == "__main__":
    contraptions = Contraption.objects
    c = ContraptionHtml(contraption=contraptions[0])