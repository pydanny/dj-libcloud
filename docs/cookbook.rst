========
Cookbook
========

Using eu-west-1
-----------------

.. code-block:: python

    LIBCLOUD_PROVIDERS = {
        'amazon_s3_eu_west': {
            'type': 'libcloud.storage.types.Provider.S3_EU_WEST',
            'user': os.environ.get('AWS_ACCESS_KEY'),
            'key': os.environ.get('AWS_SECRET_KEY'),
            'bucket': 'my-assets-cdn',
            'secure': True,
        }
    }

    DEFAULT_LIBCLOUD_PROVIDER = 'amazon_s3_eu_west'

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
    