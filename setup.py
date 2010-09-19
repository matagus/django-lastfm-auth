# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="django-lastfmauth",
    version=__import__("lastfmauth").__version__,
    url="http://github.com/matagus/django-lastfm-auth",
    license="BSD",
    description="Django app to let your website visitors register/login using LastFM authentication webservice.",
    long_description=open("docs/usage.rst").read(),

    author="Matias Agustin Mendez",
    author_email="me@matagus.com.ar",

    packages=find_packages(),
    package_dir={"lastfmauth": "lastfmauth"},

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Topic :: Internet :: WWW/HTTP"
    ],
    zip_safe=False,
)
