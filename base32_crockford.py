"""
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

"""

import string


__all__ = ["encode", "decode", "normalize"]


# The encoded symbol space does not include I, L, O or U;
# the last five symbols are exclusively for checksum values
SYMBOLS = "0123456789ABCDEFGHJKMNPQRSTVWXYZ*~$=U"
ENCODE_SYMBOLS = {i: ch for (i, ch) in enumerate(SYMBOLS)}
DECODE_SYMBOLS = {ch: i for (i, ch) in enumerate(SYMBOLS)}
NORMALIZE_SYMBOLS = string.maketrans("IiLlOo", "111100")

BASE = 32
CHECK_BASE = 37


def encode(number, checksum=False):
    """
    Encodes a base 10 positive integer into a symbol string.

    Raises a ValueError on invalid input.

    If checksum is set to True, a check symbol will also be
    calculated and appended to the string.
    """
    number = int(number)
    if number < 0:
        raise ValueError("Number '%d' is not a positive integer" % number)

    check_symbol = ''
    if checksum:
        check_symbol = ENCODE_SYMBOLS[number % CHECK_BASE]

    if number == 0:
        return '0' + check_symbol

    symbol_string = ''
    while number > 0:
        remainder = number % BASE
        number //= BASE
        symbol_string = ENCODE_SYMBOLS[remainder] + symbol_string

    return symbol_string + check_symbol


def decode(symbol_string, checksum=False, strict=False):
    """
    Decodes a given symbol string into a base 10 number.

    Raises a ValueError on invalid input.

    If checksum is set to True, the string is assumed to have a
    trailing check symbol which will be validated. If the
    checksum validation fails, a ValueError is raised.

    If strict is set to True, a ValueError is raised if the
    normalization step requires changes to the string.
    """
    symbol_string = normalize(symbol_string, strict=strict)
    if checksum:
        symbol_string, check_symbol = symbol_string[:-1], symbol_string[-1]

    # The letter 'U' is only valid as a check symbol
    if 'U' in symbol_string:
        raise ValueError("String '%s' contains invalid characters" %
                         symbol_string)

    number = 0
    for symbol in symbol_string:
        number = number * BASE + DECODE_SYMBOLS[symbol]

    if checksum:
        check_value = DECODE_SYMBOLS[check_symbol]
        modulo = number % CHECK_BASE
        if check_value != modulo:
            raise ValueError("Invalid check symbol '%s' for string '%s'" %
                             (check_symbol, symbol_string))

    return number


def normalize(symbol_string, strict=False):
    """
    Normalizes a given symbol string to account for error
    resistance and prepare it for decoding. These transformations
    are applied:

       1. Hyphens are removed
       2. 'I', 'i', 'L' or 'l' are converted to '1'
       3. 'O' or 'o' are converted to '0'
       4. All characters are converted to uppercase

    If the strict parameter is set to True, a ValueError is raised
    if any of the above transformations are applied.
    """
    string = str(symbol_string).translate(NORMALIZE_SYMBOLS, '-').upper()

    if strict and string != symbol_string:
        raise ValueError("Normalization required for string '%s'" %
                         symbol_string)

    return string
