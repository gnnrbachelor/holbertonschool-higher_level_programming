#!/usr/bin/python3
"""Writes string to text file"""


def write_file(filename="", text=""):
    """Writes string to file"""
    with open(filename, "w", encoding="utf=8") as f:
        return f.write(text)
