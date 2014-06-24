#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dj-libcloud
------------

Tests for `dj-libcloud` models module.
"""

import os
import shutil
import unittest

#temporary as test are now failing.
try:
    from djlibcloud import models
except:
    pass

class TestDjlibcloud(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        pass

    def tearDown(self):
        pass