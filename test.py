#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import base32_crockford as b32


class EncodeTests(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(b32.encode(1234), '16J')

    def test_encode_checksum(self):
        self.assertEqual(b32.encode(1234, checksum=True), '16JD')

    def test_encode_zero_checksum(self):
        self.assertEqual(b32.encode(0, checksum=True), '00')

    def test_encode_negative(self):
        self.assertRaises(ValueError, b32.encode, -1)

    def test_encode_float(self):
        self.assertEqual(b32.encode(4.2), '4')

    def test_encode_split(self):
        self.assertEqual(b32.encode(123456, split=2), '3R-J0')
        self.assertEqual(b32.encode(123456, split=3), '3RJ-0')


class DecodeTests(unittest.TestCase):
    def test_decode(self):
        self.assertEqual(b32.decode('16J'), 1234)

    def test_decode_unicode(self):
        self.assertEqual(b32.decode(u'16J'), 1234)

    def test_decode_checksum(self):
        self.assertEqual(b32.decode('16JD', checksum=True), 1234)

    def test_decode_bad_checksum(self):
        self.assertRaises(ValueError, b32.decode, '16JE', checksum=True)

    def test_decode_strict(self):
        self.assertRaises(ValueError, b32.decode, '16j', strict=True)
        self.assertEqual(b32.decode('16J', strict=True), 1234)

    def test_decode_invalid(self):
        self.assertRaises(ValueError, b32.decode, 'u')
        self.assertRaises(ValueError, b32.decode, '!')


class NormalizeTests(unittest.TestCase):
    def test_normalize(self):
        self.assertEqual(b32.normalize('ix-Lb-Ko'), '1X1BK0')

    def test_normalize_strict(self):
        self.assertRaises(ValueError, b32.normalize, 'ix-Lb-Ko', strict=True)
        self.assertEqual(b32.normalize('1X1BK0', strict=True), '1X1BK0')

    def test_normalize_invalid_unicode(self):
        self.assertRaises(ValueError, b32.normalize, u'ä')

    def test_normalize_invalid_type(self):
        self.assertRaises(TypeError, b32.normalize, 1234)
        self.assertRaises(TypeError, b32.normalize, ['16J'])


if __name__ == '__main__':
    unittest.main()
