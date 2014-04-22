=============================
dj-libcloud
=============================

.. image:: https://badge.fury.io/py/dj-libcloud.png
    :target: https://badge.fury.io/py/dj-libcloud

Adds easy support for libcloud to Django. This allows for handling of media assets for Django and is designed to work easily with Python 3.3+ and Django 1.6+. In the works is support for Python 2.7.

WARNING: This project is in an ALPHA state. The only testing done so far is me running `collectstatic` from my local machine and a Heroku app. That works for me, but please don't count on it working for you. Yet.  

Documentation
-------------

The full documentation is at https://dj-libcloud.readthedocs.org.


Quickstart
------------------------

Libcloud verifies server SSL certificates before it lets you do anything. It will search your system for the CA certificate, and if it doesn't find it then it will blow up. See https://libcloud.readthedocs.org/en/latest/other/ssl-certificate-validation.html

Installing CA certificate bundle on Mac OS X::

    # Assuming you are using homebrew for Mac OS X dependency management.
    $ brew install curl-ca-bundle

Install dj-libcloud::

    $ pip install dj-libcloud

Then use it in a project::

    # settings.py

    STATIC_URL = 'https://my-assets.cdn/static/'
    MEDIA_URL = 'https://my-assets.cdn/media/'
    STATICFILES_STORAGE = 'djlibcloud.storage.PipelineStorage'
    LIBCLOUD_PROVIDERS = {
        'amazon_s3': {
            'type': 'libcloud.storage.types.Provider.S3',  # TODO List all the type options
            'user': os.environ.get('AWS_ACCESS_KEY'),
            'key': os.environ.get('AWS_SECRET_KEY'),
            'bucket': 'my-assets-cdn',  # TODO Add better message if bucket not found
            'secure': True,
        }
    }

    DEFAULT_LIBCLOUD_PROVIDER = 'amazon_s3'

Features
--------

* Works for uploading media assets using Python 3.3 and Django 1.6.
* In theory supports all the backends that libcloud supports.
* Code borged from work of Jannis Leidel, Django core developer, the master of Django static asset managment, and a great guy.

TODO
-----

* Tests! OMG TESTS!!!
* More documentation.
* Backport to Python 2.7
* Add better error message if bucket not found
* Come up with more storage types so we aren't dependant on django-pipeline. Nothing wrong with pipeline, just want to provide more options.

CREDIT
------

Many thanks to Jannis Leidel for giving me the code to get this started.