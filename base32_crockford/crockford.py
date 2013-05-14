import string


__all__ = ["base32"]


class Base32Crockford:
    SYMBOLS = "0123456789ABCDEFGHJKMNPQRSTVWXYZ*~$=U"
    ENCODE_SYMBOLS = {i: ch for (i, ch) in enumerate(SYMBOLS)}
    DECODE_SYMBOLS = {ch: i for (i, ch) in enumerate(SYMBOLS)}
    NORMALIZE_SYMBOLS = string.maketrans("IiLlOo", "111100")

    def encode(self, number, checksum=False):
        """
        """
        if number == 0:
            return '0'

        check_digit = ''
        if checksum:
            check_digit = self.ENCODE_SYMBOLS[number % 37]

        symbol_string = ''
        while number > 0:
            remainder = number % 32
            number /= 32
            symbol_string = self.ENCODE_SYMBOLS[remainder] + symbol_string

        return symbol_string + check_digit

    def decode(self, symbol_string, checksum=False, strict=False):
        """
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
        """
        string = symbol_string.translate(self.NORMALIZE_SYMBOLS, '-').upper()

        if strict and string != symbol_string:
            raise ValueError("Normalization required for string")

        return string


base32 = Base32Crockford()
