from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.template.defaulttags import csrf_token
from django.shortcuts import render, render_to_response
from django.core.context_processors import csrf

from blog import jutils

def authenticate(request):
    if request.method == "POST":
        user_provided = request.POST['passphrase']
        if jutils.check_passphrase(user_provided):
            request.session['authenticated'] = True

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def authenticate_logout(request):
    request.session['authenticated'] = False;
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def csrfmiddlewaretoken(request):
    a = csrf(request)
    return HttpResponse(csrf_token)
