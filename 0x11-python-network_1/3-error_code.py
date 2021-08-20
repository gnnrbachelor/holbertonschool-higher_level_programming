#!/usr/bin/python3
"""Error Code"""
if __name__ == "__main__":
    import urllib.request as request
    import urllib.error as error
    import sys
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
