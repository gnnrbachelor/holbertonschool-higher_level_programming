#!/usr/bin/python3
"""Module for appending string to end of file"""


def append_write(filename="", text=""):
    """Appends text to file"""
    with open(filename, "a", encoding="utf=8") as f:
        return f.write(text)
