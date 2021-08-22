#!/usr/bin/python3
"""Returns github data"""
from sys import argv
import requests

if __name__ == "__main__":
    req = requests.get("https://api.github.com/repos/{}/{}/commmits".format(argv[2], argv[1]))
    data = req.json()
    if len(data) > 10:
        size = 10
    else:
        size = len(data)
    for element in range(size):
#       print("{}: {}".format(data[element].get("sha"), data[element].get("commit").get("author").get("name")))
        print(data)
