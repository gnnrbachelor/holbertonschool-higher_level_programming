#!/usr/bin/python3
"""Module for square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Creates Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str() representation of square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
