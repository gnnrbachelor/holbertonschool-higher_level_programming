#!/usr/bin/python3
"""Module for writing object to text file using JSON"""

import json


def save_to_json_file(my_object, filename):
    """Saves json rep of object to file"""
    with open(filename, "w") as f:
        json.dump(my_object, f)
