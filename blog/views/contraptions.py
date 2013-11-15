from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.template.defaulttags import csrf_token
from django.shortcuts import render, render_to_response
from blog.linksdb.linksengine import Contraption, Page
import logging
from django.core.urlresolvers import reverse

__author__ = 'teo'

def section_contraptions(request):
    log = logging.getLogger(__name__)
    log.info("we're in the contraptions section.")

    ctx = RequestContext(request)
    ctx["section"] = 'contraptions'
    ctx['contraptions'] = Contraption.objects
    t = get_template("index.html")
    html = t.render(ctx)
    return render(request, "index.html", ctx)


def section_contraptions_add(request):
    if request.method == 'POST':
        log = logging.getLogger(__name__)
        log.info("we're trying to save a new contraption.")

        form_title = request.POST.get('title', None)
        form_description = request.POST.get('description', None)
        form_visible = False
        if request.POST.get('visible', None) == 'on':
            form_visible = True
        else:
            form_visible = False

        c = Contraption(
            title = form_title,
            description = form_description,
            visible = form_visible)
        c.save()

    return HttpResponseRedirect(reverse('section_contraptions'))