from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.template.defaulttags import csrf_token
from django.shortcuts import render, render_to_response
from juniper import settings
from blog.linksdb.linksengine import Link
import datetime

def section_links(request):
    ctx = RequestContext(request)
    ctx["section"] = 'links'
    ctx['links'] = Link.objects
    t = get_template("index.html")
    html = t.render(ctx)
    return render(request, "index.html", ctx)

def section_links_addlink(request):
    Link(
        url=request.POST['link'],
        date=datetime.datetime.now,
        comment='comment').save()
    return HttpResponseRedirect('/section/links/')

def section_links_delete(request):
    return