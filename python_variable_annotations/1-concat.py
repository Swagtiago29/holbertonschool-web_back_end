#!/usr/bin/env python3
"""
This module provides a function to concatenate two strings.

The `concat` function takes two strings as input and returns their concatenation.

Module-level documentation provides an overview of the functionality of this script.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenate two strings and return the resulting string.

    Parameters:
    str1 (str): The first string to concatenate.
    str2 (str): The second string to concatenate.

    Returns:
    str: The concatenation of str1 and str2.

    Example:
    >>> concat("Hello, ", "world!")
    'Hello, world!'
    """
    return str1 + str2