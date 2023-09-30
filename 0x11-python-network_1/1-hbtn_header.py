#!/usr/bin/python3
"""
script that takes in a URL sends a request to the URL and
displays the value of the X-Request-Id
"""
import urllib.request
import sys


if __name__ == "__main__":
    result = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        result = response.info()

        print(result.get('X-Request-Id'))
