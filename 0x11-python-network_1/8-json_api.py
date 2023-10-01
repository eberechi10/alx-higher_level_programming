#!/usr/bin/python3
"""script that take a letter to send POST request to
http://0.0.0.0:5000/search_user.
"""

import sys
import requests


if __name__ == "__main__":
    letter = '' if len(sys.argv) < 2 else sys.argv[1]
    URL = 'http://0.0.0.0:5000/search_user'
    data = {'q': letter}
    response = requests.post(URL, data=data)

    try:
        res = response.json()

        if res.get('id') is None:
            print("No result")
        else:
            print(f"[{res.get('id')}] {res.get('name')}")
    except ValueError:
        print("Not a valid JSON")
