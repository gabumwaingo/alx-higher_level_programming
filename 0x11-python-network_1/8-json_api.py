#!/usr/bin/python3
""" Takes in a letter
sends a post request to the url with the letter as a parameter
"""

import sys
import requests

if __name__ == "__main__":

    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': q}

    response = requests.post(url, data=payload)
    if response.headers.get('content-type') == 'application/json':
        data = response.json()
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    else:
        print("Not a valid JSON")
