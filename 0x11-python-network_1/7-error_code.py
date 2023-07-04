#!/usr/bin/python3
""" sends a request to a url and prints the response """

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    if response.status_code  >= 400:
        print(f"Error code: {response.status_code}")

    else:
        print(response.text)
