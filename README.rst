=============================
dj-libcloud
=============================

.. image:: https://badge.fury.io/py/dj-libcloud.png
    :target: https://badge.fury.io/py/dj-libcloud

Adds easy python 3 and 2.7 support to Django for management of static assets. This is a wrapper around the excellent `Apache Libcloud`_ library.

.. _`Apache Libcloud`: https://libcloud.apache.org/

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

Then use it in a project, e.g. for your static files::

    # settings.py

    STATIC_URL = 'https://s3.amazonaws.com/my-assets/'
    STATICFILES_STORAGE = 'djlibcloud.storage.LibCloudStorage'

    LIBCLOUD_PROVIDERS = {
        'default': {
            'type': 'libcloud.storage.types.Provider.S3',
            'user': os.environ.get('AWS_ACCESS_KEY'),
            'key': os.environ.get('AWS_SECRET_KEY'),
            'bucket': 'my-assets',
            'secure': True,
        },
    }

Other LibCloud Providers
------------------------

If you want to use other libcloud providers (Rackspace, Openstack, other AWS centers, et al), please visit:

* The `libcloud list of supported providers`_
* The `dj-libcloud cookbook`_.

.. _`libcloud list of supported providers`: https://libcloud.readthedocs.org/en/latest/storage/supported_providers.html
.. _`dj-libcloud cookbook`: http://dj-libcloud.readthedocs.org/en/latest/cookbook.html

Features
--------

* Works for uploading media assets using Python 3.3 and Django 1.6.
* In theory supports all the backends that libcloud supports.

FAQ
-----

Because you just had to ask.

Why not use dj-static or whitenoise?
++++++++++++++++++++++++++++++++++++++++++++++++++++++

Those are great libraries, but are not what you want when handling user uploaded media.

Why not just update django-storages?
++++++++++++++++++++++++++++++++++++++++++++++++++++++

`libcloud` is awesome and has a dedicated team devoted to it. We can have it do most of the heavy lifting. On the other hand, converting `django-storages` to work with Python 3 looked like too much work. Sometimes you just have to start anew, right?

What storage providers does dj-libcloud support?
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

dj-libcloud is a wrapper around libcloud, meaning it supports all the providers of that library. Check out the `full list of supported providers`_!

.. _`full list of supported providers`: https://libcloud.readthedocs.org/en/latest/storage/supported_providers.html



How can I contribute?
++++++++++++++++++++++++++++++++++++

Please read http://dj-libcloud.readthedocs.org/en/latest/contributing.html

What about compressors like django-pipeline?
++++++++++++++++++++++++++++++++++++++++++++++++++++++

Working on it. Currently the `PipelineCachedCloudStorage` class breaks the second time you run it. See https://github.com/pydanny/dj-libcloud/issues/7

CREDIT
------

Many thanks to Jannis Leidel (@jezdez) for giving me the code to get this started. He's a Django core developer, the master of Django static asset managment, and overall a great great guy.
