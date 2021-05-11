#!/usr/bin/python3
"""MyInt class"""


class MyInt(int):
    """Invert __eq__ and __ne__"""
    def __eq__(self, other):
        """inverts __eq__"""
        return (not super().__eq__(other))

    def __ne__(self, other):
        """Inverts __ne__"""
        return (not super().__ne__(other))
