#!/usr/bin/python3

""" script that fetches an url and prints response body """

import requests


if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')

    print("Body response:")
    print(f"\t- type: {type(response.text)}")

    print(f"\t- content: {response.text}")
