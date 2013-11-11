from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.template.defaulttags import csrf_token
from django.shortcuts import render, render_to_response
from juniper import settings
from blog.linksdb.linksengine import Link
import datetime
from django.core.urlresolvers import reverse

import logging

def section_links(request):
    log = logging.getLogger(__name__)
    log.debug("we're in the section_links handler.")

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
    return HttpResponseRedirect(reverse('section_links'))

def section_links_delete(request):
    link = Link.objects(id=request.GET['id'])[0]
    link.delete()
    return HttpResponseRedirect(reverse('section_links'))