#!/usr/bin/python3
""" Method that calculates the fewest number of operations needed to
result in exactly n H characters in the file. """


def minOperations(n):
    """
    Method that calculates the fewest number of operations needed to result
    in exactly n H characters in the file.
    Args:
        n: int
    Returns:
        int: fewest number of operations needed to result in exactly n H
        characters in the file.
    """
    if n <= 1:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(n // i) + i
    return 0
