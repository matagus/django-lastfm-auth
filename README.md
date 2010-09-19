## lastfmauth app for django projects

Last.fm 2.0 API provides an authentication webservice. It works the same way Facebook Connect does,
but with Last.fm user credentials. With django-lastfmauth it is easy to redirect a user to Last.Fm:
Last.fm will do the login and ask them permission to your application to do it. Then, it will 
redirect the user to your website (you can set the callback url, please see bellow).

So far, this app does all this job, but it needs some more work.


### Requirements
Tested with django 1.2 and python 2.6.

### Instalation
Register your app and get a key in [LastFM API page](http://www.last.fm/api/)
Set the callback url to http://your-domain/login_complete/

Then download and install lastfmauth app: 

    pip install -E path/to/your/env/ django-lastfmauth

or 

    easy_install django-lastfmauth

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

Create app tables in your database:

    python manage.py syncdb

### Usage
Put somewhere in your templates a link to let visitors login using LastFM:

    <a href="{% url lastfmauth_login %}">{% trans 'Login using your LastFm account' %}</a>

### License
This work is under MIT License.
