from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from blog.posts.entry import Entry
from juniper import settings
import os

def get_md_entries():
    md_dir = settings.MARKDOWN_DIR
    files = os.listdir(md_dir)
    entries = []
    for f in files:
        e = Entry(f)
        e.read()
        entries.append(e)
    entries.sort(key=lambda x: x.post_date)
    return entries

def section_weblog(request):
    ctx = Context()
    ctx["section"] = 'weblog'
    ctx["md_dir"] = settings.MARKDOWN_DIR
    ctx["md_entries"] = get_md_entries()
    t = get_template("index.html")
    html = t.render(ctx)
    return HttpResponse(html)

def section_weblog_entry(request, param):
    ctx = Context()
    ctx["section"] = 'weblog'
    ctx["md_dir"] = settings.MARKDOWN_DIR
    ctx["md_entries"] = get_md_entries()
    ctx["single_entry"] = True
    for e in ctx["md_entries"]:
        if e.md_file == param:
            ctx["entry"] = e
            break
    t = get_template("index.html")
    html = t.render(ctx)
    return HttpResponse(html)


