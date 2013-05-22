#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import base32_crockford


class Base32CrockfordTests(unittest.TestCase):

    def test_encode(self):
        self.assertEqual(base32_crockford.encode(1234), '16J')

    def test_encode_checksum(self):
        self.assertEqual(base32_crockford.encode(1234, checksum=True), '16JD')

    def test_encode_zero_checksum(self):
        self.assertEqual(base32_crockford.encode(0, checksum=True), '00')

    def test_encode_negative(self):
        self.assertRaises(ValueError, base32_crockford.encode, -1)

    def test_encode_float(self):
        self.assertEqual(base32_crockford.encode(4.2), '4')

    def test_decode(self):
        self.assertEqual(base32_crockford.decode('16J'), 1234)

    def test_decode_unicode(self):
        self.assertEqual(base32_crockford.decode(u'16J'), 1234)

    def test_decode_checksum(self):
        self.assertEqual(base32_crockford.decode('16JD', checksum=True), 1234)

    def test_decode_bad_checksum(self):
        self.assertRaises(ValueError, base32_crockford.decode, '16JE', checksum=True)

    def test_decode_strict(self):
        self.assertRaises(ValueError, base32_crockford.decode, '16j', strict=True)

    def test_decode_invalid(self):
        self.assertRaises(ValueError, base32_crockford.decode, 'u')
        self.assertRaises(ValueError, base32_crockford.decode, '!')

    def test_normalize(self):
        self.assertEqual(base32_crockford.normalize('ix-Lb-Ko'), '1X1BK0')

    def test_normalize_strict(self):
        self.assertRaises(ValueError, base32_crockford.normalize, 'ix-Lb-Ko', strict=True)

    def test_normalize_invalid_unicode(self):
        self.assertRaises(ValueError, base32_crockford.normalize, u'ä')

    def test_normalize_invalid_type(self):
        self.assertRaises(TypeError, base32_crockford.normalize, ['16J'])

if __name__ == '__main__':
    unittest.main()
