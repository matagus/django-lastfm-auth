# -*- coding: UTF-8 -*-
from django.db import models


class LastfmProfile(models.Model):
    """
    """

    user = models.OneToOneField("auth.User")

    name = models.CharField(max_length=200)
    is_subscriber = models.BooleanField(default=False)
    key = models.CharField(max_length=32, editable=False)

    def __unicode__(self):
        return u"%s is %s in last.fm" % (self.user, self.name)
