#!/usr/bin/python3

     import hidden_4 *
if __name__ == "__main__":
    
    names = dir()
    for i in range(len(names)):
        if names[i][:2] != '__':
            print("{}".format(names[i]))
