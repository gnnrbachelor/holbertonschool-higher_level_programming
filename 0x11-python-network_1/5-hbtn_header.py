#!/usr/bin/python3
"""Displays value of X-Request-Id variable"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
