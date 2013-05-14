import string


__all__ = ["base32"]


class Base32Crockford:
    SYMBOLS = "0123456789ABCDEFGHJKMNPQRSTVWXYZ*~$=U"
    ENCODE_SYMBOLS = {i: ch for (i, ch) in enumerate(SYMBOLS)}

    NORMALIZE = string.maketrans("IiLlOo", "111100")

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

    def decode(self, symbol_string, checksum=False):
        """
        """
        pass

    def normalize(self, symbol_string):
        """
        """
        return symbol_string.translate(self.NORMALIZE, '-').upper()


base32 = Base32Crockford()
