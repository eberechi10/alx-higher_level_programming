#!/usr/bin/python3
""" script that takes in a URL, send request to the URL."""

import sys
import urllib.request

if __name__ == "__main__":

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
