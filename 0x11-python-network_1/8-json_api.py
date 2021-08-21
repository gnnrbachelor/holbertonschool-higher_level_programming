#!/usr/bin/python3
"""Sends POST request to http://0.0.0.0:5000/search_user"""

if __name__ == "__main__":
    import requests
    from sys import argv
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ''

    try:
        url = 'http://0.0.0.0:5000/search_user'
        pl = {'q': q}
        r = requests.post(url, pl).json()
    
        if {'id', 'name'} <= r.keys():
            print('[{id}] {name}'.format(id=r.get('id'), name=r.get('name')))
        else:
            print("No result")
    except ValueError:
        print('Not a valid JSON')

