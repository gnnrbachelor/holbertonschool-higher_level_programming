#!/usr/bin/python3
"""Returns github id"""
if __name__ == "__main__":
    import requests
    from sys import argv
    url = "https://api.github.com/users"
    response = requests.get(url, auth=(argv[1], argv[2])).json()
    print(response.get('id'))
