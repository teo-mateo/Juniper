from django.conf.urls import patterns, include, url
from blog.views_old import index, contraptions, contact
from blog.views.weblog import section_weblog, section_weblog_entry, section_weblog_tags


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
    url(r'^section/weblog/$', section_weblog, name='section_weblog'),
    url(r'^section/contraptions/$', contraptions, name='section_contraptions'),
    url(r'^section/contact/$', contact, name='section_contact'),
    url(r'^section/weblog/entry/([\w\-. ]+)$', section_weblog_entry, name='section_weblog_entry'),
    url(r'^section/weblog/tags/([\w\-. ]+)$', section_weblog_tags, name='section_weblog_tags'),
)
