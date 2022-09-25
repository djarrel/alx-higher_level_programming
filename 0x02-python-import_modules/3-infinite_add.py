#!/usr/bin/python3
def main():
    import sys
    n = len(sys.argv) - 1
    sum = 0
    for i in range(n):
        sum += int(sys.argv[i + 1])
    print("{:d}".format(sum))
if __name__ == "__main__":
    main()
