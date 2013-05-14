import string


__all__ = ["base32"]


class Base32Crockford:
    SYMBOLS = "0123456789ABCDEFGHJKMNPQRSTVWXYZ*~$=U"
    ENCODE_SYMBOLS = {i: ch for (i, ch) in enumerate(SYMBOLS)}
    DECODE_SYMBOLS = {ch: i for (i, ch) in enumerate(SYMBOLS)}
    NORMALIZE_SYMBOLS = string.maketrans("IiLlOo", "111100")

    def encode(self, number, checksum=False):
        """
        Encodes a base 10 number into a symbol string.

        If checksum is set to True, a checksum digit will also be
        calculated and appended to the string.
        """
        check_digit = ''
        if checksum:
            check_digit = self.ENCODE_SYMBOLS[number % 37]

        if number == 0:
            return '0' + check_digit

        symbol_string = ''
        while number > 0:
            remainder = number % 32
            number /= 32
            symbol_string = self.ENCODE_SYMBOLS[remainder] + symbol_string

        return symbol_string + check_digit

    def decode(self, symbol_string, checksum=False, strict=False):
        """
        Decodes a given symbol string into a base 10 number.

        If checksum is set to True, the string is assumed to have a
        trailing checksum digit which will be validated. If the
        checksum validation fails, a ValueError is raised.

        If strict is set to True, a ValueError is raised if the
        normalization step requires changes to the string.
        """
        symbol_string = self.normalize(symbol_string, strict=strict)
        if checksum:
            symbol_string, check_digit = symbol_string[:-1], symbol_string[-1]

        number = 0
        for char in symbol_string:
            number = number * 32 + self.DECODE_SYMBOLS[char]

        if checksum:
            check_value = self.DECODE_SYMBOLS[check_digit]
            modulo = number % 37
            if check_value != modulo:
                raise ValueError("Invalid checksum digit")

        return number

    def normalize(self, symbol_string, strict=False):
        """
        Normalizes a given symbol string to account for error
        resistance and prepare it for decoding. These transformations
        are applied:

           1. Hyphens are removed
           2. 'I' or 'i' are converted to '1'
           3. 'O' or 'o' are converted to '0'
           4. All characters are converted to uppercase

        If the strict parameter is set to True, a ValueError is raised
        if any of the above transformations are applied.
        """
        string = symbol_string.translate(self.NORMALIZE_SYMBOLS, '-').upper()

        if strict and string != symbol_string:
            raise ValueError("Normalization required for string")

        return string


base32 = Base32Crockford()
