#!/usr/bin/python3
"""
Module to calculate the minimum number of operations
to reach exactly n 'H' characters in a file.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed
    to result in exactly n H characters.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: Minimum number of operations needed, or 0 if impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    current = 1
    # We will divide n by its factors to simulate the operations
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            operations += i  # Each factor contributes to the operations
            n //= i  # Reduce n by the factor
    if n > 1:
        operations += n
        # If n is a prime number, it contributes to the operations
    return operations
