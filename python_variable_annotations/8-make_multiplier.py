#!/usr/bin/env python3
from typing import Callable

"""
This module defines a function `make_multipier` that creates a multiplier function.

The function `make_multipier` accepts a float `multiplier` and returns a new
function that multiplies its input by this multiplier.

Example usage:
    multiply_by_3 = make_multipier(3.0)
    result = multiply_by_3(4.0)  # result will be 12.0
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function creates a multiplier function.

    Args:
        multiplier (float): The value by which other numbers will be
        multiplied.

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
            float: The result of multiplying the input value by the multiplier
        """
        return x * multiplier

    return multi
