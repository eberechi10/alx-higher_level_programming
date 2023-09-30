#!/usr/bin/python3

"""
script that takes in a URL sends request to the URL and
displays the value of the X-Request-Id variable found
"""
import requests
import sys


if __name__ == "__main__":
    result = requests.get(sys.argv[1])
    print(result.headers.get('X-Request-Id'))
