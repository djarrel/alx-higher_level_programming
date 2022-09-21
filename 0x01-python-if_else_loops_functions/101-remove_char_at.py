#!/usr/bin/python3
def remove_char_at(str, n):
    new = ''
    for c in range(0, len(str)):
        if c == n:
            continue
        new += str[c]
    return new
