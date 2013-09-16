from django.conf.urls import patterns, include, url
from blog.views import index, weblog, contraptions, contact

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'juniper.views.home', name='home'),
    # url(r'^juniper/', include('juniper.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^section/weblog/$', weblog, name='section_weblog'),
    url(r'^section/contraptions/$', contraptions, name='section_contraptions'),
    url(r'^section/contact/$', contact, name='section_contact'),
)
