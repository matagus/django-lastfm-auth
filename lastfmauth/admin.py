# -*- coding: utf-8 -*-
from django.contrib import admin
from lastfmauth.models import LastfmProfile


class LastfmProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "is_subscriber")

admin.site.register(LastfmProfile, LastfmProfileAdmin)
