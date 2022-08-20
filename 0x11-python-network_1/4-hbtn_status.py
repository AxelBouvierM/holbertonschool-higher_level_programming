#!/usr/bin/python3
""" task 4 """

if __name__ == "__main__":
    import requests

    url = 'https://intranet.hbtn.io/status'
    body = requests.get(url).text
    to_print = "Body response:\n\t- type: {}\n\t- content: {}\
".format(type(body), body, body)
    print(to_print)
