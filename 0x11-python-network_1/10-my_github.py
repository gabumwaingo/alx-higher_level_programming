#!/usr/bin/python3
""" takes your github logins and displays your github id """

import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        data = response.json()
        print("{}".format(data['id']))

    else:
        print("None")
