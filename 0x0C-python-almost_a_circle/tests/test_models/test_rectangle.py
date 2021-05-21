#!/usr/bin/python3
"""Test of Rectangle Class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Rect_Inst(unittest.TestCase):
    """Test Rect Inst"""
    def test_rect_parent(self):
        """Test for Rect as Base"""
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_rect_basic(self):
        """Basic test of rectangle class"""
        rect_1 = Rectangle(1, 2)
        rect_2 = Rectangle(2, 1)
        self.assertEqual(rect_1.id, rect_2.id - 1)
