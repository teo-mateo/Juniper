__author__ = 'teo'
import json

class ContraptionsEncoder(json.JSONEncoder):
    def encode(self, o):
        return {
            'id':unicode(o.id),
            'title': unicode(o.title),
            'description': unicode(o.description),
            'visible': bool(o.visible)
            }

    def default(self, obj):
        if hasattr(obj, '__iter__'):
            return [ self.encode_object(x) for x in obj ]
        else:
            return self.encode_object(obj)

