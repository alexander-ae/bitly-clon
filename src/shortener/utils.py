# -*- coding: utf-8 -*-
# utils.py

import string
import re
import math

ALPHABET_62 = string.digits + string.ascii_lowercase + string.ascii_uppercase
ALPHABET_58 = re.sub(r'[0OlI]', '', ALPHABET_62)  # removemos caracteres confusos


def encode_to_alphabet(num, alphabet=ALPHABET_58):
    """
    Codifica el número a base 58.

    Inspirado en el sistema que utiliza Flickr.
    """
    base = len(alphabet)
    digits = []

    while num >= 0:
        digits.append(num % base)
        num = math.floor(num / base)

        if num == 0:
            break

    chars = []

    while(len(digits)):
        chars.append(alphabet[int(digits.pop())])

    return ''.join(chars)


def decode_from_alphabet(str_encoded, alphabet=ALPHABET_58):
    """
    Decodifica el número de base 58 a base 10.
    """
    num = 0
    base = len(alphabet)
    index = 0
    while len(str_encoded):
        num = alphabet.index(str_encoded[-1]) * math.pow(base, index) + num
        str_encoded = str_encoded[:-1]
        index = index + 1

    return num
