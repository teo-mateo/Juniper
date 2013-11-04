from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from juniper import settings
from blog.linksdb.linksengine import Link


def section_links(request):
    ctx = Context()
    ctx["section"] = 'links'
    ctx['links'] = Link.objects
    t = get_template("index.html")
    html = t.render(ctx)
    return HttpResponse(html)

def section_links_addlink(request):
    ctx=Context()
    ctx['section'] = 'links'
    Link(url=request.GET['link'], comment='comment').save()
    ctx['links'] = Link.objects

    t = get_template("index.html")
    html = t.render(ctx)
    return HttpResponse(html)
