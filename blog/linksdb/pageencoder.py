__author__ = 'teo'
import json

class PageEncoder(json.JSONEncoder):
    def encode(self, o):
        return {
            'id': unicode(o.id),
            'title': unicode(o.title),
            'content': unicode(o.content),
            'lastmodified': o.lastModified.isoformat()
        }

    def default(self, obj):
        if hasattr(obj, '__iter__'):
            return [ self.encode_object(x) for x in obj ]
        else:
            return self.encode_object(obj)
