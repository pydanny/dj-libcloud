.. :changelog:

History
-------

0.2.0(2014-06-23)
++++++++++++++++++

* Updated url method to return correct values for Rackspace Cloudfiles, Microsoft Azure, Google Storage, non-US Amazon SV (Thanks Jannis!)
* Improved the cookbook immensely (Thanks Jannis!)
* Add link from README to cookbook
* Fix ``url`` method for Google Storage, Rackspace Cloudfiles and
  Microsoft Azure. Also return the correct value for non-US Amazon S3
  buckets.

0.1.2 (2014-04-24)
++++++++++++++++++

* Confirmed to work with Python 2.7
* Remove django-pipeline specific code from storages
* Add cookbook to docs that includes django-pipeline

0.1.1 (2014-04-21)
++++++++++++++++++

* Fixed second-time run problem by just using LibCloudStorage class
* Made django-pipeline optional
* Removed unnecessary files
* Moved TODO to issue tracker

0.1.0 (2014-04-21)
++++++++++++++++++

* First release on PyPI.
* Frustration over lack of easy media asset support for Django and Python 3.