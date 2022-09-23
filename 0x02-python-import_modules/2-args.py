#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    if n == 0:
        print("{} arguments.".format(n))
    else:
        print("{} arguments:".format(n))
    for i in range(n + 1):
        if i != 0:
            print("{}: {}".format(i, sys.argv[i]))
