# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dj-libcloud
------------

Tests for `dj-libcloud` models module.
"""

import os
import shutil
import unittest
from django.core.files.storage import get_storage_class
from django.conf import settings
from djlibcloud.storage import LibCloudStorage


class TestDjlibcloud(unittest.TestCase):

    storage_class = LibCloudStorage

    def setUp(self):
        pass

    def test_get_filesystem_storage(self):
        """
        get_storage_class returns the class for a storage backend name/path.
        """
        self.assertEqual(
            get_storage_class('djlibcloud.storage.LibCloudStorage'),
            LibCloudStorage)
        self.assertEqual(settings.DEFAULT_LIBCLOUD_PROVIDER, 'local')

    @unittest.expectedFailure
    def test_improperly_configured(self):
        storage = self.storage_class()

