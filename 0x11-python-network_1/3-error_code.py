#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response """

if __name__ == "__main__":
    import sys
    mport urllib.request
    import urllib.error

    request = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.URLError as error:
        print("Error code: {}".format(error.code))
