#!/usr/bin/python3
"""
A method that determines if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    A method that determines if a given data set
    represents a valid UTF-8 encoding.
    """
    bytes_remaining = 0

    for byte in data:
        if bytes_remaining == 0:
            if byte >> 7 == 0b0:
                continue
            elif byte >> 5 == 0b110:
                bytes_remaining = 1
            elif byte >> 4 == 0b1110:
                bytes_remaining = 2
            elif byte >> 3 == 0b11110:
                bytes_remaining = 3
            else:
                return False

            if bytes_remaining == 1 or bytes_remaining > 4:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            bytes_remaining -= 1

    return bytes_remaining == 0
