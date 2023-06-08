#!/usr/bin/python3

if __name__ == "__main__":
    from hidden_4 import *

    lists = dir()
    for i in range(len(lists)):
        if lists[i][:2] != '__':

            print("{}".format(lists[i]))
