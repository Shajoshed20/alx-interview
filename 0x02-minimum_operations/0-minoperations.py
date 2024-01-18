#!/usr/bin/python3
"""
Function to calculates the fewest number of operations
needed to result in exactly `n` `H` characters in the file.
"""


def minOperations(n):
    """
    Returns an integer
    If `n` is impossible to achieve, return `0`
    """
    if n <= 1:
        return 0  # It's already there or impossible

    initial = 1
    begin = 0
    count = 0

    #when the intial value is less than n
    while initial < n:
        left = n - initial
        if (left % initial == 0):
            begin = initial
            initial += begin
            count += 2
        else:
            initial += begin
            count += 1
    return count
