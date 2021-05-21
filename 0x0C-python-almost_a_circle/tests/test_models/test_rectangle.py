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
