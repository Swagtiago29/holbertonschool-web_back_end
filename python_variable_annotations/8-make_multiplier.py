#!/usr/bin/env python3
from typing import Callable

"""
This module provides a utility to create a multiplier function.

The `make_multipier` function takes a float `multiplier` as an argument and 
returns a function that can multiply any given number by this multiplier. 
This allows for creating specialized multiplier functions based on the 
multiplier value provided.

Example usage:
    multiply_by_3 = make_multipier(3.0)
    result = multiply_by_3(4.0)  # result will be 12.0
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function creates a multiplier function.

    Args:
        multiplier (float): The value by which other numbers will be multiplied.

    Returns:
        Callable[[float], float]: A function that takes a float as input and 
                                  returns the product of the input and the 
                                  multiplier.
    """
    def multi(x: float) -> float:
        """
        Multiplies the given number by the multiplier.

        Args:
            x (float): The value to be multiplied.

        Returns:
            float: The result of multiplying the input value by the multiplier.
        """
        return x * multiplier

    return multi
