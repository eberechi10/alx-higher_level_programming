#!/usr/bin/python3

"""
script that takes in a URL and an email and send POST request to
the passed URL.
"""
import sys
import requests


if __name__ == "__main__":
    URL = sys.argv[1]
    EMAIL = sys.argv[2]
    data = {'email': EMAIL}

    ressult = requests.post(URL, data=data, timeout=5).text
    print(result)
