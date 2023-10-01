#!/usr/bin/python3
"""
script that takes URL and email and send POST request to
the passed URL with the email.
"""
import requests
import sys

try:
    data = {'email': sys.argv[2]}
    result = requests.post(sys.argv[1], data)
    print(result.text)
except BaseException:
    pass
