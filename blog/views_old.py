from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context

# todo get rid of this! use different classes for each view.

def index(request):
    ctx = Context()
    # ctx["baseurl"] = 'http://%s' % Site.objects.get_current().domain
    t = get_template("index.html")
    html = t.render(ctx)
    return HttpResponse(html)

def contact(request):
    ctx = Context()
    ctx["section"] = 'contact'
    t = get_template("index.html")
    html = t.render(ctx)
    return HttpResponse(html)
