# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns("lastfmauth.views",
    url('^login/$', "do_login", name='lastfmauth_login'),
    url('^login_complete/$', "login_complete", name='lastfm_login_complete'),
)
