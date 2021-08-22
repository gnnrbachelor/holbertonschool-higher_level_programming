#!/usr/bin/python3
""" Returns github data """
from sys import argv
import urllib.request as requests

if __name__ == "__main__":
    req = requests.get("https://api.github.com/repos/{}/{}/commmits".format(argv[2]. arv[1])).json()
if len(req) > 10:
    size = 10
else:
    size = len(req)
for element in range(size):
    print("{}:{}".format(req[element].get('sha'), req.get('commit').get('author').get('name')))
