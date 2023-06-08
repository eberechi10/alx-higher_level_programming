#!/usr/bin/python3

    import sys

if __name__ == "__main__":
   
    args = sys.argv
    total = 0
   
    if len(args) > 1:
        for arg in sys.argv[1:]:
            total += int(arg)

    print(total)
