#!/usr/bin/python3
"""Module for reading from text file"""


def read_file(filename=""):
    """Reads from text file"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
