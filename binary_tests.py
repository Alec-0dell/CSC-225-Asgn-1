# Tests operations on binary numbers.
# CSC 225, Assignment 1
# Given tests, Winter '23

import unittest
import binary as bn


class TestBinary(unittest.TestCase):
    def test01_add(self):
        msg = "Testing basic binary addition"
        self.assertEqual(bn.add("00000011", "00000010"), "00000101", msg)
        self.assertEqual(bn.add("01010101", "11001100"), "00100001", msg)
        self.assertEqual(bn.add("00000000", "00000000"), "00000000", msg)
        self.assertEqual(bn.add("00000000", "11001100"), "11001100", msg)
        self.assertEqual(bn.add("11110000", "00001111"), "11111111", msg)
        self.assertEqual(bn.add("10101010", "10101010"), "01010100", msg)
        self.assertEqual(bn.add("11001100", "00000011"), "11001111", msg)
        self.assertEqual(bn.add("11011010", "10101010"), "10000100", msg)
        self.assertEqual(bn.add("11111111", "11111111"), "11111110", msg)

        

    def test02_negate(self):
        msg = "Testing basic binary negation"
        self.assertEqual(bn.negate("00000001"), "11111111", msg)
        self.assertEqual(bn.negate("11111111"), "00000001", msg)
        self.assertEqual(bn.negate("00000000"), "00000000", msg)
        self.assertEqual(bn.negate("10101010"), "01010110", msg)
        self.assertEqual(bn.negate("11110000"), "00010000", msg)

    def test03_subtract(self):
        msg = "Testing basic binary subtraction"
        self.assertEqual(bn.subtract("00000011", "00000010"), "00000001", msg)
        self.assertEqual(bn.subtract("00000101" ,"00000011"), "00000010" , msg)
        self.assertEqual(bn.subtract("00100001" ,"01010101"), "11001100" , msg)
        self.assertEqual(bn.subtract("00000000" ,"00000000"), "00000000" , msg)
        self.assertEqual(bn.subtract("11001100" ,"00000000"), "11001100" , msg)
        self.assertEqual(bn.subtract("11111111" ,"11110000"), "00001111" , msg)
        self.assertEqual(bn.subtract("01010100" ,"10101010"), "10101010" , msg)
        self.assertEqual(bn.subtract("11001111" ,"11001100"), "00000011" , msg)
        self.assertEqual(bn.subtract("10000100" ,"11011010"), "10101010" , msg)
        self.assertEqual(bn.subtract("11111110" ,"11111111"), "11111111" , msg)

    def test04_binary_to_decimal(self):
        msg = "Testing basic binary-to-decimal conversion"
        self.assertEqual(bn.binary_to_decimal("00000000"), 0, msg)
        self.assertEqual(bn.binary_to_decimal("00000001"), 1, msg)
        self.assertEqual(bn.binary_to_decimal("11111111"), -1, msg)
        self.assertEqual(bn.binary_to_decimal("00000010"), 2, msg)
        self.assertEqual(bn.binary_to_decimal("11111110"), -2, msg)
        self.assertEqual(bn.binary_to_decimal("10000010"), -126, msg)
        self.assertEqual(bn.binary_to_decimal("10000001"), -127, msg)
        self.assertEqual(bn.binary_to_decimal("10000000"), -128, msg)
        self.assertEqual(bn.binary_to_decimal("01111101"), 125, msg)
        self.assertEqual(bn.binary_to_decimal("01111110"), 126, msg)
        self.assertEqual(bn.binary_to_decimal("01111111"), 127, msg)
        

    def test05_decimal_to_binary(self):
        msg = "Testing basic decimal-to-binary conversion"
        self.assertEqual(bn.decimal_to_binary(5), "00000101", msg)
        self.assertEqual(bn.decimal_to_binary(0),"00000000", msg)
        self.assertEqual(bn.decimal_to_binary(1),"00000001", msg)
        self.assertEqual(bn.decimal_to_binary(-1),"11111111",msg)
        self.assertEqual(bn.decimal_to_binary(2),"00000010", msg)
        self.assertEqual(bn.decimal_to_binary(-2),"11111110", msg)
        self.assertEqual(bn.decimal_to_binary(-126),"10000010", msg)
        self.assertEqual(bn.decimal_to_binary(-127),"10000001", msg)
        self.assertEqual(bn.decimal_to_binary(-128),"10000000", msg)
        self.assertEqual(bn.decimal_to_binary(125),"01111101", msg)
        self.assertEqual(bn.decimal_to_binary(126),"01111110", msg)
        self.assertEqual(bn.decimal_to_binary(127),"01111111", msg)
        
    def test06_flip(self):
        msg = "Testing basic flipping of binary digits"
        self.assertEqual(bn.flip("11111111"), "00000000", msg)
        self.assertEqual(bn.flip("00000000"), "11111111", msg)
        self.assertEqual(bn.flip("10101010"), "01010101", msg)
        self.assertEqual(bn.flip("11110000"), "00001111", msg)




if __name__ == "__main__":
    unittest.main()
