base32-crockford
================

A Python module implementing the alternate base32 encoding as described
by Douglas Crockford at: http://www.crockford.com/wrmg/base32.html.

According to his description, the encoding is designed to:

   * Be human and machine readable
   * Be compact
   * Be error resistant
   * Be pronounceable

It uses a symbol set of 10 digits and 22 letters, excluding I, L O and
U. Decoding is not case sensitive, and 'i' and 'l' are converted to '1'
and 'o' is converted to '0'. Encoding uses only upper-case characters.

Hyphens can be present in symbol strings to improve readability, and
are removed when decoding.

A check symbol can be appended to a symbol string to detect errors
within the string.

Installation
------------

::

   pip install base32-crockford

Usage
-----

::

   >>> import base32_crockford
   >>> base32_crockford.encode(42)
   '1A'
   >>> base32_crockford.decode('1A')
   42
   >>> base32_crockford.encode(42, checksum=True)
   '1A5'
   >>> base32_crockford.decode('1A5', checksum=True)
   42
   >>> base32_crockford.normalize('La5')
   '1A5'
