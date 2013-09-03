from django.conf.urls import patterns, include, url
from Juniper.views import hello, current_datetime, hours_ahead, index, weblog, contraptions, contact

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Juniper.views.home', name='home'),
    # url(r'^Juniper/', include('Juniper.Juniper.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^section/weblog/$', weblog, name='section_weblog'),
    url(r'^section/contraptions/$', contraptions, name='section_contraptions'),
    url(r'^section/contact/$', contact, name='section_contact'),

)
