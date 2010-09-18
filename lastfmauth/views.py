# -*- coding: UTF-8 -*-
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

from lastfmauth.models import LastfmProfile

API_KEY = settings.LASTFM_API_KEY

def do_login(request):
    signin_url = "http://www.last.fm/api/auth/?api_key=%s" % API_KEY
    return HttpResponseRedirect(signin_url)

def login_complete(request):
    token = request.GET["token"]

    user = authenticate(token=token)
    if user:
        login(request, user)

    return HttpResponseRedirect("/admin/")
