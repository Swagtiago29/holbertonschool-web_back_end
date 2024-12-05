#!/usr/bin/env python3
"""
This module contains a function `sum_mixed_list` that computes the sum of a
list containing both integers and floating-point numbers.

The function takes a list as input, which may contain mixed data types
(`int` and `float`), and returns the sum of the elements in the list as a
floating-point number.

Example usage:
    sum_mixed_list([1, 2.5, 3, 4.5])  # Returns 11.0
"""

from typing import List, Union

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
