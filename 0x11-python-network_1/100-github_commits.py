#!/usr/bin/python3
""" Gets 10 recent commits in a github repo from recent to oldest """

import sys
import requests

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo_name}/commits"
    params = {"per_page": 10}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        commit = response.json()
        for c in commit:
            sha = c['sha']
            author_name = c['commit']['author']['name']
            print(f"{sha}: {author_name}")

    else:
        print("Request failed")
