#!/usr/bin/python3
""" A script that reads stdin line by line and computes metrics"""
import sys
from collections import defaultdict


def print_statistics(total_size, status_codes):
    """
    This function prints the total file size and
    the number of lines for each status code.
    """
    print("File size: {:d}".format(status_codes))
    for i in sorted(total_size.keys()):
        if total_size[i] != 0:
            print("{}: {:d}".format(i, total_size[i]))


stat_code_dict = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
       "404": 0, "405": 0, "500": 0}

count = 0
size = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            print_statistics(stat_code_dict, size)

        stlist = line.split()
        count += 1

        try:
            size += int(stlist[-1])
        except:
            pass

        try:
            if stlist[-2] in stat_code_dict:
                stat_code_dict[stlist[-2]] += 1
        except:
            pass
    print_statistics(stat_code_dict, size)


except KeyboardInterrupt:
    print_statistics(stat_code_dict, size)
    raise
