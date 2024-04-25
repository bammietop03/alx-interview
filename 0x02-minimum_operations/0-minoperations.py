#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations
in this file: Copy All and Paste. Given a number n,
write a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """ Minimum Operations """

    if not isinstance(n, int):
        return 0

    operations = 0
    iterator = 2
    while (iterator <= n):
        if not (n % iterator):
            n = int(n / iterator)
            operations += iterator
            iterator = 1
        iterator += 1
    return operations
