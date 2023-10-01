#!/usr/bin/python3

"""script to take url and retrieve value of header"""

import urllib.request as ur
import sys

try:
    reqsult = ur.Request(sys.argv[1])

    with ur.urlopen(reqsult) as response:
        print(response.getheader('X-Request-Id'))
except BaseException:
    pass
