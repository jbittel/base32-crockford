base32-crockford
================

A Python module implementing the alternate base32 encoding as described
by Douglas Crockford at: http://www.crockford.com/wrmg/base32.html.

He designed the encoding to:

   * Be human and machine readable
   * Be compact
   * Be error resistant
   * Be pronounceable

It uses a symbol set of 10 digits and 22 letters, excluding I, L O and
U. Decoding is not case sensitive, and 'i' and 'l' are converted to '1'
and 'o' is converted to '0'. Encoding uses only upper-case characters.

Hyphens may be present in symbol strings to improve readability, and
are removed when decoding.

A check symbol can be appended to a symbol string to detect errors
within the string.

Installation
------------

To install, simply run::

   pip install base32-crockford

Usage
-----

Basic usage example::

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

Encode
~~~~~~

::

   base32_crockford.encode(n[, checksum=False[, split=0]])

Encode an integer into a symbol string.

When ``True``, optional ``checksum`` causes a check symbol to be
calculated and appended to the string. This can help detect errors
when decoding.

When specified, optional ``split`` causes the output string to be
divided into clusters of that size separated by hyphens.

Decode
~~~~~~

::

   base32_crockford.decode(s[, checksum=False[, strict=False]])

Decode an encoded symbol string.

Optional ``checksum`` can be provided as a counterpart to the same
argument when encoding. When ``True``, the trailing check symbol is
stripped off and validated. If the check symbol validation fails, a
``ValueError`` is raised.

When ``True``, optional ``strict`` causes a ``ValueError`` to be
raised if the symbol string requires normalization.

Normalize
~~~~~~~~~

::

   base32_crockford.normalize(s[, strict=False])

Normalize an encoded symbol string by applying these transformations:

   #. Remove hyphens
   #. Replace 'I' and 'L' with '1'
   #. Replace 'O' with '0'
   #. Convert all characters to uppercase

Ordinarily this function is automatically used when decoding, but
can be utilized independently to clean or validate a symbol string.
Invalid characters within the normalized string causes a
``ValueError`` to be raised.

When ``True``, optional ``strict`` causes a ``ValueError`` to be
raised if the symbol string requires normalization.

Changelog
---------

Version 0.2.0

   * Add optional split parameter when encoding

Version 0.1.0

   * Initial release
