from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context

def index(request):
    ctx = Context()
    # ctx["baseurl"] = 'http://%s' % Site.objects.get_current().domain
    t = get_template("index.html")
    html = t.render(ctx)
    return HttpResponse(html)


def weblog(request):
    ctx = Context()
    ctx["section"] = 'weblog'
    t = get_template("index.html")
    html = t.render(ctx)
    return HttpResponse(html)


def contraptions(request):
    ctx = Context()
    ctx["section"] = 'contraptions'
    t = get_template("index.html")
    html = t.render(ctx)
    return HttpResponse(html)


def contact(request):
    ctx = Context()
    ctx["section"] = 'contact'
    t = get_template("index.html")
    html = t.render(ctx)
    return HttpResponse(html)
