#!/usr/bin/python3
"""Module creates object from JSON file"""

import json


def load_from_json_file(filename):
    """Creates an object from JSON file"""
    with open(filename) as f:
        return json.load(f)
