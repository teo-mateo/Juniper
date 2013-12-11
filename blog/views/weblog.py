from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context, RequestContext
from blog.posts.entry import Entry
from django.shortcuts import render, render_to_response
from juniper import settings
import os

def get_all_entries():
    print 'getting blog entries from ' + settings.MARKDOWN_DIR
    md_dir = settings.MARKDOWN_DIR
    files = os.listdir(md_dir)
    entries = []
    for f in files:
        if f.endswith(".md"):
            e = Entry(f)
            e.read()
            entries.append(e)
    entries.sort(key=lambda x: x.post_date, reverse=True)
    return entries



def section_weblog(request):
    ctx = RequestContext(request)
    ctx["section"] = 'weblog'
    ctx["page_title"] = 'Weblog'
    ctx["md_dir"] = settings.MARKDOWN_DIR
    ctx["md_entries"] = get_all_entries()
    t = get_template("index.html")
    html = t.render(ctx)
    return render(request, "index.html", ctx)

def section_weblog_entry(request, param):
    ctx = RequestContext(request)
    ctx["section"] = 'weblog'
    ctx["md_dir"] = settings.MARKDOWN_DIR
    ctx["md_entries"] = get_all_entries()
    ctx["single_entry"] = True
    for e in ctx["md_entries"]:
        if e.md_file == param:
            ctx["entry"] = e
            ctx["page_title"] = e.post_title
            break
    t = get_template("index.html")
    html = t.render(ctx)
    return render(request, "index.html", ctx)

def section_weblog_tags(request, param):
    weblog_entries = get_all_entries()

    ctx = Context()
    ctx["section"] = 'weblog'
    ctx["page_title"] = "Tags"
    ctx["md_dir"] = settings.MARKDOWN_DIR
    ctx["md_entries"] = []
    ctx["single_entry"] = False

    for e in weblog_entries:
        if param in e.post_tags:
            ctx["md_entries"].append(e)

    t = get_template("index.html")
    html = t.render(ctx)
    return HttpResponse(html)

