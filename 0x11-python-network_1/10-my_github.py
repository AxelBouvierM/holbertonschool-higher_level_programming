#!/usr/bin/python3
""" Task 10 """

import requests
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    password = argv[2]
    response = requests.get('https://api.github.com/user',
                            auth=(user, password))
    a = requests.get('https://api.github.com/user')
    print(response.json().get("id"))
