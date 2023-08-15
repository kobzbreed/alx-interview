#!/usr/bin/python3
"""
0-minoperations module
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to
    result in exactly n H characters
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n //= divisor
        else:
            divisor += 1

    return operations