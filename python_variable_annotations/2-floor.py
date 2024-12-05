#!/usr/bin/env python3
"""
This module provides a function to compute the floor of a floating-point number.

The `floor` function takes a float as input and returns the largest integer
less than or equal to that number. The floor is computed using Python's built-in
`math.floor()` function from the `math` module.

Module-level documentation explains the functionality and usage of the script.
"""

import math


def floor(n: float) -> int:
    """
    Return the largest integer less than or equal to the input float.

    This function uses the `math.floor()` function to return the floor of 
    the given float, which is the greatest integer less than or equal to 
    the number.

    Parameters:
    n (float): The number to compute the floor of.

    Returns:
    int: The largest integer less than or equal to n.

    Example:
    >>> floor(3.7)
    3

    >>> floor(-3.7)
    -4
    """
    return math.floor(n)
