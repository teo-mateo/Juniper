import os
import sys	
sys.path.append('/home/tman/gits/Juniper/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'juniper.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
