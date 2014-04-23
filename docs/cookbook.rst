========
Cookbook
========

With django-pipeline:

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
    