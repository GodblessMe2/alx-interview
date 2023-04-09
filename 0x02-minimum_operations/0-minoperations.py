#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    """
      minOperations
      Get fewest # of operations needed to result in exactly n H characters
    """
    # All outputs should be at least 2 char
    if (n < 2):
        return 0
    result, lest = 0, 2
    while lest <= n:
        if n % lest == 0:
            result += lest
            # Set n to the remainder
            n = n / lest
            lest -= 1
        # Increment lest until it evenly-divide n
        lest += 1
    return result
