#!/usr/bin/python3
""" Task 5 """

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers['X-Request-Id'])
