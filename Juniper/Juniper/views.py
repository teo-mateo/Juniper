from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.contrib.sites.models import Site

import datetime

def hello(request):
    return HttpResponse("Hello world!")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

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
    