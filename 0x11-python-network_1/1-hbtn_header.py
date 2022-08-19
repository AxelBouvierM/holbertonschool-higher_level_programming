#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the value"""
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    with urllib.request.urlopen(sys.argv[1]) as response:
        reque = response.headers.get('X-Request-Id')
        print(reque)
