=============================
dj-libcloud
=============================

.. image:: https://badge.fury.io/py/dj-libcloud.png
    :target: https://badge.fury.io/py/dj-libcloud

.. image:: https://travis-ci.org/pydanny/dj-libcloud.png?branch=master
    :target: https://travis-ci.org/pydanny/dj-libcloud

.. image:: https://coveralls.io/repos/pydanny/dj-libcloud/badge.png?branch=master
    :target: https://coveralls.io/r/pydanny/dj-libcloud?branch=master

Adds easy support for libcloud to Django. This allows for handling of media assets for Django and is designed to work easily with Python 3.3+ and Django 1.6+. In the works is support for Python 2.7.

Many thanks go to Jannis Leidel for giving me the code to get this running.

Documentation
-------------

The full documentation is at https://dj-libcloud.readthedocs.org.

Quickstart for Mac OS X
------------------------

Other quickstarts will happen. Just working on Mac OS X for now.

Get curl-ca-bundle::

    brew install curl-ca-bundle
    export SSL_CERT_FILE=/usr/local/opt/curl-ca-bundle/share/ca-bundle.crt

Install dj-libcloud::

    pip install dj-libcloud

Then use it in a project::

    # settings.py

    STATIC_URL = 'https://my-assets.cdn/static/'
    MEDIA_URL = 'https://my-assets.cdn/media/'
    STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
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

* TODO