from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.template.defaulttags import csrf_token
from django.shortcuts import render, render_to_response
from blog.linksdb.linksengine import Contraption, Page, ContraptionHtml
import logging
from django.core.urlresolvers import reverse
from blog.linksdb.contraptionsencoder import ContraptionsEncoder
from blog.linksdb.pageencoder import PageEncoder

import json
from bson import json_util

__author__ = 'teo'

def section_contraptions(request):
    log = logging.getLogger(__name__)
    log.info("we're in the contraptions section.")


    ctx = RequestContext(request)
    ctx["section"] = 'contraptions'

    #transform the markdown content to html
    contraptions = Contraption.objects.order_by('order')
    ctx["contraptions"] = []
    for c in contraptions:
        if c.visible:
            ctx["contraptions"].append(ContraptionHtml(c))
        elif request.session['authenticated'] == True:
            ctx["contraptions"].append(ContraptionHtml(c))

    t = get_template("index.html")
    html = t.render(ctx)
    return render(request, "index.html", ctx)

def section_contraptions_get_contraption_raw(request):
    log = logging.getLogger(__name__)
    log.info("we're getting a raw contraption!")

    if request.method == 'GET':
        id_param = request.GET.get('id', None)
        if id_param <> None:
            o = Contraption.objects(id=id_param)[0]
            return HttpResponse(json.dumps(ContraptionsEncoder().encode(o)), mimetype="application/json")

def section_contraptions_delete_contraption(request):
    log = logging.getLogger(__name__)
    log.info("we're trying to delete a contraption.");
    if request.method == 'GET':
        id_param = request.GET.get('id', None)
        if id_param <> None:
            Contraption.objects(id=id_param)[0].delete()
            return HttpResponse(json.dumps({"status": "ok"}), mimetype="application/json")

def section_contraptions_view(request):
    log = logging.getLogger(__name__)
    log.info("we're trying to view a contraption")

    ctx = RequestContext(request)
    ctx["section"] = 'contraption_view'
    if request.method == 'GET':
        id_param = request.GET.get('id', None)
        if id_param <> None:
            ctx['contraption'] = ContraptionHtml(Contraption.objects(id=id_param)[0])

    t = get_template("index.html")
    html = t.render(ctx)
    return render(request, "index.html", ctx)

def section_contraptions_add(request):
    if request.method == 'POST':
        log = logging.getLogger(__name__)
        log.info("we're trying to save a new contraption.")

        form_order = request.POST.get('order', 0)
        form_title = request.POST.get('title', None)
        form_description = request.POST.get('description', None)
        form_visible = False
        if request.POST.get('visible', None) == 'on':
            form_visible = True
        else:
            form_visible = False

        c = Contraption(
            order = form_order,
            title = form_title,
            description = form_description,
            visible = form_visible)
        c.save()

    return HttpResponseRedirect(reverse('section_contraptions'))

def section_contraptions_edit(request):
    if request.method == 'POST':
        log = logging.getLogger(__name__)
        log.info("we're trying to change a contraption")

        form_id = request.POST.get('id', None)
        form_order = request.POST.get('order', 0)
        form_title = request.POST.get('title', None)
        form_description = request.POST.get('description', None)
        form_visible = False
        if request.POST.get('visible', None) == 'on':
            form_visible = True
        else:
            form_visible = False

        c = Contraption.objects(id=form_id)[0]
        c.order = form_order
        c.title = form_title
        c.description = form_description
        c.visible = form_visible;
        c.save()

    return HttpResponseRedirect(reverse('section_contraptions'))