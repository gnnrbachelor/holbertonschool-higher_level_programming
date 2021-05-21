#!/usr/bin/python3
"""Unitests for class base"""

import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle

class Test_Base_Inst(unittest.TestCase):
    """Test for Instance of Base Class"""

    def test_pep8(self):
        """Test for Pep8"""
        pep8style_guide = pep8.StyleGuide()
        result = pep8style_guide.check_files(["models/base.py",
                                              "models/rectangle.py"])
        self.assertEqual(result.total_errors, 0, 'PEP8 style errors: %d' % result.total_errors)

    def test_no_arguments(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)
