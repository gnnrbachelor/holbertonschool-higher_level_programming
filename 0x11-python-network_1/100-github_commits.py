#!/usr/bin/python3
"""Returns github data"""
from sys import argv
import requests

if __name__ == "__main__":
    """
    Returns github data
    """
    req = requests.get("https://api.github.com/repos/{}/{}/commmits"
                       .format(argv[2], argv[1])).json()
    if len(req) > 10:
        size = 10
    else:
        size = len(req)
    for element in range(size):
        print("{}:{}".format(req[element].get(
            'sha'), req.get('commit').get('author').get('name')))
