#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations
in this file: Copy All and Paste. Given a number n,
write a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    if n <= 1:
        return n

    min_ops = [0] * (n + 1)

    # Iterate from 2 to n
    for i in range(2, n + 1):
        # Initialize min_ops[i] to a large value, as it's initially unreachable
        min_ops[i] = float('inf')
        # Check all possible factors of i
        for j in range(1, i):
            if i % j == 0:
                min_ops[i] = min(min_ops[i], min_ops[j] + (i // j))

    return min_ops[n]
