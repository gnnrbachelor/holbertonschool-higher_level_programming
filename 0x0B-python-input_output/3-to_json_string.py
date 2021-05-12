#!/usr/bin/python3
"""Module returns JSON rep of object"""

import json


def to_json_string(my_obj):
    """Returns JSON obj"""
    return json.dumps(my_obj)
