from sun2000_modbus.datatypes import decode, DataType

import unittest


class TestDataTypes(unittest.TestCase):
    def test_decode_string(self):
        resp = b'SUN2000-10KTL-M1\x00\x00\x00\x00SUN2000-12'
        dec = decode(resp, DataType.STRING)
        self.assertEqual(dec, "SUN2000-10KTL-M1\x00\x00\x00\x00SUN2000-12")
