#!/usr/bin/python3
"""Module for reading from text file"""


def read_file(filename=""):
    f = open(filename, "r", encoding="utf-8")
    print(f.read(), end="")
