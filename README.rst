=============================
dj-libcloud
=============================

.. image:: https://badge.fury.io/py/dj-libcloud.png
    :target: https://badge.fury.io/py/dj-libcloud

.. image:: https://travis-ci.org/pydanny/dj-libcloud.png?branch=master
    :target: https://travis-ci.org/pydanny/dj-libcloud

.. image:: https://coveralls.io/repos/pydanny/dj-libcloud/badge.png?branch=master
    :target: https://coveralls.io/r/pydanny/dj-libcloud?branch=master

Adds easy support for libcloud to Django. This allows for handling of media assets for Django and is designed to work easily with Python 3.3+ and Python 2.7. The current target Django environment is 1.6.

Many thanks go to Jannis Leidel for giving me the code to get this running.

Documentation
-------------

The full documentation is at https://dj-libcloud.readthedocs.org.

Quickstart
----------

Install dj-libcloud::

    pip install dj-libcloud

Then use it in a project::

    # settings.py

    STATIC_URL = 'https://my-assets-cdn/static/'
    MEDIA_URL = 'https://my-assets-cdn/media/'
    STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
    LIBCLOUD_PROVIDERS = {
        'amazon_s3': {
            'type': 'libcloud.storage.types.Provider.S3',
            'user': os.environ.get('AWS_ACCESS_KEY'),
            'key': os.environ.get('AWS_SECRET_KEY'),
            'bucket': 'caniusepython3-assets',
            'secure': True,
        }
    }

    DEFAULT_LIBCLOUD_PROVIDER = 'amazon_s3'

Features
--------

* TODO