from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.template.defaulttags import csrf_token
from django.shortcuts import render, render_to_response
from juniper import settings
from blog.linksdb.linksengine import Link, LinkTag
import datetime
from django.core.urlresolvers import reverse

import logging

def section_links(request):
    log = logging.getLogger(__name__)
    log.debug("we're in the section_links handler.")

    ctx = RequestContext(request)
    ctx["section"] = 'links'
    ctx['links'] = Link.objects
    ctx['all_tags'] = LinkTag.objects
    t = get_template("index.html")
    html = t.render(ctx)
    return render(request, "index.html", ctx)

def section_links_addlink(request):
    if request.method == 'POST':
        Link(
            url=request.POST['link'],
            date=datetime.datetime.now,
            comment='comment').save()

    elif request.method == 'GET':
        security_token = request.GET.get('security_token', None)
        link = request.GET.get('link', None)
        title = request.GET.get('title', None)
        tags_raw = request.GET.get('tags', None)
        tags_split = tags_raw.split(',')

        tag_objects = []
        for t in tags_split:
            db_tags = LinkTag.objects(tag=t)
            if len(db_tags) == 1:
                tag_objects.append(db_tags[0])
            elif len(db_tags) == 0:
                db_tag_new = LinkTag(tag=t)
                db_tag_new.save()
                tag_objects.append(db_tag_new)


        if security_token == '4df52be1-5f8e-4c1b-9205-6a83fecf7ed1':

            Link(
                url = link,
                date = datetime.datetime.now,
                comment = '',
                title = title,
                tags = tag_objects
            ).save()

    return HttpResponseRedirect(reverse('section_links'))

def section_links_delete(request):
    link = Link.objects(id=request.GET['id'])[0]
    link.delete()
    return HttpResponseRedirect(reverse('section_links'))