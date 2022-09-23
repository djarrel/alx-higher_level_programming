#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    if n < 1:
        print("{} arguments.".format(n))
    else:
        print("{} arguments:".format(n))
        for i in range(n):
                print("{}: {}".format(i + 1, sys.argv[i + 1]))
