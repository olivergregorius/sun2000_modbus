from sun2000_modbus.datatypes import decode, DataType

import unittest


class TestDataTypes(unittest.TestCase):
    def test_decode_string(self):
        value = b'SUN2000-10KTL-M1\x00\x00\x00\x00SUN2000-12'
        decoded = decode(value, DataType.STRING)
        self.assertEqual(decoded, 'SUN2000-10KTL-M1\x00\x00\x00\x00SUN2000-12')

    def test_decode_uint16_be(self):
        value = b'\x04\xD2'
        decoded = decode(value, DataType.UINT16_BE)
        self.assertEqual(decoded, 1234)

    def test_decode_uint32_be(self):
        value = b'\x07\x5B\xCD\x15'
        decoded = decode(value, DataType.UINT32_BE)
        self.assertEqual(decoded, 123456789)

    def test_decode_int16_be(self):
        value = b'\xfb\x2e'
        decoded = decode(value, DataType.INT16_BE)
        self.assertEqual(decoded, -1234)

    def test_decode_int32_be(self):
        value = b'\xf8\xa4\x32\xeb'
        decoded = decode(value, DataType.INT32_BE)
        self.assertEqual(decoded, -123456789)

    def test_decode_bitfield16(self):
        value = b'\x3e\x22'
        decoded = decode(value, DataType.BITFIELD16)
        self.assertEqual(decoded, '0011111000100010')

    def test_decode_bitfield32(self):
        value = b'\x3e\x22\xaf\x45'
        decoded = decode(value, DataType.BITFIELD16)
        self.assertEqual(decoded, '00111110001000101010111101000101')

    def test_decode_multidata(self):
        value = b'\x3e\x22\xaf\x45'
        decoded = decode(value, DataType.MULTIDATA)
        self.assertEqual(decoded, b'\x3e\x22\xaf\x45')

    def test_decode_invalid(self):
        value = b'\x3e'
        self.assertRaises(ValueError, decode, value, 'invalid')
