## lastfmauth app for django projects

So far this is a very alpha app and it need some more work to be complete.

### Requirements
Tested with django 1.2 and python2.6.

### Instalation
Register your app and get a key in [LastFM API page] (http://www.last.fm/api/)

Add to your settings.py:

    INSTALLED_APPS = (
        ...
        'lastfmauth',
        ...
    )

    AUTHENTICATION_BACKENDS = (
        "lastfmauth.backends.LastfmAuthBackend",
        ...
    )

    LASTFM_API_KEY = "YOUR API KEY"
    LASTFM_SECRET = "YOUR SECRET KEY"
    LASTFM_WS_BASE_URL = "http://ws.audioscrobbler.com/2.0/"

Add to your urls.py:
    ...
    (r'^lastfmauth/', include('lastfmauth.urls')),
    ...
