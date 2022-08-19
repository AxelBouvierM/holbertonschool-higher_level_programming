#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    value = {'email': sys.argv[2]}
    info = urllib.parse.urlencode(value)
    info = info.encode('utf-8')
    request = urllib.request.Request(sys.argv[1], info)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode())
