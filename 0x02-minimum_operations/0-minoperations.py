#!/usr/bin/python3
"""
Function to calculates the fewest number of operations
needed to result in exactly `n` `H` characters in the file.
"""


def minOperations(n):
    if n <= 1:
        return 0  # It's already there or impossible

    # Initialize an array to store the minimum operations for each position
    dp = [float('inf')] * (n + 1)

    # Base case: It takes 0 operations to have 1 'H'
    dp[1] = 0

    # Iterate through all positions up to n
    for i in range(2, n + 1):
        # Iterate through all possible lengths of the copy buffer
        for j in range(1, i):
            # the length of the copy buffer evenly divides the current position
            if i % j == 0:
                # pasting = minimum of current cost & cost of copying + pasting
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0
