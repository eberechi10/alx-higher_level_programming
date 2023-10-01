#!/usr/bin/python3

"""script to use urlib for make requests"""


if __name__ == "__main__":
    import urllib.request as url
    req = url.Request('https://intranet.hbtn.io/status')
    with url.urlopen(req) as response:
        node = response.read()
        print("Body response:")
        print("\t- type:", type(node))
        print("\t- content:", node)
        print("\t- utf8 content:", node.decode('utf-8'))
