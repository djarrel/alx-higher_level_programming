#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i_range = range(len(my_list))
    for i in reversed(i_range):
        print("{:d}".format(my_list[i]))
