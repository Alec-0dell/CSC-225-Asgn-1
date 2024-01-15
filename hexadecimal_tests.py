# Tests operations on hexadecimal numbers.
# CSC 225, Assignment 1
# Given tests, Winter '23

import unittest
import hexadecimal as hx


class TestHexadecimal(unittest.TestCase):
    def test01_binary_to_hex(self):
        msg = "Testing basic binary-to-hex conversion"
        self.assertEqual(hx.binary_to_hex("0000010100011010"), "0x051A", msg)
        self.assertEqual(hx.binary_to_hex("0000000100100011"), "0x0123", msg)
        self.assertEqual(hx.binary_to_hex("0100010101100111"), "0x4567", msg)
        self.assertEqual(hx.binary_to_hex("1000100110101011"), "0x89AB", msg)
        self.assertEqual(hx.binary_to_hex("1100110111101111"), "0xCDEF", msg)

    def test02_hex_to_binary(self):
        msg = "Testing basic hex-to-binary conversion"
        self.assertEqual(hx.hex_to_binary("0x051A"), "0000010100011010", msg)
        self.assertEqual(hx.hex_to_binary("0x0123"), "0000000100100011", msg)
        self.assertEqual(hx.hex_to_binary("0x4567"), "0100010101100111", msg)
        self.assertEqual(hx.hex_to_binary("0x89AB"), "1000100110101011", msg)
        self.assertEqual(hx.hex_to_binary("0xCDEF"), "1100110111101111", msg)
        
    def test_3_char_to_bin(self):
        msg = "Testing a singular hex character to binary"
        self.assertEqual(hx.char_to_bin("0"), "0000", msg)
        self.assertEqual(hx.char_to_bin("1"), "0001")
        self.assertEqual(hx.char_to_bin("2"), "0010")
        self.assertEqual(hx.char_to_bin("3"), "0011")
        self.assertEqual(hx.char_to_bin("4"), "0100")
        self.assertEqual(hx.char_to_bin("5"), "0101")
        self.assertEqual(hx.char_to_bin("6"), "0110")
        self.assertEqual(hx.char_to_bin("7"), "0111")
        self.assertEqual(hx.char_to_bin("8"), "1000")
        self.assertEqual(hx.char_to_bin("9"), "1001")
        self.assertEqual(hx.char_to_bin("a"), "1010")
        self.assertEqual(hx.char_to_bin("B"), "1011")
        self.assertEqual(hx.char_to_bin("C"), "1100")
        self.assertEqual(hx.char_to_bin("D"), "1101")
        self.assertEqual(hx.char_to_bin("E"), "1110")
        self.assertEqual(hx.char_to_bin("F"), "1111")
        
    def test_4_bit_to_char(self):
        msg = "Testing a singular hex character to binary"
        self.assertEqual(hx.bit_to_char("0000"), "0", msg)
        self.assertEqual(hx.bit_to_char("0001"), "1")
        self.assertEqual(hx.bit_to_char("0010"), "2")
        self.assertEqual(hx.bit_to_char("0011"), "3")
        self.assertEqual(hx.bit_to_char("0100"), "4")
        self.assertEqual(hx.bit_to_char("0101"), "5")
        self.assertEqual(hx.bit_to_char("0110"), "6")
        self.assertEqual(hx.bit_to_char("0111"), "7")
        self.assertEqual(hx.bit_to_char("1000"), "8")
        self.assertEqual(hx.bit_to_char("1001"), "9")
        self.assertEqual(hx.bit_to_char("1010"), "A")
        self.assertEqual(hx.bit_to_char("1011"), "B")
        self.assertEqual(hx.bit_to_char("1100"), "C")
        self.assertEqual(hx.bit_to_char("1101"), "D")
        self.assertEqual(hx.bit_to_char("1110"), "E")
        self.assertEqual(hx.bit_to_char("1111"), "F")


if __name__ == "__main__":
    unittest.main()
