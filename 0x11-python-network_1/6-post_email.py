#!/usr/bin/python3
""" Sends post request to a url with email as paraneter
Displays the body of the response """
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
