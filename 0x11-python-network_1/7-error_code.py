#!/usr/bin/python3
""" Task 7 """

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)
    if response:
        print(response.text)
    else:
        print("Error code: {}".format(response.status_code))
