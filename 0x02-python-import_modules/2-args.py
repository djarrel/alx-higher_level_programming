#!/usr/bin/python3
import sys


def main():
    length = len(sys.argv)
    print('{:d} argument{:}'.format(length - 1, '.' if length == 1 else
                                    (':' if length == 2 else 's:')))
    i = 1
    for arg in sys.argv[1:]:
        print("{:d}: {}".format(i, arg))
        i += 1


if __name__ == "__main__":
    main()
