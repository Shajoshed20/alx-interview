#!/usr/bin/python3
"""A Script for Validating UTF-8 encoding"""


def validUTF8(data):
    """
    A method that determines if a given data set
    represents a valid UTF-8 encoding.
    """
    # Variable to keep track of the number of bytes in the current character
    num_bytes = 0

    byte_1 = 1 << 7
    byte_2 = 1 << 6

    for bytes in data:

        mask_byte = 1 << 7

        if num_bytes == 0:
            # Check if the byte is a continuation byte (10xxxxxx)
            while mask_byte & bytes:
                num_bytes += 1
                mask_byte = mask_byte >> 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            if not (bytes & byte_1 and not (bytes & byte_2)):
                return False

        num_bytes -= 1

    if num_bytes == 0:
        return True

    return False
