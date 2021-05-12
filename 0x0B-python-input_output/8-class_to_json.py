#!/usr/bin/python3
"""
Module for class_to_jsonReturns the dictionary description of data structure for
JSON serialization of an object
"""

import json


def class_to_json(obj):
    """
    Returns the dictionary description of data structure for
    JSON serialization of an object
    """
    return obj.__dict__

