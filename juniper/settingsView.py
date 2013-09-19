from django.conf import settings

class SettingsView(object):

    class Defaults(object):
        pass

    def __init__(self):
        self.defaults = SettingsView.Defaults()

    def __getattr__(self, item):
        return getattr(settings, item, getattr(self.defaults, item))