# -*- coding: UTF-8 -*-
from hashlib import md5
from urllib2 import urlopen

from django.conf import settings
from django.contrib.auth.models import User
from django.core.serializers.json import simplejson

from lastfmauth.models import LastfmProfile

API_KEY = settings.LASTFM_API_KEY
SECRET = settings.LASTFM_SECRET
WS_URL = settings.LASTFM_WS_BASE_URL


class LastfmAuthBackend:
    """
    """

    def authenticate(self, token=None):

        api_sig = md5("api_key%smethodauth.getSessiontoken%s%s"\
            % (API_KEY, token, SECRET)).hexdigest()

        get_session_url = "%s?method=auth.getSession&token=%s&api_key=%s&api_sig=%s&format=json"\
            % (WS_URL, token, API_KEY, api_sig)

        try:
            session_data = urlopen(get_session_url).read()
            session_dict = simplejson.loads(session_data)
            user_dict = session_dict["session"] 
        except:
            # couln't authenticate against lastfm api
            return None

        # try to find a user instance with a matching lastfm profile,
        # otherwise we create it:
        user, user_created = User.objects.get_or_create(
            lastfmprofile__name=user_dict["name"],
            defaults={"username": user_dict["name"]})
           
        if user_created:
            user.set_password(User.objects.make_random_password())
            user.save()

            # then we must create a lastfm profile... 
            profile, profile_created = LastfmProfile.objects.get_or_create(
                name=user_dict["name"], defaults={"key": user_dict["key"], 
                "is_subscriber": int(user_dict["subscriber"]), "user": user})

        # else: 
        # FIXME:
        # should we update key session? and user info?
            
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
