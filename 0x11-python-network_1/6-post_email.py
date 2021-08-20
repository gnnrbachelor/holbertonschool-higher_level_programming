#!/usr/bin/python3
"""Sends POST request to email"""

if __name__ == "__main__":
    import requests
    from sys import argv
    pl = {'email': argv[2]}
    r = requests.post(argv[1], data=pl)
    print(r.text)
