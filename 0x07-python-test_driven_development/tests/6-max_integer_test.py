#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests max_integer function"""

    def test_mod_docstring(self):
        """Tests mod docstring"""
        mod = __import__('6-max_integer').__doc__
        self.assertTrue(len(mod) > 1)

    def test_func_docstring(self):
        """Test func docstring"""
        func = max_integer.__doc__
        self.assertTrue(len(func) > 1)

    def test_none_passed(self):
        """Test for none passed"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_empty_list(self):
        """Test for empty List"""
        self.assertIsNone(max_integer([]))

    def test_no_arguments(self):
        """Test for no arguments"""
        self.assertIsNone(max_integer())

    def test_char_passed(self):
        """Test for char passed"""
        with self.assertRaises(TypeError):
            max_integer([2, 5, 6, "t", 7])

    def test_one_argument(self):
        """Test one element"""
        self.assertEqual(max_integer([3]), 3)

    def test_positive(self):
        """Test for normal positive no"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_positive_negative(self):
        """Test positive and negative values"""
        self.assertEqual(max_integer([-20, 5, 6, -2, 14]), 14)

    def test_negative_only(self):
        """Test negative values"""
        self.assertEqual(max_integer([-200, -2, -3, -40, -120]), -2)

    def test_multiple_max_values(self):
        """Test multiple same max values"""
        self.assertEqual(max_integer([1, 7, 54, 2, 54]), 54)

    def test_same(self):
        """Test all same values"""
        self.assertEqual(max_integer([15, 15, 15, 15, 15]), 15)


