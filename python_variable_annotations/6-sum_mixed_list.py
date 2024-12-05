#!/usr/bin/env python3
from typing import List, Union

"""
This module contains a function to sum elements of a mixed list containing 
integers and floating-point numbers.

The `sum_mixed_list` function takes a list of numbers (both `int` and `float`)
and returns the sum of those numbers as a floating-point value.
"""


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    Sum the elements of a mixed list and return the result as a float.

    This function takes a list that may contain both integers and floating-point
    numbers, sums the values, and returns the total as a float.

    Parameters:
    mxd_lst (List[Union[float, int]]): A list of numbers (both float and int).

    Returns:
    float: The sum of the numbers in the list as a float.

    Example:
    >>> sum_mixed_list([1, 2.5, 3, 4.5])
    11.0
    """
    e: float = 0.0  # Initialize sum as a float
    for i in mxd_lst:
        e = e + i  # Add each element (either int or float)
    return e
