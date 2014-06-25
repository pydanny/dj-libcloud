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

from djlibcloud.storage import parse_date


class TestHelpers(unittest.TestCase):

    def test_parse_date(self):

        date = parse_date("Sunday, 06-Nov-94 08:49:37 GMT")
        self.assertEqual(date.day, 6)
        self.assertEqual(date.month, 11)
        self.assertEqual(date.year, 1994)

        # second case <= 68
        date = parse_date("Sunday, 06-Nov-05 08:19:32 GMT")
        self.assertEqual(date.year, 2005)
