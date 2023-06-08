#!/usr/bin/python3

if __name__ == "__main__":
    import add_0 as add
    add = add.add

    a = 1
    b = 2

    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
