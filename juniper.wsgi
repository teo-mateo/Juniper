import os
import sys
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.join(os.path.dirname(__file__), 'juniper'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'juniper.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
