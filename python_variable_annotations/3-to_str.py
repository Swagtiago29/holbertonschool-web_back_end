#!/usr/bin/env python3
"""
This module provides a function to convert an integer to a string.

The `to_str` function takes an integer as input and returns its string
representation using Python's built-in `str()` function.
"""


def to_str(n: int) -> str:
    """
    Convert an integer to its string representation.

    Parameters:
    n (int): The integer to convert to a string.

    Returns:
    str: The string representation of the integer n.

    Example:
    >>> to_str(42)
    '42'
    """
    return str(n)
