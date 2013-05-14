#!/usr/bin/env python

import os
import unittest

from base32_crockford import base32


class Base32CrockfordTests(unittest.TestCase):

    def test_encode(self):
        assert base32.encode(1234) == '16J'

    def test_encode_checksum(self):
        assert base32.encode(1234, checksum=True) == '16JD'

    def test_normalize(self):
        assert base32.normalize('ix-Lb-Ko') == '1X1BK0'

if __name__ == '__main__':
    unittest.main()
