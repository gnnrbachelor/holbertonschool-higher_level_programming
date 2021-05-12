#!/usr/bin/python3
"""Module returning python object from json"""

import json


def from_json_string(my_string):
    """Returns python object from json"""
    return json.loads(my_string)
