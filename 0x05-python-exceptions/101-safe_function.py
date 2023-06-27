#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as x:
        sys.stderr.write(f"Exception: {x}\n")
        return None
