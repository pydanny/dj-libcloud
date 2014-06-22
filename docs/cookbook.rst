========
Cookbook
========

Amazon
------

Using eu-west-1
^^^^^^^^^^^^^^^

.. code-block:: python

    STATIC_URL = 'https://s3-eu-west-1.amazonaws.com/my-assets/'
    STATICFILES_STORAGE = 'djlibcloud.storage.LibCloudStorage'

    LIBCLOUD_PROVIDERS = {
        'amazon_s3_eu_west': {
            'type': 'libcloud.storage.types.Provider.S3_EU_WEST',
            'user': os.environ.get('AWS_ACCESS_KEY'),
            'key': os.environ.get('AWS_SECRET_KEY'),
            'bucket': 'my-assets',
            'secure': True,
        },
    }

    DEFAULT_LIBCLOUD_PROVIDER = 'amazon_s3_eu_west'

Google Cloud Storage
--------------------

.. code-block:: python

    STATIC_URL = 'https://storage.googleapis.com/my-assets/'
    STATICFILES_STORAGE = 'djlibcloud.storage.LibCloudStorage'

    LIBCLOUD_PROVIDERS = {
        'google_cloud_storage': {
            'type': 'libcloud.storage.types.Provider.GOOGLE_STORAGE',
            'user': os.environ.get('GOOGLE_ACCESS_KEY'),
            'key': os.environ.get('GOOGLE_SECRET_KEY'),
            'bucket': 'my-assets',
            'secure': True,
        },
    }

    DEFAULT_LIBCLOUD_PROVIDER = 'google_cloud_storage'

Rackspace Cloudfiles
--------------------

.. code-block:: python

    STATIC_URL = 'https://<long>-<hash>.ssl.cf5.rackcdn.com'
    STATICFILES_STORAGE = 'djlibcloud.storage.LibCloudStorage'

    LIBCLOUD_PROVIDERS = {
        'rackspace_cloudfiles': {
            'type': 'libcloud.storage.types.Provider.CLOUDFILES',
            'user': os.environ.get('RACKSPACE_USER_NAME'),
            'key': os.environ.get('RACKSPACE_API_KEY'),
            'bucket': 'my-assets',
            'secure': True,
        },
    }

    DEFAULT_LIBCLOUD_PROVIDER = 'rackspace_cloudfiles'

Microsoft Azure
---------------

.. code-block:: python

    AZURE_ACCOUNT_NAME = os.environ.get('AZURE_ACCOUNT_NAME')
    STATIC_URL = 'https://%s.blob.core.windows.net/my-assets/' % AZURE_ACCOUNT_NAME
    STATICFILES_STORAGE = 'djlibcloud.storage.LibCloudStorage'

    LIBCLOUD_PROVIDERS = {
        'microsoft_azure': {
            'type': 'libcloud.storage.types.Provider.AZURE_BLOBS',
            'user': AZURE_ACCOUNT_NAME,
            'key': os.environ.get('AZURE_ACCOUNT_KEY'),
            'bucket': 'my-assets',
            'secure': True,
        },
    }

    DEFAULT_LIBCLOUD_PROVIDER = 'microsoft_azure'


Using django-pipeline
----------------------

.. code-block:: python

    # core/storage.py

    from djlibcloud.storage import LibCloudStorage
    from pipeline.storage import PipelineMixin

    class PipelineCloudStorage(PipelineMixin,
                               LibCloudStorage):
        """ UNTESTED! """
        pass


.. code-block:: python

    # settings.py
    STATICFILES_STORAGE = 'core.storage.PipelineCloudStorage'
