#!/usr/bin/python3
""" to evaluate candidates applying for a back-end position
with multiple challenges, related to this:
    """

import sys
import requests

if __name__ == "__main__":
    repo_n = sys.argv[1]
    owner_n = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_n}/{repo_n}/commits"

    r = requests.get(url)
    commits = r.json()
    try:
        for inde in range(10):
            sha = commits[inde].get("sha")
            author = commits[inde].get("commit").get("author").get("name")
            print(f"{sha}: {author}")
    except IndexError:
        pass
