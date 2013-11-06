from django.conf.urls import patterns, include, url
from blog.views_old import index, contraptions, contact
from blog.views.weblog import section_weblog, section_weblog_entry, section_weblog_tags
from blog.views.links import section_links, section_links_addlink
from blog.views.juniperauth import authenticate, authenticate_logout

from django import http

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

def session_test_1(request):
    request.session['test'] = 'Session Vars Worked!'
    return http.HttpResponseRedirect('done/?session=%s' % request.session.session_key)

def session_test_2(request):
    return http.HttpResponse('<br>'.join([
        request.session.session_key,
        request.GET.get('session'),
        request.session.get('test', 'Session is Borked :(')]))



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'juniper.views.home', name='home'),
    # url(r'^juniper/', include('juniper.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', section_weblog, name='index'),
    url(r'^authenticate$', authenticate, name='authenticate'),
    url(r'^authenticate/logout$', authenticate_logout, name='authenticate_logout'),
    url(r'^section/weblog/$', section_weblog, name='section_weblog'),
    url(r'^section/links/$', section_links, name='section_links'),
    url(r'^section/links/addlink/$', section_links_addlink, name='section_links_addlink'),
    url(r'^section/contraptions/$', contraptions, name='section_contraptions'),
    url(r'^section/contact/$', contact, name='section_contact'),
    url(r'^section/weblog/entry/([\w\-. ]+)$', section_weblog_entry, name='section_weblog_entry'),
    url(r'^section/weblog/tags/([\w\-. ]+)$', section_weblog_tags, name='section_weblog_tags'),
    url(r'^session-test/$', session_test_1),
    url(r'^session-test/done/$', session_test_2),

)

