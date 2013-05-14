#!/usr/bin/env python

import unittest

from base32_crockford import base32


class Base32CrockfordTests(unittest.TestCase):

    def test_encode(self):
        self.assertEqual(base32.encode(1234), '16J')

    def test_encode_checksum(self):
        self.assertEqual(base32.encode(1234, checksum=True), '16JD')

    def test_encode_zero_checksum(self):
        self.assertEqual(base32.encode(0, checksum=True), '00')

    def test_decode(self):
        self.assertEqual(base32.decode('16J'), 1234)

    def test_decode_checksum(self):
        self.assertEqual(base32.decode('16JD', checksum=True), 1234)

    def test_decode_bad_checksum(self):
        self.assertRaises(ValueError, base32.decode, '16JE', checksum=True)

    def test_decode_strict(self):
        self.assertRaises(ValueError, base32.decode, '16j', strict=True)

    def test_normalize(self):
        self.assertEqual(base32.normalize('ix-Lb-Ko'), '1X1BK0')

    def test_normalize_strict(self):
        self.assertRaises(ValueError, base32.normalize, 'ix-Lb-Ko', strict=True)


if __name__ == '__main__':
    unittest.main()
