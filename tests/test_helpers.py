# !/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from djlibcloud.storage import parse_date


class TestHelpers(unittest.TestCase):

    def test_parse_date(self):
        assert parse_date('Sun, 06 Nov 1994 08:49:37 GMT    ') == datetime(1994, 11, 6, 8, 49, 37)
        assert parse_date('Sunday, 06-Nov-94 08:49:37 GMT') == datetime(1994, 11, 6, 8, 49, 37)
        assert parse_date(' Sun Nov  6 08:49:37 1994') == datetime(1994, 11, 6, 8, 49, 37)
        assert parse_date('foo') is None

    def test_parse_date_overflows(self):
        assert parse_date(' Sun 02 Feb 1343 08:49:37 GMT') == datetime(1343, 2, 2, 8, 49, 37)
        assert parse_date('Thu, 01 Jan 1970 00:00:00 GMT') == datetime(1970, 1, 1, 0, 0)
        assert parse_date('Thu, 33 Jan 1970 00:00:00 GMT') is None