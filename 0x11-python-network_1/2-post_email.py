#!/usr/bin/python3

"""script that takes in a URL and an email, it sends a POST request to
the passed URL
"""
import urllib.parse
import urllib.request

import sys


if __name__ == "__main__":

    URL = sys.argv[1]
    EMAIL = sys.argv[2]

    values = {'email': EMAIL}

    data = urllib.parse.urlencode(values).encode('ascii')

    result = urllib.request.Request(url=URL, data=data)
    with urllib.request.urlopen(result) as response:
        body = response.read()

        print(body.decode('utf-8'))
