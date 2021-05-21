#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""
    def test_empty_list(self):
        """Test empty list []"""
        empty = []
        self.assertIsNone(max_integer(empty))

    def test_no_args(self):
        """Test default argument"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Test only one number in the list"""
        only = [7]
        self.assertEqual(max_integer(only), 7)

    def test_positive_end(self):
        """Tests all positive with max at end"""
        e = [2, 15, 3, 36, 12, 71]
        self.assertEqual(max_integer(e), 71)

    def test_positive_middle(self):
        """Tests all positive with max in middle"""
        m = [1, 57, 18, 71, 14, 33]
        self.assertEqual(max_integer(m), 71)

    def test_positive_beginning(self):
        """Tests all positive with max at beginning"""
        b = [71, 1, 18, 6, 4, 40]
        self.assertEqual(max_integer(b), 71)

    def test_one_negative(self):
        """Tests list with one negative number"""
        on = [71, 1, 5, -36, 14, 74]
        self.assertEqual(max_integer(on), 74)

    def test_all_negative(self):
        """Tests list with all negative numbers"""
        neg = [-64, -80, -7, -51, -71]
        self.assertEqual(max_integer(neg), -7)

    def test_all_floats(self):
        """Test list with all floats"""
        fl = [1.5, 2.5, 3.5, 2.1]
        self.assertEqual(max_integer(fl), 3.5)

    def test_all_string(self):
        """Test list all strings"""
        st = ["Alex", "Rivera", "Holberton"]
        self.assertEqual(max_integer(st), "Rivera")

    def test_none(self):
        """Tests none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_comb_arg(self):
        """Tests combination of types in list"""
        liststr = [7, "Alex", 71, 1, 11]
        with self.assertRaises(TypeError):
            max_integer(liststr)

if __name__ == "__main__":
    unittest.main()
