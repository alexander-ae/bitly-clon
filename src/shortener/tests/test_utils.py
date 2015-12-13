from shortener.utils import encode_to_alphabet, decode_from_alphabet


def test_encode_decode_to_alphabet():
    assert decode_from_alphabet(encode_to_alphabet(1)) == 1
    assert decode_from_alphabet(encode_to_alphabet(4096)) == 4096
    assert decode_from_alphabet(encode_to_alphabet(4096**2)) == 4096**2
