#!/usr/bin/python3
"""Returns github id"""
if __name__ == "__main__":
    import requests
    from sys import argv
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(argv[1], argv[2])).json()
    if "id" in response:
        print(response['id'])
    else:
        print(None)
